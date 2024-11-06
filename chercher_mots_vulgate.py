import requests
from bs4 import BeautifulSoup
import pandas as pd

def search_biblegateway(keyword):
    url = f"https://www.biblegateway.com/quicksearch/?quicksearch={keyword}&version=VULGATE"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    results = []
    for item in soup.find_all('li', class_='row bible-item'):
        reference = item.find('a', class_='bible-item-title').get_text(strip=True)
        verse_text = item.find('div', class_='bible-item-text').get_text(strip=True)
        results.append({'Keyword': keyword, 'Reference': reference, 'Verse': verse_text})
    
    return results

def save_to_excel(data, filename):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)

if __name__ == "__main__":
    keywords = input("Enter the keywords to search, separated by commas: ").split(',')
    all_results = []
    for keyword in keywords:
        keyword = keyword.strip()
        results = search_biblegateway(keyword)
        all_results.extend(results)
    
    save_to_excel(all_results, 'bible_search_results.xlsx')
    print(f"Results saved to bible_search_results.xlsx")
