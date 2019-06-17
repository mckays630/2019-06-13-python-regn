# -*- fill-column: 80 -*-

# License: CC0
#
# To the extent possible under law, Pariksheet Nanda has waived all copyright
# and related or neighboring rights to Feedback Summary. This work is published
# from: United States.

library(spacyr)
library(dplyr)
library(readr)

df <- read_csv("feedback.csv")

## Initialize spaCy.
python <- "/usr/bin/python3" # nolint
options(spacy_python_executable = python)
## system2(python,
##         args = c("-m", "spacy", "download", "--user", "en")) # nolint
spacy_initialize(check_env = FALSE)

