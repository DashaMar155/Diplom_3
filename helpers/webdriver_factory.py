import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

logger = logging.getLogger(__name__)

class WebdriverFactory:
    @staticmethod
    def get_webdriver(browser_name: str, headless: bool = False) -> webdriver.WebDriver:
        logger.info(f"Запускаем браузер: {browser_name} (headless={headless})")

        if browser_name.lower() == "firefox":
            options = FirefoxOptions()
            options.set_preference("dom.webnotifications.enabled", False)
            options.set_preference("media.navigator.permission.disabled", True)
            if headless:
                options.add_argument("--headless")
            return webdriver.Firefox(options=options)

        elif browser_name.lower() == "chrome":
            options = ChromeOptions()
            options.add_argument("--disable-notifications")
            if headless:
                options.add_argument("--headless")
            return webdriver.Chrome(options=options)

        else:
            logger.error(f"Unsupported browser: {browser_name}")
            raise ValueError(f"Unsupported browser: {browser_name}")

