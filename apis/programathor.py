import time
import re
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

def clean_text(text):
    if text:
        return re.sub(r'\s+', ' ', text).strip()
    return None

# Subclasse para suprimir erro no __del__
class SilentChrome(uc.Chrome):
    def __del__(self):
        pass

def fetch_programathor_jobs(busca):
    jobs = []
    url = f"https://programathor.com.br/jobs-{busca}/remoto"

    options = uc.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")

    driver = None
    try:
        driver = SilentChrome(options=options, headless=True, use_subprocess=True)
        driver.get(url)
        time.sleep(5)

        for index in range(1, 21):
            try:
                empresa_xpath = f"/html/body/div[3]/div/div[2]/div[2]/div[{index}]/a/div/div[2]/div/div[1]/span[1]"
                cargo_xpath = f"/html/body/div[3]/div/div[2]/div[2]/div[{index}]/a/div/div[2]/div/h3"
                tags_xpath = f"/html/body/div[3]/div/div[2]/div[2]/div[{index}]/a/div/div[2]/div/div[2]"
                link_xpath = f"/html/body/div[3]/div/div[2]/div[2]/div[{index}]/a"

                empresa_el = driver.find_element(By.XPATH, empresa_xpath)
                cargo_el = driver.find_element(By.XPATH, cargo_xpath)
                tags_el = driver.find_element(By.XPATH, tags_xpath)
                link_el = driver.find_element(By.XPATH, link_xpath)

                empresa = clean_text(empresa_el.text)
                cargo = clean_text(cargo_el.text)
                if cargo.lower().startswith("vencida"):
                    continue

                tags = [tag.strip() for tag in tags_el.text.split("|") if tag.strip()]
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

    except Exception as e:
        print(f"[Programathor] Erro ao buscar vagas: {e}")
        if driver:
            try:
                driver.quit()
            except:
                pass

    return jobs
