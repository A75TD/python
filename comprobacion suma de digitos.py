import random


def generar_numero_aleatorio():
    return random.randint(10000, 99999)


def obtener_digitos(numero):
    digito_1 = numero // 10000
    digito_2 = (numero % 10000) // 1000
    digito_3 = (numero % 1000) // 100
    digito_4 = (numero % 100) // 10
    digito_5 = numero % 10
    return digito_1, digito_2, digito_3, digito_4, digito_5


def calcular_sumas(digitos):
    suma_primeros_tres = sum(digitos[:3])
    suma_ultimos_dos = sum(digitos[3:])
    return suma_primeros_tres, suma_ultimos_dos


def comprobar_condicion(numero_aleatorio):
    digitos = obtener_digitos(numero_aleatorio)
    suma_primeros_tres, suma_ultimos_dos = calcular_sumas(digitos)

    if suma_primeros_tres == suma_ultimos_dos:
        print(f"El número aleatorio {numero_aleatorio} cumple con la condición.")
    else:
        print(f"El número aleatorio {numero_aleatorio} no cumple con la condición.")


def continuar():
    respuesta = input(
        "¿Desea verificar otra vez? (Ingrese 's' para sí, 'n' para no): "
    ).lower()
    return respuesta == "s"


if __name__ == "__main__":
    while True:
        try:
            numero_aleatorio = generar_numero_aleatorio()
            comprobar_condicion(numero_aleatorio)
        except ValueError:
            print("Error: Se produjo un error al intentar generar un número aleatorio.")
        except ZeroDivisionError:
            print("Error: División por cero.")
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")

        if not continuar():
            break
