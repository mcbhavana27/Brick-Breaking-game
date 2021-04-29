from colorama import init, Fore, Style, Back

# Define scene length(vertical), width(horizontal),
scr_len = 40
scr_wid = 150
scr_size = 500


colors = {
    'Blue': '\x1b[0;34m',
    'Green': '\x1b[0;32m',
    'Cyan': '\x1b[0;36m',
    'Red': '\x1b[0;31m',
    'Purple': '\x1b[0;35m',
    'Brown': '\x1b[0;33m',
    'Gray': '\x1b[0;37m',
    'Yellow': '\x1b[1;33m',
    'White': '\x1b[1;37m'
}
RESET = '\x1b[0m'


groundx = 36
posx=37
posy=30


class Live:
    lives = 5

class Score:
    score=0
