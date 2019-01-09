import math

tipo = str(input('informe o tipo de juros (simples ou composto): '))
if (tipo != 'simples' and tipo != 'composto'):
    print ('informe um tipo valido (simples ou composto).')

else: 
    c = float(input('informe o capital inicial: '))
    n = float(input('informe a taxa de juros (a.a): '))
    m = 2 * c
    

if (tipo == 'simples'):
    t = ((m/c)-1)/n 
    print ('o tempo necessario:',t, 'anos')

elif (tipo == 'composto'):
    t = math.log(m/c)/math.log(1+n)
    print ('o tempo necessário:',t, 'anos')

   




    

