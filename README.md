# PhoneCheck CLI

A small, dependency-light CLI utility that validates and describes phone numbers using the [`phonenumbers`](https://pypi.org/project/phonenumbers/) library (Google's libphonenumber port for Python).  
Given a list of numbers, the script prints validation status, formatted variants (E.164 / national), number type (MOBILE, FIXED_LINE, etc.), carrier, timezone(s), and a location description.

> Designed for quick debugging, data-cleaning checks, or as a learning tool to explore what `phonenumbers` can extract from international phone numbers.

## Features
- Parse and validate international phone numbers
- Output E.164 and national formats
- Detect number type (MOBILE, FIXED_LINE, etc.)
- Show carrier name, timezone(s), and approximate location
- Safe fallback for unknown/invalid numbers

## Requirements
- Python 3.8+
- `phonenumbers` (install with `pip`)

## Installation
```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
# .\venv\Scripts\Activate.ps1   # Windows PowerShell
pip install phonenumbers
