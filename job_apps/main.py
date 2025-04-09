from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import os
import json

def next_clicked() -> bool:
    """assumes if there is none, the only button left is Review"""
    try:
        next_button = driver.find_element(By.XPATH, "//button[starts-with(@aria-label, 'Continue to next step')]")
        next_button.click()
        return True
    except NoSuchElementException:
        return False


def answer_questions():
    # parent = driver.find_element(By.CLASS_NAME, 'jobs-easy-apply-content')
    true_parent = driver.find_element(By.CLASS_NAME, 'pb4')
    
    pass


def application_submitted() -> bool:
    try:
        submit_button = driver.find_element(By.XPATH, "//button[starts-with(@aria-label, 'Submit application')]")
        submit_button.click()
        return True
    except NoSuchElementException:
        return False


def review_application():
    """Assumes no next button"""
    review_button = driver.find_element(By.XPATH, "//button[starts-with(@aria-label, 'Review your application')]")
    review_button.click()


def apply_to_posting():
    easy_apply = driver.find_element(By.XPATH, "//button[starts-with(@aria-label, 'Easy Apply')]")
    easy_apply.click()

    # for one click applications
    if application_submitted():
        return
    
    if not next_clicked():
        review_application()


def scroll_and_apply(role: str):
    search_bar = driver.find_element(By.XPATH, "//input[starts-with(@id, 'jobs-search-box-keyword-id-ember')]")
    search_bar.send_keys(role)
    search_bar.send_keys(Keys.RETURN)


    easy_apply_opt = driver.find_element(By.CSS_SELECTOR, "[aria-label='Easy Apply filter.']")
    easy_apply_opt.click()

    postings_ul = driver.find_element(By.CLASS_NAME, 'scaffold-layout__list-container')

    for li in postings_ul.find_elements(By.TAG_NAME, 'li'):
        li.click()
        apply_to_posting()


with open('/Users/brianbarry/Desktop/computing/brian_utils/job_apps/roles.json', 'r') as f:
    roles = json.load(f)

load_dotenv()
username = os.getenv('lk_user')
password = os.getenv('lk_password')

entrypoint = 'https://www.linkedin.com/jobs'


# Set up the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Open the target URL
driver.get(entrypoint)  # Replace with the actual URL


driver.implicitly_wait(10)

username_input = driver.find_element(By.ID, "session_key")
username_input.send_keys(username)
username_input = driver.find_element(By.ID, "session_password")
username_input.send_keys(password)

sign_in_button = driver.find_element(By.XPATH, "//button[@data-id='sign-in-form__submit-btn']")
sign_in_button.click()

driver.implicitly_wait(10)

driver.get('https://www.linkedin.com/jobs/')


for role in roles:
    apply_to_jobs(role)
button = driver.find_element(By.XPATH, "//button[contains(@class, 'artdeco-button__text') and text()='texty']")
button.click()

# Close the browser after interaction (optional)
driver.quit()