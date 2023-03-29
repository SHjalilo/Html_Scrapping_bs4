# Import Required Modules
from bs4 import BeautifulSoup
import requests
 
# HTML Code
html_content = """
<ul>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ul>
"""
 
# Parse the html content
soup = BeautifulSoup(html_content, "lxml")
 
# Find all li tag
datas = soup.find_all("li")
 
# Iterate through all li tags
for data in datas:
    # Get text from each tag
    print(data.text)
 
print(f"Total {len(datas)} li tag found")