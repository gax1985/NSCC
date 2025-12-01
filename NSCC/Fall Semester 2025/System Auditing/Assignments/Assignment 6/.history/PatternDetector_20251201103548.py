import python_grok
from python_grok import Pattern, PatternDetector

TheDictionaryHolder = []


def TheFileLoaderDetector():
    with open(".\\cardKeyLog.txt","r") as file:
        for line in file:
            for title in line.split():
                TheDictionaryHolder[0].append(title)


