numbers = '123,21,37,3'

def split(text, sep):
    parts = []
    current_part = []
    for char in text:
        if char != sep:
            current_part.append(char)
        else:
            parts.append(''.join(current_part))
            current_part = []
    parts.append(''.join(current_part))
    return parts

def split2(text, sep):
    parts = []
    start = 0
    for current, char in enumerate(text):
        if char == sep:
            parts.append(text[start:current])
            start = current + 1
    parts.append(text[start:])
    return parts

print(split2(numbers, ','))
print(split2(numbers, ',') == ['123', '21', '37', '3'])
print(split2(numbers, '2') == ['1', '3,', '1,37,3'])
