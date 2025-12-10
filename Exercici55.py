print("Números parells fins a 100:")
for i in range(2, 101, 2):
    print(i, end=", " if i < 100 else "\n")
print("Números senars fins a 100:")
for i in range(1, 101, 2):
    print(i, end=", " if i < 100 else "\n")
