**Task 1** - Data Cleaning and Preprocessing

Objective:

As part of my Data Analyst Internship, this task was focused on cleaning a raw dataset by fixing common data issues such as missing values, inconsistent formats, and duplicate records. I used Python and Pandas to carry out the entire cleaning process.

---

Dataset Used:

- Input File: [`database.csv`](database.csv)
- Cleaned Output: [`cleaned_database.csv`](cleaned_database.csv)
- Tools: Python (Spyder 6), Pandas

The dataset is a fictional user signup data (names, age, gender, country, signup date, and email). It’s similar to basic customer information datasets like those used in CRM systems or the Customer Personality Analysis dataset on Kaggle.

---

What I Did (Steps Followed)

1. Renamed column headers to lowercase and replaced spaces with underscores.
2. Converted "age" to numeric (e.g., handled "twenty-eight") and filled missing values using the median.
3. Filled missing names with "Unknown".
4. Standardized gender values to "male" and "female".
5. Standardized country names (e.g., "us","united states" → "usa").
6. Parsed various date formats in "signup_date" using "infer_datetime_format=True".
7. Dropped duplicate records from the dataset.
8. Exported the final cleaned dataset to "cleaned_database.csv" and the output is screenshotted and saved as "task1_output.png".

---

Files in This Repo

- [`task1.py`](task1.py): Code for data cleaning
- [`task1_output.png`](task1_output.png): Screenshot of cleaned dataset
- [`README.md`](README.md): This file

---

Tools I Used 

- Python 3.11
- Pandas library
- Spyder 6 IDE
- GitHub (for version control)

---

My Takeaways

This task gave me real hands-on experience with data preprocessing. I learned how important it is to clean data before moving on to analysis or visualization. It also helped me get better at handling date formats, missing data, and text standardization.

---

Submission Info

This project was done for Task 1 of the Data Analyst Internship.

🔗 [Submission Link](https://forms.gle/o2uMAByM719GzebC7)

