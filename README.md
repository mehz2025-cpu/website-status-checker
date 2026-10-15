# Website Status Checker

A Python tool that checks the availability of multiple websites concurrently.

## Features

* Accepts multiple website URLs from user input
* Checks websites using HTTP requests
* Uses multithreading for concurrent checks
* Reports HTTP status codes
* Summarizes online, offline, and error results
* Uses a timeout to avoid waiting indefinitely

## Technologies

* Python
* Requests
* Threading
* Queue

## Requirements

Python 3 and the `requests` library.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run the program with:

```bash
python status_checker.py
```

Enter the number of websites you want to check, then enter their URLs.

## Note

A website returning a non-2xx HTTP status code is reported as `DOWN`. Connection failures and request exceptions are reported as `ERROR`.
