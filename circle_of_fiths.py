#!/usr/bin/python3
# -*- coding: utf-8 -*-
from music21.note import Note
from enum import Enum


class MajorMinor(Enum):
    MAJOR = 1
    MINOR = 0


major = MajorMinor.MAJOR
minor = MajorMinor.MINOR


class CircleOfFifths:
    def __init__(self):
        base_note = Note('C4', quarterLength=4)
        self.notes = [base_note]
        for i in range(6):
            new_note = base_note.transpose('P5')
            while new_note.octave > 4:
                new_note = new_note.transpose('P-8')
            self.notes.append(new_note)
            base_note = new_note
        base_note = Note('D4-', quarterLength=4)
        self.notes.append(base_note)
        for i in range(4):
            new_note = base_note.transpose('P5')
            while new_note.octave > 4:
                new_note = new_note.transpose('P-8')
            self.notes.append(new_note)
            base_note = new_note

    def base_note(self, index: int, major_minor: MajorMinor = major):
        if major_minor == major:
            return self.notes[index % 12]
        elif major_minor == minor:
            return self.notes[(index + 3) % 12]


if __name__ == "__main__":
    cf = CircleOfFifths()
