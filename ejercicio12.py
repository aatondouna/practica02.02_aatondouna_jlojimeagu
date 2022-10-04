pan = 3.49
descuento = 0.6
n = int(input('numero de panes del dia'))
panes_dia = pan*n
print(int(input("cuantos de los panes son de otro dia")))
panes_otro_dia = pan*descuento
print("cuanto se vendio de los panes de otro dia", panes_otro_dia)
print("cuanto es el dinero de los panes vendidos hoy que son del dia", panes_dia)
print('total', panes_dia+panes_otro_dia)