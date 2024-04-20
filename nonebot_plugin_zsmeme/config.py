import requests
from lxml import etree
import random




url = 'https://wiki.biligame.com/zspms/%E8%A1%A8%E6%83%85%E5%8C%85'
response = requests.get(url).text
html = etree.HTML(response)
def the_link_url():
    list_path = html.xpath(f"/html/body/div[2]/div[2]/div[4]/div[5]/div/ul[{random.randint(1,2)}]/li")
    url_list = []
    for the_path in list_path:
        url_path = the_path.xpath("./div/div/div/a/@href")[0]
        url_list.append(url_path)
    link_url = random.choice(url_list)
    return link_url


def the_meme_url():
    meme_home_page = 'https://wiki.biligame.com' + the_link_url()
    meme_response = requests.get(meme_home_page).text
    meme_html = etree.HTML(meme_response)
    meme_url = meme_html.xpath("/html/body/div[2]/div[2]/div[4]/div[4]/div[2]/p[1]/a/@href")[0]
    return meme_url

