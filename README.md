# Event Scraper for BookMyShow

This Python script scrapes event details (name and date) from BookMyShow starting from a specific event ID and continuously scrapes new events. It saves the scraped data into a CSV file.

## Requirements
- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/repositoryname.git
   cd repositoryname
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python scraper.py
   ```

## Features
- Scrapes event details (name and date) from BookMyShow.
- Saves the data into a CSV file.
- Automatically increments event IDs and scrapes continuously.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
