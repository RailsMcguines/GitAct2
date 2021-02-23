def arp(val1,val2,oper):
    if oper == '/':
        res = val1 / val2
    if oper == '+':
        res = val1 + val2   
    elif oper == '*':
        res = val1 * val2   
    elif oper == '-':
        res = val1 - val2
    elif oper == '/':
        res = val1 / val2
    else:
        res="Error"
    return res

print("Ingrese el primer valor")
val1=input()
va=val1.isnumeric()
if va:   
    val1=int(va)
    print("Ingrese un segundo valor")
    va2=input()
    if va2.isnumeric():
        val2=int(va2)
        print("Ingrese un operador +, *, -, /")
        oper = input()
        #print("La suma de estos números es: " + str(val1+val2))
        res = arp(val1,val2,oper)
        #res = maxi(val1)
        print("La suma de estos números es: " + str(res))
        input()
    else:
        print("El segundo valor ingresado no fue numérico")
else:
    print("no ingreso un valor númerico")