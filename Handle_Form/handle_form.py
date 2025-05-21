import pyautogui as pg
import subprocess as sb
import time 
import random
import requests

from Handle_Form.form_actions import ensure_focus_on_browser, fill_name, fill_password, fill_text_area, fill_dropdown, fill_ciy, send_form

class Form:
    def __init__(self):
        pass

    def load_from(self):
        edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        url = "https://www.selenium.dev/selenium/web/web-form.html"
        sb.Popen([edge_path, url]) 

    def fill_form(self):
        ensure_focus_on_browser()
        fill_name()
        fill_password()
        fill_text_area()
        fill_dropdown()
        fill_ciy()
        send_form()