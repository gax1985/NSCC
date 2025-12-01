import python_grok

TheDictionaryHolder = [[]]


def TheFileLoaderDetector():
    with open(".\\cardKeyLog.txt","r") as file:
        for line in file:
            for title in line.split():
                TheDictionaryHolder.append(title)


