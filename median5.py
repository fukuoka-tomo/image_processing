import cv2
import os
import numpy as np
def main():

    '''
    評価用画像のカラー画像、メディアンフィルタ実行
    RGBそれぞれでメディアンフィルターを実施、その結果をカラーとして合成
    '''
    f_name = "bridge1"
    filep = "clack1"
    #画像ファイルパス
    #path = "/home/fuku/openCV/concrete-crack-images-for-classification/images"
    #
    #path = "/home/fuku/openCV/test/bridge1/l128-d128"
    # at jupyter in docker 
    
    """ カラー画像に対してメディアンフィルタを実行後、RGB要素に分割して数値計算処理
    img = cv2.imread("/home/test/bridge1.tif")
    res_img = cv2.medianBlur(img, 21)
    filtered = culc(img, res_img)
    cv2.imwrite("/home/test/bridge1_color_median2.jpeg",filtered)
    """

     
    #カラー画像をRGB要素に分割してそれぞれにメディアンフィルタを実行後、RGB要素ごとに数値計算処理
    img = cv2.imread("/home/test/bridge1.tif")
    #res_img = cv2.medianBlur(img, 21)
    filtered = culc2(img)
    cv2.imwrite("/home/test/bridge1_color_median3.jpeg",filtered)
        
    
    """
    path = "/home/test/bridge1/l128-d128"
    files = get_images(path)
    i = 0
    for file in files:
        i += 1
        print (f'{i}/{len(files)}')
        f_path = path + "/" + file

        img = cv2.imread(f_path)
        size = 21
        res_img = cv2.medianBlur(img,size)
        #print (res_img)
        filtered = culc(img, res_img)

        file_r = file.split(".")[0]
        cv2.imwrite(f"./{f_name}/l128-d128/median-jpeg/{file_r}.jpeg",filtered)
    """

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

def culc(ib,im):
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

def culc2(ib):
    max_b = 255
    # split color
    bgr = cv2.split(ib)
    medianed = []
    for c in bgr:
        medianed.append(cv2.medianBlur(c, 11))
    #h = ib.shape[0]
    #w = ib.shape[1]
    color = []
    #print (f"{im[0][-3]}-{im[0][-2]}-{im[0][-1]}")
    #print (type(ans))

    for color_b, color_m in zip(bgr, medianed):
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
