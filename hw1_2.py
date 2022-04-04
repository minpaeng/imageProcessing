from skimage import io
import matplotlib.pyplot as plt
import numpy as np


def make_histo(img):
    histo = np.zeros(shape=(256,))
    count = 0
    for image_row in img:
        for pixel_value in image_row:
            histo[pixel_value] += 1

    for i in histo:
        count += i

    return histo, count


def make_histo_sum(histogram):
    histo_sum = [histogram[0]]
    for a in range(1, len(histogram)):
        histo_sum.append(histogram[a] + histo_sum[a - 1])

    return histo_sum


plt.figure(figsize=(10, 6))

# 입력 영상 히스토그램
plt.subplot(3, 5, (1, 2))
original = io.imread('sample_Images/engineer.tif')
plt.title('original image histogram')
io.imshow(original)

original_histo, count_pixel = make_histo(original)

plt.subplot(3, 5, (3, 5))
plt.bar(np.arange(256), original_histo)


# 원하는 영상 히스토그램
plt.subplot(3, 5, (6, 7))
target = io.imread('sample_Images/twins.tif')
plt.title('target image histogram')
io.imshow(target)

target_histo, count_pixel_t = make_histo(target)

plt.subplot(3, 5, (8, 10))
plt.bar(np.arange(256), target_histo)


# 평활화
sum_origin = make_histo_sum(original_histo)
sum_target = make_histo_sum(target_histo)
equalization_original, equalization_target = [], []
for x in range(0, 256):
    n = 255 / count_pixel
    n_t = 255 / count_pixel_t
    equalization_original.append(round(sum_origin[x] * n))
    equalization_target.append(round(sum_target[x] * n_t))

equalization_original = np.uint8(equalization_original)
equalization_target = np.uint8(equalization_target)
# print(len(set(equalization_original)))                      # 166
# print(len(set(equalization_target)))                        # 212


# 역평활화 함수 계산(룩업 테이블 생성)
LUT = np.zeros((256,), 'uint8')

for j, h in enumerate(equalization_original):
    # h에 대해, 바로 이전 값과 같다면 이미 룩업 테이블에 계산된 것이므로 다음 원소 탐색
    if (j > 0) and (h == equalization_original[j - 1]):
        continue

    # 처음 나타나는 h라면 s와 매핑
    lower_bound = 0
    lower_bound_idx = 0
    for i, s in enumerate(equalization_target):
        # h값이 s보다 클때동안 lower_bound에 s 저장
        if h > s:
            lower_bound = s
            lower_bound_idx = i
        # h와 s가 같다면 룩업 테이블에 값 추가 및 다음 원소 탐색을 위해 break
        elif h == s:
            LUT[h] = i
            break
        # h값이 s보다 작아진다면 lower_bound와 현재 s 비교
        # 차를 구함: 차가 작은 쪽의 index를 룩업 테이블에 저장
        else:
            item = lower_bound_idx if (h - lower_bound) < (s - h) else i
            LUT[h] = item
            break


# print(len(set(LUT)))                            # 150

# 원본 -> 평활화 변환
st = equalization_original[original]

# 평활화 -> 명세화 변환
st = LUT[st]
# print(st.shape)                                    # (256, 256)

plt.subplot(3, 5, (11, 12))
plt.title('Histogram Specification')
io.imshow(st)

plt.subplot(3, 5, (13, 15))
plt.hist(st.flatten(), bins=256, range=(0, 256))

plt.tight_layout()
io.show()
