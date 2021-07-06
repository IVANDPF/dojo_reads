# dojo_reads

Sentencias If // elif // else

#Sentencia if
if True: 
	print('el bloque va a ejecturar este if')
ej: 
x = 10
if x >= 9 
	print("La condicion es veradera, esta sentencia se ejecuta")


#Sentencia else
if not true
	print('la sentencia if no se ejecuta')
else
	print('la sentencia else (caso base) se ejecutrara')
ej:
if y = 3
if y > 4 
	print('no voy a imprimir, este bloque no se cumple')
else:
	print('Al no ser verdadera mi condicion, esta sentencia se ejecuta')


#Sentencia elif
z=1
if z >9 
	print('no voy a imprimir esta sentencia, porque su condicion no es verdadera')
	print(z+10)

elif z>5
	print('Ejecutaremos esta condicion, dado que es verdadera')
	print(z+11)
else: 
	print('Para este ejemplo, esta condicion no se ejecutra, dado que no entre en esta sentencia')
	print(z)

----------------------------

for <elem> in <iterable>
	<nuestro cod html>

nums = [4, 5, 7, 89]
for n in nums
	print(n)
4
5
7
89

diccionario = {'A': 4, 'B': 3, 'C': 0}
for palabra in diccionario
	print(palabra)
A
B
C

diccionario = {'A': 4, 'B': 3, 'C': 0}
for valores in diccionario.values():
	print(valores)
4
3
0

diccionario = {'A': 4, 'B': 3, 'C': 0}
for palabra, valores in diccionario.items():
	print("palabra=", palabra, " valores=", valores)
palabra=A, valores=4
palabra=B, valores=3
palabra=C, valores=0


Range
for i in range(6):
	print(i)
0
1
2
3
4
5

range(max) -> max -1
range(min, max) -> min, max-1
range(min,max,step) -> min, max-1, de step en step

for num in range(0,11,2)
	print(num)
0
2
4
6
8
10



------------
MODIFICANDO LA ITERACION DEL BUCLE
list = [2,4,6,7,8,9]
for i in list
	if i == 7:
		break
		print(i)
2
4
6


list = [1,2,3,5,7,9]
for e in list
	if e % 2 != 0:
		continue
	print(e)
2


----------------------------
# While

i = 1
while i < 10:
	print(i)
	i += 1
1
2
3
4
5
6
7
8
9

-> ejecuta lo siguiente 


i = 1
while i < 6
	print(i)
	if(i == 3):
		break
	i += 1
1
2
3

-> ejecuta lo siguiente codigo




i = 0
while i < 8
	i += 1
	if i == 3:
		continue
	print(i)
1
2
4
5
6
7
8



i = 1
while i < 5 
	print(i)
	i +=1
else:
	print("La " , i , "ya no es mas menor que 5")
1
2
3
4
La 5 ya no es mas menor que 5

