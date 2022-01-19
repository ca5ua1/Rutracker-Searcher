#!/bin/python

import sys
from pyfzf.pyfzf import FzfPrompt
from rutracker_api import RutrackerApi

fzf = FzfPrompt()
api = RutrackerApi()

api.login("LOGIN", "PASSWORD")

search = api.search(" ".join(sys.argv[1:]))
search

choice = fzf.prompt(list(search['result'][0:16]))

result = search['result'][0]
i = 0
while (i <= 16):
    if str(search['result'][i]) == choice[0]:
        result = search['result'][i]
        break
    else:
        i = i+1


print(result.get_magnet())
