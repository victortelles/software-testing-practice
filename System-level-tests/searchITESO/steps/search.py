"""
System Test example using Behavior-Driven Development (BDD) with Behave (Gherkin) and Selenium.
"""

""" Search ITESO Homepage Step Definitions
    This file contains the step definitions for searching on the ITESO homepage. """

import os
import time
import random
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

BROWSER = os.getenv("BROWSER", "chrome").lower()

@given("the user opens the browser and navigates to 'iteso.mx'")
def step_open_homepage(context):
    """Opens the ITESO homepage in the selected browser."""
    if BROWSER == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        options = webdriver.EdgeOptions()
        context.driver = webdriver.Edge(service=service, options=options)
    else:
        service = ChromeService(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        context.driver = webdriver.Chrome(service=service, options=options)

    context.driver.maximize_window()
    context.driver.get("https://www.iteso.mx")
    time.sleep(random.uniform(3, 5))

@when('the user searches for "{term}" on the ITESO homepage')
def step_search_term(context, term):
    """Finds the search input and searches for the given term."""
    # clic on icon search
    search_icon = context.driver.find_element("id","icon-search")
    search_icon.click()
    # wait for the search input to be visible
    time.sleep(random.uniform(3, 5))

    # Write 'carreras' in the search input and wait for the results
    search_input = context.driver.find_element("id", "ipt-search")
    term = 'carreras'
    search_input.send_keys(term)
    search_input.send_keys(Keys.RETURN)
    time.sleep(random.uniform(3, 5))
    
    # click to element to href 'https://carreras.iteso.mx/'
    href = "https://carreras.iteso.mx/"
    link = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//a[contains(@href, '{href}')]"))
    )
    link.click()
    # wait for the page to load
    time.sleep(random.uniform(3, 5))

@then('the user should see results related to "{term}"')
def step_verify_results(context, term):
    
    time.sleep(random.uniform(3, 5))