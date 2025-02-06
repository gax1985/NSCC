

Here are the **if statements**, **for statements**, **while statements**, and **exception statements** from the given workflow:

### **If Statements**
- Checking if tables exist in the database setup:
  ```python
  cursor.execute('''CREATE TABLE IF NOT EXISTS students (student_id INTEGER PRIMARY KEY, name TEXT, program TEXT)''')
  cursor.execute('''CREATE TABLE IF NOT EXISTS courses (course_id INTEGER PRIMARY KEY, course_code TEXT, title TEXT, semester TEXT, year INTEGER)''')
  cursor.execute('''CREATE TABLE IF NOT EXISTS grades (student_id INTEGER, course_id INTEGER, grade TEXT, FOREIGN KEY(student_id) REFERENCES students(student_id), FOREIGN KEY(course_id) REFERENCES courses(course_id))''')
  ```

- Check if the file exists and if the table name is valid before reading and inserting data.
    
    python
    
    ```
    def insert_data_from_csv(filename, table_name, cursor):
        if os.path.exists(filename) and table_name in ["students", "courses", "grades"]:
            try:
                df = pd.read_csv(filename)
                df.to_sql(table_name, conn, if_exists='append', index=False)
                conn.commit()
            except pd.errors.ParserError as e:
                print(f"CSV parsing error: {e}")
            except Exception as e:
                print(f"General error: {e}")
        else:
            print("File does not exist or invalid table name.")
    ```
### **For Statements**
- Looping through completed courses, current courses, and remaining courses in the document creation:
  ```python
  for course in advising_plan['completed_courses']:
      md_content += f"- {course['course_code']}: {course['title']} (Grade: {course['grade']})\n"
  
  for course in advising_plan['current_courses']:
      md_content += f"- {course['course_code']}: {course['title']}\n"
  
  for course in advising_plan['remaining_courses']:
      md_content += f"- {course['course_code']}: {course['title']}\n"
  ```

- Loop through failed students to format the report.
    
    python
    
    ```
    def generate_failed_students_report(cursor):
        failed_students = cursor.execute("SELECT student_id, course_id FROM grades WHERE grade < 'C'").fetchall()
        
        report = []
        for student_id, course_id in failed_students:
            student_name = cursor.execute("SELECT name FROM students WHERE student_id=?", (student_id,)).fetchone()
            course_title = cursor.execute("SELECT title FROM courses WHERE course_id=?", (course_id,)).fetchone()
            report.append({
                "student_id": student_id,
                "student_name": student_name["name"],
                "course_id": course_id,
                "course_title": course_title["title"]
            })
        
        return report
    ```
- Iterate through fetched courses to compile structured data.
    
    python
    
    ```
    def get_student_info(student_id, cursor):
        student_info = cursor.execute("SELECT * FROM students WHERE student_id=?", (student_id,)).fetchone()
        completed_courses = cursor.execute("SELECT * FROM grades WHERE student_id=? AND grade >= 'C'", (student_id,)).fetchall()
        current_courses = cursor.execute("SELECT * FROM courses WHERE student_id=?", (student_id,)).fetchall()
        
        # Compiling structured data
        course_data = []
        for course in completed_courses + current_courses:
            course_data.append({
                "course_id": course["course_id"],
                "title": course["title"],
                "semester": course["semester"],
                "year": course["year"]
            })
            
        return student_info, course_data
    ```
### **While Statements**
- There are no direct while statements in the provided workflow. However, if you were to handle retries or waiting for certain conditions, you might use a while loop like this:
  ```python
  while not condition_met:
      # Perform some action
      if some_condition:
          break
  ```

- Handle prerequisites or course dependencies more dynamically.
    
    python
    
    ```
    def generate_advising_plan(student_id, cursor):
        student_info, completed_courses, current_courses = get_student_info(student_id, cursor)
        required_courses = cursor.execute("SELECT * FROM required_courses WHERE program=?", (student_info['program'],)).fetchall()
        
        remaining_courses = [course for course in required_courses if course not in completed_courses]
        
        # Checking prerequisites
        advising_plan = []
        while remaining_courses:
            course = remaining_courses.pop(0)
            if not has_prerequisites(course, completed_courses):
                remaining_courses.append(course)  # Defer course till prerequisites are met
            else:
                advising_plan.append(course)
        
        return {
            'student_info': student_info,
            'completed_courses': completed_courses,
            'current_courses': current_courses,
            'remaining_courses': advising_plan
        }
    ```
### **Exception Statements**
- Handling potential exceptions in the database setup and CSV data import:
  ```python
  try:
      conn = sqlite3.connect('advising_system.db')
      cursor = conn.cursor()
      cursor.execute('''CREATE TABLE IF NOT EXISTS students (student_id INTEGER PRIMARY KEY, name TEXT, program TEXT)''')
      cursor.execute('''CREATE TABLE IF NOT EXISTS courses (course_id INTEGER PRIMARY KEY, course_code TEXT, title TEXT, semester TEXT, year INTEGER)''')
      cursor.execute('''CREATE TABLE IF NOT EXISTS grades (student_id INTEGER, course_id INTEGER, grade TEXT, FOREIGN KEY(student_id) REFERENCES students(student_id), FOREIGN KEY(course_id) REFERENCES courses(course_id))''')
      conn.commit()
  except sqlite3.Error as e:
      print(f"Database error: {e}")
  except Exception as e:
      print(f"General error: {e}")
  
  try:
      df = pd.read_csv(filename)
      df.to_sql(table_name, conn, if_exists='append', index=False)
      conn.commit()
  except pd.errors.ParserError as e:
      print(f"CSV parsing error: {e}")
  except Exception as e:
      print(f"General error: {e}")
  ```

- Ensure database connection and table creation handle specific exceptions.
    
    python
    
    ```
    def setup_database():
        try:
            conn = sqlite3.connect('advising_system.db')
            cursor = conn.cursor()
            # Creating tables
            cursor.execute('''CREATE TABLE IF NOT EXISTS students (student_id INTEGER PRIMARY KEY, name TEXT, program TEXT)''')
            cursor.execute('''CREATE TABLE IF NOT EXISTS courses (course_id INTEGER PRIMARY KEY, course_code TEXT, title TEXT, semester TEXT, year INTEGER)''')
            cursor.execute('''CREATE TABLE IF NOT EXISTS grades (student_id INTEGER, course_id INTEGER, grade TEXT, FOREIGN KEY(student_id) REFERENCES students(student_id), FOREIGN KEY(course_id) REFERENCES courses(course_id))''')
            conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"General error: {e}")
        return conn, cursor
    ```