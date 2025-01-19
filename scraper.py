#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Event Scraper for BookMyShow

# This Python script scrapes event details (name and date) from BookMyShow.
# It starts scraping from a specific event ID (429875) and increments the ID for each subsequent request.
# Event data is extracted from the event page and saved into a CSV file.
# The script uses the 'requests' library to fetch the event pages and 'BeautifulSoup' for parsing HTML content.
# The script runs continuously, scraping events every 5 seconds, and appends the event name and date to the CSV file.
# The CSV file is created if it doesn't exist, with the header "Show Name" and "Event Date".
# Custom headers (User-Agent) are used to mimic a real browser request to avoid being blocked.
#---------------------------------------------------------------------------------------------------------------------


import requests
from bs4 import BeautifulSoup
import time
import csv


# Starting event ID
start_event_id=429875

# CSV file path where event data will be saved
csv_file="events.csv"

# User-Agent to mimic a real browser request
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.9",
    "Connection":"keep-alive",
    "Upgrade-Insecure-Requests":"1"
}

# Function to write event details to a CSV file
def write_to_csv(show_name, show_date):
    # Open the CSV file in append mode
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([show_name, show_date])

# Function to scrape event name and date from the event page
def scrape_event_info(event_id):
    # Generate the URL for the event using the event_id
    url = f"https://in.bookmyshow.com/activities/bebop/ET00{event_id}?webview=true"
    
    print(f"Scraping URL: {url}")  # Debugging output
    
    try:
        response = requests.get(url, headers=headers)  # Pass headers with the request
        response.raise_for_status()  # Raise an error if the request was unsuccessful
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract the event name from the title tag
    show_name = soup.find("title")
    if show_name:
        show_name_text = show_name.text.strip()
        # Remove ' - BookMyShow' from the title (if present)
        show_name_text = show_name_text.replace(" - BookMyShow", "")
        print(f"Found event: {show_name_text}")
    else:
        show_name_text = "Unknown Event"
    
    # Extract event date - you may need to modify this based on actual structure
    show_date = soup.find("div", class_="event-date")  # Modify this if necessary
    if show_date:
        show_date_text = show_date.text.strip()
    else:
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

