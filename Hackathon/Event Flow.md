

Certainly! Here’s a step-by-step walkthrough of the backend flow for your project. This outline assumes you’re using SQLite for the database, pandas for CSV handling, and a Markdown to PDF conversion library like WeasyPrint or pdfkit.

### Backend Flow Walkthrough

#### 1. **Database Setup**
   - **Event**: Application Initialization
   - **Actions**:
     - Connect to the SQLite database.
     - Create tables for students, courses, grades, and advising plans if they don’t already exist.
   - **Code Example**:
     ```python
     def setup_database():
         conn = sqlite3.connect('advising_system.db')
         cursor = conn.cursor()
         cursor.execute('''CREATE TABLE IF NOT EXISTS students (student_id INTEGER PRIMARY KEY, name TEXT, program TEXT)''')
         cursor.execute('''CREATE TABLE IF NOT EXISTS courses (course_id INTEGER PRIMARY KEY, course_code TEXT, title TEXT, semester TEXT, year INTEGER)''')
         cursor.execute('''CREATE TABLE IF NOT EXISTS grades (student_id INTEGER, course_id INTEGER, grade TEXT, FOREIGN KEY(student_id) REFERENCES students(student_id), FOREIGN KEY(course_id) REFERENCES courses(course_id))''')
         conn.commit()
         return conn, cursor
     ```

#### 2. **CSV Data Import**
   - **Event**: User Uploads CSV File
   - **Actions**:
     - Read CSV file using pandas.
     - Insert data into the appropriate tables in the SQLite database.
   - **Code Example**:
     ```python
     def insert_data_from_csv(filename, table_name, cursor):
         df = pd.read_csv(filename)
         df.to_sql(table_name, conn, if_exists='append', index=False)
         conn.commit()
     ```

#### 3. **Student Information Retrieval**
   - **Event**: Advisor Requests Student Information
   - **Actions**:
     - Query the database to get student’s personal details, completed courses, and current courses.
     - Compile this data into a structured format for further processing.
   - **Code Example**:
     ```python
     def get_student_info(student_id, cursor):
         student_info = cursor.execute("SELECT * FROM students WHERE student_id=?", (student_id,)).fetchone()
         completed_courses = cursor.execute("SELECT * FROM grades WHERE student_id=? AND grade >= 'C'", (student_id,)).fetchall()
         current_courses = cursor.execute("SELECT * FROM courses WHERE student_id=?", (student_id,)).fetchall()
         return student_info, completed_courses, current_courses
     ```

#### 4. **Advising Plan Generation**
   - **Event**: Advisor Requests Advising Plan for a Student
   - **Actions**:
     - Use the retrieved student information to generate an advising plan.
     - Include completed courses, current courses, and remaining required courses.
     - Account for course dependencies.
   - **Code Example**:
     ```python
     def generate_advising_plan(student_id, cursor):
         student_info, completed_courses, current_courses = get_student_info(student_id, cursor)
         required_courses = cursor.execute("SELECT * FROM required_courses WHERE program=?", (student_info['program'],)).fetchall()
         remaining_courses = [course for course in required_courses if course not in completed_courses]
         advising_plan = {
             'student_info': student_info,
             'completed_courses': completed_courses,
             'current_courses': current_courses,
             'remaining_courses': remaining_courses
         }
         return advising_plan
     ```

#### 5. **Document Creation**
   - **Event**: Advisor Finalizes Advising Plan
   - **Actions**:
     - Convert the advising plan to a Markdown document.
     - Convert the Markdown document to a PDF.
   - **Code Example**:
     ```python
     def generate_markdown_document(advising_plan):
         md_content = f"# Advising Plan for {advising_plan['student_info']['name']}\n\n"
         md_content += "## Completed Courses\n"
         for course in advising_plan['completed_courses']:
             md_content += f"- {course['course_code']}: {course['title']} (Grade: {course['grade']})\n"
         md_content += "## Current Courses\n"
         for course in advising_plan['current_courses']:
             md_content += f"- {course['course_code']}: {course['title']}\n"
         md_content += "## Remaining Courses\n"
         for course in advising_plan['remaining_courses']:
             md_content += f"- {course['course_code']}: {course['title']}\n"
         return md_content

     def convert_markdown_to_pdf(md_content):
         html_content = markdown.markdown(md_content)
         pdfkit.from_string(html_content, 'advising_plan.pdf')
     ```

#### 6. **Failed Students Report Generation**
   - **Event**: Advisor Requests Report of Failed Students
   - **Actions**:
     - Query the database for students who have failed courses.
     - Generate a report listing these students.
   - **Code Example**:
     ```python
     def generate_failed_students_report(cursor):
         failed_students = cursor.execute("SELECT student_id, course_id FROM grades WHERE grade < 'C'").fetchall()
         # Generate report here
         return failed_students
     ```

### Summary
1. **Database Setup**: Initialize the SQLite database and create tables.
2. **CSV Data Import**: Import student, course, and grade data from CSV files into the database.
3. **Student Information Retrieval**: Query the database for student information.
4. **Advising Plan Generation**: Generate advising plans based on retrieved data.
5. **Document Creation**: Convert advising plans to Markdown and then to PDF.
6. **Failed Students Report Generation**: Generate and retrieve reports on failed students.

This flow ensures that the system can handle the essential tasks of importing data, generating advising plans, and creating necessary reports, all while maintaining a user-friendly and efficient process. If you need more detailed explanations or further assistance, feel free to ask!
