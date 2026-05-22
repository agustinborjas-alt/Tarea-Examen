# =============================================================================
# Ejercicio 10 - Administrador de Empleados (Menu interactivo)
# Tarea-Examen Programacion
#
# Utiliza las clases Empleado (ejercicio 8) y EmpleadoComision (ejercicio 9).
# Administra una lista de empleados con las siguientes opciones de menu:
#   a) Agregar cualquier tipo de empleado
#   b) Eliminar un empleado por nombre
#   c) Mostrar todos los empleados
#   d) Buscar un empleado por nombre
#
# Se aplica programacion a la defensiva en todas las entradas del usuario.
# =============================================================================

from datetime import date
from ejercicio8 import Empleado
from ejercicio9 import EmpleadoComision


# -----------------------------------------------------------------------------
# Funciones auxiliares para lectura defensiva de datos del usuario
# -----------------------------------------------------------------------------

def leer_texto(mensaje):
    """Lee una cadena no vacia desde la consola."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("  [!] El campo no puede estar vacio. Intente de nuevo.")


def leer_flotante(mensaje, minimo=None, maximo=None):
    """
    Lee un numero flotante desde la consola.
    Valida opcionalmente un rango [minimo, maximo].
    """
    while True:
        try:
            valor = float(input(mensaje).strip())
            if minimo is not None and valor < minimo:
                print(f"  [!] El valor debe ser >= {minimo}. Intente de nuevo.")
                continue
            if maximo is not None and valor > maximo:
                print(f"  [!] El valor debe ser <= {maximo}. Intente de nuevo.")
                continue
            return valor
        except ValueError:
            print("  [!] Entrada invalida. Ingrese un numero valido.")


def leer_fecha(mensaje):
    """
    Lee una fecha en formato DD/MM/AAAA desde la consola.
    Valida que la fecha no sea futura.
    """
    while True:
        entrada = input(mensaje).strip()
        try:
            fecha = date(
                int(entrada[6:10]),
                int(entrada[3:5]),
                int(entrada[0:2]),
            )
            if fecha > date.today():
                print("  [!] La fecha no puede ser futura. Intente de nuevo.")
                continue
            return fecha
        except (ValueError, IndexError):
            print("  [!] Formato invalido. Use DD/MM/AAAA.")


def leer_porcentaje(mensaje):
    """
    Lee el porcentaje de comision como valor decimal (0.01 - 0.50).
    El usuario puede ingresarlo como porcentaje entero (ej. 15 = 15%) o
    como decimal (ej. 0.15). Se normaliza internamente a decimal.
    """
    while True:
        try:
            valor = float(input(mensaje).strip())
            # Si el usuario ingresa > 1, se asume que es porcentaje entero
            if valor > 1:
                valor = valor / 100
            if not (0 < valor <= 0.50):
                print("  [!] El porcentaje debe ser mayor a 0% y maximo 50%.")
                continue
            return valor
        except ValueError:
            print("  [!] Entrada invalida. Ingrese un numero.")


# -----------------------------------------------------------------------------
# Inciso a) Agregar un empleado (Empleado o EmpleadoComision) a la lista.
# -----------------------------------------------------------------------------

def agregar_empleado(lista):
    """Solicita el tipo y los datos del empleado y lo agrega a la lista."""
    print("\n  Tipo de empleado:")
    print("    1. Empleado")
    print("    2. EmpleadoComision")

    opcion = input("  Seleccione (1/2): ").strip()

    if opcion not in ("1", "2"):
        print("  [!] Opcion invalida. No se agrego ningun empleado.")
        return

    # Datos comunes a ambos tipos
    nombre = leer_texto("  Nombre              : ")
    apellidos = leer_texto("  Apellidos           : ")
    nss = leer_texto("  NSS                 : ")
    salario = leer_flotante(
        "  Salario ($)         : ", minimo=1000.0
    )
    fecha = leer_fecha("  Fecha nacimiento    : (DD/MM/AAAA) ")

    if opcion == "1":
        # -- Crear Empleado --
        try:
            emp = Empleado.con_datos(nombre, apellidos, nss, salario)
            emp.set_fecha_nacimiento(fecha)
            lista.append(emp)
            print(f"\n  [OK] Empleado '{nombre} {apellidos}' agregado.")
        except ValueError as e:
            print(f"  [!] Error al crear empleado: {e}")

    else:
        # -- Crear EmpleadoComision --
        ventas = leer_flotante("  Ventas totales ($)  : ", minimo=0.0)
        porcentaje = leer_porcentaje(
            "  Porcentaje comision : (ej. 15 para 15%, max 50%) "
        )
        try:
            emp = EmpleadoComision(nombre, apellidos, nss, salario, ventas, porcentaje)
            emp.set_fecha_nacimiento(fecha)
            lista.append(emp)
            print(f"\n  [OK] EmpleadoComision '{nombre} {apellidos}' agregado.")
        except ValueError as e:
            print(f"  [!] Error al crear empleado: {e}")


# -----------------------------------------------------------------------------
# Inciso b) Eliminar un empleado de la lista por nombre.
#   Se elimina el primero que coincida (busqueda insensible a mayusculas).
# -----------------------------------------------------------------------------

def eliminar_empleado(lista):
    """Elimina de la lista el primer empleado cuyo nombre coincida."""
    if not lista:
        print("\n  [!] La lista de empleados esta vacia.")
        return

    nombre_buscado = leer_texto("  Nombre a eliminar: ").lower()

    for i, emp in enumerate(lista):
        if emp.get_nombre().lower() == nombre_buscado:
            eliminado = lista.pop(i)
            print(
                f"\n  [OK] Se elimino a '{eliminado.get_nombre()} "
                f"{eliminado.get_apellidos()}' de la lista."
            )
            return

    print(f"\n  [!] No se encontro ningun empleado con nombre '{nombre_buscado}'.")


# -----------------------------------------------------------------------------
# Inciso c) Mostrar todos los empleados registrados en la lista.
# -----------------------------------------------------------------------------

def mostrar_empleados(lista):
    """Imprime todos los empleados de la lista."""
    if not lista:
        print("\n  [!] La lista de empleados esta vacia.")
        return

    print(f"\n  Total de empleados: {len(lista)}")
    print("  " + "-" * 50)
    for i, emp in enumerate(lista, start=1):
        print(f"\n  [{i}] {emp}")
        print("  " + "-" * 50)


# -----------------------------------------------------------------------------
# Inciso d) Buscar un empleado por nombre.
#   Muestra todos los empleados que coincidan con el nombre ingresado.
# -----------------------------------------------------------------------------

def buscar_empleado(lista):
    """Busca y muestra empleados cuyo nombre coincida con la busqueda."""
    if not lista:
        print("\n  [!] La lista de empleados esta vacia.")
        return

    nombre_buscado = leer_texto("  Nombre a buscar: ").lower()

    encontrados = [
        emp for emp in lista
        if emp.get_nombre().lower() == nombre_buscado
    ]

    if not encontrados:
        print(f"\n  [!] No se encontro ningun empleado con nombre '{nombre_buscado}'.")
        return

    print(f"\n  Se encontraron {len(encontrados)} resultado(s):")
    print("  " + "-" * 50)
    for emp in encontrados:
        print(f"\n  {emp}")
        print("  " + "-" * 50)


# -----------------------------------------------------------------------------
# Menu principal del programa.
# -----------------------------------------------------------------------------

def mostrar_menu():
    """Imprime las opciones del menu."""
    print("\n" + "=" * 50)
    print("  ADMINISTRADOR DE EMPLEADOS")
    print("=" * 50)
    print("  a) Agregar empleado")
    print("  b) Eliminar empleado por nombre")
    print("  c) Mostrar todos los empleados")
    print("  d) Buscar empleado por nombre")
    print("  s) Salir")
    print("=" * 50)


def main():
    """Funcion principal: ejecuta el menu en bucle hasta que el usuario salga."""
    lista_empleados = []

    while True:
        mostrar_menu()
        opcion = input("  Seleccione una opcion: ").strip().lower()

        if opcion == "a":
            agregar_empleado(lista_empleados)
        elif opcion == "b":
            eliminar_empleado(lista_empleados)
        elif opcion == "c":
            mostrar_empleados(lista_empleados)
        elif opcion == "d":
            buscar_empleado(lista_empleados)
        elif opcion == "s":
            print("\n  Hasta luego.\n")
            break
        else:
            print("\n  [!] Opcion no reconocida. Intente de nuevo.")


if __name__ == "__main__":
    main()
