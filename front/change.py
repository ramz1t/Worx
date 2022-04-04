import bs4


def change_text_by_element_id(element_id: str, text: str, filename: str):
    with open(filename) as file:
        txt = file.read()
        soup = bs4.BeautifulSoup(txt, 'lxml')

    old_tag = soup.select(element_id)
    old_tag[0].string = text

    with open(filename, "w") as file:
        file.write(str(soup))
