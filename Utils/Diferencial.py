import numpy as np
from .Quantization import uniform_quantization

# This module aims to perform a differential codification of a given signal
def DPCMCode(
    data, nbits
):
    
    # First, lets get the first value of the signal
    # and append it to the output
    output = [ data[0] ]

    # Now, iterate over the signal
    # and get the difference between
    # the current and the previous value
    for i in range(1, len(data)):

        # Get difference
        diff = data[i] - data[i-1]

        # Append difference to output
        output.append( diff )

    # Quantize output
    _, y, parsing_dict = uniform_quantization(
        output, nbits
    )

    # We must provide the first value
    # in order to decode the signal
    return y, parsing_dict, data[0]

def DPCMDecode(
    data, parsing_dict, first_value
):

    # First, lets get the first value of the signal
    # and append it to the output
    output = [ first_value ]
    current_value = first_value

    # Now, iterate over the signal
    # and get the difference between
    # the current and the previous value
    for i in range(0, len(data)):

        # Get difference and its corresponding value
        diff = parsing_dict[ data[i] ]

        # Get current value
        current_value += diff

        # Append difference to output
        output.append( current_value )

    return output