# Op.gg Scraper

This is a Python application that uses the Selenium library to perform web scraping on the op.gg website. The application is configured to be used with Conda as a virtual environment, and a librerias.yml file is provided to install the necessary dependencies.

## Installation

1 - Clone the repository to your local machine.

2 - Create a Conda virtual environment using the librerias.yml file:
```
conda env create -f enviroment.yml
```
3 - Activate the virtual environment:
```
conda activate my_enviroment
```
4 - Run the main.py script to start the op.gg scraper.

## Usage
After setting up the virtual environment and installing the dependencies, you can run the main.py script to start scraping data from the op.gg website. The script is designed to extract data from a specified summoner profile and region, which need to be indicated at the beginning of the script. You can modify the script to specify the summoner name and region that you want to scrape.

The script will collect data such as player profiles, match history, and statistics for the specified summoner name and region. You can customize the scraping parameters and data collection as needed.

Please note that web scraping may be subject to the terms of service of the website being scraped, and it is your responsibility to ensure that your use of this application complies with all applicable laws and regulations. Use at your own risk.

## Contributing
If you would like to contribute to this project, feel free to submit a pull request or open an issue. Any contributions are welcome!

## License
This project is licensed under the MIT License.