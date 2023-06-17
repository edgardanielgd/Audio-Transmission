import numpy as np

# Transform a text into an array of numbers
def convertTextToVector( text ):
    numbers = np.array( list( map( lambda x: ord(x), text ) ) )
    return numbers

# Get a sentence from a vector of numbers
def buildTextFromVector( numbers ):
    text = "".join( list( map( lambda x: chr(x), numbers ) ) )
    return text