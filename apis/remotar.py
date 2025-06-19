import time
import re
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip() if text else None

class SilentChrome(uc.Chrome):
    def __del__(self):
        pass

def fetch_remotar_jobs(busca):
    driver = None
    try:
        jobs = []
        url = f"https://remotar.com.br/search/jobs?q=+{busca}&t=4"

        options = uc.ChromeOptions()
        options.add_argument("--headless=new")  # Comente esta linha se quiser ver o navegador rolando
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--window-size=1920,3000")
        options.add_argument("--disable-dev-shm-usage")

        driver = SilentChrome(options=options, headless=True, use_subprocess=True)
        driver.get(url)

        # Scroll dinâmico até o fim da página
        last_height = 0
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1.5)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        # Coleta das vagas após o scroll
        for index in range(2, 70):  # Margem ampla para até 50+ vagas
            try:
                base = f"/html/body/div/main/div/div[2]/div[3]/div/div[1]/div[{index}]/div/div/div"

                cargo_xpath = f"{base}/div[1]/div[2]/div[1]/a/p"
                empresa_xpath = f"{base}/div[1]/div[2]/div[2]/a/div/p[1]"
                tags_xpath = f"{base}/div[2]/div"
                link_xpath = f"{base}/div[3]/a"

                cargo_el = driver.find_element(By.XPATH, cargo_xpath)
                empresa_el = driver.find_element(By.XPATH, empresa_xpath)
                tags_el = driver.find_element(By.XPATH, tags_xpath)
                link_el = driver.find_element(By.XPATH, link_xpath)

                cargo = clean_text(cargo_el.text)
                empresa = clean_text(empresa_el.text)
                tags = [t.strip() for t in tags_el.text.split("#") if t.strip()]
                link = link_el.get_attribute("href")

                jobs.append({
                    'empresa': empresa,
                    'cargo': cargo,
                    'descricao': None,
                    'salario': None,
                    'tags': tags,
                    'link': link
                })

            except Exception:
                continue

        if driver:
            try:
                driver.quit()
            except:
                pass
            driver = None

        return jobs

    except Exception as e:
        print(f"[Remotar] Erro ao buscar vagas: {e}")
        if driver:
            try:
                driver.quit()
            except:
                pass
        return []
