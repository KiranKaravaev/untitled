import time
import pyautogui
from tkinter import *
import math
from selenium import webdriver


class Browser:
    def __init__(self):
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

        self.driver = webdriver.Firefox(firefox_profile=fp)

    def connect_site(self, url):
        self.driver.get(url)

    def find_name_click_wait(self, name, time_wait):
        element = self.driver.find_element_by_class_name(name)
        element.click()
        time.sleep(time_wait)

    def find_id_click_wait(self, id, time_wait):
        element = self.driver.find_element_by_id(id)
        element.click()
        time.sleep(time_wait)

    def find_name_reload(self, name, time_wait):
        while 1:
            self.driver.refresh()
            time.sleep(time_wait)
            try:
                temp = self.driver.find_element_by_class_name(name)
            except:
                break

    def find_id_reload(self, id, time_wait):
        while 1:
            self.driver.refresh()
            time.sleep(time_wait)
            try:
                temp = self.driver.find_element_by_id(id)
            except:
                break

    def exist_class_name(self, name):
        try:
            temp = self.driver.find_element_by_class_name(name)
        except:
            return 0
        return 1

    def exist_id(self, id):
        try:
            temp = self.driver.find_element_by_id(id)
        except:
            return 0
        return 1

    def build_MA(self):
        # build MA
        self.find_id_click_wait('header_my_avatar', 3)  # profile
        self.find_name_click_wait('tip.header_buttons_hover.slide_profile_link.tc', 3)  # residency
        if self.exist_class_name('button_green.region_details_move'):  # exist region_move
            self.find_name_click_wait('button_green.region_details_move', 3)  # region_move
            self.find_id_click_wait('move_here', 3)  # move
            self.find_id_click_wait('move_here_ok', 3)  # move_ok
            self.find_name_click_wait('header_buttons_hover_close', 3)  # close
            self.find_name_reload('button_red.pointer.map_d_b_ind.index_registartion_home', 3)
        else:
            self.find_name_click_wait('header_buttons_hover_close', 3)  # close
        self.find_name_click_wait('tip.hov.pointer.quest_have_perk_ma', 3)  # MA
        self.find_name_click_wait('button_green.index_ma_quest', 3)  # MA build
        if self.exist_class_name('button_green.button_academy'):  # exist MA build ok
            self.find_name_click_wait('button_green.button_academy', 3)  # MA build ok
        self.find_name_click_wait('header_buttons_hover_close', 3)  # close

    def auto_work(self):
        # auto work
        self.find_name_click_wait('item_menu.work_menu.ajax_action.header_menu_item.tc', 3)  # work
        if self.exist_class_name('tip.button_white.no_pointer'):  # exist white btn work
            self.find_name_click_wait('dot.hov2.factory_slide', 3)  # factory
            self.find_name_click_wait('factory_whose.hov2.wrap50.tc.pointer.width520.float_left', 3)  # region factory
            self.find_name_click_wait('button_green.region_details_move', 1)  # region_move
            self.find_id_click_wait('move_here', 3)  # move
            self.find_id_click_wait('move_here_ok', 3)  # move_ok
            self.find_name_click_wait('header_buttons_hover_close', 3)  # close
            self.find_name_reload('tip.button_white.no_pointer', 3)
        if self.exist_class_name('work_w_autom.button_red.tip'):
            self.find_name_click_wait('work_w_autom.button_red.tip', 3)  # auto work

    def enter_google(self, login, password):
        # enter google
        enter_google = self.driver.find_element_by_class_name("sa_sn.float_left.imp.gogo")
        enter_google.click()
        self.login_enter_enter(login, password)

    @staticmethod
    def login_tab_enter(login, password):
        # enter proxy
        pyautogui.typewrite(login)
        time.sleep(3)
        pyautogui.press('tab')
        time.sleep(3)
        pyautogui.typewrite(password)
        time.sleep(3)
        pyautogui.press('enter')
        time.sleep(3)

    @staticmethod
    def login_enter_enter(login, password):
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

    browser = Browser()
    browser.connect_site("https://rivalregions.com")
    time.sleep(3)
    browser.login_tab_enter('Selkirankaravaev', 'X1j4BfB')
    browser.connect_site("https://rivalregions.com")
    browser.enter_google('karavaevkiran@gmail.com', 'rbh13z2001')
  #  browser.enter_google('karavaevkiran@gmail.com', 'rbh13z2001')

    time.sleep(10000)


if __name__ == '__main__':
    main()
