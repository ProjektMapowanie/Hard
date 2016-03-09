import matplotlib.pyplot as plt
import numpy as n
import tabulate as t

x = 0.5
h1 = n.arange(20)+0.
piataki = 5**h1
kroki = 0.4/piataki
#pochodna = n.sin(h1)

pochodna = (n.sin(x + kroki) - n.sin(x - kroki))/(2*kroki)



prawdziwaPochodna = n.cos(0.5)
bladBezw = n.abs((pochodna - prawdziwaPochodna))
table = [h1, kroki, pochodna, bladBezw]
print t.tabulate(table)


plt.figure()
plt.plot(h1,bladBezw,'o')
plt.xscale('log')
plt.yscale('log')


plt.show()
k = n.min(bladBezw)
indexx = n.where(bladBezw==k)[0][0]


print "Wartosc indeksu: " , indexx
