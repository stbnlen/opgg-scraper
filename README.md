# Op.gg Scraper

This is a scraper script built using Selenium to extract information about League of Legends matches from the op.gg website. The script automates the process of gathering data, allowing users to retrieve various details about matches.

## Installation

Clone the repository:

```
git clone git@github.com:stbnlen/opgg-scraper.git
```

Navigate to the project directory:

```
cd opgg-scraper
```

Install the dependencies using pip:

```
pip install -r requirements.txt
```

Make sure you have Python and pip installed on your system before proceeding with the installation.

## Usage

Enter the necessary information when prompted, such as the summoner name and region.

Run the script:

```
python app.py
```

Wait for the script to scrape the data from the op.gg website.

The scraped data will be saved to a file named stats.csv in the project directory.

The script uses Selenium to automate web browsing, so it requires a compatible web driver to be installed and configured. Make sure to download the appropriate web driver for your browser and operating system. The script is currently set up to work with Chrome, but you can modify it to use a different browser by updating the driver configuration.

## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on the project's GitHub repository.

## Disclaimer

This script is intended for educational purposes only. Use it responsibly and adhere to the terms and conditions of the op.gg website. The scraping process should not be abused or used for any malicious activities.

## License

The project is licensed under the MIT License. Feel free to modify and distribute the code for your own purposes.