from PySide6 import QtCore, QtGui, QtWidgets
from .Graph import get_deeper_length

def paintCodificationTree( tree, canvasParent, canvasLayout ):

    # Remove previous drawing
    if canvasLayout.count() == 1:
        canvasLayout.takeAt( 0 )
    
    # Get width and height
    deep = get_deeper_length( tree )
    last_level_count = 2**deep - 1
    width = last_level_count * 20
    height = deep*20 + (deep-1)*30
    
    # Create a pixmap where we will draw into
    pixmap = QtGui.QPixmap( width, height )

    # Create a painter
    painter = QtGui.QPainter( pixmap )
    
    # Set pen
    pen = QtGui.QPen()
    pen.setWidth( 2 )
    pen.setColor( QtGui.QColor( 255, 255, 255 ) )
    painter.setPen( pen )

    # Set font size
    font = QtGui.QFont()
    font.setPixelSize( 12 )
    painter.setFont( font )

    # We need to keep track of greater width and height in order
    # to resize label as soon we finish the printing process
    drawNode( painter, tree, (last_level_count//2)*20, 0, deep - 1 )
    #painter.drawEllipse( width//2 + 20, 0, 20, 20 )

    # Resize label
    label = QtWidgets.QLabel()
    # label.setFixedSize( max_width - min_width + 20, max_height + 20 )
    label.setFixedSize( width, height )

    # Set pixmap
    label.setPixmap( pixmap )

    # Add label to layout
    canvasLayout.addWidget( label )

    # Delete painter
    del painter

def drawNode( painter, node, x, y, height ):

    # Draw circle
    painter.drawEllipse( x, y, 20, 20 )
    
    # Draw text
    painter.drawText( x, y + 30, str( node.leafValue if node.leafValue is not None else " " ) )
    
    # Draw left child
    if node.left != None:
        painter.drawLine( x + 10, y + 20, x - 20 * 2**(height-1) + 10, y + 30 )

        # Draw associated code
        painter.drawText( x - 10* 2**(height-1) , y + 20, "1" )

        drawNode( painter, node.left, x - 20 * 2**(height-1), y + 30, height - 1 )

    
    # Draw right child
    if node.right != None:
        painter.drawLine( x + 10, y + 20, x + 20 * 2**(height-1) + 10, y + 30 )

        # Draw associated code
        painter.drawText( x + 10 * 2**(height-1) + 10, y + 20, "0" )

        drawNode( painter, node.right, x + 20 * 2**(height-1), y + 30, height - 1 )