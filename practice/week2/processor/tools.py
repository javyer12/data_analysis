# function to convert a string to lowercase
def to_lowercase_strip(s):
    newString = s.lower().replace(" ", "/")
    return newString

def to_lowercase_add_space(s):
    newString = s.lower().replace("", "-")
    return newString