# List - Mutable
values = [1, 2, 3, "raju", 5.6, 7, 8]

print(values[0])
print(values[3])

print(values[-1])

print(values[1:3])

values.insert(3, "rashed")
print(values)

values.append("END")
print(values)

values[2] = "Update"
print(values)

del values[-1]
print(values)

# Tuple (Immutable)

values = (1, 2, 3, "raju", 5.6, 7, 8)
print(values)
print(values[1])

# lis = []
#
# for i in values:
#     lis.append(i)
# print(lis)

# Dictionary

dic = {1: 'First Name', "a": 2, "c": "Hello"}
print(dic)
print(dic["a"])
print(dic[1])

dict = {}
dict["FirstName"] = "Abdullah Al"
dict["LastName"] = "Faroque"
print(dict)
print(dict["LastName"])
