#Ejercicios con arreglos

#sumar elementos de arreglo unidimensional
def sumarreglos1(arreglo):
    ns=0
    for i in range (len(arreglo)):
        ns=ns+arreglo[i]
    return ns

#uso sumarreglos1
aU=[1,2,3,4,5,6] #suma 21
s=sumarreglos1(aU)
print(s)

#modificar arreglo unidimensional elevando elementos a una potencia x
def elevarreglos1(arreglo,x):
    for i in range(len(arreglo)):
        arreglo[i]=math.pow(arreglo[i],x)

#uso elevarreglos1 al cuadrado
elevarreglos1(aU,2) #1,4,9,16,25,36
print(aU)
