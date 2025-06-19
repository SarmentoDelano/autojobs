import time
import re
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

def clean_text(text):
    if text:
        return re.sub(r'\s+', ' ', text).strip()
    return None

# Subclasse que evita erro WinError 6
class SilentChrome(uc.Chrome):
    def __del__(self):
        pass

def fetch_gupy_jobs(busca):
    driver = None
    try:
        jobs = []
        url = f"https://portal.gupy.io/job-search/term={busca}&workplaceTypes[]=remote"

        options = uc.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-dev-shm-usage")

        driver = SilentChrome(options=options, headless=True, use_subprocess=True)
        driver.get(url)
        time.sleep(5)

        for index in range(1, 21):
            try:
                empresa_xpath = f"/html/body/div[1]/div[3]/div/div/main/div[2]/ul/li[{index}]/div/a/div/div[1]/div/p"
                cargo_xpath = f"/html/body/div[1]/div[3]/div/div/main/div[2]/ul/li[{index}]/div/a/div/h3"
                link_xpath = f"/html/body/div[1]/div[3]/div/div/main/div[2]/ul/li[{index}]/div/a"

                empresa_el = driver.find_element(By.XPATH, empresa_xpath)
                cargo_el = driver.find_element(By.XPATH, cargo_xpath)
                link_el = driver.find_element(By.XPATH, link_xpath)

                empresa = clean_text(empresa_el.text)
                cargo = clean_text(cargo_el.text)
                href = link_el.get_attribute("href")
                link = href if href.startswith("http") else f"https://portal.gupy.io{href}"

                jobs.append({
                    'empresa': empresa,
                    'cargo': cargo,
                    'descricao': None,
                    'salario': None,
                    'tags': [],
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
        print(f"[Gupy] Erro ao buscar vagas: {e}")
        if driver:
            try:
                driver.quit()
            except:
                pass
        return []
