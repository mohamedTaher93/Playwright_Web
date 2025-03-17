import os
import sys

from robot.api.deco import keyword

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Pom.Home_Page import Home_Page
from Resources import constants
from Utilities.Browser import Browser

class Common_Keywords:

    def __init__(self):
        self.page = None
        self.home_page = None

    async def async_init(self):
        self.page = await Browser.get_instance()
        if self.page is None:
            raise ValueError("Failed to initialize page.")
        self.home_page = Home_Page()

    @keyword("Open Application")
    async def open_application(self):
        if self.page is None:
            raise ValueError("Failed to initialize page.")
        await self.page.goto(constants.URL)

    @keyword("Tear Down Application")
    async def tear_down_application(self):
        if self.page:
            await Browser.close_app()
