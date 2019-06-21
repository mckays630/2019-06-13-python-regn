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

# To use similarity scores, we can't use the small model.
model = "en_core_web_md"
try:
    nlp = spacy.load(model)
except OSError:
    raise IOError(("Error: You're missing the spacy model. Install it with:\n"
                   "    python3 -m spacy download --user " + model))

# For some reason my IPython interpreter keeps starting in the main git
# directory, so search recursively to find an exact file match.
path = next(pathlib.Path().rglob("feedback.csv")) 
df = pd.read_csv(path)
df = df.dropna()
# Run model on strings.
df['doc'] = df['feedback'].apply(lambda x: nlp(x))

# Split up sentences.
col_sents = df['doc'].apply(lambda x: x.sents).apply(pd.Series).stack().apply(lambda x: x.as_doc())
col_sents.name = 'doc'
col_sents.index = col_sents.index.droplevel(-1)
df = df.iloc[:, :-2].join(col_sents)
df.reset_index(inplace = True)

# Pace is always talked about at workshops, so separate it from other feedback.
patterns = {
    'PACE_PATTERN': [{'LEMMA': 'pace'}],
    'FAST_PATTERN': [{'LEMMA': 'fast'}],
    'SLOW_PATTERN': [{'LEMMA': 'slow'}],
}
pace_matcher = spacy.matcher.Matcher(nlp.vocab)
for name, pattern in patterns.items():
    pace_matcher.add(name, None, pattern)

def is_related_to_pace(doc):
    matches = pace_matcher(doc)
    return len(matches) > 0
    
df_pace = df[df['doc'].apply(is_related_to_pace)]
df = df[~df.index.isin(df_pace.index)]
