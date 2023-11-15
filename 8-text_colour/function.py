

def color(color="default", text=""):
    array_color = {
        'default': '0',
        'grey': '1;30',
        'red': '1;31',
        'green': '1;32',
        'yellow': '1;33',
        'blue': '1;34',
        'purple': '1;35',
        'nevy': '1;36',
        'white': '1;0',
    }
    
    return f"\033[{array_color.get(color, '0')}m{text}\033[0m"


