



# Query to Check for Imprisoned Hackers 



**SELECT** *[Fields that you want to display separated by commas --> tablename.fieldname]*

**FROM** *[Tables to be accessed, and separated by commas]*

**WHERE** *[Conditions that must be satisfied AND FK's = PK's in other table; sentence.imprisoned = True AND sentence.REFERENCE_ID = real_name.REFERENCE_ID]*



> [!example] 
> **SELECT** Hacker.Hacker_NAME, country.COUNTRY_NAME, Arrest_Record.Sentence
> **FROM** Hacker, Country, Arrest_Record
> **WHERE** Hacker.Country_ID = Country.Country_ID **AND** Arrest_record.Hacker_ID = Hacker.Hacker_ID **AND** Arrest_Record.Arrested = 1; 
> 
>*HackerTable*
>HACKER_ID **PK**
>HACKER_NAME **VARCHAR**
>COUNTRY_ID **FK**
>
>*COUNTRY*
>Country_ID **PK**
>Country_name **VARCHAR**
>
>*Arrest_Record*
>ARREST_ID **PK**
>HACKER_ID **FK**
>ARRESTED **BOOLEAN**
>SENTENCE **VARCHAR**
>
 
