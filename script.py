import time
import pyautogui
from tkinter import *
import math
from selenium import webdriver


def find_name_click_wait(driver, name, time_wait):
    element = driver.find_element_by_class_name(name)
    element.click()
    time.sleep(time_wait)


def find_id_click_wait(driver, id, time_wait):
    element = driver.find_element_by_id(id)
    element.click()
    time.sleep(time_wait)


def find_name_reload(driver, name, time_wait):
    while 1:
        driver.refresh()
        time.sleep(time_wait)
        try:
            temp = driver.find_element_by_class_name(name)
        except:
            break


def find_id_reload(driver, id, time_wait):
    while 1:
        driver.refresh()
        time.sleep(time_wait)
        try:
            temp = driver.find_element_by_id(id)
        except:
            break


def exist_class_name(driver, name):
    try:
        temp = driver.find_element_by_class_name(name)
    except:
        return 0
    return 1


def exist_id(driver, id):
    try:
        temp = driver.find_element_by_id(id)
    except:
        return 0
    return 1


def build_MA(driver):
    # build MA
    find_id_click_wait(driver, 'header_my_avatar', 3)  # profile
    find_name_click_wait(driver, 'tip.header_buttons_hover.slide_profile_link.tc', 3)  # residency
    if exist_class_name(driver, 'button_green.region_details_move'):  # exist region_move
        find_name_click_wait(driver, 'button_green.region_details_move', 3)  # region_move
        find_id_click_wait(driver, 'move_here', 3)  # move
        find_id_click_wait(driver, 'move_here_ok', 3)  # move_ok
        find_name_click_wait(driver, 'header_buttons_hover_close', 3)  # close
        find_name_reload(driver, 'button_red.pointer.map_d_b_ind.index_registartion_home', 3)
    else:
        find_name_click_wait(driver, 'header_buttons_hover_close', 3)  # close
    find_name_click_wait(driver, 'tip.hov.pointer.quest_have_perk_ma', 3)  # MA
    find_name_click_wait(driver, 'button_green.index_ma_quest', 3)  # MA build
    if exist_class_name(driver, 'button_green.button_academy'):  # exist MA build ok
        find_name_click_wait(driver, 'button_green.button_academy', 3)  # MA build ok
    find_name_click_wait(driver, 'header_buttons_hover_close', 3)  # close


def auto_work(driver):
    # auto work
    find_name_click_wait(driver, 'item_menu.work_menu.ajax_action.header_menu_item.tc', 3)  # work
    if exist_class_name(driver, 'tip.button_white.no_pointer'):  # exist white btn work
        find_name_click_wait(driver, 'dot.hov2.factory_slide', 3)  # factory
        find_name_click_wait(driver, 'factory_whose.hov2.wrap50.tc.pointer.width520.float_left', 3)  # region factory
        find_name_click_wait(driver, 'button_green.region_details_move', 1)  # region_move
        find_id_click_wait(driver, 'move_here', 3)  # move
        find_id_click_wait(driver, 'move_here_ok', 3)  # move_ok
        find_name_click_wait(driver, 'header_buttons_hover_close', 3)  # close
        find_name_reload(driver, 'tip.button_white.no_pointer', 3)
    if exist_class_name(driver, 'work_w_autom.button_red.tip'):
        find_name_click_wait(driver, 'work_w_autom.button_red.tip', 3)  # auto work


def enter_google(driver, login, password):
    # enter google
    enter_google = driver.find_element_by_class_name("sa_sn.float_left.imp.gogo")
    enter_google.click()
    login_enter_enter(driver, login, password)


def login_tab_enter(driver, login, password):
    # enter proxy
    pyautogui.typewrite(login)
    time.sleep(3)
    pyautogui.press('tab')
    time.sleep(3)
    pyautogui.typewrite(password)
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)


def login_enter_enter(driver, login, password):
    # enter proxy
    pyautogui.typewrite(login)
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.typewrite(password)
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)


def main():

    # init proxy
    proxy_host = "176.114.8.14"
    proxy_port = 45785

    # init Firefox profile
    fp = webdriver.FirefoxProfile()
    fp.set_preference("network.proxy.type", 1)
    fp.set_preference("network.proxy.http", proxy_host)
    fp.set_preference("network.proxy.http_port", proxy_port)
    fp.set_preference("network.proxy.https", proxy_host)
    fp.set_preference("network.proxy.https_port", proxy_port)
    fp.set_preference("network.proxy.ssl", proxy_host)
    fp.set_preference("network.proxy.ssl_port", proxy_port)
    fp.set_preference("network.proxy.ftp", proxy_host)
    fp.set_preference("network.proxy.ftp_port", proxy_port)

    driver = webdriver.Firefox(firefox_profile=fp)
    driver.get("https://rivalregions.com/")
    time.sleep(1)

    login_tab_enter(driver, 'Selkirankaravaev', 'X1j4BfB')

    enter_google(driver, 'karavaevkiran@gmail.com', 'rbh13z2001')
    find_name_click_wait(driver, 'item_menu.wars_menu.ajax_action.header_menu_item.tc', 3)
    find_name_click_wait(driver, 'button_blue.war_4_start', 3)
    find_name_click_wait(driver, 'tip.button_green.hide_for_guide.war_w_auto_wd', 3)
    if exist_class_name(driver, 'tip.button_green.hide_for_guide.war_w_auto_wd'):
        find_id_reload(driver, 'header_my_fill_bar_countdown', 30)
        find_id_click_wait(driver, 'header_my_fill_bar', 3)


    time.sleep(10000)
    driver.quit()


if __name__ == '__main__':
    main()
