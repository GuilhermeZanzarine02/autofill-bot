import pyautogui as pg
import time, random
import requests

from Files.get_data import filter_name, get_data_fromCSV

def ensure_focus_on_browser():
    """Clica em uma posição fixa no navegador para garantir foco"""
    pg.moveTo(200, 200)
    pg.click()
    time.sleep(1.5)


def move_and_click(x, y):
    """Move o mouse para as posições (x, y) e clica."""

    pg.moveTo(x, y)
    time.sleep(1.5)
    pg.click()


def write_text(text):
    """Preenche o campo do formulário com um texto."""

    pg.write(text, interval=0.1)


def fill_name():
    """Função responsalvel por preencher o campo do nome."""
    name = filter_name()
    move_and_click(400, 270)
    time.sleep(1.5)
    write_text(name)
    time.sleep(1.5)


def fill_password():
    """Função responsalvel por preencher o campo do senha."""
    move_and_click(400, 370)
    time.sleep(1.5)
    write_text("@teste_123")
    time.sleep(1.5)

def fill_text_area():
     try:
        res = requests.get("https://api.chucknorris.io/jokes/random")

        if res.status_code == 200:
            data = res.json()
            joke = data['value']

     except Exception as e:
        print(f"Erro ao buscar texto: {e}")

     move_and_click(400, 470)
     time.sleep(1.5)
     write_text(joke)
     time.sleep

def fill_dropdown():
    position = [360, 420, 500]
    random_position = random.choice(position)
    move_and_click(800, 270)
    time.sleep(2)
    move_and_click(800, random_position)

def fill_ciy():
    city, email = get_data_fromCSV()
    random_city = random.choice(city)
    move_and_click(800, 400)
    time.sleep(1.5)
    write_text(random_city)
    time.sleep(1.5)

def send_form():
    move_and_click(800, 700)

