from sympy import Symbol,pprint
import sympy as sym
import sympy.plotting as syp
import matplotlib.pyplot as plt
%matplotlib inline


sigma = Symbol('sigma')
mu = Symbol('mu')
x = Symbol('x')


part_1 = 1/(sym.sqrt(2*sym.pi*sigma**2))
part_2 = sym.exp(-1*((x-mu)**2)/(2*sigma**2))
%matplotlib notebook
my_gauss_function = part_1*part_2

#gunluk hayattaki sembollere yakın ifade etmek istersek pprint kullanıyoruz

#pprint(part_1)
#pprint(part_2)
#pprint(my_gaussfunction)

gauss_function = 1/(sym.sqrt(2*sym.pi*sigma))
gauss_function.subs({mu:0,sigma:1})
#print(gauss_function)

syp.plot(my_gauss_function.subs({mu:1,sigma:3}),(x,-10,10),title="gauss distribution")


#FOR DONGUSUYLE YAPIMI
x_values,y_values = [],[]

for value in range(-50,50):
    y=my_gauss_function.subs({mu:0,sigma:10,x:value}).evalf()
    y_values.append(y)
    x_values.append(value)
    #print(value,y)

plt.plot(x_values,y_values)
plt.show()
