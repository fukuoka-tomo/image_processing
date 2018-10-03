import cv2
import numpy as np
def main():

    '''
    画素数を指定した正方形で切り抜き分割、端数は切り捨て
    '''
    f_name = "bridge1"
    # 16bit
    #img = cv2.imread(f"{f_name}.tif",-1)
    # 8bit
    img = cv2.imread(f"{f_name}.tif")
    #print (img)
    #print (img.shape)
    height, width, channels = img.shape
    length = 1000

    h_num = int(height / length)
    w_num = int(width / length)

    start_h = 0
    start_w = 0
    for i in range(h_num):
        ht_num = (i+1) * length
        for j in range(w_num):
        	gn = f"{i}-{j}"
        	print (gn, end=' ')
        	img2 = cv2.imread(f"./{f_name}/{length}/{gn}.tif")
        	gray = cv2.cvtColor(img2,cv2.COLOR_RGB2GRAY)
        	k = 3
        	res_img = cv2.medianBlur(gray,k, (41,41))
        	#res_img = cv2.medianBlur(img2,k)
        	cv2.imwrite(f"./{f_name}/{length}/gray_median/{gn}.tif",res_img)
        	#cv2.imwrite(f"./{f_name}/{length}/color_median/{gn}.tif",res_img)

def culc():
	a

if __name__ == '__main__':
    main()
