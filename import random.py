import random
def crearEntrenador(tupla):
    nombreEntrenador = input("Ingrese el nombre del entrenador: ").strip()
    nombrePokemon = input("Ingrese el nombre del pokemon: ").strip()

    ataque = random.randint(150, 250)
    vida = random.randint(500, 900)

    tupla.append((nombreEntrenador, nombrePokemon, ataque, vida))

    print(f"Entrenador '{nombreEntrenador}' con pokemon '{nombrePokemon}' "
          f"creado correctamente. (Ataque: {ataque}, Vida: {vida})")


def listaEntrenador(tupla):
    n = len(tupla)

    if n == 0:
        print(" No hay entrenadores registrados todavia")
        return

    for i in range(n):
        for j in range(0, n - i - 1):
            if tupla[j][2] > tupla[j + 1][2]:
                tupla[j], tupla[j + 1] = tupla[j + 1], tupla[j]

    print("\n" + "=" * 70)
    print(f"{'#':<4}{'Entrenador':<15}{'Pokemon':<15}{'Ataque':<10}{'Vida':<10}")
    print("=" * 70)
    for idx, (entrenador, pokemon, ataque, vida) in enumerate(tupla, start=1):
        print(f"{idx:<4}{entrenador:<15}{pokemon:<15}{ataque:<10}{vida:<10}")
    print("=" * 70 + "\n")


def borraPorPokemon(tupla):
    n = len(tupla)

    if n == 0:
        print("  No hay entrenadores registrados todavia.")
        return

    try:
        vidaBuscada = int(input("Ingrese el valor de vida a buscar: "))
    except ValueError:
        print(" Debe ingresar un numero entero valido.")
        return

    for i in range(n):
        indiceMenor = i
        for j in range(i + 1, n):
            if tupla[j][3] < tupla[indiceMenor][3]:
                indiceMenor = j
        tupla[i], tupla[indiceMenor] = tupla[indiceMenor], tupla[i]

    izquierda = 0
    derecha = n - 1
    posicionEncontrada = -1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        vidaMedio = tupla[medio][3]

        if vidaMedio == vidaBuscada:
            posicionEncontrada = medio
            break
        elif vidaMedio < vidaBuscada:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    if posicionEncontrada != -1:
        eliminado = tupla.pop(posicionEncontrada)
        print(f"  Se elimino al entrenador '{eliminado[0]}' y su pokemon "
              f"'{eliminado[1]}' (Vida: {eliminado[3]}).")
    else:
        print(f" No se encontro ningun pokemon con vida = {vidaBuscada}.")


def peleaPokemon(lista):
    listaEntrenador(lista)

    if len(lista) < 2:
        print(" Se necesitan al menos 2 pokemones para pelear.")
        return

    try:
        num1 = int(input("Ingrese el numero del primer pokemon: "))
        num2 = int(input("Ingrese el numero del segundo pokemon: "))
    except ValueError:
        print("Debe ingresar numeros enteros validos.")
        return

    if num1 == num2 or not (1 <= num1 <= len(lista)) or not (1 <= num2 <= len(lista)):
        print("Numeros invalidos. Deben ser distintos y estar en el rango mostrado")
        return

    idx1 = num1 - 1
    idx2 = num2 - 1

    entrenador1, pokemon1, ataque1, vida1 = lista[idx1]
    entrenador2, pokemon2, ataque2, vida2 = lista[idx2]

    golpe1 = ataque1 * random.randint(0, 5)
    golpe2 = ataque2 * random.randint(0, 5)

    vidaFinal1 = vida1 - golpe2
    vidaFinal2 = vida2 - golpe1

    print(" ¡Comienza la pelea! ")
    print(f"{pokemon1} (de {entrenador1}) ataca con {golpe1} de daño.")
    print(f"{pokemon2} (de {entrenador2}) ataca con {golpe2} de daño.")
    print(f"Vida restante de {pokemon1}: {vidaFinal1}")
    print(f"Vida restante de {pokemon2}: {vidaFinal2}\n")

    indiceMayor = max(idx1, idx2)
    indiceMenor = min(idx1, idx2)

    if vidaFinal1 <= 0 and vidaFinal2 <= 0:
        print(f" Ambos pokemones quedaron sin vida. "
              f"{entrenador1} y {entrenador2} pierden a sus pokemones.")
        lista.pop(indiceMayor)
        lista.pop(indiceMenor)

    elif vidaFinal1 == vidaFinal2:
        print(f" ¡Empate! Ambos entrenadores pierden: {entrenador1} y {entrenador2}.")
        lista.pop(indiceMayor)
        lista.pop(indiceMenor)

    elif vidaFinal1 > vidaFinal2:
        print(f"¡Gana {pokemon1} del entrenador {entrenador1} "
              f"con {vidaFinal1} de vida restante!")
        lista[idx1] = (entrenador1, pokemon1, ataque1, vidaFinal1)
        lista.pop(idx2)

    else:
        print(f" ¡Gana {pokemon2} del entrenador {entrenador2} "
              f"con {vidaFinal2} de vida restante!")
        lista[idx2] = (entrenador2, pokemon2, ataque2, vidaFinal2)
        lista.pop(idx1)


def mostrarMenu():
    print("=" * 40)
    print("         JUEGO DE POKEMON ")
    print("=" * 40)
    print("1. Crear Entrenador")
    print("2. Listar Entrenadores")
    print("3. Borrar por Pokemon")
    print("4. Pelea Pokemon")
    print("5. Fin")
    print("=" * 40)


def main():
    entrenadores = []

    while True:
        mostrarMenu()
        opcion = input("Seleccione una opcion (1-5): ").strip()

        if opcion == "1":
            crearEntrenador(entrenadores)
        elif opcion == "2":
            listaEntrenador(entrenadores)
        elif opcion == "3":
            borraPorPokemon(entrenadores)
        elif opcion == "4":
            peleaPokemon(entrenadores)
        elif opcion == "5":
            print("¡Gracias por jugar! Hasta pronto. ")
            break
        else:
            print(" Opcion invalida. Intente de nuevo.")


if __name__ == "__main__":
    main()