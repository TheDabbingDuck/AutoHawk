#!/usr/bin/env python3
"""
CLI interface for AutoHawk car scraper tool.
"""

import argparse
import sys
from typing import Dict, Any, Optional


def validate_year(value: str) -> int:
    """Validate that year is a positive integer."""
    try:
        year = int(value)
        if year <= 0:
            raise ValueError("Year must be a positive integer")
        return year
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid year format: {value}")


def validate_zip(value: str) -> str:
    """Validate that zip code is 5 digits."""
    if not (value.isdigit() and len(value) == 5):
        raise argparse.ArgumentTypeError(f"Invalid ZIP code format: {value}. Must be 5 digits.")
    return value


def validate_radius(value: str) -> int:
    """Validate that radius is a positive integer."""
    try:
        radius = int(value)
        if radius <= 0:
            raise ValueError("Radius must be a positive integer")
        return radius
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid radius format: {value}")


def parse_args(args: Optional[list] = None) -> Dict[str, Any]:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="AutoHawk - Web scraper for car listings",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "--make",
        type=str,
        required=True,
        help="Car manufacturer (e.g., Toyota, Honda)",
    )

    parser.add_argument(
        "--model",
        type=str,
        required=True,
        help="Car model (e.g., Camry, Civic)",
    )

    parser.add_argument(
        "--year_min",
        type=validate_year,
        required=True,
        help="Minimum year of manufacture",
    )

    parser.add_argument(
        "--year_max",
        type=validate_year,
        required=True,
        help="Maximum year of manufacture",
    )

    parser.add_argument(
        "--zip",
        type=validate_zip,
        required=True,
        help="5-digit ZIP code for search location",
    )

    parser.add_argument(
        "--radius",
        type=validate_radius,
        default=50,
        help="Search radius in miles from the specified ZIP code",
    )

    parser.add_argument(
        "--no_accidents",
        action="store_true",
        help="Filter for cars with no accident history",
    )

    parsed_args = parser.parse_args(args)

    # Additional validation
    if parsed_args.year_min > parsed_args.year_max:
        parser.error("Minimum year must be less than or equal to maximum year")

    return vars(parsed_args)


def display_search_params(params: Dict[str, Any]) -> None:
    """Display the search parameters."""
    print("\nAutoHawk Search Parameters:")
    print("-" * 40)
    for key, value in params.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    print("-" * 40)


def main() -> None:
    """Main entry point for the CLI."""
    try:
        args = parse_args()
        display_search_params(args)
        print("Starting search with the above parameters...")
        # This is where you would call the scraper function
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()