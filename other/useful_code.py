def listify(string: str):
    """
    Converts a string into a list (the string must be split by commas)
    """
    return string.replace('"', "").replace("'", "").replace("[", "").replace("]", "").split(", ")