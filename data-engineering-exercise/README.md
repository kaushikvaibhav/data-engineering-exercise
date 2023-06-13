To run and test the above code, you can follow these steps:

1. Make sure you have Python and the required dependencies installed. If not, you can install them by running the
   following command in the terminal:
2. pip install -r data_pipeline/requirements.txt
3. Open the project in PyCharm.
4. In the project explorer, navigate to the data_pipeline directory and open the main.py file.
5. Right-click inside the main.py file editor and select "Run 'main'".
6. The data pipeline code will execute, retrieving books and author details from the Open Library API and storing the
   data in CSV files.
7. After the code execution completes, you should see the CSV files (book_data.csv and author_data.csv) generated in the
   project directory.
8. You can open the generated CSV files to verify the data retrieved from the Open Library API.
   This is the basic process to run and test the code. You can modify the subject_of_interest variable in main.py to
   pull data for different subjects. Additionally, you can add additional tests or assertions in the code to verify the
   correctness of the data processing and storage steps.