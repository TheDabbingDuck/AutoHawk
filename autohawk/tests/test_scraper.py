# tests/test_scraper.py
import pytest
import sys
import os
from autohawk.scraper import AutoHawkScraper
from argparse import ArgumentTypeError


def test_browser_lifecycle():
    """Verify WebDriver can start and stop properly."""
    driver_path = r"C:\Users\caleb\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"  # Use raw string

    scraper = AutoHawkScraper(headless=True, driver_path=driver_path)

    # Test browser startup
    assert scraper.start_browser(), "Browser should start successfully"
    assert scraper.driver is not None, "WebDriver instance should exist"

    # Test browser shutdown
    scraper.close()
    assert scraper.driver is None, "WebDriver should be cleared after close"


def test_context_manager():
    """Test context manager functionality."""
    driver_path = r"C:\Users\caleb\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"  # Use raw string
    with AutoHawkScraper(headless=True, driver_path=driver_path) as scraper:
        assert scraper.driver is not None, "Browser should start in context manager"

    assert scraper.driver is None, "Browser should auto-close after context manager"


def test_year_min_greater_than_year_max():
    """Test that an error is raised when year_min > year_max."""
    from autohawk.cli import parse_args  # Import here to avoid circular dependency

    test_args = [
        "--make", "Ford",
        "--model", "Mustang",
        "--year_min", "2022",
        "--year_max", "2020",
        "--zip", "60601"
    ]

    with pytest.raises(SystemExit):
        parse_args(test_args)
