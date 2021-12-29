#! python3 
# bullet point adder - adds a bullet point to the start of each line.

import pyperclip

text = pyperclip.paste()
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)
