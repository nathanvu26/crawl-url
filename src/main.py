import os
import requests
from bs4 import BeautifulSoup

import argparse

def get_response(url: str):
    response = requests.get(url)
    return response

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", type=str, help="Url of site being crawled")
    args = parser.parse_args()
    url = args.url

if __name__ == "__main__":
    main()