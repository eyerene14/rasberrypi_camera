import os
from cameraCtrl import createVideo, takePicture, activateCamera

username = input("Enter RaspberryPi user's name: ")
#hostname = input("Enter RaspberryPi's hostname: ")


def connectToRaspy():
    print(os.system('ssh ' + username + '@raspberrypi.local'))


def logoutOfRaspy():
    print(os.system('logout'))


def moveFilesToRaspy(fromPath='pwd', fileName='', toPath='~'):
    logoutOfRaspy()
    os.system('scp ' + fromPath + '/' + fileName + ' ' +
              username + '@raspberrypi.local:' + toPath)
    connectToRaspy()
    print(os.system('ls -l'))


connectToRaspy()
