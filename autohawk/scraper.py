# scraper.py
"""
AutoHawk web scraper implementation for car listings.
"""

from typing import Dict, Any
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
import os  # Import the os module


class AutoHawkScraper:
    """Base class for Selenium-based car listing scraper."""

    def __init__(self, headless=False, driver_path=None):
        """
        Initialize the scraper.

        Args:
            headless (bool): Run browser in headless mode. Default False for visible browser.
            driver_path (str, optional): Path to the ChromeDriver executable. If None, WebDriverManager is used.
        """
        self.driver = None
        self.headless = headless
        self.driver_path = driver_path

    def start_browser(self):
        """Initialize Chrome WebDriver with error handling."""
        try:
            # Configure browser options
            options = webdriver.ChromeOptions()
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

            # Only enable headless mode if specified
            if self.headless:
                options.add_argument("--headless")

            # Set up ChromeDriver service
            if self.driver_path:
                service = Service(executable_path=self.driver_path)
            else:
                service = Service(ChromeDriverManager().install())  # Using WebDriverManager

            # Initialize WebDriver
            self.driver = webdriver.Chrome(
                service=service,
                options=options
            )
            return True

        except WebDriverException as e:
            raise RuntimeError(f"Browser initialization failed: {str(e)}") from e
        except Exception as e:
            raise RuntimeError(f"Unexpected error during setup: {str(e)}") from e

    def close(self):
        """Safely close browser and clean up resources."""
        if self.driver:
            try:
                self.driver.quit()
            except WebDriverException as e:
                print(f"Warning: Error closing browser - {str(e)}")
            finally:
                self.driver = None

    def __enter__(self):
        """Context manager entry point."""
        self.start_browser()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit point."""
        self.close()

    def search_cars(self, params: Dict[str, Any]):
        """
        Search for cars based on the provided parameters.
        (Implementation remains unchanged from original)
        """
        # Existing search implementation
        print(f"Searching for {params['make']} {params['model']} between {params['year_min']} and {params['year_max']}")
        print(f"Location: ZIP {params['zip']} with {params['radius']} mile radius")
        if params.get('no_accidents'):
            print("Filtering for cars with no accident history")

        return []
