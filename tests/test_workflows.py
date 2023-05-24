import time

from selenium import webdriver

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.top_bar import TopBar


def test_brainstorm():
    driver = webdriver.Chrome()

    # Create a new instance of the HomePage class
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    top_bar = TopBar(driver)

    # Login
    # login_page.login_user("https://app.seek.ai/login","gabriel+brainstorm@testseek.us","nCvD8a4t6XsPxUb")
    # time.sleep(10)
    #
    # # add report
    # home_page.create_new_report("Testing report","details")
    # time.sleep(5)
    # # add question
    # home_page.create_new_question('how many customers did we lose last year')
    # time.sleep(60)
    #
    # #open studio
    # top_bar.open_studio()
    # time.sleep(10)
    #
    # # regenerate the question
    # home_page.regenerate_question()
    # time.sleep(10)
    #
    # # logout
    # top_bar.logout()
    # time.sleep(10)

    # login in admin page
    login_page.login_user('https://app.seek.ai/admin/login','gabriel@testseek.us','FV55mYYaLRNkDfx')
    time.sleep(10)

    # clear text
    home_page.clean_text()

    # put SQL code

    # press to verify

    # logout

    # login again

    # assert if SQL code is correct

    # replace the SQL code

    # press answered button

    # logout

    # login in admin

    # search the question

    # assert the SQL Code

    # logout

    # login in customer

    # delete the question

    # logout

    # login in admin

    # when search the question - no results

    # logout

    # login

    # delete report
    time.sleep(100)
