my_dict = {
    'one': 'Abhilash',
    'two': 'Papun',
    'three': 'nobody'
}

print(my_dict)
print(my_dict['one'])



def get_data(my_dict, my_count):
    while my_count < 10:
        if my_count >= 5:
            print(my_dict['one']+" is a Coder.")
        else:
         print(my_dict['one'])
        
        my_count+=1


get_data(my_dict, 1)
        
