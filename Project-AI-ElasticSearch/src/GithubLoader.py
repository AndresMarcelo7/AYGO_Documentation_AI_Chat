import requests
from bs4 import BeautifulSoup

class GitHubMarkdownLoader:
    def __init__(self, repo_url):
        self.repo_url = repo_url

    def load(self):
        response = requests.get(self.repo_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            markdown_links = []
            for link in soup.find_all('a', href=True):
                href = link['href']
                if href.endswith('.md'):
                    markdown_links.append(href)
            return markdown_links
        else:
            raise Exception(f"Failed to load data from {self.repo_url}")