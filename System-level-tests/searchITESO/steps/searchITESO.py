# -*- coding: utf-8 -*-

"""
Simple test using Behave (BDD) and Selenium to open ITESO website and search something.
"""

import os
import time
import random
from behave import given, when, then
from chromedriver_py import binary_path  # Import the chromedriver binary path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService


@given("I am on the ITESO homepage")
def step_open_homepage(context):
    """Open the ITESO homepage."""
    service = ChromeService(executable_path=binary_path)
    context.driver = webdriver.Chrome(service=service)
    context.driver.get("https://www.iteso.mx")
    time.sleep(random.uniform(3, 5))


@when("I search for 'carreras'")
def step_search_carreras(context):
    wait = WebDriverWait(context.driver, 15)

    # Search for the search button and click it
    search_button = wait.until(EC.element_to_be_clickable((By.ID, 'icon-search')))
    search_button.click()

    # Wait for the search input to be visible and enter the search term
    search_input = wait.until(EC.visibility_of_element_located((By.ID, 'ipt-search')))
    search_input.send_keys("carreras")
    search_input.send_keys(Keys.RETURN)
    time.sleep(random.uniform(3, 5))

    # Search for the "Carreras" link and click it
    careers_link = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//a[contains(@data-cturl, "carreras.iteso.mx")]')
        )
    )
    careers_link.click()

    # Wait for the new tab to open
    WebDriverWait(context.driver, 10).until(lambda d: len(d.window_handles) > 1)

    # Switch to the new tab
    context.driver.switch_to.window(context.driver.window_handles[-1])
    time.sleep(5)

@then('I should see results related to ITESO academic programs')
def step_verify_results(context):
    wait = WebDriverWait(context.driver, 15)

    #validate that the page contain url  'https://carreras.iteso.mx/'
    assert context.driver.current_url == 'https://carreras.iteso.mx/', f"Wrong URL. Found: {context.driver.current_url}"

    # Validate that the page contains id´s "humanidades", "ingenierias", and "negocios"
    humanidades = wait.until(EC.presence_of_element_located((By.ID, "humanidades-tab")))
    assert humanidades.is_displayed()

    ingenierias = wait.until(EC.presence_of_element_located((By.ID, "ingenierias-tab")))
    assert ingenierias.is_displayed()

    negocios = wait.until(EC.presence_of_element_located((By.ID, "negocios-tab")))
    assert negocios.is_displayed()

    context.driver.quit()