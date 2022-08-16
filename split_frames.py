import cv2
import time
import numpy as np
import multiprocessing as mp

num_processes = mp.cpu_count()
# input_file = "E:\\streetLights\\Data\\29thDecember\\day\\left\\GH011366.MP4"
input_file = "E:\\IIIT-Hyderabad\\monodepth2\\YoloPInput1.mp4"
cap = cv2.VideoCapture(input_file)
frame_jump_unit = cap.get(cv2.CAP_PROP_FRAME_COUNT) // num_processes
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)
def process_video(group_number):
    cap = cv2.VideoCapture(input_file)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_jump_unit * group_number)
    proc_frames = 0

    while proc_frames < frame_jump_unit:
        ret, frame = cap.read()
        if ret == False:
            break
        oppath = "E:\\IIIT-Hyderabad\\monodepth2\\input_frames"
        # frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite(oppath + "/%s_y.jpg" % str(frame_jump_unit * group_number + proc_frames), frame)
        proc_frames += 1


    cap.release()
    return None


if __name__ == "__main__":
    kernel = np.ones((7, 7), np.float32) / 49
    start_time = time.time()
    p = mp.Pool(num_processes)
    p.map(process_video, range(num_processes))

    t3 = time.time()

    print(t3 - start_time)
