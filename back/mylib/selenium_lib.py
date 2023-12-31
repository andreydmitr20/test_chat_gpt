import asyncio
from selenium import webdriver
from .config import config
from .log import log, d


async def selenium_connect(options=None):
    chromedriver_path = (
        config.selenium_prefix
        + config.selenium_host
        + ":"
        + config.selenium_port
        + config.selenium_postfix
    )
    try:
        if options is None:
            options = webdriver.ChromeOptions()
            options.add_argument("window-size=1280,1024")
            # options.add_argument("--headless")
            options.add_experimental_option("useAutomationExtension", False)
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
        driver = webdriver.Remote(
            command_executor=chromedriver_path,
            options=options,
        )
        # driver = webdriver.Chrome(options=options)
        # driver.get("https://google.com")
        return driver

    except Exception as exception:
        log.warning(f"{exception}")
        return None


async def selenium_disconnect(driver):
    if driver:
        driver.quit()
