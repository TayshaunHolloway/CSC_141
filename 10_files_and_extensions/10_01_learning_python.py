#In Python you can store as much information as you want.
#In Python you can connect pieces of information.
#In Python you can model real-world situations.

from pathlib import Path

print("--- Reading in the entire file:")
path = Path('learning_python.txt')
contents = path.read_text()
print(contents)

print("\n--- Looping over the lines:")
lines = contents.splitlines()
for line in lines:
    print(line)