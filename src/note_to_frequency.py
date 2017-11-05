import sys
class NoteToFrequency():
    fourth_octave = {"C4":261.63, "C#4":277.2, "D4":293.66, "Eb4":311.1, "E4":329.63, "F4":349.23, "F#4":370.00, "G4":392.00, "G#4":415.3, "A4":440.00, "Bb4":466.2, "B4":493.88}
    def validate_note(self, note):
        return note[:len(note) - 1] + "4" in self.fourth_octave.keys() and 0 <= int(note[len(note) - 1] <= 8)
    def get_frequency(self, note):
        midOctaveFrequency = self.fourth_octave[note[:len(note) - 1] + "4"]
        return "Frequency is %.2f." % float(midOctaveFrequency / 2**(4 - int(note[len(note) - 1])))

note = raw_input("Enter a note: ")
given_note = NoteToFrequency()
while given_note.validate_note(note) == False:
    note = raw_input("Please enter a valid note. If you would like to exit, press Enter: ")
    if note == "":
        print "Exited."
        sys.exit()
print given_note.get_frequency(note)
