print("1.Square using lambda")
my_list = [5, 4, 3]
print(sorted(list(map(lambda item: item**2, my_list))))

print("2.List sorting using lambda")
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
print(sorted(a, key = lambda item: item[0]))
print(sorted(a, key = lambda item: item[1]))