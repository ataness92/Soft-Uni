notes = []

while True:
    note = input()

    if note == 'End':
        break

    notes.append(note)

sorted_notes = sorted(notes, key= lambda x: int(x.split('-')[0]))
sorted_notes = [x.split('-')[1] for x in sorted_notes]
print(sorted_notes)




