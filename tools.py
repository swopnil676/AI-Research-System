# from langchain.tools import tool
# from bs4 import BeautifulSoup
# from tavily import TavilyClient
# import os
# import requests
# from dotenv import load_dotenv
# load_dotenv()
# from rich import print

# tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


# @tool
# def web_search(query : str) -> str:
#     """Search the web for recent and reliable information on a topic. Returns Titles , URLs and snippets."""
#     results = tavily.search(query=query, max_results=5)

#     out = []

#     for r in results['results']:
#         out.append(
#             f"Title : {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n"
#         )

#     return "\n----\n".join(out)


# @tool
# def scrape_url(url: str) -> str:
#     """Scrape and return clean text content from a given URL for deeper reading."""
#     try:
#         resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
#         soup = BeautifulSoup(resp.text, "html.parser")
#         for tag in soup(["script", "style", "nav", "footer"]):
#             tag.decompose()
#         return soup.get_text(separator=" ", strip=True)[:3000]
#     except Exception as e:
#         return f"Could not scrape URL: {str(e)}"

# # print(scrape_url.invoke("https://www.hindustantimes.com/cricket/new-zealand-odis-in-countdown-to-world-cup-india-s-chance-to-fix-bowling-101793709519519.html"))



# Updated code for groq api call

from langchain.tools import tool
from bs4 import BeautifulSoup
from tavily import TavilyClient
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

tavily = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


@tool
def web_search(query: str) -> str:
    """Search the web and return actual source titles, URLs and snippets."""

    response = tavily.search(
        query=query,
        search_depth="advanced",
        max_results=5,
        include_answer=False
    )

    sources = []

    for result in response.get("results", []):

        url = result.get("url", "").strip()

        # Accept only actual HTTP/HTTPS URLs
        if not url.startswith(("https://", "http://")):
            continue

        sources.append({
            "title": result.get("title", "Untitled"),
            "url": url,
            "snippet": result.get("content", "")[:500]
        })

    return json.dumps(sources, indent=4, ensure_ascii=False)


@tool
def scrape_url(url: str) -> str:
    """Scrape clean webpage content from a valid source URL."""

    try:
        response = requests.get(
            url,
            timeout=15,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        for tag in soup([
            "script", "style", "nav",
            "footer", "header", "aside"
        ]):
            tag.decompose()

        content = soup.get_text(separator=" ", strip=True)

        return content[:6000]

    except requests.RequestException as e:
        return f"Could not access webpage: {str(e)}"
