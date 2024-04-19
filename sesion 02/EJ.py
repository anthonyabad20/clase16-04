



list_1 = []
list_2 = []

list_1.append("anthony")
list_1.append(20)
list_1.append("ing de minas")

list_2.append("pedro")
list_2.append(25)
list_2.append("ing electronica")
suma_listas = list_1 + list_2
print("El resultado de la suma de lista es: ", suma_listas)

suma_listas.reverse()
print("Los valores de mi nueva lista son: {} ".format(suma_listas))

suma_listas.remove(20)
suma_listas.remove(25)

print("la lista actualizada es {}".format(suma_listas))



