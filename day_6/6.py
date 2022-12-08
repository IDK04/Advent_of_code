text = ''
test = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
with open('input', 'r') as file:
    for line in file.readlines():
        text += line.strip()

def repeated_letters(text):
    for i in range(14):
        if i < len(text) and text.count(text[i]) >= 2:
            return True
    return False

def find_marker_index(text):
    counter = 0
    while True:
        text_to_verify = text[counter:counter+14]
        if not repeated_letters(text_to_verify):
            return counter+14
        else:
            counter += 1

print(find_marker_index(text))