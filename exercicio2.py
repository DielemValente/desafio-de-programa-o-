i=int(input("insira o numero de termos do vetor: "))
x=int(input("insira a diferença entre os valores: "))
n=[]
cont=0

for k in range(i):
	print("insira o valor de: n[",k,"]")
	temp=int(input())
	n.append(temp)

for j in range(i):
	for k in range(i):
		temp=n[j]-n[k]
		if temp==x:
			cont+=1

print(cont)