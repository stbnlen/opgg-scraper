from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from functions import get_page, get_games, get_details, results, get_damage_stats, create_dataframe

options = webdriver.EdgeOptions()
options.add_argument("-inprivate")
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

NAME = "Your_nickname"
REGION = "Your_region"

get_page(driver, NAME, REGION)

get_games(driver=driver)

get_details(driver=driver)


from bs4 import BeautifulSoup

html = driver.page_source

soup = BeautifulSoup(html, 'lxml')

div = soup.find('div', {'class': 'css-164r41r e1r5v5160'})
lis = div.find_all('li')


result_texts, game_type, kill, death, assist, length, champion, percentage, tier, cs, cs_per_minute, wards = results(lis=lis)


damage_dealt, damage_taken = get_damage_stats(soup=soup, name=NAME)


divs = soup.find_all('div', {'class': 'css-1dm3230 eo0wf2y0'})

game_items = []

for div in divs:
    tbodies = div.find_all('tbody')
    for tbody in tbodies:
        trs = tbody.find_all('tr')
        for tr in trs:
            td_name = tr.find('td', {'class': 'name'})
            if td_name and td_name.find('a', text='itzpipeqlo'):
                td_items = td_name.find_next_sibling('td', {'class': 'items'})
                td_it = td_items.find_all('img', {'width': '22'})
                items = [td['alt'] for td in td_it if td_it]
                game_items.append(items)


objetivos = []

for div in divs:
    resumen_divs = div.find_all('div', {'class': 'summary'})
    for resumen in resumen_divs:
        spans = resumen.find_all('span')
        # Usar list comprehensions para obtener los textos de los elementos span
        textos = [span.text for span in spans[:3]]  # Usar slicing para obtener los primeros 3 elementos
        objetivos.append(textos)


baron = [key1 if key1 else '0' for key1, _, _ in objetivos] + ['0'] * 7
dragon = [key2 if key2 else '0' for _, key2, _ in objetivos] + ['0'] * 7
tower = [key3 if key3 else '0' for _, _, key3 in objetivos] + ['0'] * 7


# Verificar que todas las listas tienen la misma longitud
assert all(len(lst) == len(result_texts) for lst in [champion, kill, death, assist, damage_dealt, damage_taken, game_type, length, percentage, tier, cs, cs_per_minute, game_items, wards, baron, dragon, tower, result_texts]), "Las listas tienen longitudes diferentes"

# Crear el DataFrame directamente desde las listas usando el constructor de pandas
objects = {
                "result": result_texts,
                "champion": champion,
                "kill": kill,
                "death": death,
                "assist": assist,
                "dmg_dealt": damage_dealt,
                "dmg_taken": damage_taken,
                "game_type": game_type,
                "length": length,
                "kill_percentage": percentage,
                "average_tier": tier,
                "cs": cs,
                "cs_per_minute": cs_per_minute,
                "items": game_items,
                "control_wards": wards,
                "baron": baron,
                "dragon": dragon,
                "tower": tower
            }

df = create_dataframe(objects)

df.to_csv('stats.csv')

driver.close()