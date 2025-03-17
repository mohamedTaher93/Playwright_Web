import logging
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Pom.Home_Page import Home_Page
from Utilities.Browser import Browser


class Home_Common_Keywords:
    exp_home_title = "QA Practice"
    # page = Browser.get_instance()
    # home_page = Home_Page(page)

    def __init__(self):
        self.page = None
        self.home_page = None

    async def async_init(self):
        self.page = await Browser.get_instance()
        self.home_page = Home_Page()

    async def check_home_page_opened(self):
        actual_home_title = await self.home_page.get_home_page_title()
        logging.info(f"Actual Title: {actual_home_title}")
        assert actual_home_title == self.exp_home_title, f"Home page not opened successfully as the home title {actual_home_title} not {self.exp_home_title}"

    async def click_on_bugs_form(self):
        await self.home_page.click_on_bugs_form_element()