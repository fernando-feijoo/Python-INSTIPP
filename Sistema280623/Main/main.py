# print("Ingresse el nombre:")
# nombre = input()
# print(f"Ingrese el apellido, {nombre}:")
# apellido = input()
# print(f"Un placer, {nombre} {apellido}")

# numUno = int(input("Ingrese un número:"))
# if numUno == 2:
#    numDos = int(input("Ingrese un número:"))
#    print(f"El reesultado de la resta es: {numDos - numUno}")
# else:
#    print("El número no es 2.")

# /*----------------------------------------------------*/

# bucle = "SI"
#
# while bucle == "SI":
#     num = int(input("Ingrese un número:"))
#     if num % 2 == 0:
#         print("El número es par.")
#     else:
#         print("El número es impar.")
#
#     bucle = str(input("Desea continuar SI/NO:"))

# /*----------------------------------------------------*/

# for i in range(10):
#     print(f"El número es {1}")

# /*----------------------------------------------------*/

# num = int(input("Ingrese el número: "))
#
# for i in range(13):
#     print(f"{num} x {i} = {num * i} ")

# /*----------------------------------------------------*/

# num = int(input("Ingrese un número: "))
#
# while num < 5:
#    print("Hola")
#    num = num + 1
# print("Gracias")

# /*----------------------------------------------------*/

# op = 0
#
# while op != 5:
#     print("|******************|")
#     print("| [1] Sumar        |")
#     print("| [2] Restar       |")
#     print("| [3] Multiplicar  |")
#     print("| [4] Dividir      |")
#     print("| [5] Salir        |")
#     print("|******************|")
#
#     op = int(input("Ingrese la opción: "))
#
#     if (op > 0) and (op < 5):
#         numUno = float(input("Ingrese el primer número: "))
#         numDos = float(input("Ingrese el segundo número: "))
#
#     if op == 1:
#         print(f"El resultado de la suma es: {numUno + numDos:.0f}")
#     elif op == 2:
#         print(f"El resultado de la resta es: {numUno - numDos:.0f}")
#     elif op == 3:
#         print(f"El resultado de la multiplicación es: {numUno * numDos:.0f}")
#     elif op == 4:
#         print(f"El resultado de la división es: {numUno / numDos:.2f}")
#     elif op == 5:
#         print("Gracias por usar el sistema.")
#     else:
#         print("El número ingresado no es correcto.")

# /*----------------------------------------------------*/

# lista = ['Juan', 'Pedro', 'Luis', 'Carmen']
# # print(lista[0])
# # print(lista[1])
# # print(lista[3])
#
# # For que recorre los elementos de esa lista.
# for datos in lista:
#     print(datos)
#
# numeros = []
# numeros.append(9)
# numeros.append(28)
# numeros.append(58)
# numeros.append(30)
# numeros.pop(2)
# for datos in numeros:
#     print(datos)
#
# nuevaLista = [1, 2, 3, 4, 5]
#
# print(numeros + nuevaLista)

# /*----------------------------------------------------*/

# # La empresa Suavito frabricante de telas requiere, almacenar los registros de su producción de telas a demás de calcular el costo de producción
# # que se ocupo en dicho lote. Los datos a almacenar y calcular son codigo, color, tipo de tela, metraje, costo x metro, duracion de la produccion.
# # Presentar el tipo de tela, las horas, el metraje, el costo y el valor total.
#
# registros = []
#
# while True:
#     print("|====================|\n"
#           "|  [1]  Ingreso      |\n"
#           "|  [2]  Ver lista    |\n"
#           "|  [3]  Salir        |\n"
#           "|====================|\n")
#
#     op = int(input("Ingrese acción: "))
#
#     if op == 1:
#         codigo = input("Ingrese el código de la tela: ")
#         color = input("Ingrese el color de la tela: ")
#         tipo = input("Ingrese el tipo de tela: ")
#         metraje = float(input("Ingrese el metraje de la tela: "))
#         costo_metro = float(input("Ingrese el costo por metro de la tela: "))
#         duracion = float(input("Ingrese la duración de la producción: "))
#
#         registro = [codigo, color, tipo, metraje, costo_metro, duracion]
#         registros.append(registro)
#
#         print("\n\n¡Registro almacenado exitosamente!\n\n")
#
#     elif op == 2:
#         print("|========================================================|")
#         print("|   Tipo de Tela   |   Horas   |   Metraje   |   Costo   |")
#         print("|========================================================|")
#
#         total_costo = 0
#
#         for registro in registros:
#             codigo, color, tipo, metraje, costo_metro, duracion = registro
#             costo = costo_metro * metraje
#
#             total_costo += costo
#
#             print(f"|  {tipo:15} |  {duracion:8.2f} |  {metraje:10.2f} |  {costo:8.2f} |")
#
#         print("|========================================================|")
#         print(f"Valor total de la producción: {total_costo:.2f}\n\n")
#     elif op == 3:
#         print("¡Hasta luego!")
#         break
#     else:
#         print("Opción inválida. Por favor, seleccione una opción válida.\n")

# /*----------------------------------------------------*/