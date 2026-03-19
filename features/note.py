import pathlib
import os


def discover_notes_names():

    return list(pathlib.Path('your_directory').glob('*.txt'))
def take_a_note(note, note_name) -> str:

    with open("../data/notes/" + note_name + ".txt", "a") as f:
        f.write(note + "\n")

    return "note added to " + note_name


def delete_note(note_name) -> str:

    os.remove("../data/notes/" + note_name + ".txt")

    return "note removed"

def access_note(note_name) -> str:

    with open("../data/notes/" + note_name + ".txt", "r") as file:
        content = file.read()

    return content


if __name__ == "__main__":
    print(access_note("notes"))
