from mido import MidiFile
from mido import MidiTrack
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Invert a MIDI file. Usage: remidi.py [base note value]')
    parser.add_argument('input', help='the path to the MIDI file to transform')
    parser.add_argument('output', help='the path to the resulting MIDI file')
    parser.add_argument('--basenote', type=int, default=72, required=False,
                        help='the note value (v) of the base note such that every note value x is transformed to v - (x - v) (inversion) [v=72 is default and is a middle C]')

    args = parser.parse_args()
    input_file = args.input
    output_file = args.output
    basenote = args.basenote

    mid = MidiFile(input_file)
    inverted = MidiFile()

    for track in mid.tracks:
        new_track = MidiTrack()

        for message in track:
            if 'note' in dir(message):
                inverted_note = basenote - (message.note - basenote)
                new_track.append(message.copy(note=inverted_note))
            else:
                new_track.append(message)

        inverted.tracks.append(new_track)

    inverted.save(args.output)
