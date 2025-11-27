

# Assignment 6: Anomaly Detection Plan

## Phase 1: Setup & Data Ingestion (Est. 30 mins)
- [ ] **Step 1.1:** Create `anomaly_detector.py` file. (5 mins)
- [ ] **Step 1.2:** Add the **Required Comment Block** at the top. (5 mins)
    * *Include:* Name, ISEC2077, Assignment 6, Date.
- [ ] **Step 1.3:** Write code to open `cardKeyLog.txt` in read mode. (5 mins)
- [ ] **Step 1.4:** Write a `for` loop to read the file line-by-line. (5 mins)
- [ ] **Step 1.5:** Split each line using `.split('\t')` and `print()` the first 5 lines to test. (10 mins)

## Phase 2: The Logic (Est. 45 mins)
- [ ] **Step 2.1:** Convert the `Hour` and `Minute` strings to Integers `int()`. (15 mins)
- [ ] **Step 2.2:** **Condition A:** Write `if` statement for **Missing IN** (HourIN == 0). (10 mins)
- [ ] **Step 2.3:** **Condition B:** Write `if` statement for **Missing OUT** (HourOUT == 0). (10 mins)
- [ ] **Step 2.4:** **Verification:** Check that the "22-hour shift" employee is flagged as "Missing IN". (5 mins)
- [ ] **Step 2.5:** Run the code and ensure exactly **10 anomalies** are printed to the console. (5 mins)

## Phase 3: Generating the Report (Est. 30 mins)
- [ ] **Step 3.1:** Modify code to open `ANOMALIES.TXT` in write (`'w'`) mode. (5 mins)
- [ ] **Step 3.2:** Write Line 1 format: `{EmpNum}, {Month}, {Day}`. (10 mins)
- [ ] **Step 3.3:** Write Line 2 format: Description (e.g., "Employee carded IN but didn't card OUT"). (5 mins)
- [ ] **Step 3.4:** Write Line 3 format: `============` (separator). (5 mins)
- [ ] **Step 3.5:** Run the full script and open `ANOMALIES.TXT` to verify formatting. (5 mins)

## Phase 4: Final Polish (Est. 20 mins)
- [ ] **Step 4.1:** **CRITICAL:** Add comments explaining every function and logic block. (15 mins)
- [ ] **Step 4.2:** Zip the `.py` source code and `ANOMALIES.TXT` for Dropbox submission. (5 mins)