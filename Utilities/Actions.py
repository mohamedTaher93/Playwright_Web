from playwright.async_api import Page
import os
import sys

from Resources import constants
from Utilities.Browser import Browser

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Actions:
    default_timeout = constants.TIME_OUT
    # def __init__(self, page: Page):
    #     self.page = page

    def __init__(self):
        self.page = None

    async def async_init(self):
        self.page = await Browser.get_instance()

    async def wait_for_page_to_load(self):
        await self.page.wait_for_load_state('domcontentloaded', timeout=constants.TIME_OUT)

    async def get_element_text(self, locator: str, wait_timeout=default_timeout):
        element_text = await self.page.text_content(locator, timeout=wait_timeout)
        return element_text

    async def click_element(self, locator: str, wait_timeout=default_timeout):
        await self.page.click(locator, timeout=wait_timeout)

