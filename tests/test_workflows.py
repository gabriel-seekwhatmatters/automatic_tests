import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.command_palette_admin import CommandPaletteAdmin
from pages.command_palette_client import CommandPaletteClient
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.question_search_page import QuestionSearchPage
from pages.top_bar import TopBar
from pages.tree_view import TreeView


def test_brainstorm():
    driver = webdriver.Chrome()

    # Create a new instance of the HomePage class
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    top_bar = TopBar(driver)
    command_palette_admin = CommandPaletteAdmin(driver)
    command_palette_client = CommandPaletteClient(driver)
    tree_view = TreeView(driver)
    question_search_page = QuestionSearchPage(driver)

    # Login
    login_page.login_user("https://app.seek.ai/login","gabriel+brainstorm@testseek.us","nCvD8a4t6XsPxUb")
    time.sleep(25)

    # add report
    home_page.create_new_report("Testing report","details")
    time.sleep(5)
    # add question
    home_page.create_new_question('how many customers did we lose last year')
    time.sleep(60)

    # open studio
    top_bar.open_studio()
    time.sleep(10)

    # regenerate the question
    x = driver.current_url
    home_page.regenerate_question()
    time.sleep(60)

    # logout
    top_bar.logout_client()
    time.sleep(10)

    # login in admin page
    login_page.login_user('https://app.seek.ai/admin/login','gabriel@testseek.us','FV55mYYaLRNkDfx')
    time.sleep(20)

    # make sure the correct command palette it's displayed
    command_palette_admin.check_current_command_palette('Account Name: Seek Testing')

    # clear text
    # command_palette_admin.clean_text_admin()
    #
    # # put SQL code
    # command_palette_admin.write_text_admin("select count(*) from BSI_SAASY_PROD.BSI_REPORTING.REPORT_LICENSING_PACKS_CUSTOMER_PACKS_VIEW where \"STATUS\" = 'cancelled' and \"DATEADDED\" >= '2022-01-01' and \"DATEADDED\" < '2023-01-01'")
    #
    # # press to verify
    # home_page.press_verify_button()
    # time.sleep(20)
    # # logout
    # top_bar.logout_admin()
    #
    # # login again
    # login_page.login_user("https://app.seek.ai/login", "gabriel+brainstorm@testseek.us", "nCvD8a4t6XsPxUb")
    #
    # # assert if SQL code is correct
    # time.sleep(10)
    # tree_view.open_specific_number_rapport_and_question("5")
    # time.sleep(20)
    # y = driver.find_element(By.CSS_SELECTOR,
    #                         '#root > div.MuiBox-root.css-1pco6v8 > div > div > main > div > div > div.MuiBox-root.css-bgpqg > div > div.MuiBox-root.css-bpra72 > div > div > div > section > div > div > div.overflow-guard > textarea').get_attribute(
    #     'value')
    # print(y)
    # print("select count(*) from BSI_SAASY_PROD.BSI_REPORTING.REPORT_LICENSING_PACKS_CUSTOMER_PACKS_VIEW where \"STATUS\" = 'cancelled' and \"DATEADDED\" >= '2022-01-01' and \"DATEADDED\" < '2023-01-01'")
    # assert y == "select count(*) from BSI_SAASY_PROD.BSI_REPORTING.REPORT_LICENSING_PACKS_CUSTOMER_PACKS_VIEW where \"STATUS\" = 'cancelled' and \"DATEADDED\" >= '2022-01-01' and \"DATEADDED\" < '2023-01-01'";
    #
    # # replace the SQL code
    # command_palette_client.clean_text_from_client()
    # command_palette_client.write_text_client("select count(*) from BSI_SAASY_PROD.BSI_REPORTING.REPORT_LICENSING_PACKS_CUSTOMER_PACKS_VIEW where \"STATUS\" = 'cancelled'")
    #
    # # press answered button
    # home_page.press_mark_as_answered_button()
    # time.sleep(20)
    #
    # # logout
    # top_bar.logout_client()
    # time.sleep(10)
    #
    # # login in admin
    # login_page.login_user('https://app.seek.ai/admin/login', 'gabriel@testseek.us', 'FV55mYYaLRNkDfx')
    # time.sleep(20)
    #
    # # search the question
    # top_bar.open_question_search_tab_admin()
    # time.sleep(2)
    # question_search_page.select_specific_client_from_dropdown("Brainstorm")

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
    # time.sleep(100)
