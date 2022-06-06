import win32gui,win32process
import win32con
import psutil
from selenium import webdriver
import uiautomation as auto
from pywinauto import Application
from time import sleep


while(1):
    browser = Application(backend='uia')
    browser.connect(title_re=".*Chrome.*")
    element_name="Address and search bar"
    dlg = browser.top_window()
    url = dlg.child_window(title=element_name, control_type="Edit").get_value()
    print(url)
    sleep(3)

###################
# def get_window_pid(title):
#     hwnd = win32gui.FindWindow(None, title)
#     threadid,pid = win32process.GetWindowThreadProcessId(hwnd)
#     return pid

# print(get_window_pid('Google Chrome'))



# c = webdriver.Chrome(executable_path='E:\Malware\CryptoJacking-Detection-System\Pid_to_url_testing\chromedriver.exe')
# c.service.process # is a Popen instance for the chromedriver process
# p = psutil.Process(c.service.process.pid)
# print (p.get_children(recursive=True))

# hwnd = win32gui.GetForegroundWindow()
# win32gui.FindWindow('chrome')
# print(hwnd)
# omniboxHwnd = win32gui.FindWindowEx(hwnd, 0, 'Chrome_OmniboxView', None)
# omniboxHwnd

# # print(omniboxHwnd)
# def getWindowText(hwnd):
#     buf_size = 1 + win32gui.SendMessage(hwnd, win32con.WM_GETTEXTLENGTH, 0, 0)
#     buf = win32gui.PyMakeBuffer(buf_size)
#     win32gui.SendMessage(hwnd, win32con.WM_GETTEXT, buf_size, buf)
#     return str(buf)

# print(getWindowText(omniboxHwnd))

# from time import sleep
# import uiautomation as automation

# if __name__ == '__main__':
#     sleep(3)
#     control = automation.GetFocusedControl()
#     controlList = []
#     while control:
#         controlList.insert(0, control)
#         control = control.GetParentControl()
#     if len(controlList) == 1:
#         control = controlList[0]
#     else:
#         control = controlList[1]
#     address_control = automation.FindControl(control, lambda c, d: isinstance(c, automation.EditControl) and "Address and search bar" in c.Name)
#     print (address_control.CurrentValue())