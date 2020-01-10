import subprocess

editplus = '''C:/Users/Venus/AppData/Local/UiPath/app-19.10.1/UiRobot.exe execute --file "D:/Workspace/ui_20200102/EditPlusUiTest.xaml"'''
lims='''C:/Users/pc7/AppData/Local/UiPath/app-19.10.1/UiRobot.exe execute --file "D:/Workspace/ui_20191219/Main.xaml"'''

def commander(cmd):
    _result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    _lines = _result.stdout.readlines()
    return _lines


# if __name__ == "__main__":
#     _lines = commander(cmd=editplus2)
#     print(_lines)
