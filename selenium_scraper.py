#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Event Scraper for BookMyShow

# This Python script scrapes event details (name and date) from BookMyShow.
# It starts scraping from a specific event ID (429875) and increments the ID for each subsequent request.
# Event data is extracted from the event page and saved into a CSV file.
# The script uses Selenium WebDriver to simulate a browser and extract information like event name and date.
# It runs continuously, incrementing the event ID and scraping events, then waits for 5 seconds before checking the next event.
# The scraped event details are saved in a CSV file called 'events.csv' in the current working directory.
# It runs in headless mode, meaning no browser window is opened during scraping.
# The script can be interrupted manually to stop scraping.
#--------------------------------------------------------------------------------------------------------------------------------

import time
import csv
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Starting event ID
start_event_id = 429875

# CSV file path where event data will be saved
csv_file = "events.csv"

# Get the current directory where the Jupyter notebook is running
current_directory = os.getcwd()

# Path to chromedriver in the same folder as Jupyter
chromedriver_path = os.path.join(current_directory, "chromedriver.exe")

# User-Agent to mimic a real browser request
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (without opening the browser window)
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (optional)
chrome_options.add_argument("--window-size=1920x1080")  # Set window size (optional)

# Initialize WebDriver with Service and Options
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Function to write event details to a CSV file
def write_to_csv(show_name, show_date):
    # Open the CSV file in append mode
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([show_name, show_date])

# Function to scrape event name and date from the event page using Selenium
def scrape_event_info(event_id):
    # Generate the URL for the event using the event_id
    url = f"https://in.bookmyshow.com/activities/bebop/ET00{event_id}?webview=true"
    
    print(f"Scraping URL: {url}")  # Debugging output
    
    # Load the event page in the browser
    driver.get(url)
    
    try:
        # Wait for the page to load completely
        driver.implicitly_wait(10)  # Waits for a maximum of 10 seconds for the page to load
    except Exception as e:
        print(f"Error loading page {url}: {e}")
        return

    # Extract event name from the title tag (head)
    show_name = driver.title
    show_name_text = show_name.replace(" - BookMyShow", "").strip() if show_name else "Unknown Event"
    print(f"Found event: {show_name_text}")
    
    # Extract event date (Modify the class name based on actual page structure)
    try:
        show_date_element = driver.find_element(By.CLASS_NAME, "event-date")  # Modify if needed
        show_date_text = show_date_element.text.strip() if show_date_element else "Unknown Date"
    except Exception as e:
        print(f"Error finding event date: {e}")
        show_date_text = "Unknown Date"

    print(f"Event: {show_name_text}, Date: {show_date_text}")
    
    # Write the event details to CSV
    write_to_csv(show_name_text, show_date_text)

# Function to continuously scrape and increment event IDs
def scrape_events():
    event_id = start_event_id  # Start with the initial event ID
    
    while True:
        scrape_event_info(event_id)
        event_id += 1  # Increment the event ID for the next check
        time.sleep(5)  # Wait for 5 seconds before checking again (adjust as needed)

# Create CSV file with header if it doesn't exist
def initialize_csv():
    try:
        with open(csv_file, mode='r') as file:
            pass  # If file exists, do nothing
    except FileNotFoundError:
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Show Name", "Event Date"])

# Start the scraper
initialize_csv()
scrape_events()

# Close the Selenium driver after scraping is done
driver.quit()

