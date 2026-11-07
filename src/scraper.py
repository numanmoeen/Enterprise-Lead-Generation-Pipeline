import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

def scrape_company_text(url: str) -> str:
    """
    Fetches a webpage and strips scripts, styles, and navigation to minimize LLM token usage.
    """
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Remove noisy DOM elements that waste API tokens
        for element in soup(["script", "style", "nav", "footer", "header", "noscript", "svg"]):
            element.decompose()

        clean_text = " ".join(soup.stripped_strings)
        # Cap text length to keep token usage predictable
        return clean_text[:6000]
    except Exception as e:
        print(f"[Scraper Warning] Failed to fetch {url}: {e}")
        return ""

def get_sample_leads() -> list[dict]:
    """
    Provides realistic raw scraped data so the pipeline can be demoed out-of-the-box.
    Replace or extend this with live URLs via scrape_company_text().
    """
    return [
        {
            "source_url": "https://apexdentalclinic.example.com",
            "raw_text": (
                "Apex Dental & Orthodontics Lahore. Over 25 dental specialists across 3 branches. "
                "Patients can book appointments by calling our reception desk between 9 AM and 5 PM. "
                "Specializing in cosmetic dentistry, implants, and Invisalign for families and professionals."
            )
        },
        {
            "source_url": "https://primeestates.example.com",
            "raw_text": (
                "Prime Estates Brokerage. A team of 40 real estate agents handling commercial and "
                "luxury residential properties. Currently managing inquiries via manual WhatsApp messages "
                "and contact forms. Looking to expand our digital footprint."
            )
        }
    ]