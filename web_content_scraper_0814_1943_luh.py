# 代码生成时间: 2025-08-14 19:43:24
import requests
from bs4 import BeautifulSoup
import gradmin

"""
Web Content Scraper using GrAdmin and BeautifulSoup.
This script is designed to scrape web content from a given URL
and display the result in a simple web interface.
"""

def scrape_content(url: str) -> str:
    """
    Scrape content from the given URL.

    Args:
    url (str): The URL to scrape content from.

    Returns:
    str: The scraped content as a string.

    Raises:
    Exception: If an error occurs while scraping content.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        raise Exception(f"Failed to retrieve content: {e}")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()

def main():
    """
    Main function to run the GrAdmin interface.
    """
    with gradmin.Interface(fn=scrape_content, inputs="text", outputs="text") as demo:
        demo.launch()

if __name__ == "__main__":
    main()