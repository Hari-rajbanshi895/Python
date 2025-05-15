'''SETS IN PYTHON'''
# => Sets are unordered
# => They are mutuable

# name = {'hari',7,3.5,False}
# print(name) # sets are unordered they can print anything rondom elements 

'''Print empty set'''
# name = set() 
# print(type(name))

# name = {'hari',7,3.5,False}
# for i in name:
#     print(i)

'''Methods in sets'''
# => Union (A U B)
# => Union_update

# num = {1,2,3,8,9}
# num1 = {4,5,6,7,9}
# print(num.union(num1))
# num1.update(num)

# => INTERSECTION (A N B)
# => INTERSECTION_UPDATE(UPDATES THE INTERSECTION OF SETS)

# cities = {"Tokyo","Kathmandu","Madrid","Quak"}
# cities1 = {"Tokyo","Bhaktapur","Delhi","Gorkha","Quak"}
# print(cities.intersection(cities1))
# cities2 = cities.intersection_update(cities1)
# print(cities2)


# => SYMMETRIC_DIFFERENCE
# => UPDATE_SYMMETRIC_DIFFERENCE

# cities = {"Tokyo","Bhaktapur","Delhi","Gorkha","Quak"}
# cities1 = {"Tokyo","Kathmandu","Madrid","Quak"}
# cities3 = cities.symmetric_difference_update(cities1)
# print(cities3)
# print(cities.symmetric_difference(cities1))

# => DIFFERENCE

# cities = {"Tokyo","Bhaktapur","Delhi","Gorkha","Quak"}
# cities1 = {"Tokyo","Kathmandu","Madrid","Quak"}
# cities2 = cities.difference(cities1)
# print(cities2)

# => ISDISJOINT

# cities = {"Tokyo","Bhaktapur","Delhi","Gorkha","Quak"}
# cities1 = {"Tokyo","Kathmandu","Madrid","Quak"}
# cities2 = cities.isdisjoint(cities1)
# print(cities2)

# => ISSUPERSET
# => ISSUBSET

# cities = {"Tokyo","Madrid","Seoul","Kathmandu","Delhi"}
# cities2 = {"Tokyo","Kathmandu"}
# cities3 = cities.issuperset(cities2)
# cities4 = cities2.issubset(cities)
# print(cities3)
# print(cities4)


# => add()

# cities = {"Tokyo","Madrid","Seoul","Kathmandu","Delhi"}
# cities.add("Bhaktapur")
# print(cities)

# => update()

# cities = {"Tokyo","Madrid","Seoul","Kathmandu","Delhi"}
# cities1 = {"Tokyo","Kathmandu","Madrid","Quak"}
# cities.update(cities1)
# print(cities)

# => remove(),discard() {used to remove element from set}

# cities = {"Tokyo","Kathmandu","Madrid","Quak"}
# cities.remove("Tokyo")
# print(cities)

# cities = {"Tokyo","Kathmandu","Madrid","Quak"}
# cities.discard("Tokyo")
# print(cities)


# => clear() {Clears the whole elements of set}

# cities = {"Tokyo","Kathmandu","Madrid","Quak"}
# cities.clear()
# print(cities)

# => pop() {Deletes last item in set}

# cities = {"Tokyo","Kathmandu","Madrid","Quak"}
# cities.pop() 
# print(cities)





