---

# Olympic Player Data Scraper

This project scrapes player and medal data from the [Paris 2024 Olympics](https://olympics.com/en/paris-2024) website using Selenium and stores the extracted data in a CSV file.

## Features

- Automatically navigates to the Paris 2024 Olympics website.
- Accepts cookies and navigates to the medal table page.
- Scrapes details like country name, gold, silver, bronze, and total medal counts for each player.
- Saves the scraped data to a CSV file (`Olympic_players_data.csv`).

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- Selenium
- Google Chrome browser

You can install the necessary Python libraries using:

```bash
pip install selenium pandas
```

## Installation

1. Clone this repository.
2. Install the required dependencies by running:
   ```bash
   pip install selenium pandas
   ```

## Usage

1. Run the `scrape_olympic_players.py` script to start scraping:
   ```bash
   python scrape_olympic_players.py
   ```
2. The scraper will open a Chrome window, navigate to the Olympics website, and begin scraping player and medal data.
3. The data will be stored in a CSV file named `Olympic_players_data.csv` in the same directory.

### Example Output (CSV)

The CSV file will have the following structure:

| Country | Player Name   | Gold | Silver | Bronze | Total Medals |
|---------|---------------|------|--------|--------|--------------|
| IND     | CHOPRA Neeraj | 1    | 0      | 0      | 1            |


Note: The first two columns are country names, as one may contain the country code and the other the full name.

## How It Works

- The script launches a Chrome browser and navigates to the Paris 2024 Olympics website.
- It accepts cookies, navigates through the menu to the "Medal Table" page, and then clicks the "Medallists" link.
- A scrolling mechanism is implemented to scrape all player data progressively.
- The scraped data includes information such as country, player name, gold, silver, bronze, and total medal counts.
- The data is saved to a CSV file.


## Acknowledgments

- [Selenium WebDriver](https://www.selenium.dev/)
- [Pandas](https://pandas.pydata.org/)

---