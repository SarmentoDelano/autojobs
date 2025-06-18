import time
import re
import os
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def clean_text(text):
    if text:
        return re.sub(r'\s+', ' ', text).strip()
    return None

def fetch_infojobs_jobs(busca):
    try:
        jobs = []
        url = f"https://www.infojobs.com.br/vagas-de-emprego-{busca}-trabalho-home-office.aspx"

        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--log-level=3")
        options.add_argument("--disable-logging")
        options.add_argument("--disable-dev-shm-usage")

        # ✅ SUPRIME logs visuais e console popup
        service = Service(log_path=os.devnull)
        service.creationflags = subprocess.CREATE_NO_WINDOW
        driver = webdriver.Chrome(service=service, options=options)

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

        driver.quit()
        return jobs

    except Exception as e:
        print(f"[InfoJobs] Erro ao buscar vagas: {e}")
        return []
