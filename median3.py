import cv2
import os
import numpy as np
def main():

    '''
    訓練用画像のグレースケール、メディアンフィルタ実行
    '''
    f_name = "concrete-clack1"
    filep = "clack1"
    #画像ファイルパス
    path = "/home/fuku/openCV/concrete-crack-images-for-classification/images"
    labels = get_labels(path)
    for label in labels:
    	path2 = path + "/" + label
    	files = get_images(path2)
    	i = 0
    	for file in files:
    		i += 1
    		print (f'{i}/{len(files)} {label}')
    		f_path = path2 + "/" + file

    		img = cv2.imread(f_path)
    		gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    		size = 21
    		res_img = cv2.medianBlur(gray,size)
    		#print (res_img)
    		filtered = culc(gray, res_img)
    		cv2.imwrite(f"./{f_name}/{label}/{file}",filtered)
    

def get_labels(path):
	tmp = os.listdir(path)
	#print (tmp)
	return tmp

def get_images(path):
	files = os.listdir(path)
	#print (path)
	files_file = [f for f in files if os.path.isfile(os.path.join(path, f))]
	#print (files_file[0])
	return files_file

def culc(ib,im):
	max_b = 255
	h = ib.shape[0]
	w = ib.shape[1]
	ans = np.zeros((h,w))
	#print (f"{im[0][-3]}-{im[0][-2]}-{im[0][-1]}")
	#print (type(ans))
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
