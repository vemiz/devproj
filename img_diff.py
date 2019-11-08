import cv2
import imutils
import numpy as np
from skimage.measure import compare_ssim

image1 = cv2.imread('00000053.jpg')
image2 = cv2.imread('00000076.jpg')
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)


# Helper method to get image dimensions
def getsize(img):
    dimensions = img.shape
    return dimensions


# Image differencing on grayscale images.
def img_diff(i1, i2):
    img1 = i1
    img2 = i2
    diff = None
    threshold = 150000
    if getsize(img1) != getsize(img2):
        print("The images are not equal in size")
    else:
        diffimg = cv2.subtract(img1, img2)
        diff = np.count_nonzero(diffimg)

    if diff > threshold:
        print("The difference of the images are bigger than the threshold")
        print("Threshold: " + str(threshold))
        print("Difference: " + str(diff))
    else:
        print("The images are equal within the threshold")
        print("Threshold: " + str(threshold))
        print("Difference: " + str(diff))


def get_diff_mask(i1, i2):
    diff = cv2.absdiff(i1, i2)
    mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    th = 1
    imask = mask > th

    canvas = np.zeros_like(i2, np.uint8)
    canvas[imask] = i2[imask]

    cv2.imshow("Mask", mask)
    # return mask


# Compute SSIM between two images
(score, diff) = compare_ssim(gray1, gray2, full=True)
print("Image similarity:", score)
diff = (diff * 255).astype("uint8")
thresh = cv2.threshold(diff, 0, 255,
                       cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
# The diff image contains the actual image differences between the two images
# and is represented as a floating point data type in the range [0,1]
# so we must convert the array to 8-bit unsigned integers in the range
# [0,255] image1 we can use it with OpenCV

masked_img = cv2.bitwise_and(image1, image1, mask=diff)
cv2.imshow('diff', diff)
cv2.imshow("Thresh", thresh)
cv2.imshow('Masked', masked_img)
cv2.waitKey()
