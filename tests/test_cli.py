"""
Tests for the AutoHawk CLI module.
"""

import pytest
import sys
import os


from cli import parse_args, validate_year, validate_zip, validate_radius


def test_parse_args_valid_inputs():
    """Test that valid CLI arguments are parsed correctly."""
    test_args = [
        "--make", "Toyota",
        "--model", "Camry",
        "--year_min", "2015",
        "--year_max", "2020",
        "--zip", "90210",
        "--radius", "100",
        "--no_accidents"
    ]

    args = parse_args(test_args)

    assert args["make"] == "Toyota"
    assert args["model"] == "Camry"
    assert args["year_min"] == 2015
    assert args["year_max"] == 2020
    assert args["zip"] == "90210"
    assert args["radius"] == 100
    assert args["no_accidents"] is True


def test_parse_args_defaults():
    """Test that default values are set correctly."""
    test_args = [
        "--make", "Honda",
        "--model", "Civic",
        "--year_min", "2018",
        "--year_max", "2022",
        "--zip", "10001"
    ]

    args = parse_args(test_args)

    assert args["radius"] == 50  # Default value
    assert args["no_accidents"] is False  # Default value


def test_validate_year_valid():
    """Test that valid years are accepted."""
    assert validate_year("2020") == 2020


def test_validate_year_invalid():
    """Test that invalid years raise an exception."""
    with pytest.raises(Exception):
        validate_year("not_a_year")

    with pytest.raises(Exception):
        validate_year("-1")

    with pytest.raises(Exception):
        validate_year("0")


def test_validate_zip_valid():
    """Test that valid ZIP codes are accepted."""
    assert validate_zip("12345") == "12345"


def test_validate_zip_invalid():
    """Test that invalid ZIP codes raise an exception."""
    with pytest.raises(Exception):
        validate_zip("1234")  # Too short

    with pytest.raises(Exception):
        validate_zip("123456")  # Too long

    with pytest.raises(Exception):
        validate_zip("abcde")  # Non-numeric


def test_validate_radius_valid():
    """Test that valid radius values are accepted."""
    assert validate_radius("25") == 25


def test_validate_radius_invalid():
    """Test that invalid radius values raise an exception."""
    with pytest.raises(Exception):
        validate_radius("not_a_number")

    with pytest.raises(Exception):
        validate_radius("-10")

    with pytest.raises(Exception):
        validate_radius("0")


def test_year_min_greater_than_year_max():
    """Test that an error is raised when year_min > year_max."""
    test_args = [
        "--make", "Ford",
        "--model", "Mustang",
        "--year_min", "2022",
        "--year_max", "2020",
        "--zip", "60601"
    ]

    with pytest.raises(Exception):
        parse_args(test_args)