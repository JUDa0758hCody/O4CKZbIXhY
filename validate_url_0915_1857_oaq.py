# 代码生成时间: 2025-09-15 18:57:22
import requests
from urllib.parse import urlparse
import gr

"""
A Python program to validate the URL link validity using Gradio framework.

This program takes a URL input from the user and checks if the URL is valid
and reachable. It displays the result to the user using a simple GUI.
"""

class URLValidator:
    """Class to validate URL link validity."""

    def validate(self, url: str) -> bool:
        """Validate the given URL."""
        try:
            # Parse the URL to ensure it has a scheme and netloc
            result = urlparse(url)
            if not all([result.scheme, result.netloc]):
                return False

            # Send a HEAD request to check if the URL is reachable
            response = requests.head(url, allow_redirects=True, timeout=5)
            # Check for successful status code (200-299)
            return 200 <= response.status_code < 300
        except Exception as e:
            # Log any exceptions and return False
            print(f"Error validating URL: {e}")
            return False


def main():
    """Main function to run the URL validator GUI."""
    # Create a Gradio interface
    title = "URL Link Validator"
    description = "Enter a URL to check its validity."
    url_input = gr.Textbox(label="URL")
    result = gr.Textbox(label="Result")
    validator = URLValidator()
    """Define the function to be called when the user submits the form."""
    def check_url(url):
        result_value = "Valid" if validator.validate(url) else "Invalid"
        return result_value

    # Create the Gradio interface
    gr.Interface(
        fn=check_url,
        inputs=url_input,
        outputs=result,
        title=title,
        description=description,
        examples=[["https://www.example.com"]],
        max_output_length=10,
    ).launch()

if __name__ == "__main__":
    main()