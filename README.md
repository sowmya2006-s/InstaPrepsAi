# InstaPrepsAI - Training Kit

This repository contains all the projects and exercises completed as part of the **InstaPrepsAI Training Kit**. The training included hands-on work with React, Rails, Python, Postgres, and Excel data manipulation.

---

1. **Company Document**
   - Created a 2-page document about the company **InstaPrepsAI**.

2. **Hello World Project**
   - Built a "Hello World" project in one of the following:
     - React
     - Android Studio
     - Ruby on Rails (RoR)

3. **Postgres Database**
   - Created a Postgres database to store student data.
   - Created a table and performed delete operations.

4. **Excel to Database (Python)**
   - Wrote a Python program to import Excel data into Postgres.
   - **Tools used:** `pandas`, `openpyxl`, `psycopg2`.
   - Sample file: `data.xlsx`.

5. **Excel Column Rename (Python)**
   - Wrote a Python program to change column names in an Excel file.

---

6. **Fetch Data from API**
   - For React/Android/Swift developers:
     - Fetched data from: `http://staging.instapreps.com/api/board`
     - Displayed board data on a page using **React**.
     - Used `axios` for API requests.

7. **Rails API - Students**
   - For Rails developers:
     - Created a Rails API that provides a list of students in JSON format.
     - Implemented `Student` model and `StudentsController#index`.
     - Endpoint: `/students`
     - Example JSON response:

```json
[
  { "id":1, "name":"Riya", "age":16, "grade":"10th" },
  { "id":2, "name":"Arjun", "age":17, "grade":"11th" },
  { "id":3, "name":"Sowmya", "age":18, "grade":"12th" }
]
