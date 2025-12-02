##########################################################################
# Mohammad Al Jokhadar | ISEC2077 | Assignment 6 | Dec. 2nd, 2025
##########################################################################

# This script reads a tab-separated log file, uses the first row as headers,
# and converts the remaining rows into a list of dictionaries.


def load_and_parse_log(filepath="cardKeyLog.txt"):
    """
    Reads a tab-separated file, treating the first line as headers
    and subsequent lines as data rows.

    Args:
        filepath (str): The path to the log file.

    Returns:
        A list of dictionaries, where each dictionary represents a row.
        Returns an empty list if the file is empty or headers are missing.
    """
    log_entries = []

    try:
        with open(filepath, "r") as file:
            # 1. Read the header row and clean it up.
            header_line = file.readline()
            if not header_line:
                return []  # File is empty

            headers = [h.strip() for h in header_line.split("\t")]

            # 2. Loop through the rest of the lines in the file.
            for line in file:
                # Skip any blank lines
                if not line.strip():
                    continue

                values = line.strip().split("\t")

                # 3. Create a dictionary for the row.
                # We use a try-except block to handle potential errors if a row
                # doesn't have the same number of columns as the header.
                try:
                    # The map(int, values) part converts each value from a string to an integer.
                    entry_dict = dict(zip(headers, map(int, values)))
                    log_entries.append(entry_dict)
                except (ValueError, TypeError):
                    print(f"Warning: Skipping malformed row: {line.strip()}")

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return []

    return log_entries


def main():
    # The list of log entries is now returned by the function.
    log_contents = load_and_parse_log()
    print(log_contents)

    # You can now work with the log_contents list.
    # For example, let's print the first 5 entries to verify.
    # if log_contents:
    #     print("Successfully loaded log file. Here are the first 5 entries:")
    #     for entry in log_contents[:5]:
    #         print(entry)


if __name__ == "__main__":
    main()
