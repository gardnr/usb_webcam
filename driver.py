from subprocess import call

from gardnr import drivers, metrics


class UsbWebCam(drivers.Sensor):
    def setup(self):
        self.metric_name = 'webcam-image'
        self.image_file_name = 'image'
        self.image_file_extension = '.jpg'

    def read(self):
        full_file_name = '{file_name}{file_extension}'.format(
            file_name=self.image_file_name,
            file_extension=self.image_file_extension
        )

        # create the image file from webcam
        call(['fswebcam', '-S', '20', full_file_name])

        with open(full_file_name, 'rb') as image_file:
            image_bytes = image_file.read()

        metrics.create_file_log(
            self.metric_name,
            image_bytes,
            extension=self.image_file_extension
        )
