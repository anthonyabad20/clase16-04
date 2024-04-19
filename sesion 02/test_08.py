"""
crear 3 variables: nombre, edad, pais de residencia y distrito

requisitos
- nombre: string, edad: int, pais de rsidencia: string, distrito: string
- concatenar estos datos e indicar una pracion como la siguiente
Jose tiene X años, es del distrito de "destrito y veene de "pais de residencia"
- Obtener el modulo de su edad al usarlo con el número 5, mostrar el modulo

"""
nombre = "anthony"
edad = "20"
distrito = "Ayabaca"
Pais = "Perú"

print("{} tiene {} años, es del distrito de {} y viene de {}".format(nombre, edad, distrito, Pais))
modulo = int(edad) % 5
print("el modulo de su la edad dividido entre 5 es: {}".format(modulo))


