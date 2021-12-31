from bs4 import BeautifulSoup
import requests
from utils import sender


URL = "https://www.brasiltronic.com.br/monitor-gamer-acer-nitro-xv280k-4k-60hz-ips-28-polegadas-amd-freesync-com-alto-falante-p1329178"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

site = requests.get(URL, headers=headers)
soup = BeautifulSoup(site.content, "html.parser")

title = soup.find("h1", class_="col-12").get_text().strip()
price = float(soup.find("strong", class_="sale-price").span.get_text().strip()[3:8])


if price <= 1000:
    sender.email_sender(URL)
