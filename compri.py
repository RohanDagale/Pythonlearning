'''
List comprehension
Dictionary comprehension
set comprehension
Generator Comprehension

'''

list_1 = [1, 5, 6,73, 86, 55, 58, 86, 33 ,60]
divided_by_3 = []
for item in list_1:
    if item%3 == 0:
        divided_by_3.append(item)

print('without usign list comprehension',divided_by_3)
print('with using list comprehension', [item for item in list_1 if item%3 == 0])


dict1 = {'a': 45, 'b': 65, 'A':5}
print({k.lower():dict1.get(k.lower(), 0) + dict1.get(k.upper(), 0) for k in dict1.keys()})