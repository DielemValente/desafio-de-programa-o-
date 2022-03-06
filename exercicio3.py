lin = 0
col = 0
cont = 0
msg=""

list = []
list1 = []
x = input("Insira a string: ")
list[:0] = x

temp = len(x)

for i in range (temp):
    if list[i] != " ":
        list1.append(list[i])

T = len(list1)
rT = int(T**(1/2))

for i in range(rT+2):
    for j in range (rT+2):
        if (i*j) >= T:
            lin = i
            col = j
            break

grid = [[0 for x in range (col)] for y in range(lin)]

for x in range (lin):
    for y in range(col):
        if cont < T:
            grid[x][y] = list1[cont]
            cont += 1

for y in range(lin):
	msg=msg+" "
	for x in range(col):
		if grid[y][x] != 0:
			msg=msg+str(grid[x][y])

print(msg)