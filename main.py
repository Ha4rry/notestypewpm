#!/usr/bin/env python

import time

save_filename = "latestnotesoutput.txt"

input("PRESS ENTER TO START")
start = time.time()
notes = input("Type notes below:\n")
end = time.time()
time_taken = end - start

word_count_average = len(notes)/5
minutes = time_taken/60
wpm = word_count_average / minutes
print(f"\nFinal WPM: {round(wpm, 1)}")
with open(save_filename, "w") as save_file:
    save_file.write(notes)
print(f"\nNotes saved to {save_filename}")
