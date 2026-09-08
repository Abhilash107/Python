from private import PrivateClass
my_obj = PrivateClass()
print(my_obj.public_data)
# print(my_obj.__private_data)# throws: AttributeError: 'PrivateClass' object has no attribute '__private_data'
# name mangling


# but still it can be achieve by:
print(my_obj._PrivateClass__private_data)# IMP


