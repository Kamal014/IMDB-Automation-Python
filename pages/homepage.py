import selenium.webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    search_bar = (By.CSS_SELECTOR, "#suggestion-search")
    home_icon = (By.ID, "home_img_holder")
    menu_icon = (By.XPATH, "//span[@class='ipc-responsive-button__text']")
    close_menu = (By.XPATH, "//label[@for ='imdbHeader-navDrawer'][@title= 'Close Navigation Drawer']")
    menus_quick_links = (By.XPATH, "//span[@class = 'ipc-list-item__text'][@role = 'presentation']")
    imdb_rating = (By.XPATH, "//div/div[@data-testid = 'hero-rating-bar__aggregate-rating__score']/span[@class]")
    top_10_on_imdb_this_week = (
        By.XPATH, "//div[@class = 'top-ten']/div[2]/div/div[@data-testid = 'shoveler']/div[2]/div/a/span")
    search_bar_dropdowns = (By.XPATH, "//li[@role= 'menuitem'] [@class='ipc-list__item searchCatSelector__item']/span")
    search_bar_dropdown_selected = (By.XPATH, "//label[@data-testid = 'category-selector-button']/span")

    def get_search_bar(self):
        return self.driver.find_element(*HomePage.search_bar)

    def get_home_icon(self):
        return self.driver.find_element(*HomePage.home_icon)

    def get_menu_icon(self):
        return self.driver.find_element(*HomePage.menu_icon)

    def get_close_menu(self):
        return self.driver.find_element(*HomePage.close_menu)

    def get_menus_quick_links(self):
        return self.driver.find_elements(*HomePage.menus_quick_links)

    def get_imdb_rating(self):
        return self.driver.find_element(*HomePage.imdb_rating)

    def get_search_bar_dropdowns(self):
        return self.driver.find_elements(*HomePage.search_bar_dropdowns)

    def get_search_bar_dropdown_selected(self):
        return self.driver.find_element(*HomePage.search_bar_dropdown_selected)
