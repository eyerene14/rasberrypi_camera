import os

username = input("Enter RaspberryPi user's name: ")
#hostname = input("Enter RaspberryPi's hostname: ")


def connectToRaspy():
    print(os.system('ssh ' + username + '@raspberrypi.local'))


def logoutOfRaspy():
    print(os.system('logout'))


'''
def moveFilesToRaspy(fromPath='pwd', fileName='cameraCtrl', toPath='~'):

    if os.path.exists(fileName):
        try:
            os.system('rm ' + fileName)
        except Exception as e:
            print(e)

    logoutOfRaspy()
    os.system('scp ' + fromPath + '/' + fileName + ' ' +
              username + '@raspberrypi.local:' + toPath)
    connectToRaspy()
    print(os.system('ls -l'))
'''


def gitForkCameraCmds(fileName='cameraCtrl.py'):
    if os.path.exists(fileName):
        try:
            os.system('rm ' + fileName)
        except Exception as e:
            print(e)
    os.system(
        'wget https: // raw.githubusercontent.com/eyerene14/rasberrypi_camera/main/cameraCtrl.py - O cameraCtrl.py')


print(os.path)
connectToRaspy()
gitForkCameraCmds()
