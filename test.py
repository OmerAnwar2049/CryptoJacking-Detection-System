import win32gui
import win32con

hwnd = win32gui.GetForegroundWindow()
# win32gui.FindWindow('chrome')
# print(hwnd)
omniboxHwnd = win32gui.FindWindowEx(hwnd, 0, 'Chrome_OmniboxView', None)

omniboxHwnd

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