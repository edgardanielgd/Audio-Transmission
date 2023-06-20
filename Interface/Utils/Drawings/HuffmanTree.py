from PySide6 import QtCore, QtGui, QtWidgets

def paintCodificationTree( tree, canvas ):
    # Get canvas
    logCanvas = canvas
    
    # Create a pixmap where we will draw into
    pixmap = QtGui.QPixmap( logCanvas.size() )
    
    # Create a painter
    painter = QtGui.QPainter( pixmap )
    
    # Set pen
    pen = QtGui.QPen()
    pen.setWidth( 2 )
    pen.setColor( QtGui.QColor( 255, 255, 255 ) )
    painter.setPen( pen )

    # Set font size
    font = QtGui.QFont()
    font.setPixelSize( 20 )
    painter.setFont( font )
    
    # Draw tree

    # Get dimensions of canvas
    width = logCanvas.width()
    height = logCanvas.height()

    # We need to keep track of greater width and height in order
    # to resize label as soon we finish the printing process
    drawNode( painter, tree, width//2, 0, width, height )

    
    # Set pixmap
    logCanvas.setPixmap( pixmap )

    # Update canvas
    logCanvas.update()

    # Delete painter
    del painter

def drawNode( painter, node, x, y, max_width = -1, max_height = -1 ):
    # Draw node
    painter.drawEllipse( x, y, 20, 20 )
    
    # Draw text
    painter.drawText( x + 5, y + 15, str( node.leafValue if node.leafValue is not None else " " ) )
    
    # Draw left child
    if node.left != None:
        painter.drawLine( x + 10, y + 20, x - 50, y + 50 )

        # Draw associated code
        painter.drawText( x - 20, y + 30, "1" )

        given_width, given_height = drawNode( painter, node.left, x - 50, y + 50 )
    
    # Draw right child
    if node.right != None:
        painter.drawLine( x + 10, y + 20, x + 50, y + 50 )

        # Draw associated code
        painter.drawText( x + 30, y + 30, "0" )

        given_width, given_height = drawNode( painter, node.right, x + 50, y + 50 )
    
    return max_width, max_height