import cv2
import numpy as np
def main():

    '''
    画素数を指定した正方形で切り抜き分割、端数は切り捨て
    '''
    f_name = "sample1"
    filep = "bridge1"
    # 16bit
    #img = cv2.imread(f"{f_name}.tif",-1)
    # 8bit
    #img = cv2.imread(f"{f_name}/{filep}.jpg")
    img = cv2.imread("bridge1.tif")
    #print (img)
    print (img.shape)
    print (img)
    print (type(img))
    height, width, channels = img.shape
    length = 1000

    h_num = int(height / length)
    w_num = int(width / length)

    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    print ("after grayscale")
    print (gray)
    
    size = 21
    res_img = cv2.medianBlur(gray,size)
    print ("after median")
    print (res_img)
    #res_img = cv2.medianBlur(img2,k)
    filtered = culc(gray, res_img)
    #cv2.imwrite(f"./{f_name}/gray_median/asr_02({size}).jpg",res_img)
    cv2.imwrite(f"./{f_name}/gray_median/{filep}({size}_c)_2.tif",filtered)
    #cv2.imwrite(f"./{f_name}/{length}/color_median/{gn}.tif",res_img)

def culc(ib,im):
	max_b = 255
	h = ib.shape[0]
	w = ib.shape[1]
	ans = np.zeros((h,w))
	print (f"{im[0][-3]}-{im[0][-2]}-{im[0][-1]}")
	print (type(ans))
	for i in range(h):
		for j in range(w):
			if im[i][j] == 0:
				im[i][j] = 1
			ans[i][j] = (ib[i][j] * 0.5 * max_b)/(im[i][j])

	#print ("culced")
	#print (ans)
	#print (f'h:{ans.shape[0]},w:{ans.shape[1]}')
	return ans


if __name__ == '__main__':
    main()
