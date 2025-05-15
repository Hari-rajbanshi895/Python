""" DICTONARY IN PYTHON """
# => Ordered in new version
# => Mutuable

result = {
    "name":"himal",
    "age":19,
    "is_male":True
    }

result.update({'dob':2002})
print(result)

result.pop("age")
print(result)

result.popitem()
print(result)

del result['is_male']
print(result)

result.clear()
print(result)




# print(type(result))
# print(result.keys())
# print(result.values())

# print(result['name'])
# print(result.get('name1'))

# for i in result.keys():
#     print(f"The corresponding {i} is {result[i]}")
# # print(result['name'])
# # print(result)
# # result.pop('age')
# # print(result)

