# Purpose
Inverse the tonality of a MIDI file. Given a basenote, every tone is inverted with respect to that basenote (in which inverted means that the distance is flipped, so a negative distance becomes a positive distance and vice versa). Python 3 is used for writing this script.

# Installation
```
pip install -r requirements.txt
```

# Usage
```
python remidi.py [input file] [output file] --basenote [basenote]
```

Where input file is the file to inverted, output file is the file to save the result to and basenote is the basenote used for the inversion. A basenote of 72 is often a good choice, since it is the middle C.

## Usage example
```
python remidi.py data/the_entertainer.mid data/the_entertainer_inverted.mid --basenote 72
```

Basenote can be ommitted (and then it is automatically set to a value of 72):

```
python remidi.py data/the_entertainer.mid data/the_entertainer_inverted.mid
```