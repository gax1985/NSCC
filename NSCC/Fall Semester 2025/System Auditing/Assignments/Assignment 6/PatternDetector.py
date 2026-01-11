<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
##########################################################################
# Mohammad Al Jokhadar | ISEC2077 | Assignment 6 | Dec. 2nd, 2025
##########################################################################
def main():

    from time import sleep # This is added in order to add pauses

    # Let us create a variable to store log entries :
    log_entries = []

    # ... and create a dictionary of anomalies, containing two lists for each type of anomaly :

    anomalies = {"no_punch_in": [], "no_punch_out": []}

    def load_and_parse_log(filepath="cardKeyLog.txt"):

        # Since the contents of the file that we have is separated by tabs (to make it appear as a table)
        # , we will consider the first line as headers and subsequent lines as data rows.

        try:
            with open(filepath, "r") as file:
                header_line = file.readline() # the .readline() sub-module reads the first line of the file
                if not header_line: # ... if the header line is empty, return nothing
                    return []
                headers = [h.strip() for h in header_line.split("\t")] # extract the text from all the items in headers

                for line in file:
                    if not line.strip(): # If the line's contents are empty, proceed ....
                        continue
                    values = line.strip().split("\t") # ... the delimeter here is the TABs , thus they are known as "\t"
                    try:
                        entry_dict = dict(zip(headers, map(int, values))) # the zip function assigns the contents of lists
                                                                          # together in parallel
                        log_entries.append(entry_dict)                    # ... this would add the entry_dict dictionary
                                                                          # to the log entries list
                    except (ValueError, TypeError):                       # Exception is added to handle issues with
                                                                          # values and content types
                        print(f"Warning: Skipping malformed row: {line.strip()}")
        except FileNotFoundError:                                         # Exception is added to handle issues with the file at hand
            print(f"Error: The file '{filepath}' was not found.")

        return log_entries

    # Let us run the first function :
    load_and_parse_log()    # We should now call the function!

##############################
# Anomalies Finder function :
##############################
    def find_anomalies():


        # The aggregation of final results :
        #####################################

        # Now , what we can do is to check for matches. When they are found,
        # we add any matches to the anomalies dictionary.
        # Since the data is already structured, the most reliable method
        # is to check the dictionary values directly.
=======

from pygrok import Grok
import json

def grokker():


def file_loader():
    with open(".\\cardKeyLog.txt","r") as file:

=======
=======
=======

from pygrok import Grok
import json

def grokker():


def file_loader():
    with open(".\\cardKeyLog.txt","r") as file:


>>>>>>> Stashed changes

from pygrok import Grok
import json

def grokker():


def file_loader():
    with open(".\\cardKeyLog.txt","r") as file:


>>>>>>> Stashed changes

from pygrok import Grok
import json

def grokker():


def file_loader():
    with open(".\\cardKeyLog.txt","r") as file:


>>>>>>> Stashed changes

>>>>>>> Stashed changes

        for log in log_entries:
            # Check for employees who have not punched in (HourIN is 0 and MinIN is 0)
            if log["HourIN"] == 0 and log["MinIN"] == 0:
                anomalies["no_punch_in"].append(log)   # We add the log entry that matches the results to the appropriate list

            # Check for employees who have not punched out (HourOUT is 0 and MinOUT is 0)
            if log["HourOUT"] == 0 and log["MinOut"] == 0:
                anomalies["no_punch_out"].append(log) # We add the log entry that matches the results to the appropriate list

        return anomalies

    find_anomalies()  # the anomalies finder is called!
######################
# The Presenter :
######################
    def presenter():

        # Let us present the results :

        print("\n--- Anomaly Scan Complete ---")

        sleep(2)

        print(
            f"""#####################################################################################################################
                
Dearest employer ... the following employees did not follow correct procedures for proper time keeping :
        
# The number of  individuals did not punch in when starting their shift :
########################################################################
Number of individuals : {len(anomalies["no_punch_in"])} 
        
Details :
######### """)

        for employee in anomalies["no_punch_in"]:
            print(
                f" The employee # {employee["EmpNum"]} did not punch in when starting their shift."
            )

        print(
            "#####################################################################################################################"
        )

        print(f"""# The following individuals did not punch out when starting their shift :
########################################################################
Number of individuals : {len(anomalies["no_punch_out"])}
        
Details :
#########"""
        )

        for employee in anomalies["no_punch_out"]:
            print(
                f" The employee # {employee["EmpNum"]} did not punch out when ending their shift."
            )

    presenter()


##################################################
# Writing to the 'ANOMALIES.TXT' external file :
################################################

    def the_external_writer(report_file="ANOMALIES.txt"):

        # The pathlib library is imported to handle filesystem paths in a modern, object-oriented way.
        from pathlib import Path

        # A Path object is created for the report file, making it easier to work with.
        report_file_path = Path(report_file)

        # The 'with' statement ensures the file is automatically closed even if errors occur.
        # The file is opened in 'w' (write) mode, which means the file will be created fresh each time the script runs.
        with report_file_path.open(mode="w") as file:

            # This section iterates through the list of "no punch in" anomalies.
            for employee in anomalies["no_punch_in"]:
                # Line 1: Write the employee number, month, and day, followed by a newline character.
                file.write(f"{employee['EmpNum']},{employee['MonthIN']},{employee['DayIN']}\n")
                # Line 2: Write the description of the anomaly.
                file.write("The employees punched OUT but did not punch IN!\n")
                # Line 3: Write a separator to make the report easier to read.
                file.write("***********************************************************************\n")

            # This section iterates through the list of "no punch out" anomalies.
            for employee in anomalies["no_punch_out"]:
                # Line 1: Write the employee number, month, and day.
                file.write(f"{employee['EmpNum']},{employee['MonthIN']},{employee['DayIN']}\n")
                # Line 2: Write the description of the anomaly.
                file.write("The employees punched IN but did not punch OUT!\n")
                # Line 3: Write the separator.
                file.write("***********************************************************************\n")

    # Finally, the writer function is called to generate the ANOMALIES.txt file.
    the_external_writer(report_file="ANOMALIES.txt")


if __name__ == "__main__":
    main() # Call the main function to run the program
