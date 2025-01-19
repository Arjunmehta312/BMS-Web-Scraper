# Event Scraper for BookMyShow

This repository contains two Python scripts that scrape event details (name and date) from BookMyShow.

## Scripts

### 1. `scraper.py`
- **Description**: This script uses the `requests` library to scrape event details from BookMyShow.
- **How it works**: It fetches event pages using the provided event IDs starting from `429875` and increments the event ID for each subsequent request.
- **Event Data**: The script extracts the event name from the title tag and the event date from the page content. The extracted data is saved in a CSV file.
- **Output**: Event name and date are appended to a CSV file, `events.csv`.
- **Libraries Used**: `requests`, `BeautifulSoup`

### 2. `selenium_scraper.py`
- **Description**: This script uses `Selenium` to scrape event details from BookMyShow.
- **How it works**: It launches a headless Chrome browser using `Selenium` WebDriver to load event pages and extract event details.
- **Event Data**: Like the first script, it extracts the event name and event date from the page and saves them in a CSV file.
- **Output**: Event name and date are saved in the CSV file `events.csv`.
- **Libraries Used**: `selenium`, `BeautifulSoup`, `chromedriver`

## Installation

To run both scripts, you will need to install the following dependencies.

### Installation Steps:
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/repository-name.git
    cd repository-name
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Make sure you have a working version of `chromedriver` installed and available in your system's path if you're running the Selenium scraper.

## Running the Scripts

### To run the `scraper.py` script:
```bash
python scraper.py
