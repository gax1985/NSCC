


## Slide 2 - The Project Technical Content - Demonstration, Explanation of how it works, 2-3 minutes  

###### What is this project about?     

>[!Brad]
>
>>Currently, Mr. Purcell's process for developing a roadmap for students that need to take an extended courseload is almost entirely manual, requiring cross-referencing multiple files and resources while working within a given  student's needs. We aim to expedite the process through file and dataset analysis, effectively removing the need to filter through unnecessary information manually and consolidating the workflow into a single interface.  


>[!Evan]
>
>>The core of the project is streamlining michael’s work-flow, he wants a intuitive solution that can let him spend more time focusing on student’s needs and less time navigating spreadsheets and pdfs.
>

###### Which factors determined your choice in this project?     


>[!Brad]
>
>>I tend to let any team members that I'm with take the reigns in choosing a given project or task.  This isn't due to lack of interest, but is more about team cohesion. I'm happy to work on any project, as I find the process of bringing ideas into reality motivates me more than any given project... ...Plus, the amount of work Mike has to do each semester is astounding, and I'd like to give the poor guy a break.  


>[!Evan]
>
>>I was interested in this project due to the open-ended nature, I think there are a lot of different approaches to this and it’s interesting to see/to have seen how different groups tackled it.

###### Which elements did you want to tackle in this project?     

>[!Brad]
>
>>Initially, I had anticipated leveraging my hardware and systems administration experience to implement a means of  serving pre-processed data.   

>[!Evan]
>
>>I was drawn to the data ingestion portion of the project. Mainly how to take the academic maps that michael provided and turn them into usable data.

###### What was your specialty in this project?     

>[!Brad]
>
>>I ended up taking on the duty of front-end design and implementation. I do not see myself as a UX designer and was concerned in my ability to perform what was needed of me. I ended up learning a lot and creating something that I did not think I would be able to do within the timeframe.`

>[!Evan]
>
>>I worked on creating the backend functionality that process data and returns formatted data to the user interface.

## Slide 3

###### Where is the data coming from?
    

>[!Brad]
>
>>The data is coming from an exported .xlsx spreadsheet document, as well as a collection of PDF courseplan maps.I must admit, this is not the ideal dataset to work with, but we rarely get to choose the parameters of a given project in the I.T. industry. 

>[!Evan]
>
>>The student grade spreadsheets are from peoplesoft. The academic maps are from the school.
###### What sort of challenges did you face when you were obtaining and working with the data?

>[!Brad]
>
>>Filtering through and extracting values from keys contained in fairly-sized data objects was a bit daunting.The biggest challenge was ensuring the correct information was being rendering in the right place, regardless of size. 

>[!Evan]
>
>>We did not have access to easy computer readable ways of knowing which classes are part of which program, the two avenues I considered were either extracting all the information from the pdf, or webscraping from the nscc website.

###### How did you resolve these challenges?

>[!Brad]
>
>>I found that keeping the scope in mind, as well as ensuring the user experience didn't stray too far from the current workflow allowed for design constraints that proved critical in successful implementation.

>[!Evan]
>
>>It took some time and experimentation but I was able to successfully extract the course listings from each academic map pdf without needing to hardcode any of the relationships, meaning it could be extrapolated towards future academic maps.
###### Were there any privacy  and security considerations involving the sample data being used in this project? if so, how do you see yourself tackling these challenges ( a pointer to the Future slide)?

>[!Brad]
>
>>I wasn't too concerned about the sample data provided, but I did raise my eyebrows at the current process.The manual exporting of bulk data, coupled with the process of document matching and referencing that I can only imagine to be a clerical nightmare is something that I see as a disaster waiting to happen. Even our team's implementation requires data and documents to be locally accessible. Given that PeopleSoft is an Oracle product, I would assume there is a means of dynamically accessing this data by leveraging cloud services. A few API calls and a relational database would almost entirely remove the need for local file management.

>[!Evan]
>
>>We were considering hosting the app on a server or even through sharepoint(i think that is what is is called) but decided the occams razor approach to data security is simple to have the whole thing run locally therefore not transmitting the data anywhere and keeping it entirely secure.




