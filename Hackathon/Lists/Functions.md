

 **Establishing the database connection**:
  ```python
  def setup_database():
      # Create database and tables
  ```
- [ ] **Insert data from CSV**:
  ```python
  def insert_data_from_csv(filename, table_name, cursor):
      # Read CSV and insert into the database
  ```
- [ ] **Retrieve student info**:
  ```python
  def get_student_info(student_id, cursor):
      # Query database for student info
  ```
- [ ] **Generate advising plan**:
  ```python
  def generate_advising_plan(student_id, cursor):
      # Create advising plan based on student data
  ```
- [ ] **Generate Markdown document**:
  ```python
  def generate_markdown_document(advising_plan):
      # Convert advising plan to Markdown format
  ```
- [ ] **Convert Markdown to PDF**:
  ```python
  def convert_markdown_to_pdf(md_content):
      # Convert Markdown to PDF
  ```
- [ ] **Generate failed students report**:
  ```python
  def generate_failed_students_report(cursor):
      # Retrieve and list students who have failed courses
  ```


