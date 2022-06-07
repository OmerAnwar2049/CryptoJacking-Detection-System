import uiautomation as auto
from pywinauto import Application
from time import sleep

class Url_Fetcher:

    def __init__(self):
        self.urls = {}


    def getSingleUrl(self):
        
        browser = Application(backend='uia')
        browser.connect(title_re=".*Chrome.*")
        element_name="Address and search bar"
        dlg = browser.top_window()
        url = dlg.child_window(title=element_name, control_type="Edit").get_value()
        
        if url not in self.urls:
            self.urls[url] = 1
            return ('https://'+url)
        return ("-1")


