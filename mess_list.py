messy_list = ["a", 2, 3, 1, False, [1, 2, 3]]

# Your code goes below here
messy_list.insert(0, messy_list.pop(3))
print(messy_list)
messy_list.remove("a")
messy_list.remove(False)
del(messy_list[len(messy_list)-1])
print(messy_list)