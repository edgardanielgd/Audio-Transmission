# Beat tracking example
import librosa

# We will need a different attribute 
import soundfile as sf

import numpy as np
from matplotlib import pyplot as plt

# Utilities
from Utils.Quantization import uniform_quantization
from Utils.Huffman import encode_huffman, decode_huffman_input
from Utils.Diferencial import DPCMCode, DPCMDecode

print("Read file with custom sampling rate")

# # File to be parsed
# filename = "car.wav"

# # 1. Get the file path to an included audio example
# y, sr = librosa.load(
#   "./Videos/" + filename, # File name
#   duration=10, # Video time slice (from 0 to duration)
#   sr=44100, # Sampling rate
#   mono=True, # Convert to mono
# )

def processWithHuffman( y, sr ):
    # Parsing dict must be one of the items sent
    # to receiver in order to make him able
    # to decode the given output

    # Quantize both channels separately
    _, y, parsing_dict = uniform_quantization(
      y, 8
    )

    # Get huffman bytes representation
    # for each symbol
    encode_dict, encoded_bits = encode_huffman( y )

    # Do not print this, thats not a good idea

    ########
    # Now decode data
    decoded_levels = decode_huffman_input( encode_dict, encoded_bits )

    decoded_signal = np.array(list(map(
      lambda x: parsing_dict[ x ], # Level to signal value
      decoded_levels
    )), dtype=np.float32)

    # Test a bit of chaos
    # decoded_signal[44100*2:44100*3] = np.random.rand(44100)

    # Create another audio file with the decoded data, same sampling rate
    sf.write("./Outputs/" + filename, decoded_signal, samplerate = 44100, format="WAV")

    """
    f0, voicing, voicing_probability = librosa.pyin(y=y, sr=sr, fmin=50, fmax=300)

    S = np.abs(librosa.stft(y))

    times = librosa.times_like(S, sr=sr)

    fig, ax = plt.subplots()
    librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max),
                            y_axis='log', x_axis='time', ax=ax)
    ax.plot(times, f0, linewidth=2, color='white', label='f0')
    ax.legend()
    plt.show()
    """

def processWithDPCM( y, sr ):
  coded, parsing_dict, first_value = DPCMCode( y, 4 )
  
  decoded_signal = DPCMDecode( coded, parsing_dict, first_value )

  # Create another audio file with the decoded data, same sampling rate
  sf.write("./Outputs/" + filename, decoded_signal, samplerate = 44100, format="WAV")

    
# processWithHuffman( y, sr )
# processWithDPCM( y, sr )
