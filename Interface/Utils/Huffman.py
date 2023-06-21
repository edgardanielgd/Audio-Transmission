import numpy as np

# Build a codification tree
def build_huffman_probabilities(
  data
):
  """
    Receive an array of data and then calculates the
    huffman codification tree based on levels
    probability
  """

  # Get data probabilities as the first step
  n = len( data )
  unique_labels, unique_count = np.unique( 
    data , return_counts = True
  )
  
  unique_counts_dict = dict(zip(
     unique_labels, unique_count / n
  ))

  # Simple probabilities assignation
  return unique_counts_dict

# Build huffman codification tree (this is the tricky section)
def build_huffman_tree(
  data
):

  class Node:
    def __init__(self, value):
      # At each point, 
      self.left = None
      self.right = None
      self.value = value
      self.leafValue = None
      
  # Get all possible values probabilities
  probabilities = build_huffman_probabilities(data)

  # Sort probabilities in increased order
  sorted_probabilities = sorted(
    probabilities.items(), 
    key = lambda x : x[1]
  )

  # Create hoffman tree by means of two queues
  queue1 = []
  queue2 = []

  # Init queues
  for key, value in sorted_probabilities:
    node = Node( value )

    # Reference to level
    node.leafValue = key
    queue1.append( node )
  
  # Main grouping algorithm
  q1length = len(queue1)
  q2length = len(queue2)
  
  while( q1length + q2length > 1 ):
    # Choose the lower values in both queues

    possibleValues = []

    # Append possible values when necessary
    if q1length > 1:
      possibleValues.append( queue1[0] )
      possibleValues.append( queue1[1] )
    elif q1length > 0:
      possibleValues.append( queue1[0] )

    if q2length > 1:
      possibleValues.append( queue2[0] )
      possibleValues.append( queue2[1] )
    elif q2length > 0:
      possibleValues.append( queue2[0] )

    # Sort possible values (increasing order)
    sortedValues = sorted(
      possibleValues,
      key = lambda x: x.value
    )
    a = sortedValues[0]
    b = sortedValues[1]

    # Remove clustered values from lists
    if a in queue1:
      queue1.remove( a )
    if b in queue1:
      queue1.remove( b )
    if a in queue2:
      queue2.remove( a )
    if b in queue2:
      queue2.remove( b )

    # Finally append new value into new cluster
    node = Node( a.value + b.value )
    node.left = a
    node.right = b
    queue2.append( node )

    # Update queues length
    q1length = len(queue1)
    q2length = len(queue2)
  
  # Finally, having our hoffman tree
  # we can calculate encodings for each
  # data value by visiting the tree
  # Left node = 0
  # Right node = 1

  final_encodings = {}

  # Recursive iteration over hoffman tree
  def visitNode(root, sequence):

    if root is None:
      return

    # Check if this node is a leaf
    if root.leafValue is not None:
      final_encodings[root.leafValue] = sequence
      return

    visitNode(root.left, sequence + "0")
    visitNode(root.right, sequence + "1")

  # Visit parent node at all
  visitNode( queue2[0], "" )

  return final_encodings, queue2[0]

# Encode data with gotten huffman tree
def encode_huffman(
  data
):
  # First, build huffman tree for this input
  encoding_tree, root_node = build_huffman_tree( data )
  bits_encoded = ""

  # Simulate the most hardcore signal: A string of bits
  for item in data:
    bits = encoding_tree[ item ]
    bits_encoded += bits

  return encoding_tree, bits_encoded, root_node

# Do huffman decodification
def decode_huffman_input(
  huffman_codification_tree,
  input_data
):
  """
    Codified signal must be in 0s and 1s
  """
  # Recall this will be in terms of levels
  decoded_data = []
  
  # Its more useful to have a reverse dictionary at this point
  inverse_decodification = {
    v: k for k, v in huffman_codification_tree.items()
  }
  
  # Get all available codification parses
  codes = list( inverse_decodification.keys() )
  
  # We will be deducting possibilities as the read symbols 
  # before finding a match do increase
  code = ""
  code_index = 0
  
  while( code_index < len( input_data )):
    # Due to the properties of this codification
    # we can make sure that the first match is the
    # correct translation
    code += input_data[ code_index ] # <- character

    if code in codes:
      decoded_data.append( inverse_decodification[code] )

      # Reset string scanning
      code = ""

    # Update character index
    code_index += 1

  return decoded_data, inverse_decodification