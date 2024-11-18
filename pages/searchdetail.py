from selenium.webdriver.common.by import By


class SearchDetail:
    def __init__(self, driver):
        self.driver = driver

    casts = (By.XPATH, "//div[@role='presentation']/ul/li[3]/div")
    release_year = (By.XPATH, "//a[@class = 'ipc-link ipc-link--baseAlt ipc-link--inherit-color']")

    def get_casts(self):
        return self.driver.find_elements(*SearchDetail.casts)

    def get_release_year(self):
        return self.driver.find_elements(*SearchDetail.release_year)
