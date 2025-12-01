import grok

TheDictionaryHolder = [[]]


def TheFileLoaderDetector():
    with open(".\\cardKeyLog.txt","r") as file:
        for line in file:
            for title in line.split("\t"):
                TheDictionaryHolder[0].append(title)

TheFileLoaderDetector()


