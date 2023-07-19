# Bird Watcher

This project is a bird detection program that notifies the user of the presence of birds. Typically, birdwatchers or animal photographers may have to wait for hours to get their first sighting. With this program, they can be alerted of the presence of birds in real time while they are completing other tasks.

## The Algorithm

The algorithm for this code works by using DetectNet, an object detection model. It is able to detect multiple objects.

The code starts by importing the necessary tools from jetson libraries. It then prepares to open the camera and create a file for the recorded video. The camera then gets opened and starts detecting the scene for birds. If the code detects a bird in the view of the camera, it alerts the user of said bird.

## Running this project

1. SSH into your jetson nano
2. Install git and cmake
3. Clone the jetson library into your nano
4. Clone this github repository into your nano
5. Change directories to the folder with the project
6. Run the project using "python3 bird.py"

To end the recording, use ctrl+c, and the recording session will be diplayed under the name "bird_video.mp4"

[View a video explanation here]
