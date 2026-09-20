
from functools import reduce
from typing import List, Tuple, Dict, Any

# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario
#    con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.
def ejercicio_1_frecuencias_letras(texto: str) -> dict:
    texto = texto.lower()
    frec = {}
    for ch in texto:
        if ch == " ":
            continue
        if ch.isalpha():
            frec[ch] = frec.get(ch, 0) + 1
    return frec


# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
def ejercicio_2_doble_lista(nums: List[float]) -> List[float]:
    return list(map(lambda x: x * 2, nums))


# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros.
#    La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
def ejercicio_3_contienen(palabras: List[str], objetivo: str) -> List[str]:
    objetivo = objetivo.lower()
    return [p for p in palabras if objetivo in p.lower()]


# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
#    (se entiende como elemento a elemento: a - b)
def ejercicio_4_diferencia_listas(a: List[float], b: List[float]) -> List[float]:
    length = min(len(a), len(b))
    return list(map(lambda i: a[i] - b[i], range(length)))


# 5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5).
#    La función debe calcular la media y devolver una tupla (media, "aprobado"/"suspenso")
def ejercicio_5_media_estado(nums: List[float], nota_aprobado: float = 5.0) -> Tuple[float, str]:
    if not nums:
        return (0.0, "suspenso")
    media = sum(nums) / len(nums)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)


# 6. Escribe una función que calcule el factorial de un número de manera recursiva.
def ejercicio_6_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    if n in (0, 1):
        return 1
    return n * ejercicio_6_factorial(n - 1)


# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
def ejercicio_7_tuplas_a_strings(tuplas: List[Tuple[Any, ...]]) -> List[str]:
    return list(map(lambda t: ", ".join(map(str, t)), tuplas))


# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Manejo de excepciones.
def ejercicio_8_division_interactiva():
    try:
        a = input("Introduce el numerador: ")
        b = input("Introduce el denominador: ")
        a_num = float(a)
        b_num = float(b)
        resultado = a_num / b_num
    except ValueError:
        print("Error: uno de los valores no es numérico.")
        return None
    except ZeroDivisionError:
        print("Error: división por cero.")
        return None
    else:
        print("División realizada con éxito. Resultado:", resultado)
        return resultado


# 9. Escribe una función que tome una lista de nombres de mascotas y devuelva una nueva lista excluyendo
#    ciertas mascotas prohibidas en España. Usa filter()
def ejercicio_9_filtrar_mascotas(mascotas: List[str]) -> List[str]:
    prohibidas = {"mapache", "tigre", "serpiente pitón", "cocodrilo", "oso"}
    return list(filter(lambda m: m.lower() not in prohibidas, mascotas))


# 10. Escribe una función que reciba una lista de números y calcule su promedio.
#     Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
class ListaVaciaError(Exception):
    pass

def ejercicio_10_promedio(nums: List[float]) -> float:
    if not nums:
        raise ListaVaciaError("La lista está vacía; no se puede calcular el promedio.")
    return sum(nums) / len(nums)


# 11. Escribe un programa que pida al usuario que introduzca su edad. Manejo de excepciones
def ejercicio_11_edad_interactiva():
    try:
        edad_str = input("Introduce tu edad: ")
        edad = int(edad_str)
        if edad < 0 or edad > 120:
            raise ValueError("Edad fuera de rango")
    except ValueError:
        print("Entrada inválida: introduce un número entero entre 0 y 120.")
        return None
    else:
        print(f"Edad válida: {edad}")
        return edad


# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa map()
def ejercicio_12_longitudes(frase: str) -> List[int]:
    palabras = frase.split()
    return list(map(len, palabras))


# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas.
#     Las letras no pueden estar repetidas. Usa map() y filter()
def ejercicio_13_mayus_minus(chars: str) -> List[Tuple[str, str]]:
    unicas = sorted(set([c for c in chars if c.isalpha()]), key=str.lower)
    return list(map(lambda c: (c.upper(), c.lower()), unicas))


# 14. Crea una función que retorne las palabras de una lista de palabras que comiencen con una letra en específico. Usa filter()
def ejercicio_14_empiezan_por(palabras: List[str], letra: str) -> List[str]:
    letra = letra.lower()
    return list(filter(lambda p: p.lower().startswith(letra), palabras))


# 15. Crea una función lambda que sume 3 a cada número de una lista dada.
ejercicio_15_suma_3 = lambda nums: list(map(lambda x: x + 3, nums))


# 16. Escribe una función que tome una cadena de texto y un número entero n y devuelva una lista de todas las palabras que sean más largas que n. Usa filter()
def ejercicio_16_mas_largas(frase: str, n: int) -> List[str]:
    return list(filter(lambda w: len(w) > n, frase.split()))


# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Usa reduce()
def ejercicio_17_digitos_a_numero(digitos: List[int]) -> int:
    if not digitos:
        return 0
    return reduce(lambda acc, d: acc * 10 + int(d), digitos, 0)


# 18. Escribe un programa que cree una lista de diccionarios con info de estudiantes y use filter para extraer los estudiantes con calificación >= 90.
def ejercicio_18_filtrar_excelentes(estudiantes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return list(filter(lambda s: s.get("calificacion", 0) >= 90, estudiantes))


# 19. Crea una función lambda que filtre los números impares de una lista dada.
ejercicio_19_filtrar_impares = lambda nums: list(filter(lambda x: x % 2 != 0, nums))


# 20. Para una lista con elementos tipo int y str obtén una nueva lista sólo con los valores int. Usa filter()
def ejercicio_20_filtrar_enteros(items: List[Any]) -> List[int]:
    return list(filter(lambda x: isinstance(x, int), items))


# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda
ejercicio_21_cubo = lambda x: x ** 3


# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa reduce().
def ejercicio_22_producto_total(nums: List[float]) -> float:
    if not nums:
        return 0
    return reduce(lambda a, b: a * b, nums, 1)


# 23. Concatena una lista de palabras. Usa reduce().
def ejercicio_23_concatenar(palabras: List[str], separador: str = " ") -> str:
    if not palabras:
        return ""
    return reduce(lambda a, b: a + separador + b, palabras)


# 24. Calcula la diferencia total en los valores de una lista. Usa reduce().
#     (Se interpreta como sumatoria de diferencias consecutivas absolutas)
def ejercicio_24_diferencia_total(nums: List[float]) -> float:
    if len(nums) < 2:
        return 0.0
    diffs = [abs(nums[i] - nums[i - 1]) for i in range(1, len(nums))]
    return reduce(lambda a, b: a + b, diffs, 0.0)


# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.
def ejercicio_25_contar_caracteres(texto: str) -> int:
    return len(texto)


# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.
ejercicio_26_resto = lambda a, b: a % b


# 27. Crea una función que calcule el promedio de una lista de números.
def ejercicio_27_promedio(nums: List[float]) -> float:
    if not nums:
        return 0.0
    return sum(nums) / len(nums)


# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def ejercicio_28_primer_duplicado(items: List[Any]) -> Any:
    vistos = set()
    for x in items:
        if x in vistos:
            return x
        vistos.add(x)
    return None


# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con '#', excepto los últimos cuatro.
def ejercicio_29_enmascarar(valor: Any) -> str:
    s = str(valor)
    if len(s) <= 4:
        return s
    return "#" * (len(s) - 4) + s[-4:]


# 30. Crea una función que determine si dos palabras son anagramas.
def ejercicio_30_anagramas(a: str, b: str) -> bool:
    return sorted(a.replace(" ", "").lower()) == sorted(b.replace(" ", "").lower())


# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista.
#     Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
class NombreNoEncontradoError(Exception):
    pass

def ejercicio_31_buscar_nombre_interactivo():
    nombres = input("Introduce una lista de nombres separados por comas: ").split(",")
    nombres = [n.strip() for n in nombres if n.strip()]
    buscar = input("Introduce el nombre a buscar: ").strip()
    if buscar in nombres:
        print(f"{buscar} fue encontrado.")
        return True
    else:
        raise NombreNoEncontradoError(f"{buscar} no está en la lista.")


# 32. Crea una función que tome un nombre completo y una lista de empleados (diccionarios con 'nombre' y 'puesto'),
#     busque el nombre completo y devuelva el puesto si está, de lo contrario devuelve mensaje.
def ejercicio_32_buscar_empleado(nombre_completo: str, empleados: List[Dict[str, str]]) -> str:
    for e in empleados:
        if e.get("nombre", "").lower() == nombre_completo.lower():
            return e.get("puesto", "Puesto no especificado")
    return "La persona no trabaja aquí."


# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
ejercicio_33_sumar_correspondientes = lambda a, b: list(map(lambda i: a[i] + b[i], range(min(len(a), len(b)))))


# 34. Crea la clase Arbol con los métodos indicados.
class Arbol:
    def __init__(self):
        # tronco: longitud (int), ramas: lista de longitudes
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [r + 1 for r in self.ramas]

    def quitar_rama(self, posicion: int):
        # posicion en base 1 para el enunciado; si fuera 0-based, ajustar.
        idx = posicion - 1
        if 0 <= idx < len(self.ramas):
            self.ramas.pop(idx)
        else:
            raise IndexError("Posición de rama inválida")

    def info_arbol(self) -> Dict[str, Any]:
        return {"tronco": self.tronco, "num_ramas": len(self.ramas), "longitudes_ramas": list(self.ramas)}


# 35. Crea la clase UsuarioBanco con nombre, saldo y si tiene cuenta corriente. Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
class SaldoInsuficienteError(Exception):
    pass

class UsuarioBanco:
    def __init__(self, nombre: str, saldo: float, tiene_corriente: bool):
        self.nombre = nombre
        self.saldo = float(saldo)
        self.tiene_corriente = bool(tiene_corriente)

    def retirar_dinero(self, cantidad: float):
        if cantidad < 0:
            raise ValueError("Cantidad negativa")
        if self.saldo < cantidad:
            raise SaldoInsuficienteError("Saldo insuficiente para retirar")
        self.saldo -= cantidad

    def transferir_dinero(self, origen: 'UsuarioBanco', cantidad: float):
        if cantidad < 0:
            raise ValueError("Cantidad negativa")
        if origen.saldo < cantidad:
            raise SaldoInsuficienteError("Saldo insuficiente en el usuario origen")
        origen.saldo -= cantidad
        self.saldo += cantidad

    def agregar_dinero(self, cantidad: float):
        if cantidad < 0:
            raise ValueError("Cantidad negativa")
        self.saldo += cantidad


# 36. Caso de uso para UsuarioBanco (se implementa como función de demostración)
def ejercicio_36_demo_usuario_banco():
    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)
    # Agregar 20 unidades a Bob
    bob.agregar_dinero(20)
    # Transferir 80 desde Bob a Alicia (si Bob tiene saldo)
    try:
        alicia.transferir_dinero(bob, 80)  # nota: transferir_dinero definido como self recibe desde origen
    except SaldoInsuficienteError:
        # Si falla, intentamos la operación inversa para seguir el caso de uso original:
        try:
            bob.transferir_dinero(alicia, 80)
        except SaldoInsuficienteError:
            pass
    # Retirar 50 a Alicia
    try:
        alicia.retirar_dinero(50)
    except SaldoInsuficienteError:
        pass
    return {"Alicia": alicia.saldo, "Bob": bob.saldo}


# 37. Crea funciones para procesar texto: contar_palabras, reemplazar_palabras, eliminar_palabra y procesar_texto que las use.
def contar_palabras(texto: str) -> Dict[str, int]:
    palabras = [p.strip().lower() for p in texto.split() if p.strip()]
    frec = {}
    for p in palabras:
        frec[p] = frec.get(p, 0) + 1
    return frec

def reemplazar_palabras(texto: str, palabra_original: str, palabra_nueva: str) -> str:
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto: str, palabra: str) -> str:
    palabras = texto.split()
    return " ".join([p for p in palabras if p != palabra])

def procesar_texto(texto: str, opcion: str, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) < 2:
            raise ValueError("reemplazar requiere palabra_original y palabra_nueva")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) < 1:
            raise ValueError("eliminar requiere la palabra a eliminar")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida. Usa 'contar', 'reemplazar' o 'eliminar'.")


# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
def ejercicio_38_momento_del_dia(hora: int) -> str:
    # hora en formato 0-23
    if hora < 0 or hora > 23:
        raise ValueError("Hora fuera de rango")
    if 6 <= hora < 12:
        return "mañana"
    elif 12 <= hora < 20:
        return "tarde"
    else:
        return "noche"


# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
def ejercicio_39_calificacion_texto(nota: float) -> str:
    if nota < 0 or nota > 100:
        raise ValueError("Nota fuera de rango")
    if 0 <= nota <= 69:
        return "insuficiente"
    elif 70 <= nota <= 79:
        return "bien"
    elif 80 <= nota <= 89:
        return "muy bien"
    else:
        return "excelente"


# 40. Escribe una función que tome dos parámetros: figura (cadena) y datos (tupla) y calcule el área.
def ejercicio_40_area(figura: str, datos: Tuple[float, ...]) -> float:
    fig = figura.lower()
    if fig == "rectangulo":
        ancho, alto = datos
        return ancho * alto
    elif fig == "circulo":
        (radio,) = datos
        import math
        return math.pi * radio * radio
    elif fig == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    else:
        raise ValueError("Figura no soportada")


# 41. Programa que calcula el monto final de una compra aplicando un cupón si el usuario lo tiene.
def ejercicio_41_precio_final(precio_original: float, tiene_cupon: bool, valor_cupon: float = 0.0) -> float:
    if precio_original < 0:
        raise ValueError("Precio inválido")
    if tiene_cupon:
        if valor_cupon <= 0:
            raise ValueError("Valor de cupón inválido")
        precio_final = precio_original - valor_cupon
        return max(precio_final, 0.0)
    else:
        return precio_original


# -------------------------
# Bloque de pruebas rápidas (no interactivas) para verificar funciones principales.
# Ejecuta `python katas.py` para ver estas pruebas.
if __name__ == "__main__":
    print("Ejercicio 1:", ejercicio_1_frecuencias_letras("Hola Mundo"))
    print("Ejercicio 2:", ejercicio_2_doble_lista([1, 2, 3]))
    print("Ejercicio 3:", ejercicio_3_contienen(["manzana", "banana", "Ananá", "pera"], "ana"))
    print("Ejercicio 4:", ejercicio_4_diferencia_listas([10, 20, 30], [1, 2, 3]))
    print("Ejercicio 5:", ejercicio_5_media_estado([6, 7, 4]))
    print("Ejercicio 6:", ejercicio_6_factorial(5))
    print("Ejercicio 7:", ejercicio_7_tuplas_a_strings([(1, 2), ("a", "b")]))
    # Ejercicio 8 es interactivo; descomentarlo para usar:
    # ejercicio_8_division_interactiva()
    print("Ejercicio 9:", ejercicio_9_filtrar_mascotas(["Perro", "Mapache", "Gato", "Oso"]))
    try:
        print("Ejercicio 10:", ejercicio_10_promedio([1, 2, 3]))
    except ListaVaciaError as e:
        print("Ejercicio 10 error:", e)
    # Ejercicio 11 es interactivo; descomentarlo para usar:
    # ejercicio_11_edad_interactiva()
    print("Ejercicio 12:", ejercicio_12_longitudes("Esto es una prueba"))
    print("Ejercicio 13:", ejercicio_13_mayus_minus("aAbBccD"))
    print("Ejercicio 14:", ejercicio_14_empiezan_por(["Ana", "Pedro", "Alberto"], "A"))
    print("Ejercicio 15:", ejercicio_15_suma_3([1, 2, 3]))
    print("Ejercicio 16:", ejercicio_16_mas_largas("hola que tal esto es una prueba", 3))
    print("Ejercicio 17:", ejercicio_17_digitos_a_numero([5, 7, 2]))
    estudiantes = [{"nombre": "Ana", "edad": 20, "calificacion": 95}, {"nombre": "Luis", "edad": 22, "calificacion": 85}]
    print("Ejercicio 18:", ejercicio_18_filtrar_excelentes(estudiantes))
    print("Ejercicio 19:", ejercicio_19_filtrar_impares([1, 2, 3, 4, 5]))
    print("Ejercicio 20:", ejercicio_20_filtrar_enteros([1, "a", 2, "3", 4]))
    print("Ejercicio 21:", ejercicio_21_cubo(3))
    print("Ejercicio 22:", ejercicio_22_producto_total([2, 3, 4]))
    print("Ejercicio 23:", ejercicio_23_concatenar(["hola", "mundo"]))
    print("Ejercicio 24:", ejercicio_24_diferencia_total([10, 7, 3, 8]))
    print("Ejercicio 25:", ejercicio_25_contar_caracteres("hola"))
    print("Ejercicio 26:", ejercicio_26_resto(10, 3))
    print("Ejercicio 27:", ejercicio_27_promedio([10, 20, 30]))
    print("Ejercicio 28:", ejercicio_28_primer_duplicado([1, 2, 3, 2, 5]))
    print("Ejercicio 29:", ejercicio_29_enmascarar("1234567890"))
    print("Ejercicio 30:", ejercicio_30_anagramas("Roma", "Amor"))
    # Ejercicio 31 es interactivo; descomentarlo para usar:
    # ejercicio_31_buscar_nombre_interactivo()
    empleados = [{"nombre": "Juan Perez", "puesto": "Developer"}, {"nombre": "Ana Gomez", "puesto": "Manager"}]
    print("Ejercicio 32:", ejercicio_32_buscar_empleado("Ana Gomez", empleados))
    print("Ejercicio 33:", ejercicio_33_sumar_correspondientes([1,2,3],[4,5,6]))
    # Ejercicio 34: demo de uso
    arbol = Arbol()
    arbol.crecer_tronco()
    arbol.nueva_rama()
    arbol.crecer_ramas()
    arbol.nueva_rama()
    arbol.nueva_rama()
    try:
        arbol.quitar_rama(2)
    except IndexError:
        pass
    print("Ejercicio 34:", arbol.info_arbol())
    # Ejercicio 35/36 demo
    print("Ejercicio 36 (demo banco):", ejercicio_36_demo_usuario_banco())
    # Ejercicio 37 procesar texto
    texto_demo = "hola hola mundo prueba hola"
    print("Ejercicio 37 contar:", procesar_texto(texto_demo, "contar"))
    print("Ejercicio 37 reemplazar:", procesar_texto(texto_demo, "reemplazar", "hola", "buenas"))
    print("Ejercicio 37 eliminar:", procesar_texto(texto_demo, "eliminar", "prueba"))
    print("Ejercicio 38:", ejercicio_38_momento_del_dia(22))
    print("Ejercicio 39:", ejercicio_39_calificacion_texto(85))
    print("Ejercicio 40 rectangulo:", ejercicio_40_area("rectangulo", (3, 4)))
    print("Ejercicio 40 circulo:", round(ejercicio_40_area("circulo", (2,)), 2))
    print("Ejercicio 41:", ejercicio_41_precio_final(100, True, 15))