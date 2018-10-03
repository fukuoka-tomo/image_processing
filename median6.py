import cv2
import os
import numpy as np
def main():

    '''
    訓練用画像のメディアンフィルタ実行
    RGBそれぞれでメディアンフィルターを実施、その結果をカラーとして合成
    '''
    f_name = "bridge1"
    filep = "clack1"
    label1 = "Negative"
    cg = "gray"
    #画像ファイルパス
    #path = "/home/fuku/openCV/concrete-crack-images-for-classification/images/Negative"
    #path = "/home/fuku/openCV/test"
    # at jupyter in docker 
    path = f"/home/concrete-crack-images-for-classification/images/{label1}"
    files = get_images(path)
    i = 0
    for file in files:
        i += 1
        print (f'{i}/{len(files)}')
        f_path = path + "/" + file

        img = cv2.imread(f_path)
        gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        size = 5
        if cg != "gray":
            res_img = cv2.medianBlur(img,size)
            filtered = culc_color(img, res_img)
        else:
            res_img = cv2.medianBlur(gray,size)
            filtered = culc_gray(gray, res_img)        
        
        file_r = file.split(".")[0]
        #cv2.imwrite(f"./{f_name}/l128-d128/median-jpeg/{file_r}.jpeg",filtered)
        #cv2.imwrite(f"./concrete-clack1/color/Positive/{file_r}.jpeg",filtered)
        w_path = f"./concrete-clack1/{cg}-median-f{size}/{label1}/"
        if not os.path.exists(w_path):
            os.makedirs(w_path)
        cv2.imwrite(f"./concrete-clack1/{cg}-median-f{size}/{label1}/{file_r}.jpeg",filtered)
def get_labels(path):
    tmp = os.listdir(path)
    print (tmp)
    if tmp == None:
        return ["unknown"]
    #print (tmp)
    return tmp

def get_images(path):
    files = os.listdir(path)
    #print (path)
    files_file = [f for f in files if os.path.isfile(os.path.join(path, f))]
    #print (files_file[0])
    return files_file

def culc_gray(ib,im):
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

def culc_color(ib,im):
    max_b = 255
    # split color
    bgr_b = cv2.split(ib)
    bgr_m = cv2.split(im)
    #h = ib.shape[0]
    #w = ib.shape[1]
    color = []
    #print (f"{im[0][-3]}-{im[0][-2]}-{im[0][-1]}")
    #print (type(ans))
    for color_b, color_m in zip(bgr_b, bgr_m):
        h = color_b.shape[0]
        w = color_b.shape[1]
        ans = np.zeros((h,w))
        for i in range(h):
            for j in range(w):
                if color_m[i][j] == 0:
                    color_m[i][j] = 1
                ans[i][j] = (color_b[i][j] * 0.5 * max_b)/(color_m[i][j])
        color.append(ans)
    channged = cv2.merge([color[2],color[1],color[0]])
    #print ("culced")
    #print (ans)
    #print (f'h:{ans.shape[0]},w:{ans.shape[1]}')
    return channged


if __name__ == '__main__':
    main()
