import os

os.listdir()


name = input('What is the name of the virtual environment?')
# print(name)


def createVirtualEnvironment():
    os.system('python -m venv ' + name)
    os.system('ls -la')


def activateVirtualEnvironment(name='raspi'):
    os.system('. ' + name + '/bin/activate')
    #print(os.system('. ' + name + '/bin/activate'))


def importPackagesToVenv():
    if os.path.exists('requirements.txt'):
        os.system('python -m pip install -r requirements.txt')
        os.system('pip list')
    else:
        print("requirements.txt file is not in current folder")


def stopVirtualEnvironment():
    os.system('deactivate')


if os.path.exists(name):
    activateVirtualEnvironment()
else:
    createVirtualEnvironment()

# stopVirtualEnvironment()
