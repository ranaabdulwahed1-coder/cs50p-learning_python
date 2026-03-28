import random
import sys
from pyfiglet import Figlet
figlet = Figlet()
font = None
# no font
if len(sys.argv) == 1:
    fonts = Figlet().getFonts()
    font = random.choice(fonts)
elif len(sys.argv) == 2:
    sys.exit()
elif len(sys.argv) == 3:
    if sys.argv[1] in ['-f', '--font']:
        font = sys.argv[2]
figlet.setFont(font = font)
s = input()
print(figlet.renderText(s))



