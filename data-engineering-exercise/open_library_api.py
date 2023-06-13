import requests


class OpenLibraryAPI:
    def __init__(self):
        self.base_url = "https://openlibrary.org"

    def get_books_by_subject(self, subject, limit=100):
        url = f"{self.base_url}/subjects/{subject}.json?limit={limit}"
        response = self.callRestAPI(url)
        if response.status_code == 200:
            data = response.json()
            return data.get("works", [])
        else:
            print(f"Failed to retrieve books for subject '{subject}'")
            return []

    def get_author_details(self, author_key):
        url = f"{self.base_url}/authors/{author_key}.json"
        response = self.callRestAPI(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Failed to retrieve author details for key '{author_key}'")
            return None

    def callRestAPI(self, url):
        try:
            response = requests.get(url)
        except Exception as e:
            print(e)
        return response
