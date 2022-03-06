x=int(input("insira o numero de termos do vetor: "))
arr=[]

for i in range(x):
  print("insira o valor de arr[",i,"]")
  temp=int(input())
  arr.append(temp)

for i in range(x):
  for j in range(x):
    if arr[i]>arr[j]:
      temp=arr[i]
      arr[i]=arr[j]
      arr[j]=temp

mediana=int((x-1)/2)
print("o valor da mediana é: ",arr[mediana])