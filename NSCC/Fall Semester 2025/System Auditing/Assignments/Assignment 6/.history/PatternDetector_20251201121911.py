import grok

TheDictionaryHolder = [[]]


def TheFileLoaderDetector():
    with open(".\\cardKeyLog.txt","r") as file:
        for line in file:
            for title in line.split("\t"):
                if title is not type == int:
                    TheDictionaryHolder[0].append(title)

TheFileLoaderDetector()

print(TheDictionaryHolder)
