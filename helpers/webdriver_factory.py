from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class WebdriverFactory:
    @staticmethod
    def get_webdriver(browser_name):
        print(f"🧪 Запускаем браузер: {browser_name}")

        if browser_name == "firefox":
            options = FirefoxOptions()
            options.set_preference("dom.webnotifications.enabled", False)
            options.set_preference("media.navigator.permission.disabled", True)
            # options.add_argument("--headless")  # если нужно без GUI
            return webdriver.Firefox(options=options)

        elif browser_name == "chrome":
            options = ChromeOptions()
            options.add_argument("--disable-notifications")
            return webdriver.Chrome(options=options)

        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
