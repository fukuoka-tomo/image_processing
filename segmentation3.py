import cv2
import numpy as np
def main():

    '''
    画素数を指定した正方形で切り抜き分割、端数は切り捨て
    '''
    f_name = "bridge1"
    # 16bit
    img = cv2.imread(f"{f_name}.tif",-1)
    # 8bit
    #img = cv2.imread(f"{f_name}.tif")
    #print (img)
    #print (img.shape)
    height, width, channels = img.shape
    length = 128
    #差分
    diff = 128

    h_num = int((height-length) / diff)
    w_num = int((width-length) / diff)

    start_h = 0
    start_w = 0
    for i in range(h_num):
        ht_num = length + (i * diff)
        for j in range(w_num):
            wt_num = length + (j * diff)
            clp = img[start_h:ht_num, start_w:wt_num]
            gn = f"{i}-{j}"
            print (gn, end=' ')
            cv2.imwrite(f"./{f_name}/gray{length}-{diff}/{gn}.tif", clp)
            start_w = (j+1)*diff
        start_w = 0
        start_h = (i+1)*diff

if __name__ == '__main__':
    main()
