from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

import time
import json
from datetime import datetime, timedelta

import warnings 
warnings.simplefilter(action='ignore', category=DeprecationWarning)

DRIVER_PATH = '/Users/brianbarry/Desktop/computing/chromedriver'
AUTH_PATH = '/Users/brianbarry/Desktop/computing/tokens/ucsd.json'
URL = 'https://urldefense.com/v3/__https://ecotimecampus.ucsd.edu__;!!LLK065n_VXAQ!xDdhgEjrgdTw8fuonI195LYjZIvs0GauFxk7Vqzxe-0c_IqGnmi7o8986XPruexnUw$'


with open(AUTH_PATH, 'r') as f:
    login = json.load(f)
    usr, pwd = login['USR'], login['PWD']
    
    
def work_days(start_date):
    """
    start_date: str like '%m-%d-%Y' 
    generator for 2 weeks of work days after start_date"""
    start_date_obj = datetime.strptime(start_date, '%m-%d-%Y')
    for d in range(12):
        dt = start_date_obj + timedelta(days=d)
        if dt.weekday() < 5:
            yield dt.strftime('%m/%d')

            
def switch_frames(wd, name):
    """Frames sometimes take a while to load, so wait in while loop until they appear"""
    detached = True
    while detached:
        time.sleep(0.5)
        try:
            wd.switch_to.default_content()
            wd.switch_to.frame(name)
            detached = False
        except: # WebDriverException: target frame detached
            continue


if __name__ == '__main__':

    two_weeks_ago = (datetime.today() - timedelta(days=11)).strftime('%m-%d-%Y')
    if input(f'Start date 2 weeks ago on {two_weeks_ago}? (y/n):\n') == 'y':
        start_date = two_weeks_ago
    else:
        start_date = input('Enter starting date e.g., 05-02-2022 : \n')
    wd = webdriver.Chrome(DRIVER_PATH)
    wd.get(URL)

    # login page
    wd.find_element_by_id('ssousername').send_keys(usr)
    wd.find_element_by_id('ssopassword').send_keys(pwd)
    wd.find_element_by_name('_eventId_proceed').click()

    # auth page - DO THIS MANUALLY
    # time.sleep(6)
    # wd.find_element_by_xpath('/html/body/div/div/div[1]/div/form/div[1]/fieldset/div[2]/button').click()
    while not input('Done with auth?'):
        ...
        
    # ecotime
    ## nav bar
    switch_frames(wd, 'frmTop')
    wd.find_element_by_link_text('Employee Tasks').click()
    wd.find_element_by_partial_link_text('Timesheet').click()

    ## timesheet

    for d in work_days(start_date):
        switch_frames(wd, 'frmBottom')

        wd.find_element_by_partial_link_text(d).click()
        Select(wd.find_element_by_name('cbInHrs1')).select_by_value('8')
        Select(wd.find_element_by_name('cbOutHrs1')).select_by_value('5')
        Select(wd.find_element_by_name('cbOutAP1')).select_by_value('P.M.')
        Select(wd.find_element_by_name('MEALBREAK1')).select_by_value('60')
        
        # save
        switch_frames(wd, 'frmTop')
        wd.find_element_by_xpath('/html/body/span/table/tbody/tr/td[1]/a').click()
