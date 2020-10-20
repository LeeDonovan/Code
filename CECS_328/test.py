m = 25
h = 17
prev = 0
for i in range(30):
    z = h + (i**2)
    print(z)
    mod = z % m
    print(i, " Mod: ", mod )