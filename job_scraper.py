import requests
from bs4 import BeautifulSoup
def fetch_jobs(url):
   headers = {"User-Agent": "Mozilla/5.0"}
   response = requests.get(url, headers=headers, timeout=15)
   soup = BeautifulSoup(response.text, "html.parser")
   jobs = []
   for a in soup.find_all("a"):
       title = a.get_text(strip=True).lower()
       link = a.get("href")
       if title and link and "java" in title:
           if link.startswith("/"):
               link = "https://www.linkedin.com" + link
           jobs.append({
               "title": title,
               "link": link
           })
   return jobs
