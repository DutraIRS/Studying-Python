#!/usr/bin/env python
"""
selenium_web_scraping.py

This script uses Selenium to automate browser actions for the purpose of collecting Venezuelan election data from the CNE website.
It contains functions to load a webpage using a Chrome webdriver and to select a state from a dropdown menu on a webpage.

Dependencies:
    Selenium, time, pandas, pickle, os

Author: 
    DutraIRS

Date: 
    10/12/2023
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import pandas as pd
import pickle
import os

def load_page(url):
    """
    Load a webpage using a Chrome webdriver.
    
    This function initializes a Chrome webdriver, navigates to the specified URL,
    waits for 5 seconds to ensure the page is fully loaded, and then returns the driver.
    
    Parameters:
    url (str): The URL of the webpage to load.
    
    Returns:
    driver (selenium.webdriver.Chrome): The Chrome webdriver with the loaded webpage.
    """
    # Initialize the browser driver (in this case, Chrome)
    driver = webdriver.Chrome()
    
    # Navigate to the page
    driver.get(url)
    
    # Wait for 5 seconds to ensure the page is fully loaded
    time.sleep(5)
    
    return driver

def select_state(driver, state):
    """
    Select a state from a dropdown menu on a webpage using a webdriver.
    
    This function finds a dropdown menu by its ID 'cod_edo' on the webpage loaded in the provided webdriver,
    selects an option from the dropdown menu that matches the provided state name, waits for 3 seconds to ensure 
    the selection is processed, and then returns the driver.
    
    Parameters:
    driver (selenium.webdriver.Chrome): The Chrome webdriver with the loaded webpage.
    edo (str): The name of the state to select from the dropdown menu.
    
    Returns:
    driver (selenium.webdriver.Chrome): The Chrome webdriver after the state selection.
    """
    # Find the dropdown menu by its ID
    select_state = Select(driver.find_element(By.ID, 'cod_edo'))
    
    # Select the option by its visible text
    select_state.select_by_visible_text(state)
    
    # Wait for 3 seconds to ensure the selection is processed
    time.sleep(3)
    
    return driver

def select_municipality(driver, mun):
    """
    Select a municipality from a dropdown menu on a webpage using a webdriver.
    
    This function finds a dropdown menu by its ID 'cod_mun' on the webpage loaded in the provided webdriver,
    selects an option from the dropdown menu that matches the provided municipality name, waits for 3 seconds to ensure 
    the selection is processed, and then returns the driver.
    
    Parameters:
    driver (selenium.webdriver.Chrome): The Chrome webdriver with the loaded webpage.
    mun (str): The name of the municipality to select from the dropdown menu.
    
    Returns:
    driver (selenium.webdriver.Chrome): The Chrome webdriver after the municipality selection.
    """
    # Find the dropdown menu by its ID
    select_mun = Select(driver.find_element(By.ID, 'cod_mun'))
    
    # Select the option by its visible text
    select_mun.select_by_visible_text(mun)
    
    # Wait for 3 seconds to ensure the selection is processed
    time.sleep(3)
    
    return driver

def get_votes(driver):
    """
    Extract vote counts from specific div elements on a webpage using a webdriver.
    
    This function finds div elements with the class 'panel' on the webpage loaded in the provided webdriver,
    specifically targets the 9th, 10th, 11th, and 12th divs (0-indexed), waits until these divs are not empty,
    extracts the second line of text from each div, removes any periods, converts the result to an integer,
    and appends it to a list of votes.
    
    Parameters:
    driver: The webdriver with the loaded webpage.
    
    Returns:
    votes (list of int): A list of vote counts extracted from the targeted divs.
    """
    votes = []
    
    # Find the divs with the class 'panel'
    divs = driver.find_elements(By.CSS_SELECTOR, '.panel')
    
    # The text within the divs is the content you're looking for
    for div_num in [8, 9, 10, 11]:
        div = divs[div_num]
        
        # For some reason, sometimes the server returns an empty div.
        # We need to wait until it's not empty
        while len(div.text.splitlines()) == 0:
            divs = driver.find_elements(By.CSS_SELECTOR, '.panel')
            div = divs[div_num]
            
        # Extract the vote count, remove periods, convert to integer, and append to the list
        votes.append(int((div.text.splitlines()[1]).replace('.', '')))
        
    return votes

def get_metadata(driver):
    """
    Extract metadata from a specific div element on a webpage using a webdriver.
    
    This function finds div elements with the class 'panel' on the webpage loaded in the provided webdriver,
    specifically targets the 6th div (0-indexed), splits the text within this div into lines,
    and checks each line for specific keywords ("ELECTORES INSCRITOS", "PARTICIPACIÓN", "VOTOS VÁLIDOS", "VOTOS NULOS").
    If a line contains one of these keywords, the function extracts the associated number, removes any periods,
    converts the result to an integer, and stores it in a list of metadata.
    
    Parameters:
    driver: The webdriver with the loaded webpage.
    
    Returns:
    metadata (list of int): A list of metadata extracted from the targeted div. The list contains the following elements, in order:
        - Number of registered voters
        - Number of participants
        - Number of valid votes
        - Number of null votes
    """
    metadata = [0, 0, 0, 0]
    
    # Find the divs with the class 'panel'
    divs = driver.find_elements(By.CSS_SELECTOR, '.panel')
    
    # The text within the divs is the content you're looking for
    div = divs[5]
    raw = div.text.splitlines()
    
    for datapoint in raw:
        if "ELECTORES INSCRITOS" in datapoint:
            metadata[0] = int((datapoint.split(" ")[2]).replace('.', ''))
        if "PARTICIPACIÓN" in datapoint:
            metadata[1] = int((datapoint.split(" ")[1]).replace('.', ''))
        if "VOTOS VÁLIDOS" in datapoint:
            metadata[2] = int((datapoint.split(" ")[2]).replace('.', ''))
        if "VOTOS NULOS" in datapoint:
            metadata[3] = int((datapoint.split(" ")[2]).replace('.', ''))
            
    return metadata

# Check if the 'already_processed.pkl' file exists
if os.path.exists('already_processed.pkl'):
    # If it does, open the file and load the list of already processed states
    with open('already_processed.pkl', 'rb') as f:
        already_processed = pickle.load(f)
else:
    # If it doesn't, initialize an empty list of already processed states
    already_processed = []

# Load the webpage
driver = load_page('http://www.cne.gob.ve/ResultadosElecciones2018/index.php')

# Find the dropdown menu for states
select_edo = Select(driver.find_element(By.ID, 'cod_edo'))

# Get all options from the dropdown menu
options = select_edo.options

# Iterate over the options
for option in options:
    # If the option is not a separator and has not been processed yet
    if "::" not in option.text and option.text not in already_processed:
        # Initialize a DataFrame to store the results
        df = pd.DataFrame(columns = ['Estado', 'Municipio', 'Maduro', 'Falcon', 'Bertucci', 'Quijada', 'Inscritos', 'Participacao', 'Validos', 'Nulos'])
        
        # Select the state
        driver = select_state(driver, option.text)
        
        # Find the dropdown menu for municipalities
        select_mun = Select(driver.find_element(By.ID, 'cod_mun'))
        options_mun = select_mun.options
        
        # Iterate over the municipalities
        for option_mun in options_mun:
            # If the option is not a separator
            if "::" not in option_mun.text:
                # Select the municipality
                driver = select_municipality(driver, option_mun.text)
                
                # Get the votes and metadata
                votes = get_votes(driver)
                metadata = get_metadata(driver)
                
                # Save the results to the DataFrame
                temp_df = pd.DataFrame([[option.text, option_mun.text,
                                        votes[0], votes[1], votes[2], votes[3],
                                        metadata[0], metadata[1], metadata[2], metadata[3]]], 
                                        columns = ['Estado', 'Municipio', 'Maduro', 'Falcon', 'Bertucci', 'Quijada',
                                                    'Inscritos', 'Participacao', 'Validos', 'Nulos'])
                
                df = pd.concat([df, temp_df], ignore_index=True)
                
                # Wait for 3 seconds to ensure the selection is processed
                time.sleep(3)
                
        # Save the DataFrame to a CSV file after each state to prevent losing data if the server crashes   
        df.to_csv(f'{option.text}.csv', index=False)
        
        # Add the state to the list of already processed states
        already_processed.append(option.text)
        
        # Save the list of already processed states
        with open('already_processed.pkl', 'wb') as f:
            pickle.dump(already_processed, f)

# Close the driver when finished
driver.quit()