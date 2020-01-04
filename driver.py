from subprocess import call

from gardnr import drivers, metrics


class UsbWebCam(drivers.Sensor):

    metric_name = 'webcam'
    image_file_name = 'image'
    image_file_extension = '.jpg'
    device = '/dev/video0'
    resolution = '384x288'


    def read(self):
        full_file_name = '{file_name}{file_extension}'.format(
            file_name=self.image_file_name,
            file_extension=self.image_file_extension
        )

        # create the image file from webcam
        call(['fswebcam',
              '-d', self.device,
              '-S', '20',
              '-r', self.resolution,
              full_file_name])

        with open(full_file_name, 'rb') as image_file:
            image_bytes = image_file.read()

        metrics.create_file_log(
            self.metric_name,
            image_bytes,
            extension=self.image_file_extension
        )
