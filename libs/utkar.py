import image_dehazer										# Load the library
import cv2
from datetime import datetime
lol=datetime.now()
HazeImg = cv2.imread('/home/ozan/Desktop/resler/train/9.jpg')
HazeImg1=cv2.bitwise_not(HazeImg)						# read input image -- (**must be a color image**)
HazeCorrectedImg = image_dehazer.remove_haze(HazeImg1)		# Remove Haze
HazeCorrectedImg=cv2.bitwise_not(HazeCorrectedImg)	
print(datetime.now()-lol)
cv2.namedWindow('input image', cv2.WINDOW_NORMAL)
cv2.namedWindow('enhanced_image', cv2.WINDOW_NORMAL)
cv2.imshow('input image', HazeImg);						# display the original hazy image
cv2.imshow('enhanced_image', HazeCorrectedImg);	
cv2.resizeWindow('input image', 1200,900)		# display the result
cv2.resizeWindow('enhanced_image', 1200,900)	
cv2.waitKey(0)
