# Self-Driving-Car-Sim-Based
A basic and CNN-based approach to a simulator based self-driving car (Windows only). The simulator is Udacity's self-driving car simulator (https://github.com/udacity/self-driving-car-sim).

```advanced_drive + basic_drive``` both contain helper functions to perform screen/key grabs (and presses). 

```basic_drive``` uses a combination of thresholding, polynomial fitting, and perspective warping to approximate the direction the car should travel given the lane lines (and press left/right accordingly). It performs well on slight curves but cannot handle >45 degree turns (still in progress).

```advanced_drive``` requires the user to drive around the track >20 times to accumulate a dataset (screen grab + key input) to train a CNN based on the popular NVIDIA end-to-end self-driving model architecture. **Good read** - (https://images.nvidia.com/content/tegra/automotive/images/2016/solutions/pdf/end-to-end-dl-using-px.pdf). The game window should be set to 640x480 and placed on the top left corner of the screen. Progress is needed to interpret the network outputs. 

This repository can be used to show the difference between "lane-assist" and full "self-driving" techniques.
