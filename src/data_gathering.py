import requests
from xml.etree import ElementTree as ET
import random
import re

def get_pmc_ids():
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    search_params = {
        "db": "pmc",
        "term": "open access[filter]",  # Filter for open access articles
        "retmax": "10000",  # Retrieve a large number of IDs
        "retmode": "json"
    }

    response = requests.get(search_url, params=search_params)
    search_results = response.json()
    return search_results['esearchresult']['idlist']

# Step 2: Select random IDs
def select_random_ids(pmc_ids, num_ids=10):
    return random.sample(pmc_ids, num_ids)

# Step 3: Fetch article details
def fetch_articles(article_ids):
    fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    fetch_params = {
        "db": "pmc",
        "id": ",".join(article_ids),
        "retmode": "xml"
    }

    response = requests.get(fetch_url, params=fetch_params)
    return response.text

# Step 4: Parse the XML and extract acknowledgments
def parse_acknowledgments(articles_xml):
    root = ET.fromstring(articles_xml)
    namespaces = {'': root.tag.split('}')[0].strip('{')}
    ack_sections = []
    for article in root.findall('.//article'):
        ack_section = article.find('.//ack') or \
                      article.find('.//acknowledgments') or \
                      article.find('.//acknowledgements')
        
        if ack_section is not None:
            ack_text = ' '.join(ack_section.itertext())
            # Remove any title-like words ("Acknowledgments", "Acknowledgement", etc.) and leading/trailing whitespaces
            cleaned_text = re.sub(r'^\s*(?i)(Acknowledgments?|Acknowledgement|Acknowledgements)\s*\n?', '', ack_text)
            # Remove any leading 's' and newlines, and strip leading/trailing spaces
            cleaned_text = re.sub(r'^\s*s', '', cleaned_text).strip()
            ack_sections.append(cleaned_text)
            #print("Acknowledgments:", )
        else:
            pass
            #print("Acknowledgments: None found")
    return ack_sections


def parse_funding(articles_xml):
    root = ET.fromstring(articles_xml)
    namespaces = {'': root.tag.split('}')[0].strip('{')}
    funding_sections = []

    for article in root.findall('.//article'):
        funding_section = article.find('.//funding-group')
        
        if funding_section is not None:
            funding_text = ' '.join(funding_section.itertext())
            funding_sections.append(funding_text)
        else:
            funding_sections.append("")
    
    return funding_sections

