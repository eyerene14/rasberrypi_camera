import os


def activateCamera():
    os.system('sudo apt-get update')
    os.system('sudo apt-get upgrade')
    os.system('reboot')


def takePicture(new_picName='mynewpic'):
    # takes a still image
    # stores picture in home folder
    os.system('raspistill - o ' + new_picName + '.jpeg')


def createVideo(new_videoName='mynewvid', recording_duration=10000):
    # creates a video stream
    # duration of video conversion
    # 1000 = 1 sec; 10000 = 10 sec
    os.system('raspivid - o ' + new_videoName +
              '.h264 - t ' + str(recording_duration))


# createVideo('111022_830pm')
