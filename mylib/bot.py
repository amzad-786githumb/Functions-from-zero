import wikipedia
def scrap(name="Microsoft", length=1):
    results = wikipedia.summary(name, sentences=length)
    return results