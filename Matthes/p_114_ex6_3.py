py_word = {
'[]': 'list',
'()': 'tuple',
'{}': 'dictionary',
'in': 'Checking if values are in a list',
'set': 'collection of unique elements',
}
# print(py_word['in'])

for w in py_word:
    print(w, " : ")
    print("\t",py_word[w])

# p 120 ex 6.5
river = {
'nile': 'egypt',
'rhein': 'germany',
'dnieper': 'ukraine',
}
for k,v in river.items():
    print(f"The {k.title()} runs through {v.title() }")