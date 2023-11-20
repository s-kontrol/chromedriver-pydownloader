# Chromedriver Downloader

## Overview

This is a Python script designed for efficiently downloading `chromedriver` versions for Linux64 distributions. The script fetches information from [chrome-for-testing](https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json) and allows users to specify a particular version or major number.

**Intended Use:** Primarily for automation purposes.

## How to Use

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Examples of usage:

   - To download `chromedriver` for version 120:

     ```bash
     python download-chromedriver.py --version 120
     ```

   - To download a specific version (e.g., 115.0.5763.0):

     ```bash
     python download-chromedriver.py --version 115.0.5763.0
     ```

## Requirements

- Python
