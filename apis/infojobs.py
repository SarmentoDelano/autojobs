import time
import re
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

def clean_text(text):
    if text:
        return re.sub(r'\s+', ' ', text).strip()
    return None

# Subclasse que anula __del__ do driver
class SilentChrome(uc.Chrome):
    def __del__(self):
        pass

def fetch_infojobs_jobs(busca):
    driver = None
    try:
        jobs = []
        url = f"https://www.infojobs.com.br/vagas-de-emprego-{busca}-trabalho-home-office.aspx"

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
                cargo_xpath = f"/html/body/main/div[2]/form/div/div[1]/div[2]/div/div[{index}]/div/div[1]/div[1]/a/h2"
                empresa_xpath = f"/html/body/main/div[2]/form/div/div[1]/div[2]/div/div[{index}]/div/div[1]/div[1]/div[2]/div[2]/a"
                descricao_xpath = f"/html/body/main/div[2]/form/div/div[1]/div[2]/div/div[{index}]/div/div[2]"
                link_xpath = f"/html/body/main/div[2]/form/div/div[1]/div[2]/div/div[{index}]/div/div[1]/div[1]/a"

                cargo_el = driver.find_element(By.XPATH, cargo_xpath)
                empresa_el = driver.find_element(By.XPATH, empresa_xpath)
                descricao_el = driver.find_element(By.XPATH, descricao_xpath)
                link_el = driver.find_element(By.XPATH, link_xpath)

                cargo = clean_text(cargo_el.text)
                empresa = clean_text(empresa_el.text)
                descricao = clean_text(descricao_el.text)
                href = link_el.get_attribute("href")
                link = href if href.startswith("http") else f"https://www.infojobs.com.br{href}"

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

        if driver:
            try:
                driver.quit()
            except Exception:
                pass
            driver = None

        return jobs

    except Exception as e:
        print(f"[InfoJobs] Erro ao buscar vagas: {e}")
        if driver:
            try:
                driver.quit()
            except:
                pass
        return []
