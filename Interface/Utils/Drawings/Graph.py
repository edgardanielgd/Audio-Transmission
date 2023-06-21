
def get_deeper_length( graph ):
    # Iterate over all nodes and get the maximum width
    if graph is None:
        return 0

    left_length = get_deeper_length( graph.left )
    right_length = get_deeper_length( graph.right )

    return max( left_length, right_length ) + 1