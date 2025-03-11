# TODO Checklist for Used Car Price Web Scraping Tool

This checklist breaks down the project into small, iterative tasks to ensure steady progress with integrated testing at every step.

---

## 1. Project Setup and Environment
- [x] **Initialize Repository and Environment**
  - [x] Create a new Git repository.
  - [x] Set up a virtual environment.
  - [x] Create a `requirements.txt` with dependencies (Selenium, argparse, pytest, etc.).
- [x] **Project Structure**
  - [x] Create folder structure:
    - `autohawk/` for module files.
    - `tests/` for unit and integration tests.
    - Additional directories as needed (e.g., `logs/` for error logs).
- [ ] **Documentation**
  - [ ] Write a basic README with project overview, setup, and usage instructions.

---

## 2. CLI Interface Implementation
- [x] **CLI Parsing with argparse**
  - [x] Implement a basic CLI in `scraper.py` to accept parameters:
    - `--make` (string)
    - `--model` (string)
    - `--year_min` (integer)
    - `--year_max` (integer)
    - `--zip` (string)
    - `--radius` (enum: 25, 50, 100, 200)
    - `--no_accidents` (flag)
  - [x] Validate and parse input arguments.
  - [x] Print back the parsed parameters for debugging.
- [x] **Testing**
  - [x] Write pytest tests to verify correct parsing and validation of CLI arguments.

---

## 3. Selenium Scraping Framework
- [x] **Base Selenium Scraper**
  - [x] Create a base class ('AutoHawkScraper' in `scraper.py`.
    - [x] Implement methods for initializing and closing the Chrome WebDriver.
    - [x] Start with a visible browser session (for debugging purposes).
    - [x] Include basic error handling and logging stubs.
- [ ] **Testing**
  - [x] Write pytest tests to ensure that the WebDriver starts and stops correctly.

---

## 4. Website Scraper Modules
- [ ] **Carfax.com Scraper Module**
  - [ ] Develop a scraper module for carfax.com that inherits from the base class.
    - [ ] Navigate to the carfax.com homepage.
    - [ ] Accept search parameters from the CLI.
    - [ ] Simulate performing a search and extract sample listing details (VIN, price, mileage, year, URL).
    - [ ] Integrate error handling and logging.
- [ ] **Testing**
  - [ ] Write pytest tests (using mocks where needed) to simulate a scraping session and verify data extraction.
- [ ] **Future Work**
  - [ ] Plan similar modules for carmax.com and edmunds.com.

---

## 5. Data Handling and CSV Storage
- [ ] **Design CSV Schemas**
  - [ ] Define schema for `current_inventory.csv` with fields:
    - VIN, Price, Mileage, Year, Accident History, Listing URL, ZIP Code, Radius, Last Updated (ISO 8601)
  - [ ] Define schema for `price_history.csv` with fields:
    - VIN, Price, Mileage, Timestamp (ISO 8601)
- [ ] **CSV Operations**
  - [ ] Implement functions to write new listings.
  - [ ] Implement update logic to prevent duplicate VIN entries.
  - [ ] Append historical price data correctly.
- [ ] **Testing**
  - [ ] Write pytest tests to verify proper reading, writing, and updating of CSV files.

---

## 6. Error Handling, Logging, and Retry Mechanism
- [ ] **Error Logging**
  - [ ] Create a module to log errors to `errors.log` (with clear session separation).
  - [ ] Ensure immediate CLI output for errors.
- [ ] **Retry Mechanism**
  - [ ] Implement retries (2–3 attempts) with incremental back-off.
  - [ ] Introduce random delays between 2 to 5 seconds between retries.
- [ ] **Testing**
  - [ ] Write pytest tests to simulate failures and confirm that retries and logging work as expected.

---

## 7. Integration and Wiring
- [ ] **Component Integration**
  - [ ] Wire CLI inputs to the corresponding scraper functions.
  - [ ] Consolidate data from all scraper modules.
  - [ ] Integrate CSV data handling with the scraped data.
- [ ] **Main Script (`scraper.py`)**
  - [ ] Combine all components: CLI parsing, scraping, CSV updating, and error handling.
  - [ ] Print a summary of operations at the end of execution.
- [ ] **Testing**
  - [ ] Write an integration test simulating a full run with controlled input parameters.
  - [ ] Verify that there is no orphaned or disconnected code.

---

## 8. Documentation and Future Enhancements
- [ ] **Final Documentation**
  - [ ] Update README with full instructions, code comments, and examples.
  - [ ] Document the code structure and provide guidance for future development.
- [ ] **Future Enhancements**
  - [ ] Plan for switching to headless mode for deployment.
  - [ ] Extend scraping capabilities to include carmax.com and edmunds.com.
  - [ ] Integrate scheduling (e.g., using cron or Task Scheduler).
  - [ ] Explore the development of an interactive dashboard for data visualization.
  - [ ] Consider features such as price threshold alerts and email notifications.

---
