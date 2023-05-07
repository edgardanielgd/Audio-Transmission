import numpy as np

# Quantization
def uniform_quantization(sampled_signal, n_bits):
  n_levels = 2 ** n_bits
  min_v = min(sampled_signal)
  max_v = max(sampled_signal)
  delta_step = (abs(max_v) + abs(min_v)) / n_levels
  
  q_levels = np.floor(
    (
      (sampled_signal + abs(min_v)) if(min_v<0) else sampled_signal
    ) / (delta_step if delta_step != 0 else 1)
  )
  
  # to values greater or equal to L update to L-1
  q_levels[q_levels >= n_levels] = n_levels - 1
  # to values less than 0 update to 0
  q_levels[q_levels < 0] = 0
  # quantized signal
  quantized_signal = q_levels * delta_step +(min_v if(min_v<0) else 0) + 0.5 * delta_step

  # Generate parsing dictionary 
  # (takes a level index and returns the signal value)
  parsing_dict = dict(zip(q_levels, quantized_signal))
  
  return quantized_signal, q_levels, parsing_dict

# Dequantize object
def uniform_dequantization( 
  parsing_dict, quantized_signal 
):
  return map(
    lambda x : parsing_dict[ x ],
    quantized_signal
  )