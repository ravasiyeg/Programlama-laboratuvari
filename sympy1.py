x=1
x=x+x+1
print(x)
#cıktı=3
#x burada degisken olarak kullanılmıştır.

from sympy import Symbol

x=Symbol('x')
x=x+x+1
print(x)
#cıktısı=2*x+1
#x burada sembol olarak kullanılmıştır.

a=Symbol('x')
a=a+a+1
print(a)
#çıktısı 2*x+1
#symbol her zaman x'e esit olmak zorunda değil.
************************************************
from sympy import Symbol
x=Symbol('x')
y=Symbol('y')

p=x*(x+x)
print(p)
#çıktısı= 2*x**2

************************************************

from sympy import factor,expand
expr= x**2-y**2
print(factor(expr))
#çıktısı= (x-y)*(x+y)
#çarpanlara ayırır

factors=factor(expr)
print(expand(factors))#çarpanlara ayrılmış şeklini birleştirip sadeleştirir.

expr= x**3+ 3*x**2*y+ 3*x*y**2+ y**3
factors=factor(expr)
print(factors)
#(x+y)**3

**************************************************
from sympy import pprint

pprint(factors)
#daha gorsel bir çıktı verir

***************************
x=Symbol('x')
series=x
n=5
for i in range(2,n+1):
    series=series+(x**i)/i

pprint(series)

********************************************************************

expr=x*x+ x*y+ x*y+ y*y
res=expr.subs({x:1,y:2})

print(res)
#çıktı= 9.
**************************************

#subs() yöntemiyle bir sembolü diğer bir sembole göre ifade edebilir, değiştirebiliriz.

r=expr.subs({x:1-y})
print(r)
#çıktısı= y**2+ 2*y*(-y+1)+(-y+1)**2

*************************************************

x=Symbol('x')
series=x
n=5
x_value=10
for i in range(2,n+1):
    series=series+(x**i)/i
pprint(series)
series_value=series.subs({x:x_value})
print(series_value)
