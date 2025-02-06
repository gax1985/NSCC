Sure! Let's go through the script step by step and explain each part.

### Imports
```python
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os
```
- **import tkinter**: Imports the tkinter module, which is used for creating graphical user interfaces (GUIs) in Python.
- **from tkinter import \***: Imports all functions, classes, and variables from the tkinter module.
- **from tkinter import filedialog**: Imports the filedialog module, which provides dialogs for file and directory selection.
- **from tkinter import ttk**: Imports the ttk module, which provides themed widgets.
- **import os**: Imports the os module, which provides a way to interact with the operating system.

### Function: searchFile
```python
def searchFile():
    pwd = os.getcwd()
    fileLocation = filedialog.askopenfilename(parent=root, initialdir=pwd, title='Please select a file', filetypes=(('Excel Spreadsheet', '*.xlsx'), ("All files", "*.*")))
    return fileLocation
```
- **pwd = os.getcwd()**: Gets the current working directory.
- **fileLocation = filedialog.askopenfilename(...)**: Opens a file dialog box for the user to select a file. The initial directory is set to the current working directory, and the dialog box allows selection of Excel files or any file type.
- **return fileLocation**: Returns the path to the selected file.

### Function: searchFolder
```python
def searchFolder():
    pwd = os.getcwd()
    directoryLoc = filedialog.askdirectory(parent=root, initialdir=pwd, title='Please select a directory')
    return directoryLoc
```
- **pwd = os.getcwd()**: Gets the current working directory.
- **directoryLoc = filedialog.askdirectory(...)**: Opens a directory dialog box for the user to select a directory. The initial directory is set to the current working directory.
- **return directoryLoc**: Returns the path to the selected directory.

### Function: filterTermInfo
```python
def filterTermInfo(studentData):
    courses_per_term = []
    for i in range(0,len(studentData['remaining_courses'])):
        for course in studentData['remaining_courses'][i]['course_list']:
            courses_per_term.append(course)

    return courses_per_term
```
- **courses_per_term = []**: Initializes an empty list to store courses.
- **for i in range(0,len(studentData['remaining_courses']))**: Iterates through the remaining courses for each term.
- **for course in studentData['remaining_courses'][i]['course_list']**: Iterates through the course list for each term.
- **courses_per_term.append(course)**: Appends each course to the `courses_per_term` list.
- **return courses_per_term**: Returns the list of courses for all terms.

### Function: createCourselist
```python
def createCourselist(root, codes):
    sessionCombos = []
    possible_codes=[]

    for course in codes:
        possible_codes.append(course['code'])

    for i in range(6):
        var_store = Variable()
        course_id = ttk.Combobox(root, textvariable=var_store, width=9)
        course_id['values'] = possible_codes
        course_id.state(["readonly"])
        sessionCombos.append(course_id)

    return sessionCombos
```
- **sessionCombos = []**: Initializes an empty list to store combobox widgets.
- **possible_codes = []**: Initializes an empty list to store possible course codes.
- **for course in codes**: Iterates through the list of course codes.
- **possible_codes.append(course['code'])**: Appends each course code to the `possible_codes` list.
- **for i in range(6)**: Loops 6 times to create 6 combobox widgets.
- **var_store = Variable()**: Creates a variable to store the selected value of the combobox.
- **course_id = ttk.Combobox(...)**: Creates a combobox widget with the possible course codes.
- **course_id['values'] = possible_codes**: Sets the values for the combobox to the list of possible course codes.
- **course_id.state(["readonly"])**: Makes the combobox readonly.
- **sessionCombos.append(course_id)**: Appends the combobox to the `sessionCombos` list.
- **return sessionCombos**: Returns the list of combobox widgets.

### Function: placeTermCourse
```python
def placeTermCourse(courseList, bg):
    for i in range(6):
        courseList[i].place(x=57, y=(225 + (i * 20)))
        courseList[i].tkraise(aboveThis=bg)
```
- **for i in range(6)**: Loops 6 times to place 6 combobox widgets.
- **courseList[i].place(x=57, y=(225 + (i * 20)))**: Places each combobox widget at the specified x and y coordinates.
- **courseList[i].tkraise(aboveThis=bg)**: Raises the combobox above the background label.

### Main Program
```python
root = tkinter.Tk()
root.title('Student RoadmApp')
root.geometry("794x1123") #size of A4 paper at 96PPI
#root.withdraw() #use to hide tkinter window
```
- **root = tkinter.Tk()**: Creates the main tkinter window.
- **root.title('Student RoadmApp')**: Sets the title of the window.
- **root.geometry("794x1123")**: Sets the size of the window to A4 paper size at 96 PPI.
- **#root.withdraw()**: Commented out, but it hides the tkinter window.

### Adding Menu
```python
menubar = Menu(root)

file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Select Data Source', command=searchFile)
file_menu.add_command(label='Select Roadmap Directory', command=searchFolder)
file_menu.add_separator()
file_menu.add_command(label='Exit Application', command=root.destroy)
```
- **menubar = Menu(root)**: Creates a menu bar.
- **file_menu = Menu(menubar, tearoff=0)**: Creates a file menu.
- **menubar.add_cascade(label='File', menu=file_menu)**: Adds the file menu to the menu bar.
- **file_menu.add_command(label='Select Data Source', command=searchFile)**: Adds a command to the file menu to select a data source.
- **file_menu.add_command(label='Select Roadmap Directory', command=searchFolder)**: Adds a command to the file menu to select a roadmap directory.
- **file_menu.add_separator()**: Adds a separator line to the file menu.
- **file_menu.add_command(label='Exit Application', command=root.destroy)**: Adds a command to exit the application.

### Test Data and Function Calls
```python
info_test = {'id': 'W0518150', 'name': 'Evan Farrell', 'program': 'iot blah blah', 'on_track': 1, 'terms_left': 2, 'progress_roadmap': 'some image file.png', 'remaining_courses': [{'term_session': 'Fall 2019', 'course_list': [{'name': 'widgets 101', 'code': 'W1000', 'unit_value': 1, 'misc': 'could add anything else you need...'}, {'name': 'widgets 101', 'code': 'W1000', 'unit_value': 1, 'misc': 'could add anything else you need...'}]}, {'term_session': 'Winter 2020', 'course_list': [{'name': 'widgets 101', 'code': 'W1000', 'unit_value': 1, 'misc': 'could add anything else you need...'}, {'name': 'widgets 101', 'code': 'W1000', 'unit_value': 1, 'misc': 'could add anything else you need...'}]}]}

coursevar = filterTermInfo(info_test)
term_courseList = createCourselist(root, coursevar[0:6])
```
- **info_test = {...}**: Creates a dictionary with test data for a student's roadmap.
- **coursevar = filterTermInfo(info_test)**: Calls the `filterTermInfo` function with the test data to get a list of courses.
- **term_courseList = createCourselist(root, coursevar[0:6])**: Calls the `createCourselist` function to create a list of combobox widgets with the first 6 courses.

### Background Image and Layout
```python
image = PhotoImage(file="overlay-test.png")

template_bg = Label(root, image=image)
template_bg.place(x=0, y=0)

placeTermCourse(term_courseList, template_bg)

root.config(menu=menubar)
root.mainloop()
```
- **image = PhotoImage(file="overlay-test.png")**: Loads an image file for the background.
- **template_bg = Label(root, image=image)**: Creates a label widget with the background image.
- **template_bg.place(x=0, y=0)**: Places the background image at the specified coordinates.
- **placeTermCourse(term_courseList, template_bg)**: Calls the `placeTermCourse` function to place the combobox widgets on top of the background.
- **root.config(menu=menubar)**: Configures the tkinter window to use the menu bar.
- **root.mainloop()**: Starts the tkinter main loop to display the window.

### Commented-out Testing Code
```python
# for testing dialog functions


=========================================================================================

Let's go through the second script step by step and explain each part.

### Imports
```python
import fitz
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from collections import defaultdict
from PIL import Image
import cv2
import pandas as pd
import re
import numpy as np
import os
import time
import textwrap
from difflib import SequenceMatcher
```
- **import fitz**: Imports the `fitz` module, which is part of PyMuPDF, a library for working with PDF files.
- **import matplotlib.pyplot as plt**: Imports the `pyplot` module from `matplotlib` for creating plots and charts.
- **import matplotlib.patches as patches**: Imports the `patches` module from `matplotlib` for creating shapes like rectangles.
- **from collections import defaultdict**: Imports `defaultdict` from the `collections` module, which is a subclass of the dictionary that calls a factory function to supply missing values.
- **from PIL import Image**: Imports the `Image` module from the Python Imaging Library (PIL) for working with images.
- **import cv2**: Imports OpenCV, a library for computer vision tasks.
- **import pandas as pd**: Imports the `pandas` library for data manipulation and analysis.
- **import re**: Imports the `re` module for working with regular expressions.
- **import numpy as np**: Imports the `numpy` library for numerical computations.
- **import os**: Imports the `os` module for interacting with the operating system.
- **import time**: Imports the `time` module for time-related functions.
- **import textwrap**: Imports the `textwrap` module for text wrapping.
- **from difflib import SequenceMatcher**: Imports the `SequenceMatcher` class from the `difflib` module for comparing sequences.

### Constants
```python
#for testing
PDF_PATH = os.getcwd() + r"\maps\22-23\Business Intelligence Analytics - Advising Map - '22-'23.pdf"
MAP_DIR = os.getcwd() + r"\maps\22-23"
DATA_PATH= os.getcwd() + r"\SampleData\Template Data.xlsx"

LOGGING = 0
```
- **PDF_PATH**: Path to a sample PDF file.
- **MAP_DIR**: Directory containing map files.
- **DATA_PATH**: Path to a sample Excel file with template data.
- **LOGGING**: A flag to enable or disable logging (set to 0 to disable logging).

### Function: get_nparray_from_pdf
```python
def get_nparray_from_pdf(path):
    doc = fitz.open(path)
    page = doc[0]
    pix = page.get_pixmap(dpi=500)
    image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)

    cv_image = np.array(image)
    cv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR)
    return cv_image
```
- **doc = fitz.open(path)**: Opens the PDF file at the specified path.
- **page = doc[0]**: Retrieves the first page of the PDF document.
- **pix = page.get_pixmap(dpi=500)**: Renders the page as an image with a resolution of 500 DPI.
- **image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)**: Converts the rendered image to a PIL Image object.
- **cv_image = np.array(image)**: Converts the PIL Image to a NumPy array.
- **cv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR)**: Converts the image from RGB to BGR color space (used by OpenCV).
- **return cv_image**: Returns the image as a NumPy array.

### Function: pdf_coord_to_png
```python
def pdf_coord_to_png(x0_pdf, x1_pdf, y0_pdf, y1_pdf, image, page):
    width_png, height_png = image.shape[1], image.shape[0]
    width_pdf, height_pdf = page.rect.width, page.rect.height

    #calculate scaling factors
    scale_x = width_png / width_pdf
    scale_y = height_png / height_pdf

    x0_png = round(x0_pdf * scale_x)
    y0_png = round((y0_pdf * scale_y))
    x1_png = round(x1_pdf * scale_x)
    y1_png = round((y1_pdf * scale_y))

    return x0_png, x1_png, y0_png, y1_png
```
- **width_png, height_png = image.shape[1], image.shape[0]**: Gets the dimensions of the PNG image.
- **width_pdf, height_pdf = page.rect.width, page.rect.height**: Gets the dimensions of the PDF page.
- **scale_x = width_png / width_pdf**: Calculates the scaling factor for the x-axis.
- **scale_y = height_png / height_pdf**: Calculates the scaling factor for the y-axis.
- **x0_png, y0_png, x1_png, y1_png**: Converts PDF coordinates to PNG coordinates using the scaling factors.
- **return x0_png, x1_png, y0_png, y1_png**: Returns the converted coordinates.

### Function: png_to_pdf_coord
```python
def png_to_pdf_coord(x0_png, x1_png, y0_png, y1_png, image, page):
    width_png, height_png = image.shape[1], image.shape[0]
    width_pdf, height_pdf = page.rect.width, page.rect.height

    #calculate scaling factors
    scale_x = width_pdf / width_png
    scale_y = height_pdf / height_png

    x0_pdf = round(x0_png * scale_x)
    y0_pdf = round(y0_png * scale_y)
    x1_pdf = round(x1_png * scale_x)
    y1_pdf = round(y1_png * scale_y)

    return x0_pdf, x1_pdf, y0_pdf, y1_pdf
```
- Similar to `pdf_coord_to_png`, but converts PNG coordinates to PDF coordinates.

### Function: log_image
```python
def log_image(name, image):
    if LOGGING:
        cv2.imwrite(os.getcwd() + "\\imgLogs\\" + name, image)
```
- **if LOGGING**: Checks if logging is enabled.
- **cv2.imwrite(os.getcwd() + "\\imgLogs\\" + name, image)**: Saves the image to the `imgLogs` directory.

### Function: check_if_inside
```python
def check_if_inside(recA, recB):
    #recA
    xA0 = recA['x']
    yA0 = recA['y']
    xA1 = recA['x'] + recA['w']
    yA1 = recA['y'] + recA['h']

    #recB
    xB0 = recB['x']
    yB0 = recB['y']
    xB1 = recB['x'] + recB['w']
    yB1 = recB['y'] + recB['h']

    #check if each point in A is inside B
    if xA0 >= xB0 and yA0 >= yB0 and xA1 < xB1 and yA1 <= yB1:
        return True
    return False
```
- **xA0, yA0, xA1, yA1**: Gets the coordinates of the corners of rectangle A.
- **xB0, yB0, xB1, yB1**: Gets the coordinates of the corners of rectangle B.
- **if xA0 >= xB0 and yA0 >= yB0 and xA1 < xB1 and yA1 <= yB1**: Checks if rectangle A is entirely inside rectangle B.
- **return True/False**: Returns `True` if A is inside B, otherwise `False`.

### Function: parse_map
```python
def parse_map(path, count):
    image = get_nparray_from_pdf(path)
    output_image = image.copy()

    doc = fitz.open(path)
    page = doc[0]

    #define the colour range to look in
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([200, 200, 200])
    ranged_image = cv2.inRange(image, lower_black, upper_black)

    log_image(f"testranged{count}.png", ranged_image)

    # edge detection
    edges = cv2.Canny(ranged_image, 60, 80)
    kernel = np.ones((5, 5), np.uint8)

    #then dilate them to make them larger
    dilated_edges = cv2.dilate(edges, kernel, iterations=4)

    #we then want to find the two top-leftmost occurrences of the word term!
    term_recs = page.search_for("term")
    sorted(term_recs, key=lambda x: x[0])
    sorted(term_recs, key=lambda y: y[0])
    term_recs = [term_recs[0], term_recs[1]]
    term_centers = []
    for i in range(0, len(term_recs)):
        x0 = round(term_recs[i].x0)
        x1 = round(term_recs[i].x1)
        y0 = round(term_recs[i].y0)
        y1 = round(term_recs[i].y1)

        x0, x1,

        Sure! Let's continue reviewing and explaining the rest of the second script.

### Function: string_similarity
```python
def string_similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()
```
- **SequenceMatcher**: This function uses the `SequenceMatcher` class from the `difflib` module to compare two strings and returns a similarity ratio. This helps to account for typos in PDF names.

### Function: parse_maps_directory
```python
def parse_maps_directory(dir):
    programs = defaultdict(dict)

    for pdf in os.listdir(dir):
        if os.path.splitext(pdf)[1] != '.pdf':
            continue

        pdf_arr = pdf.split('-')
        programTitle = pdf_arr[0].strip()
        for program in programs.keys():
            similarity = string_similarity(programTitle, program)
            if similarity > 0.9:
                programTitle = program

        if "year1" in pdf.lower().replace(" ", ""):
            programs[programTitle]['year1'] = dir + "\\" + pdf
        elif "year2" in pdf.lower().replace(" ", ""):
            programs[programTitle]['year2'] = dir + "\\" + pdf
        else:
            programs[programTitle]['year0'] = dir + "\\" + pdf

    return programs
```
- **programs = defaultdict(dict)**: Initializes a default dictionary to store programs and their associated PDF files.
- **for pdf in os.listdir(dir)**: Iterates through all files in the specified directory.
- **if os.path.splitext(pdf)[1] != '.pdf'**: Skips files that are not PDFs.
- **pdf_arr = pdf.split('-')**: Splits the PDF file name by hyphens.
- **programTitle = pdf_arr[0].strip()**: Extracts and trims the program title.
- **for program in programs.keys()**: Iterates through existing program titles.
- **similarity = string_similarity(programTitle, program)**: Checks the similarity of the program titles.
- **if similarity > 0.9**: If the similarity is greater than 0.9, it considers them the same program.
- **programs[programTitle]['yearX'] = dir + "\\" + pdf**: Stores the PDF file path under the appropriate year key.
- **return programs**: Returns the dictionary of programs with their associated PDF files.

### Function: parse_boxes
```python
def parse_boxes(boxes, path, program, year):
    doc = fitz.open(path)
    page = doc[0]

    class_pattern = r"\b[A-Z]{4}\s\d{4}\b"
    class_list = []
    for box in boxes:
        x0 = box['x0']
        y0 = box['y0']
        x1 = box['x1']
        y1 = box['y1']

        look_area = (x0, y0, x1, y1)
        text = page.get_textbox(look_area)

        searched = re.findall(class_pattern, text)
        if len(searched) == 0:
            if "elective" in text.lower():
                class_to_add = {"name": "Elective", "code": "ELEC", "term": box['term'], "unit_value": "PLACEHOLD", "program": program, "year": year}
                class_list.append(class_to_add)
                continue
            else:
                continue
        class_code = searched[0]
        class_name = text[0:text.index(class_code)].replace("\n", "")

        if not class_name:
            continue

        class_to_add = {"name": class_name, "code": class_code, "term": box['term'], "unit_value": "PLACEHOLD", "program": program, "year": year}
        class_list.append(class_to_add)
    return class_list
```
- **doc = fitz.open(path)**: Opens the PDF file at the specified path.
- **page = doc[0]**: Retrieves the first page of the PDF document.
- **class_pattern = r"\b[A-Z]{4}\s\d{4}\b"**: Defines a regex pattern to match class codes.
- **class_list = []**: Initializes an empty list to store classes.
- **for box in boxes**: Iterates through the list of boxes.
- **look_area = (x0, y0, x1, y1)**: Defines the area to look for text.
- **text = page.get_textbox(look_area)**: Extracts text from the specified area.
- **searched = re.findall(class_pattern, text)**: Finds all matches of the class pattern in the text.
- **if len(searched) == 0**: Checks if no class code was found.
- **if "elective" in text.lower()**: Checks if the text contains the word "elective".
- **class_to_add = {...}**: Creates a dictionary for the elective class.
- **class_list.append(class_to_add)**: Appends the class to the class list.
- **class_code = searched[0]**: Extracts the class code.
- **class_name = text[0:text.index(class_code)].replace("\n", "")**: Extracts and cleans the class name.
- **class_to_add = {...}**: Creates a dictionary for the class.
- **class_list.append(class_to_add)**: Appends the class to the class list.
- **return class_list**: Returns the list of classes.

### Function: parse_programs
```python
def parse_programs(programs):
    global CLASS_DATAFRAME
    count = 0
    class_list = []
    for program in programs.keys():
        for term in programs[program].keys():
            bound_boxes = parse_map(programs[program][term], count)
            class_list = class_list + parse_boxes(bound_boxes, programs[program][term], program, term)
            count += 1

    CLASS_DATAFRAME = pd.DataFrame.from_dict(class_list)
    CLASS_DATAFRAME.to_csv("test.csv", index=False)

    print(CLASS_DATAFRAME)
```
- **global CLASS_DATAFRAME**: Declares `CLASS_DATAFRAME` as a global variable.
- **count = 0**: Initializes a counter.
- **class_list = []**: Initializes an empty list to store classes.
- **for program in programs.keys()**: Iterates through programs.
- **for term in programs[program].keys()**: Iterates through terms for each program.
- **bound_boxes = parse_map(programs[program][term], count)**: Parses the map to get bounding boxes.
- **class_list = class_list + parse_boxes(...)**: Parses the boxes and adds the classes to the class list.
- **count += 1**: Increments the counter.
- **CLASS_DATAFRAME = pd.DataFrame.from_dict(class_list)**: Converts the class list to a DataFrame.
- **CLASS_DATAFRAME.to_csv("test.csv", index=False)**: Saves the DataFrame to a CSV file.
- **print(CLASS_DATAFRAME)**: Prints the DataFrame.

### Function: load_student_data
```python
def load_student_data(path):
    global STUDENT_DATAFRAME
    STUDENT_DATAFRAME = pd.read_excel(DATA_PATH, engine='openpyxl')

    abbreviations = STUDENT_DATAFRAME['Acad Plan'].unique()
    program_names = CLASS_DATAFRAME['program'].unique()

    for abbrev in abbreviations:
        prog_df = STUDENT_DATAFRAME[STUDENT_DATAFRAME['Acad Plan'] == abbrev]
        abbrevs_classes = prog_df['Subject'] + " " + prog_df['Catalog']

        overlap = CLASS_DATAFRAME[CLASS_DATAFRAME['code'].isin(abbrevs_classes)]
        best_guess = overlap['program'].value_counts().idxmax()

        if overlap['program'].value_counts()[0] > 5:
            STUDENT_DATAFRAME['Acad Plan'] = STUDENT_DATAFRAME['Acad Plan'].replace(abbrev, best_guess)
        else:
            STUDENT_DATAFRAME['Acad Plan'] = STUDENT_DATAFRAME['Acad Plan'].replace(abbrev, best_guess)

    STUDENT_DATAFRAME['code'] = STUDENT_DATAFRAME['Subject'] + ' ' + STUDENT_DATAFRAME['Catalog']
```
- **global STUDENT_DATAFRAME**: Declares `STUDENT_DATAFRAME` as a global variable.
- **STUDENT_DATAFRAME = pd.read_excel(DATA_PATH, engine='openpyxl')**: Loads student data from an Excel file.
- **abbreviations = STUDENT_DATAFRAME['Acad Plan'].unique()**: Gets unique academic plan abbreviations.
- **program_names = CLASS_DATAFRAME['program'].unique()**: Gets unique program names.
- **for abbrev in abbreviations**: Iterates through abbreviations.
- **prog_df = STUDENT_DATAFRAME[STUDENT_DATAFRAME['Acad Plan'] == abbrev]**: Filters student data by academic plan.
- **abbrevs_classes = prog_df['Subject'] + " " + prog_df['Catalog']**: Concatenates subject and catalog for each class.
- **overlap = CLASS_DATAFRAME[CLASS_DATAFRAME['code'].isin(abbrevs_classes)]**: Finds overlap with class codes in the class data.
- **best_guess = overlap['program'].value_counts().idxmax()**: Gets the most common program.
- **if overlap['program'].value_counts()[0] > 5**: Checks if the overlap is significant.
- **STUDENT_DATAFRAME['Acad Plan'] = STUDENT_DATAFRAME['Acad Plan'].replace(abbrev, best_guess)**: Replaces the abbreviation with the best guess program.
- **STUDENT_DATAFRAME['code'] = STUDENT_DATAFRAME

======================================================================================

Let's walk through Script 3 step by step and explain each part:

### Function: gen_course
```python
def gen_course():
    course={"name": 'widgets 101',
            "code": 'W1000',
            "unit_value":1,
            "misc":"could add anything else you need..."
            }
    return course
```
- **def gen_course()**: Defines a function `gen_course` that generates a course dictionary.
- **course = {"name": 'widgets 101', "code": 'W1000', "unit_value": 1, "misc": "could add anything else you need..." }**: Creates a dictionary representing a course with fields like name, code, unit value, and a miscellaneous field.
- **return course**: Returns the course dictionary.

### Creating Course Lists
```python
course_list_A=[]
course_list_B=[]
for x in range(0,6):
    course_list_A.append(gen_course())
    course_list_B.append(gen_course())
```
- **course_list_A = []**: Initializes an empty list to store courses for term 1.
- **course_list_B = []**: Initializes an empty list to store courses for term 2.
- **for x in range(0,6)**: Iterates 6 times to generate 6 courses for each term.
- **course_list_A.append(gen_course())**: Adds a generated course to `course_list_A`.
- **course_list_B.append(gen_course())**: Adds a generated course to `course_list_B`.

### Creating Term Dictionaries
```python
term1={"term_session":"Fall 2019",
       "course_list":course_list_A
      }

term2={"term_session":"Winter 2020",
       "course_list":course_list_B
      }
```
- **term1 = {...}**: Creates a dictionary for the first term with the session name and course list.
- **term2 = {...}**: Creates a dictionary for the second term with the session name and course list.

### Creating the Remaining Courses List
```python
remaining_courses=[term1, term2]
```
- **remaining_courses = [term1, term2]**: Creates a list containing the term dictionaries.

### Creating the Student Info Dictionary
```python
student_info={
    'id':"W0518150",
    'name':"Evan Farrell",
    'program': 'iot blah blah',
    'on_track': 1, #true if the student is behind the road map 'i.e bad student'
    'terms_left': 2, #shortest number of terms left to graduate
    'progress_roadmap': "some image file.png",
    'remaining_courses':remaining_courses
}
```
- **student_info = {...}**: Creates a dictionary representing a student's information.
- **'id': "W0518150"**: Student ID.
- **'name': "Evan Farrell"**: Student name.
- **'program': 'iot blah blah'**: Student program.
- **'on_track': 1**: Indicates whether the student is on track (1 means not on track in this context).
- **'terms_left': 2**: Number of terms left to graduate.
- **'progress_roadmap': "some image file.png"**: Path to the progress roadmap image.
- **'remaining_courses': remaining_courses**: List of remaining courses.

### Printing the Student Info
```python
#print(student_info['remaining_courses'][1]["course_list"][5]['code'])
print(student_info)
```
- **#print(student_info['remaining_courses'][1]["course_list"][5]['code'])**: A commented-out line that would print the code of the 6th course in the second term.
- **print(student_info)**: Prints the `student_info` dictionary.

### Summary
This script generates sample data for a student, including their ID, name, program, on-track status, terms left to graduate, a progress roadmap, and a list of remaining courses. The `gen_course` function creates individual courses, which are then added to terms, and the terms are combined into a list of remaining courses. This data is all bundled into a `student_info` dictionary, which is printed at the end.

If you have any specific questions or need further explanations, feel free to ask! 😊
