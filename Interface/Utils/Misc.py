
# Customize controls stylesheet (Audio Recorder Button)
def configStyleSheet( recording ):
    return f"""
        QPushButton {{
            background: none;
            background-color: { "black" if not recording else "white"};
            color: { "white" if not recording else "black"};
            border-style: solid;
            border-width: 1px;
            border-color: { "white" if not recording else "black"};
        }}

        QPushButton:hover {{
            background: none;
            background-color: { "white" if not recording else "black"};
            color: { "black" if not recording else "white"};
            border-style: solid;
            border-width: 1px;
            border-color: { "black" if not recording else "white"};
        }}
    """

def registerLog( text, control ):
    # Append the text to the log (Control is a QTextEdit)
    control.append( text )
    # Scroll to the bottom
    control.verticalScrollBar().setValue(control.verticalScrollBar().maximum())