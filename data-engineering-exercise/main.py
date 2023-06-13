import re

import pandas as pd

from open_library_api import OpenLibraryAPI
'''
This class is just for demonstration purpose. Only covers few positive test case scenario. Proper error handling needs to be implemented and needs 
to provide more flexibility and options to pass multiple subjects. Currently supporting only single subject. 
We will add database or cache layer to avoid to go to Open Library API to fetch data. First we will check in our storage if not found than go to Open API.
'''
# Define the subject you are interested in
subject_of_interest = "physics"
# Initialize Open Library API
api = OpenLibraryAPI()

def flattenBook(book):
    '''
    :param book:
    :return: void
    Logic:
    This is just to show flatten the availability for better read in csv. This will need to work make it fully automatic instead of hardcoded logic.
    This logic also depends on our database choice if we choose database which supports collection like cassandra, riak then we do not need to flatten.
    We assume that our database does not support collection.
    '''
    book_availability = book.get("availability")
    if book_availability:
        book["status"] = book_availability.get("status")
    else:
        book["status"] = ""

def populateAuthorAndBook(book):
    '''
    :param book:
    :return: void
    Logic:
    This method fetches the Author using book title and populate the joining table of book and author as well as author.
    '''
    book_title = book.get("title", "")
    for i in range(len(book.get("authors", [""]))):
        author_key = book.get("authors", [""])[i].get(
            "key")
        # Clean the data and remove the /string inside the slashes/
        author_key = re.sub(r'/.*?/', '', author_key)
        # Retrieve author details
        author_details = api.get_author_details(author_key)
        # Append author data to the list
        if author_details:
            author_name = author_details.get("name", "")
            author_data.append({"author_key": author_key, "author_name": author_name})

        # Join author and book
        book_key = book.get("key", "")
        # Clean the data and remove the /string inside the slashes/
        book_key = re.sub(r'/.*?/', '', book_key)
        book_author_data.append({"book_key": book_key, "author_key": author_key})

if __name__ == '__main__':
    # Retrieve a list of books related to the subject
    books = api.get_books_by_subject(subject_of_interest, limit=100)

    # Initialize lists to store book and author data
    author_data = []
    book_author_data = []
    # Iterate through each book and retrieve author details
    for book in books:
        flattenBook(book)
        populateAuthorAndBook(book)

    # Create DataFrames from the collected data
    book_df = pd.DataFrame(books)
    book_df = book_df.drop(
        columns=['subject', 'authors', 'ia_collection', 'ia', 'has_fulltext', 'public_scan', 'availability'])
    # Rename columns using rename() method
    book_df = book_df.rename(columns={'key': 'book_key'})
    # Remove slashes and values between them in Column1
    book_df['book_key'] = book_df['book_key'].str.replace(r'\/.*?\/', '', regex=True)

    author_df = pd.DataFrame(author_data)
    book_author_df = pd.DataFrame(book_author_data).drop_duplicates();

    # Store the DataFrames as CSV files
    book_df.to_csv("book_data.csv", index=False)
    author_df.to_csv("author_data.csv", index=False)
    book_author_df.to_csv("book_author_data.csv", index=False)

    print("Data retrieval and storage completed.")
