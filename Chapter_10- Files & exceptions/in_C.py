"""
10-2. Learning C: You can use the replace() method to replace any word in a
string with a different word. Here’s a quick example showing how to replace
'dog' with 'cat' in a sentence:
Read in each line from the file you just created, learning_python.txt, and
replace the word Python with the name of another language, such as C. Print
each modified line to the screen.
"""
filename = 'learning_python.txt'
with open(filename) as file_object:
    contents = file_object.read()
    contents = contents.replace('Python', 'C')
    print(contents.rstrip())
    print('\n')

filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

c_string = ''

for line in lines:
    c_string += line.replace('Python', 'C')

print(c_string)