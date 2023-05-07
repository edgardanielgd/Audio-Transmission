# Beat tracking example
import librosa

# We will need a different attribute 
import soundfile as sf

import numpy as np
from matplotlib import pyplot as plt

# Utilities
from Utils.Quantization import uniform_quantization
from Utils.Huffman import build_huffman_tree, encode_huffman, decode_huffman_input

print("Read file with custom sampling rate")

# 1. Get the file path to an included audio example
y, sr = librosa.load(
  "car.wav", # File name
  duration=5, # Video time slice (from 0 to duration)
  sr=22050 # Sampling rate
)

print("Printing custom data")
print(type(y), len(y), type(sr), sr)

print("Quantizing signal")

# Parsing dict must be one of the items sent
# to receiver in order to make him able
# to decode the given output

_, y_levels, parsing_dict = uniform_quantization(
  y, 8
)

# Get huffman bytes representation
# for each symbol
encode_dict, encoded_bits = encode_huffman( y_levels )

# Do not print this, thats not a good idea

########
# Now decode data
decoded_levels = decode_huffman_input( encode_dict, encoded_bits )
decoded_signal = map(
  lambda x: parsing_dict[ x ], # Level to signal value
  decoded_levels
)

# Create another audio file with the decoded data, same sampling rate
sf.write("carReconstruct.wav", decoded_signal, 22050 )

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