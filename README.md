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

ADNABU-QA-ASSIGNMENT/
│
├── pages/
│ ├── base_page.py
│ ├── home_page.py
│ ├── search_results_page.py
│ ├── product_page.py
│
├── tests/
│ └── test_add_to_cart.py
│
├── reports/
│ └── report.txt
│
├── driver_setup.py
├── requirements.txt
└── README.md



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
