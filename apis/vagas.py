import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip() if text else None

def fetch_vagas_jobs(busca):
    try:
        jobs = []
        url = f"https://www.vagas.com.br/vagas-de-{busca}?m%5B%5D=100%25+Home+Office"

        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--log-level=3")              # Minimiza logs do Chrome
        options.add_argument("--disable-logging")          # Desativa logs do Selenium
        options.add_argument("--disable-dev-shm-usage")    # Alternativa para containers


        driver = webdriver.Chrome(options=options)
        driver.get(url)
        time.sleep(5)

        for index in range(1, 21):
            try:
                base = f"/html/body/div[2]/div[3]/div/div/div[2]/section/section/div/ul/li[{index}]"

                empresa_xpath = f"{base}/header/div[2]/span"
                cargo_xpath = f"{base}/header/div[2]/h2/a"
                descricao_xpath = f"{base}/div/p"
                link_xpath = f"{base}/header/div[2]/h2/a"

                empresa_el = driver.find_element(By.XPATH, empresa_xpath)
                cargo_el = driver.find_element(By.XPATH, cargo_xpath)
                descricao_el = driver.find_element(By.XPATH, descricao_xpath)
                link_el = driver.find_element(By.XPATH, link_xpath)

                empresa = clean_text(empresa_el.text)
                cargo = clean_text(cargo_el.text)
                descricao = clean_text(descricao_el.text)
                link = link_el.get_attribute("href")

                jobs.append({
                    'empresa': empresa,
                    'cargo': cargo,
                    'descricao': descricao,
                    'salario': None,
                    'tags': [],
                    'link': link
                })

            except Exception:
                continue

        driver.quit()
        return jobs

    except Exception as e:
        print(f"[Vagas.com] Erro ao buscar vagas: {e}")
        return []
