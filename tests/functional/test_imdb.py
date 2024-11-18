import time
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.homepage import HomePage
from pages.searchdetail import SearchDetail
from test_data.test_data import TestData
from utils.movie_data import get_movie_name


@pytest.mark.usefixtures('browser_setup')
class Test:
    driver = webdriver.Chrome()

    # @pytest.mark.skip
    # def test_advance_search(self):
    #     self.driver.implicitly_wait(3)
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, "//label[@aria-label= 'All']").click()
    #     time.sleep(3)
    #     action = ActionChains(self.driver)
    #     action.move_to_element(self.driver.find_element(By.XPATH,
    #                                                     "//span[@class = 'ipc-list-item__text'][@role = 'presentation'][text()='Advanced Search']")).click().perform()
    #     time.sleep(3)
    #     self.driver.execute_script("window.scrollBy(0,500)")
    #     time.sleep(3)
    #     self.driver.find_element(By.CSS_SELECTOR, "#titleTypeAccordion").click()
    #     # assert self.driver.title is "https://www.imdb.com/search/title/"
    #     self.driver.find_element(By.XPATH, "//button[@data-testid = 'test-chip-id-movie']").click()
    #     result = self.driver.find_element(By.XPATH, "//button[@data-testid = 'adv-search-get-results']").get_attribute(
    #         "aria-disabled")
    #     print(result)
    #     time.sleep(3)
    #     self.driver.execute_script("window.scrollTo(0,0)")
    #     time.sleep(3)
    #     self.driver.find_element(By.CSS_SELECTOR, "#home_img_holder").click()
    #     time.sleep(3)
    #     self.driver.get_screenshot_as_file("..\\Screenshots\\homepage.png")

    def test_search(self, get_movie_name):
        homepage = HomePage(self.driver)
        movie = get_movie_name["movie"]
        homepage.get_search_bar().send_keys(movie)
        time.sleep(3)
        try:
            self.driver.find_element(By.XPATH, "//div[.= '{}']".format(movie)).click()
        except NoSuchElementException:
            print("No search result")
        homepage.get_home_icon().click()

    def test_search_detail(self, get_movie_name):
        homepage = HomePage(self.driver)
        search_detail = SearchDetail(self.driver)
        movie = get_movie_name["movie"]
        homepage.get_search_bar().send_keys(movie)
        time.sleep(3)
        try:
            self.driver.find_element(By.XPATH, "//div[.= '{}']".format(movie)).click()
            imdb_rating = homepage.get_imdb_rating().text
            print(f'{movie} imdb rating is {imdb_rating}')
            print(f'{movie} star cast names are:')
            casts = search_detail.get_casts()
            tests = search_detail.get_release_year()
            for cast_name in casts:
                print(cast_name.text)
            print(f'{movie} released in {tests[5].text}')
            award = self.driver.find_element(By.XPATH, "//span[@class = 'ipc-metadata-list-item__list-content-item']")
            print(award.text)
        except NoSuchElementException:
            print("No search result")
        homepage.get_home_icon().click()

    def test_searchbar_dropdown(self):
        homepage = HomePage(self.driver)
        self.driver.find_element(By.XPATH, "//label[@for = 'navbar-search-category-select']").click()
        dropdowns = homepage.get_search_bar_dropdowns()

        for index in range(len(dropdowns)):
            # Re-locate dropdown options
            dropdowns = homepage.get_search_bar_dropdowns()
            option = dropdowns[index]
            option_text = option.text
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(option))
            option.click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(homepage.search_bar_dropdown_selected))
            assert homepage.get_search_bar_dropdown_selected().is_displayed()
            assert option_text == homepage.get_search_bar_dropdown_selected().text
            print(option_text)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//label[@for = 'navbar-search-category-select']"))
            ).click()
        print("All options checked")

    # def test_top_250_movies(self):
    #     self.driver.implicitly_wait(3)
    #     self.driver.find_element(By.XPATH, "//span[@class = 'ipc-responsive-button__text']").click()
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH, "//span[@role = 'presentation'][contains(text(), 'Top 250 Movies')]").click()
    #     action = ActionChains(self.driver)
    #     action.scroll_to_element(self.driver.find_element(By.XPATH,
    #                                                       "//div[@class = 'ipc-title ipc-title--base ipc-title--title ipc-title--on-textPrimary sc-647780dc-4 fqGBJc yhr-title']"))
    #     time.sleep(3)
    #     movies_list = self.driver.find_elements(By.XPATH,
    #                                             "//div[@class = 'sc-b189961a-0 hBZnfJ cli-children']//h3[@class = 'ipc-title__text']")
    #     for movie in movies_list:
    #         print(movie.text)
    #     self.driver.execute_script("window.scrollTo(0,0)")
    #
    # @pytest.fixture(params=TestData.menu_items)
    # def get_menu_item(self, request):
    #     return request.param

    # def test_menu_items(self, get_menu_item):
    #     homepage = HomePage(self.driver)
    #     homepage.get_home_icon().click()
    #     homepage.get_menu_icon().click()
    #     wait = WebDriverWait(self.driver, 10)
    #     for item in homepage.get_menus_quick_links():
    #         if item.text in get_menu_item["release_calendar"]:
    #             item.click()
    #             wait.until(EC.url_to_be('https://www.imdb.com/calendar/?ref_=nv_mv_cal'))
    #             self.driver.get_screenshot_as_file("..\\Screenshots\\release_calendar.png")
    #             homepage.get_menu_icon().click()
    #             break
    #     for item in homepage.get_menus_quick_links():
    #         if item.text in get_menu_item["top_250_movies"]:
    #             item.click()
    #             wait.until(EC.url_to_be('https://www.imdb.com/chart/top/?ref_=nv_mv_250'))
    #             self.driver.get_screenshot_as_file("..\\Screenshots\\top_250_movies.png")
    #             homepage.get_menu_icon().click()
    #             break
    #     for item in homepage.get_menus_quick_links():
    #         if item.text in get_menu_item["most_popular_movies"]:
    #             item.click()
    #             wait.until(EC.url_to_be('https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'))
    #             self.driver.get_screenshot_as_file("..\\Screenshots\\most_popular_movies.png")
    #             homepage.get_menu_icon().click()
    #             break
    # elif item.text == get_menu_item["browse_movies_by_genre"]:
    #     item.click()
    #     wait.until(EC.url_to_be('https://www.imdb.com/interest/all/'))
    #     self.driver.get_screenshot_as_file("..\\Screenshots\\browse_movies_by_genre.png")
    #     homepage.get_home_icon().click()
    #     homepage.get_menu_icon().click()
    # elif item.text == get_menu_item["top_box_office"]:
    #     item.click()
    #     wait.until(EC.url_to_be('https://www.imdb.com/chart/boxoffice/?ref_=nv_ch_cht'))
    #     self.driver.get_screenshot_as_file("..\\Screenshots\\top_box_office.png")
    #     homepage.get_home_icon().click()
    #     homepage.get_menu_icon().click()
    # elif item.text == get_menu_item["showtimes_and_tickets"]:
    #     item.click()
    #     wait.until(EC.url_to_be('https://www.imdb.com/showtimes/?ref_=nv_mv_sh'))
    #     self.driver.get_screenshot_as_file("..\\Screenshots\\showtimes_and_tickets.png")
    #     homepage.get_home_icon().click()
    #     homepage.get_menu_icon().click()
    # elif item.text == get_menu_item["movie_news"]:
    #     item.click()
    #     wait.until(EC.url_to_be('https://www.imdb.com/news/movie/?ref_=nv_nw_mv'))
    #     self.driver.get_screenshot_as_file("..\\Screenshots\\movie_news.png")
    #     homepage.get_home_icon().click()
    #     homepage.get_menu_icon().click()
    # elif item.text == get_menu_item["india_movie_spotlight"]:
    #     item.click()
    #     wait.until(EC.url_to_be('https://www.imdb.com/india/toprated/?ref_=nv_mv_in'))
    #     self.driver.get_screenshot_as_file("..\\Screenshots\\india_movie_spotlight.png")
    #     homepage.get_home_icon().click()
    #     homepage.get_menu_icon().click()
    # else:
    #     homepage.get_home_icon().click()

    # url = self.driver.current_url
    # assert url is "https://www.imdb.com/originals/?ref_=nv_sf_ori"
    # time.sleep(3)
    # upcoming_movies = self.driver.find_elements(By.XPATH, "//a[@class='ipc-metadata-list-summary-item__t']")
    # for movie in upcoming_movies:
    #     print(movie.text)
    # ----------------------#
    # ----------------------#
