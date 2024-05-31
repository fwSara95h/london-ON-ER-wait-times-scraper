# london-ON-ER-wait-times-scraper
 A python scraper for collecting the ER wait times in London, Ontario from https://www.lhsc.on.ca/adult-ed/emergency-department-wait-times


## Overview
This project is designed to scrape emergency room wait times from a specified URL ([https://www.lhsc.on.ca/adult-ed/emergency-department-wait-times](https://www.lhsc.on.ca/adult-ed/emergency-department-wait-times)), process the data, and log it into CSV files. The project includes functions for web scraping using different libraries, string manipulation, and logging.

## File Structure

```
project/
│
├── request_soup.py      # Contains various functions for web scraping using requests, cloudscraper, and requests_html.
│
├── helper_fns.py        # Contains utility functions for string manipulation and HTTP request status formatting.
│
├── file_builders.py     # Contains a function to log data to a CSV file, either creating a new file or appending to an existing one.
│
├── app.py               # The main script that orchestrates the scraping, processing, and logging of emergency room wait times.
│
└── README.md            # Project readme file.
```

## Files and Functions

### request_soup.py
- **linkToSoup_scrapingAnt**: Uses the ScrapingAnt API to fetch and parse a webpage, optionally using a proxy country and CSS selector.
- **linkToSoup**: Fetches and parses a webpage using the requests library, with optional configurations for headers, cookies, etc.
- **linkToSoup_h**: Fetches and parses a webpage using the requests_html library.
- **linkToSoup_c**: Fetches and parses a webpage using the cloudscraper library to bypass anti-bot measures.

### helper_fns.py
- **stripStr**: Removes extra whitespace from a string.
- **truncateIfLong**: Truncates a string to a specified maximum length, adding '...' if the string is too long.
- **miniStr**: Converts an object to a string, removes extra whitespace, joins lines and words with specified separators, and optionally truncates the string.
- **reqStatus**: Formats the status of an HTTP request as a string, including status code, reason, elapsed time, and URL.

### file_builders.py
- **log_data**: Logs data to a CSV file. Creates a new file if necessary, or appends to an existing file.

### app.py
- **main**: Scrapes emergency room wait times from a specified URL and logs the data. Handles scenarios including successful data retrieval, warnings for unexpected data formats, and errors during the scraping process.

## Usage

To run the scraping and logging process, execute the `app.py` script. This will start an infinite loop that scrapes the data at specified intervals (default is every 15 minutes).

```bash
python app.py
```

Ensure you have the necessary libraries installed, which you can do using the following command:

```bash
pip install requests beautifulsoup4 cloudscraper requests_html pandas
```

## Configuration

- Modify the default file names for data and log storage in the `main` function of `app.py`.
- Adjust the `scrape_interval` variable in `app.py` to change the frequency of scraping.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

This readme provides a comprehensive overview of the project structure, functionalities, and usage instructions.
