import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for char in message:
    count.setdefault(char, 0)
    print(count[char])
    count[char] = count[char] + 1
    print(count[char])
    
print(pprint.pformat(count))
