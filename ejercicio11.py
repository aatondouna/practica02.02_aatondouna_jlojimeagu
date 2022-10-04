print('Cuanto dinero desea ingresar')
dinero = float(input())
ganancia_ano1 = dinero + dinero*0.04
redondeo1 = round(ganancia_ano1, 2)
print('Este primer ano tienes', redondeo1, '€')
ganancia_ano2 = ganancia_ano1 + ganancia_ano1*0.04
redondeo2 = round(ganancia_ano2, 2)
print('Este segundo ano tienes', redondeo2, '€')
ganancia_ano3 = ganancia_ano2 + ganancia_ano2*0.04
redondeo3 = round(ganancia_ano3, 2)
print('Este tercer ano tienes', redondeo3, '€')