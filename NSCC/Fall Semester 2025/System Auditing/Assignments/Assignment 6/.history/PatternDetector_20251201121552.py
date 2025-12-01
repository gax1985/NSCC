import grok

TheDictionaryHolder = [[]]


def TheFileLoaderDetector():
    with open(".\\cardKeyLog.txt","r") as file:
        for line in file:
            for title in line.split("\t"):
                if title not int:
                    continue # This line is incorrect, it should be checking if title is a digit
                    TheDictionaryHolder[0].append(title)

TheFileLoaderDetector()

print(TheDictionaryHolder)
