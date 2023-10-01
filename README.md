# Kesaintblanc Data Scraper

This Python script is designed to scrape product data from the Kesaintblanc website. It collects information about products, including product name, URL, price, image URLs, status, stock, and more. The scraped data is saved to a CSV file for further analysis.

## Features

### Data Scraping

- Scrapes product data from Kesaintblanc's website.
- Extracts product details such as name, URL, price, image URLs, status, and stock.
- Organizes the scraped data into a CSV file.

### Customizable Parameters

- You can customize the script by adjusting the following parameters:
  - `url_base`: The base URL of the Kesaintblanc website.
  - `page_list`: The list of page numbers to scrape data from. Modify this list to scrape data from specific pages.

## Usage

1. Run the script using the following command:

   ```bash
   python script.py
   ```

2. Scraping Process:
   - The script will start scraping data from the specified pages.
   - Data for each product will be collected and saved to a CSV file named 'data.csv'.

3. Data Output:
   - The CSV file 'data.csv' will contain columns for product name, product URL, price, product image URL, status, stock, and more.

4. Customization:
   - You can customize the script by adjusting the `url_base` and `page_list` variables to scrape data from specific pages or sections of the website.

## Dependencies

- The script uses Python libraries such as `requests` and `BeautifulSoup` for web scraping. Install these dependencies using pip if you haven't already:

   ```bash
   pip install requests beautifulsoup4
   ```

## Author

- Author: [Your Name]

Feel free to customize the script and README to suit your specific use case or requirements.
```

Replace `[Your Name]` in the author section with your name or details. Additionally, make sure to update the dependencies section if there are any other dependencies required for your script.
