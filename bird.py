from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput
import time

net = detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = videoSource("/dev/video0") # 'csi://0' for MIPI CSI camera # '/dev/video0' for V4L2
display = videoOutput("bird_video.mp4") # 'my_video.mp4' for file

while True:
    img = camera.Capture()

    if img is None: # capture timeout
        continue

    detections = net.Detect(img)
    
    display.Render(img)
    display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))

    for detection in detections:
        if net.GetClassDesc(detection.ClassID) == "bird":
            print("There is a bird.")
            time.sleep(5) # stops spam
