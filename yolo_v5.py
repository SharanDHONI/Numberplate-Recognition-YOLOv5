import cv2
import torch
from PIL import Image
import numpy as np
import imutils
from imutils.video import VideoStream


# Model

def load_model():
    # model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='/media/rudram/HDD1/SASI/video-streaming/yolov5/weights/best.pt', force_reload=True)
    return model


def single_image(model):
    img = cv2.imread('/media/rudram/HDD1/rudram_final_img/num_plate/NP3/0000149.jpg')

    results = model(img) 
    print(results.pandas().xyxy[0].to_json(orient="records"))
    print(results)
    cv2.imwrite("test_img.jpg",np.squeeze(results.render()))
    cv2.imshow('YOLO', np.squeeze(results.render()))
    cv2.waitKey()

def live_video(model):
    vs = VideoStream("rtsp://admin:rudra22test***@192.168.1.205:554").start()
    while True:
        frame = vs.read()
        frame = imutils.resize(frame, width=600)
        results = model(frame) 
        print(results.pandas().xyxy[0].to_json(orient="records"))
        # print(results)
        cv2.imwrite("test_img.jpg",np.squeeze(results.render()))
        cv2.imshow('YOLO', np.squeeze(results.render()))

        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    vs.release()

def video_file(model):
    vs = VideoStream("/media/rudram/HDD1/SASI/video-streaming/yolov5/test_video2.mp4").start()
    video_obj = cv2.VideoWriter('output_video.mp4',cv2.VideoWriter_fourcc(*'mp4v'),20.0, (640,480))
    while True:
        frame = vs.read()
        # frame = imutils.resize(frame, width=600)
        results = model(frame) 
        print(results.pandas().xyxy[0].to_json(orient="records"))
        # print(results)
        # cv2.imwrite("test_img.jpg",np.squeeze(results.render()))
        video_obj.write(np.squeeze(results.render()))
        # cv2.imshow('YOLO', np.squeeze(results.render()))

        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    vs.release()

if __name__ == "__main__":
    model=load_model()
    # single_image(model)
    # live_video(model)
    video_file(model)