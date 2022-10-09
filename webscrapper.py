import json
import re
import urllib.request

from bs4 import BeautifulSoup


# 0.000001 v archivu se mění pouze číslo, pak stačí načíst stránku a scrapnout

def open_html(htmlurl):
    html = urllib.request.urlopen(htmlurl)
    return BeautifulSoup(html.read(), "html.parser")


def load_links_from_html(page, links):
    results = page.find_all("a", class_="art-link", href=True)  # art-link = označení class pro články
    for link in results:
        links.append(link.get('href'))
    return links


def scrap_idnes(urls):
    info = []
    for link in urls:
        if "idnes" in link:
            soup = open_html(link)
            description = soup.find("script").text
            if 'premium=false' in description and '"zobrazeni": "clanek"' in description and \
                    '"section": "Ona"' not in description:
                title = soup.find("title").text.replace(' - iDNES.cz', '')  # nalezení nadpisu a odstranění textu navíc
                time = soup.find(class_="time-date").text  # time
                img = soup.find(class_="more-gallery")  # number of imgs
                if img is not None:
                    img_n = re.findall("\d+", img.text)[0]
                else:
                    img_n = 1
                section = soup.find("script").text  # find section
                reg_section = re.compile(r'\bsection\b["]: \".*?\"')
                sec = re.findall(reg_section, section)[0].split(":")[1].replace('"', "")
                opener = soup.find(class_="opener") # Welcome text of the site
                if opener is None:
                    allText = ""
                else:
                    allText = opener.text.replace("\r\n", "")
                itext = soup.find(class_="bbtext")  # text of idnes site
                for item in itext.findAll('p'):
                    allText += item.text
                info.append([title, time, img_n, sec, allText])
    return info


def main_app(n):
    empty_links = []
    soup = open_html("https://www.idnes.cz/zpravy/archiv/" + str(n) + "?idostrova=idnes")
    links = load_links_from_html(soup, empty_links)
    return scrap_idnes(links)
