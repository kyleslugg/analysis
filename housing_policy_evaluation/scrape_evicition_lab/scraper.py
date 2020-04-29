from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup

import csv


URL = 'https://evictionlab.org/covid-policy-scorecard/'
state_scores = {}

driver = webdriver.Safari()

driver.get(URL)
driver.implicitly_wait(20)

soup = BeautifulSoup(driver.page_source, 'html.parser')

states = driver.find_elements_by_class_name('state-text')

for state in states:
    state_scores[state.get_attribute("data-state")] = state.text.split(':')[1].split('/')[0].strip()

driver.quit()

with open('covid_housing_policy_scorecard.csv', 'w') as csvfile:
    col_names = ['state', 'score']
    writer = csv.DictWriter(csvfile, fieldnames=col_names)
    writer.writeheader()
    for key, value in state_scores.items():
        writer.writerow({'state': key, 'score': value})
