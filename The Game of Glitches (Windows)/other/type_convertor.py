def listify(string: str):
    """
    Converts a string into a list (the string must be split by commas)
    """
    return string.replace("'", "").replace("[", "").replace("]", "").split(", ")

def unlistify(listy: list):
    """
    Converts a list into a string
    """
    return str(listy).replace("'", "").replace("[", "").replace("]", "")

def dictify(string: str):
    """
    Converts a string into a dictionary
    """
    dicty = {}
    info = string.split(", ")
    for entry in info:
        temp = entry.split(": ")
        dicty[temp[0]] = temp[1]
    return dicty
    

def undictify(dicty: dict):
    """
    Converts a dictionary into a string
    """
    return str(dicty).replace("'", "").replace("{", "").replace("}", "")