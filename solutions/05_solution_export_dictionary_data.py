'''
OPTIONAL AI GUIDANCE PROMPT
---------------------------
I am a student in an introductory Python class. I am learning many coding
principles for the very first time. I am going to paste in the instructions
to a practice problem that my professor gave me to try before class.
Please be my kind tutor and walk me through how to solve the problem step
by step.

Don't just give me the full solution all at once (unless I later ask for
it). Instead, help me work through it gradually, with clear explanations
and small, easy-to-understand examples. Please use everyday language and
explain things in a simple, friendly way.

INSTRUCTIONS:
-------------
1. Create an empty list called "books" that will hold dictionaries.

2. Use a while loop to repeatedly:
   - Ask the user to enter a book title.
   - Ask the user to enter the book's author.
   - Create a dictionary with two keys: "title" and "author".
   - Append this dictionary to the "books" list.

3. After adding a book, ask:
   "Add another book? (yes/no)"
   - If the user enters "yes", continue the loop.
   - If the user enters "no", end the loop.

4. When the loop ends:
   - Convert the list of dictionaries into a pandas DataFrame.
   - Export the DataFrame to an Excel file named
     "library_books.xlsx" using df.to_excel().
   - Do not include the index column in the Excel file.

5. Test your program by running it and entering several books.
   Then open the Excel file to confirm that the data was saved.
'''

import pandas as pd

# Step 1: create empty list
books = []

# Step 2: collect book data
while True:
    title = input("Enter book title: ").strip()
    author = input(f"Enter author of '{title}': ").strip()
    books.append({"title": title, "author": author})

    another = input("Add another book? (yes/no): ").strip().lower()
    if another != "yes":
        break

# Step 4: convert to DataFrame and export
df = pd.DataFrame(books)
df.to_excel("library_books.xlsx", index=False)

print("\nData saved to 'library_books.xlsx'")
