import librosa as lb
import numpy as np
from . import Quantization as qtz

def convertAudioToVector( frames, levels = 8 ):

    # First lets quantize the signal to a discrete set of levels
    _, y, parsing_dict = qtz.uniform_quantization(
      frames, levels
    )

    return y, parsing_dict

def buildAudioFromVector( data, parsing_dict ):
    # Now we must decode the data
    decoded_signal = np.array(list(map(
      lambda x: parsing_dict[ x ], # Level to signal value
      data
    )), dtype=np.int16)

    return decoded_signal

