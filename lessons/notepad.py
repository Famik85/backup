# CRUD
# Create
# Read
# Update
# Delete
try:
    text = open("notes.txt", "rt")
    text.close()
except:
    text = open("notes.txt", "wt")
    text.close()
text = open("notes.txt", "rt")
notes = {}
data = text.readlines()
text.close()
for line in data:
    notes[line[:line.find(" :")]] = line[line.find(": ") + 1:]
while True:
    command = str(input("Enter your command : [c],[r],[u],[d],[e] : "))
    if command.lower() == "c":
        title = str(input("Enter title of note: "))
        note = str(input("Enter text of note: "))
        notes[title] = note
    elif command.lower() == "u":
        title = str(input("Enter title of note: "))
        note = str(input("Enter text of note: "))
        notes[title] = note
    elif command.lower() == "d":
        title = str(input("Enter title of note: "))
        notes.pop(title)
    elif command.lower() == "r":
        for title, text in notes.items():
            print(title, ":", text)
    elif command.lower() == "e":
        file = open("notes.txt", "wt")
        for title, text in notes.items():
            s = title + " : " + text + "\n"
            file.write(s)
        file.close()
        break