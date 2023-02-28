
"""reducer.py"""

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
maxim=0
m_word=None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    #filename, circ= word.split(',', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    #maxim=0
    if count > maxim:
        m_word=word
        maxim = count
print (word, m_word, maxim)
