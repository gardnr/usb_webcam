# USB webcam

Compatible with Raspberry Pi and Beaglebone black

[Tutorial](https://www.raspberrypi.org/documentation/usage/webcams/)

```
sudo apt install fswebcam

gardnr add metric air image webcam

gardnr add driver webcam usb_webcam.driver:UsbWebCam -c metric_name='webcam' device='/dev/video0' resolution='1920x1080'
```
