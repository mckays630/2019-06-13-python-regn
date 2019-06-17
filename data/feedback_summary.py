# -*- fill-column: 80 -*-

# License: CC0
#
# To the extent possible under law, Pariksheet Nanda has waived all copyright
# and related or neighboring rights to Feedback Summary. This work is published
# from: United States.

"""Process the feedback using the spaCy natural language processing library
suggested by Jonathan Kin Wei Leung.

"""
# Builtin modules
import pathlib
# 3rd party
import spacy
import pandas as pd

model = "en_core_web_sm"
try:
    nlp = spacy.load(model)
except OSError:
    raise IOError(("Error: You're missing the spacy model. Install it with:\n"
                   "    python3 -m spacy download --user " + model))

# For some reason my IPython interpreter keeps starting in the main git
# directory, so search recursively to find an exact file match.
path = next(pathlib.Path().rglob("feedback.csv"))

df = pd.read_csv(path)
# Subset for testing.
df = df.dropna().groupby(['datetime', 'color']).head(1)
# Run model on strings.
df['doc'] = df['feedback'].apply(lambda x: nlp(x))

# Extract nouns.
nouns_green = set()
for _, doc in df[df['color'] == 'green']['doc'].iteritems():
    for nouns in doc.noun_chunks:
        for noun in nouns:
            nouns_green.add(noun.text)
