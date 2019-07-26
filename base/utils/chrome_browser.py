import sys
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from base.utils.settings import SettingKeys


class MobileDevices(enumerate):
    NEXUS5X = "Nexus 5X"
    NEXUS7 = "Nexus 7"
    IPHONE6 = "iPhone 6"
    IPHONE6_PLUS = "iPhone 6 Plus"
    IPAD = "iPad"


class ChromeBrowser:
    def __init__(self, settings):
        self.settings = settings
        self.chrome_options = self.get_chrome_options()
        self.driver = None

    def get_webdriver_path(self):
        os_names_webdriver_suffixes = {
            "linux": "Linux64",
            "linux2": "Linux64",
            "darwin": "Mac64",
            "cygwin": "Win64.exe",
            "win32": "Win64.exe"}
        return os.path.join(self.settings.project_dir, "base", "utils", "webdrivers",
                            "chromedriver" + os_names_webdriver_suffixes[sys.platform])

    def get_chrome_options(self):
        chrome_errors_extension = os.path.join(self.settings.project_dir, "base", "utils",
                                               "extensions", "ChromeErrorCollector.crx")
        chrome_options = Options()
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_extension(chrome_errors_extension)
        return chrome_options

    def init_driver(self):
        if self.driver is not None:
            self.driver.quit()
        capabilities = self.chrome_options.to_capabilities()

        if self.settings.get(SettingKeys.REMOTE_DRIVER) == "yes":
            driver = webdriver.Remote(
                command_executor='http://{}:4444/wd/hub'.format(self.settings.get(SettingKeys.HUB_IP)),
                desired_capabilities=capabilities)
        else:
            driver = webdriver.Chrome(executable_path=self.get_webdriver_path(),
                                      desired_capabilities=capabilities)
        self.driver = driver
        return driver

    def chrome_web(self):
        driver = self.init_driver()
        width = driver.execute_script("return window.screen.availWidth")
        height = driver.execute_script("return window.screen.availHeight")
        driver.set_window_position(0, 0)
        driver.set_window_size(width, height)
        return driver

    def chrome_mobile(self, device=MobileDevices.IPHONE6):
        self.chrome_options.add_experimental_option("mobileEmulation", {"deviceName": device})
        driver = self.init_driver()
        driver.set_window_position(0, 0)
        return driver

    def chrome_tablet(self):
        return self.chrome_mobile(MobileDevices.IPAD)
