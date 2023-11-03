import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr

class ProcessingImg:
    
    def __init__(self, new_img):
        self.new_img = new_img
        
    # changing stuff to test the git pull request
    
    print("testing for git pull request")
    
    def process(self):
        img = cv2.imread(self.new_img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # plt.imshow(cv2.cvtColor(gray,cv2.COLOR_BGR2RGB))
        
        bfilter = cv2.bilateralFilter(gray, 11, 17, 17) #Noise reduction
        edged = cv2.Canny(bfilter, 30, 200) #Edge detection
        # plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))
        plt.show()


        keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(keypoints)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]


        location = None
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 10, True)
            if len(approx) == 4:
                location = approx
                break

        mask = np.zeros(gray.shape, np.uint8)
        new_image = cv2.drawContours(mask, [location], 0,255, -1)
        new_image = cv2.bitwise_and(img, img, mask=mask)
        # plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))



        (x,y) = np.where(mask==255)
        (x1, y1) = (np.min(x), np.min(y))
        (x2, y2) = (np.max(x), np.max(y))
        cropped_image = gray[x1:x2+3, y1:y2+3]
        # plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))

        reader = easyocr.Reader(['en'])
        result = reader.readtext(cropped_image)
        #print(result)

        siz= len(result)
        #print(siz)
        num=""

        i=0

        while i < siz:
            text = result[i][-2]
            num = num + text+ " "
            i=i+1

        return num
        # plt.show()




# t = ProcessingImg("core/" + "sam1.jpg")
# t.process()