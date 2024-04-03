

array = [1, 4, 6, 2, 8, 8]
print(array.pop(array.index(8)))
# NB:  poping out of range index generated value error

# TODO: sort dictionary
chars = {'a': 2, 'c': 3, 'b': 1}
print(f'Before sorting: {chars}')
sorted = dict(sorted(chars.items(), key=lambda x: x[1]))
# sorted(chars.items(), key=lambda x: x[1])
print(f'After sorting: {sorted}')

#NB: in Python 3.7 and earlier versions
  #  dict(sorted(chars.items())  => Doesn't work (meaning : it doesn't guarente the order of the dictionary)
  #  so to solve this problem we use orderedDict(sorted(chars.items()))
