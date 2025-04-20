from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.chrome.options import Options # type: ignore
import base64
import urllib.parse
import time

def obtener_partidos():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(options=chrome_options)
    partidos_info = []

    try:
        driver.get("https://futbollibre.futbol/es/agenda/")
        time.sleep(2)

        partidos = driver.find_elements(By.CSS_SELECTOR, "ul.menu > li")

        for partido in partidos:
            try:
                titulo = partido.find_element(By.TAG_NAME, "a").text.strip()
                subitems = partido.find_elements(By.CSS_SELECTOR, "li.subitem1 > a")

                for sub in subitems:
                    href = sub.get_attribute("href")
                    parsed_url = urllib.parse.urlparse(href)
                    query = urllib.parse.parse_qs(parsed_url.query)
                    encoded_url = query.get("r", [None])[0]

                    if encoded_url:
                        decoded_url = base64.b64decode(encoded_url).decode("utf-8")
                        
                        # Abrimos el enlace para extraer el iframe sin publicidad
                        try:
                            driver.get(decoded_url)
                            time.sleep(2)
                            iframe = driver.find_element(By.TAG_NAME, "iframe")
                            enlace_limpio = iframe.get_attribute("src")

                            partidos_info.append({
                                "titulo": titulo,
                                "enlace": enlace_limpio
                            })
                        except Exception:
                            # Si falla, devolvemos el enlace decodificado base64 original
                            partidos_info.append({
                                "titulo": titulo,
                                "enlace": decoded_url
                            })
            except:
                continue

        return partidos_info

    finally:
        driver.quit()
