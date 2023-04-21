import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.top_bar import TopBar
from pages.sql_console import SqlConsole


def test_brainstorm():
    driver = webdriver.Chrome()

    # Create a new instance of the HomePage class
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    top_bar = TopBar(driver)
    sql_console = SqlConsole(driver)
    #
    # # Login
    # login_page.login_user("https://app.seek.ai/login","gabriel+brainstorm@testseek.us","6i71i0qb2SG04YDG-")
    # time.sleep(15)
    # # Create report
    # home_page.create_new_report("Testing report","details")
    #
    # # Create question
    # home_page.create_new_question('how many customers did we lose last year')
    #
    # # Open Studio
    # time.sleep(20)
    # top_bar.open_studio()
    #
    # # Regenerate the question
    # time.sleep(5)
    # home_page.regenerate_question()

    # Login in admin
    login_page.login_user("https://app.seek.ai/admin/login", "gabriel@testseek.us", "m7sncc54SX14S2SM^")

    # Clean box
    time.sleep(10)
    sql_console.press_clear_console()

    time.sleep(10)

    sql_console.type_in_console('select * from compliance_platform_api_prod.public.products limit 5')

