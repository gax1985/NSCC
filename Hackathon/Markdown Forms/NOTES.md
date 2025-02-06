


### Summary of Required Format for Forms According to Michael

#### 1. **Failing Students' Form**
- **Purpose:** List all students failing a class.
- **Format:**
  - **Student ID**
  - **Student Name**
  - **Failed Course Code**
  - **Failed Course Title**
  - **Grade**
  - **Program**
  - **Term**

#### 2. **Student Advising Form**
- **Purpose:** To advise students on their academic progress and create plans for current and next semesters.
- **Format:**
  - **Student Information:**
    - **Student ID**
    - **Student Name**
    - **Program Name**
    - **Year** (e.g., Year 1, Year 2)
  - **Courses List:**
    - **Current Semester Courses:** List all courses the student is currently enrolled in.
      - **Course Code**
      - **Course Title**
      - **Status** (e.g., IP, Completed)
      - **Interim Grade**
      - **Attendance**
    - **Next Semester Courses:** List planned courses for the next semester.
      - **Course Code**
      - **Course Title**
  - **Additional Information:**
    - **Total Units of Courses Enrolled**
    - **Scheduling Information**
    - **Completed Courses** (with Grades if passed)
    - **Incomplete Courses** (e.g., failed or withdrawn)

#### 3. **Student Information Form**
- **Purpose:** Provide detailed student information and academic progress.
- **Format:**
  - **Student Details:**
    - **Student ID** (Mandatory)
    - **Student Name** (Mandatory)
    - **Program** (e.g., Cybersecurity)
    - **Academic Advisor**
    - **Student Services Advisor**
  - **Academic Plan:**
    - **Required Courses:** List all required courses for the program.
      - **Course Code**
      - **Course Title**
      - **Prerequisites**
  - **Course History:**
    - **Completed Courses:** Include grades and term.
      - **Course Code**
      - **Course Title**
      - **Grade**
      - **Term**
    - **Current Semester Courses:**
      - **Course Code**
      - **Course Title**
      - **Status**
      - **Interim Grade**
      - **Attendance**
    - **Planned Courses for Next Semester:**
      - **Course Code**
      - **Course Title**

### Example Markdown Formats

#### Failing Students' Form
```markdown
## Failing Students

| Student ID | Student Name | Failed Course Code | Failed Course Title | Grade | Program | Term |
|:------------:|:--------------:|:--------------------:|:---------------------:|:-------:|:---------:|:------:|
| 12345      | John Doe     | CS101              | Introduction to CS  | F     | CS      | Fall 21 |
| 67890      | Jane Smith   | MATH102            | Calculus I          | F     | Math    | Spring 22 |
```

#### Student Advising Form
```markdown
## Student Advising Form

### Student Information
- **Student ID:** 12345
- **Student Name:** John Doe
- **Program Name:** Cybersecurity
- **Year:** Year 1

### Courses List

#### Current Semester Courses
| Course Code | Course Title        | Status | Interim Grade | Attendance |
|-------------|---------------------|--------|---------------|------------|
| CS101       | Introduction to CS  | IP     | B             | 95%        |
| MATH102     | Calculus I          | IP     | A             | 90%        |

#### Next Semester Courses
| Course Code | Course Title        |
|-------------|---------------------|
| CS201       | Data Structures     |
| MATH202     | Calculus II         |

### Additional Information
- **Total Units of Courses Enrolled:** 12
- **Scheduling Information:** To be scheduled by registrar
- **Completed Courses:** 
  - CS101: Introduction to CS (Grade: B)
  - MATH102: Calculus I (Grade: A)
- **Incomplete Courses:** 
  - None
```

#### Student Information Form
```markdown
## Student Information Form

### Student Details
- **Student ID:** 12345
- **Student Name:** John Doe
- **Program:** Cybersecurity
- **Academic Advisor:** Dr. Smith
- **Student Services Advisor:** Jane Doe

### Academic Plan

#### Required Courses
| Course Code | Course Title            | Prerequisites  |
|-------------|-------------------------|----------------|
| CS101       | Introduction to CS      | None           |
| CS201       | Data Structures         | CS101          |

### Course History

#### Completed Courses
| Course Code | Course Title            | Grade | Term       |
|-------------|-------------------------|-------|------------|
| CS101       | Introduction to CS      | B     | Fall 21    |
| MATH102     | Calculus I              | A     | Spring 22  |

#### Current Semester Courses
| Course Code | Course Title            | Status | Interim Grade | Attendance |
|-------------|-------------------------|--------|---------------|------------|
| CS201       | Data Structures         | IP     | B             | 95%        |
| MATH202     | Calculus II             | IP     | A             | 90%        |

#### Planned Courses for Next Semester
| Course Code | Course Title            |
|-------------|-------------------------|
| CS301       | Algorithms              |
| MATH303     | Linear Algebra          |
```

This format ensures clarity, usability, and easy input of data. If you need any modifications or further details, feel free to ask!