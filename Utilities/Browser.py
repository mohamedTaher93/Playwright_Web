import logging

import pyautogui

from playwright.async_api import async_playwright
import os
import sys
from playwright.async_api import Page


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Resources import constants



class Browser:

    screen_width, screen_height = pyautogui.size()
    _playwright = None
    _instance = None


    # @classmethod
    # async def get_instance(cls):
    #     browser_name = await constants.BROWSER.lower()
    #     if cls._instance is None:
    #         _playwright = await async_playwright().start()
    #         if browser_name.__eq__("chrome"):
    #             browser = await _playwright.chromium.launch(headless=False)
    #             await browser.new_context(viewport={"width": cls.screen_width, "height": cls.screen_height})
    #             cls._instance = await browser.new_page(java_script_enabled=True)
    #         else:
    #             raise ValueError(f"Invalid browser name {browser_name}")
    #     return cls._instance

    @classmethod
    async def get_instance(cls) -> Page:
        browser_name = await constants.BROWSER.lower()
        if cls._instance is None:
            async with async_playwright() as p:
                if browser_name.__eq__("chrome"):
                    browser = await p.chromium.launch(headless=False)
                    await browser.new_context(viewport={"width": cls.screen_width, "height": cls.screen_height})
                    cls._instance = await browser.new_page(java_script_enabled=True)
                else:
                    raise ValueError(f"Invalid browser name {browser_name}")
        return cls._instance

    @classmethod
    async def tear_down(cls):
        if cls._instance:
            await cls.close_app()
        if cls._playwright:
            logging.info("Stop the session")
            await cls._playwright.stop()

    @classmethod
    async def close_app(cls):
        logging.info("Closing the browser")
        await cls._instance.close()
        cls._instance = None