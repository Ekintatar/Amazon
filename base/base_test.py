import unittest

from base.utils.settings import Settings, SettingKeys
from base.utils.chrome_browser import ChromeBrowser
from base.base_functions import Base
from base.utils.report_html import decorator_loader, error_logger


class UnitTestHelper:
    def _get_fail_reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]

    def get_test_result(self):
        if hasattr(self, '_outcome'):
            result = self.defaultTestResult()
            self._feedErrorsToResult(result, self._outcome.errors)
        else:
            result = getattr(self, '_outcomeForDoCleanups', self._resultForDoCleanups)
        return {"error": self._get_fail_reason(result.errors),
                "failure": self._get_fail_reason(result.failures),
                "ok": not self._get_fail_reason(result.errors) and not self._get_fail_reason(result.failures)}


@decorator_loader(error_logger)
class BaseTest(unittest.TestCase, ChromeBrowser, UnitTestHelper, Base):
    device = None
    url = None

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.settings = Settings()
        ChromeBrowser.__init__(self, self.settings)

        if self.device:
            self.driver = self.chrome_mobile(self.device)
        else:
            self.driver = self.chrome_web()

        if not self.url:
            self.url = self.settings.get(SettingKeys.PARTNER_PANEL_URL)
            self.driver.get(self.url)
        self.driver.get(self.url)
