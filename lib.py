class wrapper:

    def __init__(self, driver):
        self.driver = driver

    def clicks(self, locator):
        self.driver.find_element(*locator).click()

    def enters(self, locator, data):
        self.driver.find_element(*locator).send_keys(data)
