# # list data types
# a = "one person"
# # []
# b = ["Jio", True, 78, 89.23, "Jio"]
#
# print(b)
# print(type(b))
# print(b[0])
# print(b[1])
# print(b[2])
# print(b[3])
#
# # 1.inser order is preserved
# # 2.Hetrogenious
# # 3.Duplicates
# # 4.Growable = Muttable
#
# b.append("ramu")
# print(b)
#
# b.remove("Jio")
# print(b)
# print(b*3)


# tuple data types
# ()
# (,) == single value atlest one coma
# immutable
#
# z=(1,2,3,4,5,6,7,8,9)
# print(z)
# print(type(z))
# # z.append(88)
# print(z)
# print(z[2])


# Rang Data Types
# k = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# range(4) starting =0, ending 4, step=1
# a = list(range(0, 100, 2))
# # for i in a:
# #     print(i)
# # if i % 2 == 0:
# #     print(i)
# print(a)
# print(type(a))


# Set Data Types
# {}
# insert any one -item =the order shuffled
# hetrogenious
# index not possible
# muttable
# duplicates
a = {"prema", "raju", "mahesh", "charan", "delhi", "PREMA", "prema"}
b = frozenset(a)
# print()
# print(type(b))
# b.add("roja")
# print(a)
# b.remove("prema")
# print(a)

# h = ["prema", "raju", "mahesh", "charan", "delhi", "PREMA", "prema"]
#
# f= list(set(h))
# print(f)
#
# print(f)
# k=list(f)
# print(k)
# print(h)
# result = []
# for j in h:
#     if j in result:
#         continue
#     result.append(j)
# print(result)


# dict data types

# {"key":"value"}

# h = {"prema": 1, "raju": 2, "mahesh": 3, "charan": 4, "delhi": 5, "PREMA": 6, "prema": 7}
#
# h = {"name": "mohan", "class": "10th", "school": "sri venkateswara"}
# print(h)
# print(type(h))
#
# h["mobile"]="1232344555"
#
# print(h)
#
# h.pop("mobile")
# print(h)
# h.add("roja")
# print(h)
# h.remove("prema")
# print(h)

# None


#
# list =muttable
# tuple = immutable
# set =muttable
# frozenset = immutable
# dict = muttable
#range = immutable

