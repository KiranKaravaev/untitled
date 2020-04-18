import time
import pyautogui
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


def exist_class_name(driver, name):
    exist = 1
    try:
        temp = driver.find_element_by_class_name(name)
    except:
        exist = 0
    return exist


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

    # login proxy
    pyautogui.typewrite('Selkirankaravaev')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.typewrite('X1j4BfB')
    time.sleep(1)
    pyautogui.press('enter')

    driver.get('https://rivalregions.com/')

    # enter google
    enter_google = driver.find_element_by_class_name("sa_sn.float_left.imp.gogo")
    enter_google.click()
    login = driver.find_element_by_class_name("whsOnd.zHQkBf")
    login.send_keys("karavaevkiran@gmail.com")
    login.submit()
    find_name_click_wait(driver, 'RveJvd.snByac', 5)  # next
    password = driver.find_element_by_class_name("whsOnd.zHQkBf")
    password.send_keys("rbh13z2001")
    password.submit()
    find_name_click_wait(driver, 'RveJvd.snByac', 2)  # next

    # build MA
    find_id_click_wait(driver, 'header_my_avatar', 1)  # profile
    find_name_click_wait(driver, 'tip.header_buttons_hover.slide_profile_link.tc', 1)  # residency
    if exist_class_name(driver, 'button_green.region_details_move'):  # exist region_move
        find_name_click_wait(driver, 'button_green.region_details_move', 1)  # region_move
        find_id_click_wait(driver, 'move_here', 1)  # move
        find_id_click_wait(driver, 'move_here_ok', 1)  # move_ok
        find_name_click_wait(driver, 'header_buttons_hover_close', 1)  # close
        find_name_reload(driver, 'button_red.pointer.map_d_b_ind.index_registartion_home', 1)
    else:
        find_name_click_wait(driver, 'header_buttons_hover_close', 1)  # close
    find_name_click_wait(driver, 'tip.hov.pointer.quest_have_perk_ma', 1)  # MA
    find_name_click_wait(driver, 'button_green.index_ma_quest', 1)  # MA build
    if exist_class_name(driver, 'button_white'):  # exist MA build ok
        find_name_click_wait(driver, 'button_white', 1)  # MA build ok
    find_name_click_wait(driver, 'header_buttons_hover_close', 1)  # close

    # build department

    '''
    find_name_click_wait(driver, 'item_menu.work_menu.ajax_action.header_menu_item.tc', 1)  # work
    find_name_click_wait(driver, 'dot.hov2.factory_slide', 1)  # factory
    find_name_click_wait(driver, 'factory_whose.hov2.wrap50.tc.pointer.width520.float_left', 1)  # region factory
    find_name_click_wait(driver, 'button_green.region_details_move', 1)  # region_move
    find_id_click_wait(driver, 'move_here', 1)  # move
    find_id_click_wait(driver, 'move_here_ok', 1)  # move_ok
    find_name_click_wait(driver, 'header_buttons_hover_close', 1)  # close
    '''
    time.sleep(10000)
    driver.quit()
'''
fghjklfhgkgjkkfhfhf
'''

if __name__ == '__main__':
    main()
