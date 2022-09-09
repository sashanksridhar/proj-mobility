import matplotlib.pyplot as plt
import cv2
import random

def plot_one_box(x, image, color=None, label=None, line_thickness=None):
    # Plots one bounding box on image img
    tl = line_thickness or round(0.002 * (image.shape[0] + image.shape[1]) / 2) + 1  # line/font thickness
    color = color or [random.randint(0, 255) for _ in range(3)]
    c1, c2 = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))
    cv2.rectangle(image, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
    if label:
        tf = max(tl - 1, 1)  # font thickness
        t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.rectangle(image, c1, c2, color, -1, cv2.LINE_AA)  # filled
        cv2.putText(image, label, (c1[0], c1[1] - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)

        
source_file = open('D:\\Downloads\\0.txt', 'r')
image = cv2.imread('D:\\Downloads\\0.0_y.jpg')
try:
    height, width, channels = image.shape
except:
    print('no shape info.')

classes = image_names = [0]
colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(len(classes))]


box_number = 0
for line in source_file: #例遍 txt文件得每一行
    staff = line.split() #对每行内容 通过以空格为分隔符对字符串进行切片
    print(staff)
    class_idx = int(staff[0])

    x1, y1, x2, y2 = float(staff[1])*width, float(staff[2])*height, float(staff[3])*width, float(staff[4])*height
    # x1 = round(x_center-w/2)
    # y1 = round(y_center-h/2)
    # x2 = round(x_center+w/2)
    # y2 = round(y_center+h/2)     
    
    # if class_idx == 0: 
    #     draw_people_tangle = cv2.rectangle(image, (x1,y1),(x2,y2),(0,0,255),2)   # 画框操作  红框  宽度为1
    #     cv2.imwrite(save_file_path,draw_people_tangle)  #画框 并保存
    # elif class_idx == 1:
    #     draw_car_tangle = cv2.rectangle(image,(x1,y1),(x2,y2),(0,255,0),2)     # 画框操作  绿框  宽度为1
    #     cv2.imwrite(save_file_path,draw_car_tangle)  #画框 并保存

    plot_one_box([x1,y1,x2,y2], image, color=colors[class_idx], label=classes[class_idx], line_thickness=None)

    plt.imshow(image)

    box_number += 1