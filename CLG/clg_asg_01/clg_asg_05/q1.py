# # 1. IMP
# n_std = int(input("Eneter number of studends: "))
# mark_dict = {}
# for i in range(n_std):
#     name_std = input("Enter student name: ")
#     mark_std = int(input("Enter mark of the student: "))
#     mark_dict.update({name_std:mark_std})
# print(mark_dict)

# 2.
# s_name = input("Enter name for mark: ")
# if s_name in mark_dict:
#     print("Mark of the student is: ", mark_dict[s_name])


# 3. 
# n = int(input("Enter number of entries: "))
# dict = {}
# for z in range(n):
#     dict[z] = float(input("Enter values: "))
# print(sum(dict.values()))

# 5. IMP
# tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}
# # print('Canada' in tlds)
# # print(tlds.__contains__('France'))
# for k,v in tlds.items():
#     print(f'{k:<20} {v}')
# tlds['Sweden'] = 'sw'
# tlds['Sweden'] = 'se'
# print(dict((sorted(tlds.items()))))
# print(dict(reversed(sorted(tlds.items()))))

# 6. 
# roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5}
# print(list(roman_numerals.keys()))
# print(roman_numerals.values())
# print(tuple(roman_numerals.items()))

# 7. 
# num_cubes = {k : v for k in range(1,6) for v in [k**3]}
# print(num_cubes)

# 9. 
# str='mississippi'
# print({k : str.count(k) for k in str})

# 10. IMP
# str = input("Enter a string: ")
# print({v : str.count(v.lower()) for v in 'aeiou' if str.count(v.lower())>0} )

# 11. 
# def num_to_words(num):
#     num_words = {
#     '0': 'zero',
#     '1': 'one',
#     '2': 'two',
#     '3': 'three',
#     '4': 'four',
#     '5': 'five',
#     '6': 'six',
#     '7': 'seven',
#     '8': 'eight',
#     '9': 'nine'
#     }
#     return(' '.join(num_words[d] for d in str(num)).capitalize())
# # num_to_words(123)
# print(num_to_words(123))
    
# 12. IMP
# sent = 'This is a sentence to test a this to TEST'
# sent_list = sent.lower().split()
# dict_dup = {w.lower(): sent_list.count(w.lower())-1 for w in sent_list if sent_list.count(w.lower())>1}
# print(dict_dup)


# 13. 
# def disp_unique_sorted(slist):
#     return sorted(set(s.lower() for s in slist))
# print(disp_unique_sorted(['apple', 'Apple', 'Vanana', 'vanana', 'cat', 'CAT']))

# 14. 
# str = "Hello, World!"
# print(len(set(s for s in str)))

# 15.

# 16. IMP
# set1 = {10, 20, 30} 
# set2 = {5, 10, 15, 20}
# print(set1.intersection(set2))
# print(set1.union(set2))
# print(set1.difference(set2))
# print(set1.symmetric_difference(set2))

# 17. 
# set1 = {'red', 'green', 'blue'}
# set2 = {'cyan', 'green', 'blue', 'magenta', 'red'}
# print("Is set1 equal to set2?", set1 == set2)
# print("Is set1 not equal to set2?", set1 != set2)
# print("Is set1 a subset of set2?", set1 <= set2)
# print("Is set1 a proper subset of set2?", set1 < set2)
# print("Is set1 a superset of set2?", set1 >= set2)
# print("Is set1 a proper superset of set2?", set1 > set2)

# print("Union of set1 and set2:", set1.union(set2))
# print("Intersection of set1 and set2:", set1.intersection(set2))
# print("Difference of set1 and set2:", set1.difference(set2))
# print("Symmetric difference of set1 and set2:", set1.symmetric_difference(set2))

# 18. IMP
def analyze_sets(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    symmetric_difference = set1.symmetric_difference(set2)
    print(symmetric_difference)
    print(sorted([element * 2 if element % 2 == 0 else element + 5 for element in symmetric_difference]))  
analyze_sets([1,2,5,4,5],[1,7,6])

# 19. IMP
# words = ["apple", "dogs", "cat", "bird", "fish", "zebra", "lion"]
# def unique_pairs(words):
#     unique_pairs_set = set()
#     for i in range(len(words)):
#         for j in range(i+1, len(words)):
#             word1 = words[i]
#             word2 = words[j]
#             if len(word1) >= 4 and len(word2) >= 4:
#                 if len(set(word1) & set(word2)) == 0:
#                     unique_pairs_set.add(tuple(sorted((word1, word2))))
#     return unique_pairs_set
# print(unique_pairs(words))

# 20.
# sample_dict = {
#     'person1': {'name': 'Bezos', 'net worth': 21880},
#     'person2': {'name': 'Elon', 'net worth': 31570},
#     'person3': {'name': 'Mukesh', 'net worth': 965}
# }
# sample_dict['person3']['net worth'] = 9650
# print(sample_dict)