# AdNabu QA Automation Assignment

## Objective
Automate a single test scenario:
- Search for a product
- Add the product to the cart successfully

---

## Tech Stack
- Python
- Selenium WebDriver
- PyTest

---

## Project Structure

- **pages/** → Page Object Model files  
- **tests/** → Test scripts  
- **reports/** → Execution reports  
- **driver_setup.py** → WebDriver setup  
- **requirements.txt** → Dependencies  



## Setup Instructions

1. Clone the repository

git clone <repo-link>
cd project

2. Install dependencies

pip install -r requirements.txt

3. Setup ChromeDriver
Download ChromeDriver matching your Chrome browser version
Add it to system PATH


## How to Run the Test
pytest -v

## Generate basic test report using:

pytest -v > reports/report.txt

## After execution, report will be available at:

reports/report.txt
