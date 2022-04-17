import bs4
import json
import requests


def change_text_by_element_id(element_id: str, text: str, filename: str):
    with open(filename) as file:
        txt = file.read()
        soup = bs4.BeautifulSoup(txt, 'lxml')

    tag = soup.select(element_id)
    tag[0].string = text

    with open(filename, "w") as file:
        file.write(str(soup))


def change_page(data, filename: str):
    with open(filename) as file:
        text = file.read()
        soup = bs4.BeautifulSoup(text, 'lxml')

    for element_id in data:
        tag = soup.select('#' + element_id)
        tag[0].string = str(data[element_id])

    with open(filename, "w") as file:
        file.write(str(soup))
