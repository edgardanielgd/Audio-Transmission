import numpy as np
from PIL import Image

# Get images as files paths and convert them to numpy arrays (flattened)
def convertImageToVector( img ):

    # Get image size
    width, height = img.size

    img = img.convert('RGB')
    img = np.array(img)

    # So we will get a single array of 3*width*height elements
    # representing the image

    img = img.flatten()

    return img, width, height

def buildImageFromVector( data, width, height ):
    # We will get a single array of 3*width*height elements
    # representing the image, they should be already been 
    # converted to bytes
    
    # Convert to 3D array
    img = data.reshape( (height, width, 3) )

    # Convert to image
    img = Image.fromarray( img, 'RGB' )

    return img

# Get data as bits array and convert them to numpy arrays of bytes
def convertBitsToVector( bits ):
    # Convert to numpy array
    data = np.array( bits )

    # Convert to bytes
    data = np.packbits( data )

    return data