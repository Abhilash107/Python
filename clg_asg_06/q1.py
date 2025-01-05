import numpy as np
# 1.
# print(np.zeros((3,3), int))
# print(np.ones((2,3),int))
# print(np.full((2,5),7,int))

# 2. 
# arr = np.arange(4).reshape((2,2))
# print(arr)
# print(arr**3)
# print(arr+7)
# print(arr*2)

# 3.IMP
# a1 = np.arange(2,19,2)
# a2 = np.arange(9,0,-1)
# print(a1,'\n',a2)
# print(a1.reshape((3,3))*a2.reshape((3,3)))

# 4. IMP
# arr = np.array([[1,2],[4,5]])
# print(arr[[0,1]])
# arr[[0,1]] = arr[[1,0]]
# arr[:,[0,1]] = arr[:,[1,0]]
# print(arr)

# first_row = arr[0, :].copy()  
# first_col = arr[:, 0].copy() 
# arr[0, :] = first_col
# arr[:, 0] = first_row
# print(arr)

# 5.
# list1 = [1,2,3,4,5]
# list2 = [11,12,13,14,15]
# print(np.array([list1, list2]))

# 6. imp
# arr = np.full((2,3),2)**np.arange(6).reshape((2,3))
# print(arr)
# arrf = arr.flatten()
# print(arrf)
# arrv = arr.ravel()
# print(arrv)

# 7.imp
# arr = np.array([1,1,2,3,4,5,6,4,3,2,5,3,4,3,2,2,4,3,2,4,4,5,5,6,3,2,3,3,3,2,1,1,1,1])
# print(arr.sum(), arr.min(), arr.max())
# unique_elements, counts = np.unique(arr, return_counts=True)
# for element, count in zip(unique_elements, counts):
#     print(f'Element: {element}, Count: {count}')

# 8. 
# arr = np.linspace(1.1, 6.6, 6).reshape((2,3))
# print(arr)
# print(arr.astype(int))

# 9.imp
# def format_2d_array(arr):
#     max_width = len(str(arr.max()))
#     return "\n".join(["\t".join(f"{n}" for n in row)for row in arr])
# arr = np.random.randint(0,100,(3,3))
# print(format_2d_array(arr))

# 10. 
# arr = np.arange(1,16).reshape((3,5))
# print(arr)
# print(f"Row 2: {arr[1]}")
# print(f"Col 5: {arr[:,4]}")
# print(f"Row 0,1: {arr[[0,1]]}")
# print( arr[:, 2:5])
# print(arr[0,3])
# print(arr[:2,[0,2,4]])#imp

# 11. 
# arr1 = np.array([[0,1],[2,3]])
# arr2 = np.array([[4,5],[6,7]])
# arr3 = np.vstack((arr1,arr2))
# print(arr3,"\t",arr3.shape)
# arr4 = np.hstack((arr1,arr2))
# print(arr4,"\t",arr4.shape)
# arr5 = np.vstack((arr4,arr4))
# print(arr5,"\t",arr5.shape)
# arr6 = np.hstack((arr3,arr3))
# print(arr6,"\t",arr6.shape)

# 12. IMP
# arr7 = np.concatenate((arr1,arr2),axis = 0)
# print(arr7)
# arr8 = np.concatenate((arr1,arr2),axis = 1)
# print(arr8)

# 13.
# checkboard = np.tile(["*","_"],(5,5))
# print(checkboard)

# 14. 
# arr = np.random.randint(0,100,(5,5))
# print(arr)
# print(np.bincount(arr.flatten()))

# 15.
# def mean_median(arr):
#     return float(np.mean(arr)), float(np.median(arr))
# arr1 = np.array([1,2,2,3,3,3,4,4])
# arr2 = np.array([10,20,20,30,40,4])
# arr3 = np.array([5,5,5,5,5])
# print(mean_median(arr1))
# print(mean_median(arr2))
# print(mean_median(arr3))

# 16. 
# arr = np.random.randint(10,100,(9,9,2))
# print(arr)
# ext_arr = arr[1:6,2:7]
# print(ext_arr)

# 17.
# arr = np.random.randint(10,20,(4,4))
# arr = np.sort(arr,axis=0)
# print(arr)
# arr = np.sort(arr,axis=1)
# print(arr)

# Pandas: 
# import pandas as pd
# 18. 
# data = {'A':[1,2,3], 'B':[4,5,6], 'C':[7,8,9]}
# df = pd.DataFrame(data)
# print(df)
# print(df.iloc[:,0])

# 19. 
# s1 = [1,2,3,4]
# s2 = [5,2,3,8]
# pds1 = pd.Series(s1)
# pds2 = pd.Series(s2)
# print(pds1,'\n',pds2)
# res = pds1[~pds1.isin(pds2)]
# print(res)

# 20.
# pds = pd.Series([1,1,3,7,50,45,50,1])
# print(pds.value_counts())
# print(pds.idxmin(),'\t',pds.idxmax())

# 21. 
# data = pd.Series(['Cry', 'Apple', 'Orange', 'Sky', 'Banana'])
# def contains_vowel(word):
#     vowels = 'aeiouAEIOU'
#     return any(char in vowels for char in word)
# def starts_with_vowel(word):
#     vowels = 'aeiouAEIOU'
#     return word[0] in vowels if word else False
# vowel_check = data.apply(contains_vowel)
# vowel_start_check = data.apply(starts_with_vowel)
# elements_with_vowels = data[vowel_check]
# elements_stat_with_vowels = data[vowel_start_check]
# print("Original Series:")
# print(data)
# print("\nElements containing vowels:")
# print(elements_with_vowels)
# print("\nElements starting with vowels:")
# print(elements_stat_with_vowels)

# element_has_vowel = data[data.str.contains('[AEIOUaeiou]',regex = True)]
# print(element_has_vowel)
# element_starts_with_vowel = data[data.str[0].str.match('[AEIOUaeiou]')]
# print(element_starts_with_vowel)

# 22.
# pds = pd.Series([7,11,13,17])
# print(pds)
# pds_100 = pd.Series([100.0]*5)
# print(pds_100)
# pds_random = pd.Series(np.random.randint(0,100,20))
# print(pds_random)
# temperatures = pd.Series([98.9,98.9,45.5,78.2,12.3], index=['A','B','C','D','E'])
# print(temperatures)
# temp_dict = dict(zip(temperatures.index,temperatures.values.tolist()))
# print(temp_dict)

# 23.
# data = {'Maxine':[1,2,3], 'James':[4,5,6], 'Amanda':[8,9,7]}
# temp = pd.DataFrame(data)
# print(temp)
# temp = pd.DataFrame(data, index = ['Morning', 'Afternoon', 'Evening'])
# print(temp)
# print(temp['Maxine'])
# print(temp.loc['Morning'])
# print(temp.loc[['Morning','Evening']])
# print(temp[['Maxine','Amanda']])
# print(temp[['Maxine', 'Amanda']].loc[['Morning', 'Evening']])
# print(temp.describe())
# print(temp.T)
# print(temp[sorted(temp.columns)])