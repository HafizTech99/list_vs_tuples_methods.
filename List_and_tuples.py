# 1 lists (mutable):

# inf = ["Hafiz", 25, "Lahore", 908]
# inf[0] = "Abdul Wahab"
# print(inf)



# # Slicing:

# bio = ["Abdullah", 23,"Lahore",]
# print(bio[2])

# # Sort():

# list = ["lichi", "banana", "cherry"]
# list.sort()
# print(list)

# list1 = [67,34,52,56,67]
# list1.sort()
# print(list1)

# # Sort(reverse = True):

# list2 = [45,23,56,34,24]
# list2.sort(reverse=True)
# print(list2)

# Append():
# marks = [23, 45, 56, 67]
# marks.append((89))
# print(marks)

# reverse():
# list3 = [34,55,56,23,56,67]
# list3.reverse()
# print(list3)

# insert():
# list = [2,3,3]
# list.insert(1,1)
# print(list)

# pop():
# list = [1,2,3,5]
# list.pop(3)
# print(list)

# remove():
# list = [1,2,3,4,5,5,6,5]
# list.remove(5)
# print(list)

# tuples(immutable):

# tup = (23,45,56,34)
# print(type(tup))

# We can access the values in the tuples:
# We can slicing in tuples like strings and lists:

# index():
# tup = (23,45,23,45)
# print(tup.index(23))
# # count():
# print(tup.count(23))

# Ask user to enter his three favourite movies and then store them in a list:

# movies = []
# a = input("Your favourite movie ")
# b = input("Your favourite movie ")
# c = input("Your favourite movie ")
# movies.append(a)
# movies.append(b)
# movies.append(c)
# print(movies)

# Check a list is palindrome or not:
# list1 = [1,2,1]
# copy = list1.copy()
# list1.reverse()
# if(list1 == copy):
#     print("Palindrome")
# else:
#     print("Non Palindrome")

# Count the grade A:

grade = ("A","B","C","A","F","A")
print(grade.count("A"))