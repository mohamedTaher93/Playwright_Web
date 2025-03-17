from playwright.async_api import Page
import os
import sys

from Utilities.Browser import Browser

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Utilities.Locators import locators
from Utilities.Actions import Actions


class Home_Page:
    # def __init__(self, page: Page):
    #     self.page = page
    #     self.actions = Actions(page)
    #     self.home_locators = locators["Home_Locators"]
    #
    def __init__(self):
        self.page = None
        self.actions = None
        self.home_locators = None

    async def async_init(self):
        self.page = await Browser.get_instance()
        self.actions = Actions()
        self.home_locators = await locators["Home_Locators"]

    async def get_home_page_title(self):
        await self.actions.wait_for_page_to_load()
        home_title = await self.actions.get_element_text(self.home_locators["home_page_title"])
        return home_title

    async def click_on_bugs_form_element(self):
        await self.actions.click_element(self.home_locators["bugs_form"])