from typing import List
from bs4 import BeautifulSoup


class GameStatsExtractor:
    def __init__(self, soup: BeautifulSoup):
        self.soup = soup

        self.div = self.soup.find("div", {"class": "css-164r41r e1r5v5160"})
        self.lis = self.div.find_all("li")

        self.divs = self.soup.find_all("div", {"class": "css-1dm3230 eo0wf2y0"})

    def extract_element_text(self, lis, class_name):
        return [
            li.find("div", {"class": class_name}).text
            for li in lis
            if li.find("div", {"class": class_name})
        ]

    def extract_element_split(self, lis, class_name, split_char):
        return [
            li.find("div", {"class": class_name}).text.split(split_char)
            for li in lis
            if li.find("div", {"class": class_name})
        ]

    def extract_game_results(self):
        champion = []
        cs, cs_per_minute = [], []

        result_texts = self.extract_element_text(self.lis, "result")
        game_type = self.extract_element_text(self.lis, "type")
        length = self.extract_element_text(self.lis, "length")
        percentage = self.extract_element_text(self.lis, "p-kill")
        wards = self.extract_element_text(self.lis, "ward")
        tier = self.extract_element_text(self.lis, "average-tier")

        kda = self.extract_element_split(self.lis, "k-d-a", "/")
        kill = [kda_part[0] for kda_part in kda]
        death = [kda_part[1] for kda_part in kda]
        assist = [kda_part[2] for kda_part in kda]

        for li in self.lis:
            icon_div = li.find("div", {"class": "icon"})
            if icon_div:
                img_tag = icon_div.find("img", {"width": "48"})
                if img_tag:
                    alt_text = img_tag["alt"]
                    champion.append(alt_text)

            cs_div = li.find("div", {"class": "cs"})
            if cs_div:
                cs_total = cs_div.text.split(" ")
                cs.append(cs_total[1])
                cs_per_minute.append(cs_total[2])

        return (
            result_texts,
            game_type,
            kill,
            death,
            assist,
            length,
            champion,
            percentage,
            tier,
            cs,
            cs_per_minute,
            wards,
        )

    def get_damage(self, name: str, damage_type: str) -> List[str]:
        damage = []

        trs = [
            tr
            for div in self.divs
            for tbody in div.find_all("tbody")
            for tr in tbody.find_all("tr")
        ]
        for tr in trs:
            td_name = tr.find("td", {"class": "name"})
            if td_name and td_name.find("a", text=name):
                td_damage = tr.find("td", {"class": "damage"})
                div_damage = td_damage.find("div", {"class": damage_type})
                if div_damage:
                    damage.append(div_damage.text)

        return damage

    def get_game_items(self) -> List[List[str]]:
        game_items = []

        for div in self.divs:
            tbodies = div.find_all("tbody")
            for tbody in tbodies:
                trs = tbody.find_all("tr")
                for tr in trs:
                    td_name = tr.find("td", {"class": "name"})
                    if td_name and td_name.find("a", text="itzpipeqlo"):
                        td_items = td_name.find_next_sibling("td", {"class": "items"})
                        td_it = td_items.find_all("img", {"width": "22"})
                        items = [td["alt"] for td in td_it if td_it]
                        game_items.append(items)

        return game_items

    def get_game_objectives(self):
        objetivos = []

        for div in self.divs:
            resumen_divs = div.find_all("div", {"class": "summary"})
            for resumen in resumen_divs:
                spans = resumen.find_all("span")
                textos = [span.text for span in spans[:3]]
                objetivos.append(textos)

        baron = [key1 if key1 else "0" for key1, _, _ in objetivos] + ["0"] * 4
        dragon = [key2 if key2 else "0" for _, key2, _ in objetivos] + ["0"] * 4
        tower = [key3 if key3 else "0" for _, _, key3 in objetivos] + ["0"] * 4

        return baron, dragon, tower
