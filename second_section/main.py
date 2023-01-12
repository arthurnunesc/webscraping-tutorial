from bs4 import BeautifulSoup
import requests


html_text = requests.get("https://www.infojobs.net/jobsearch/search-results/list.xhtml?keyword=Python&normalizedJobTitleIds=&provinceIds=&cityIds=&teleworkingIds=&categoryIds=&workdayIds=&educationIds=&segmentId=&contractTypeIds=&page=1&sortBy=RELEVANCE&onlyForeignCountry=false&countryIds=&sinceDate=ANY&subcategoryIds=").text
soup = BeautifulSoup(html_text, "lxml")
print(soup)
jobs = soup.select("div.ij-OfferCardContent-description")
print(jobs)