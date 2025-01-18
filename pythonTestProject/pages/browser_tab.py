from pythonTestProject.components.components import WebElement
from pythonTestProject.pages.base_page import BasePage


class BrowserWindows(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/browser-windows'
        super().__init__(driver, self.base_url)

        self.new_tab = WebElement(driver, '#tabButton')
        