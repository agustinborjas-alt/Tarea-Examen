# =============================================================================
# Ejercicio 9 - Clase EmpleadoComision
# Tarea-Examen Programacion
#
# EmpleadoComision hereda de Empleado (ejercicio 8) y agrega:
#   ventas_totales        : monto total de ventas del empleado
#   porcentaje_comision   : porcentaje que recibe sobre sus ventas
#
# Restriccion defensiva: el porcentaje no puede ser mayor al 50% del total
# de ventas, es decir, porcentaje_comision <= 0.50.
# =============================================================================

from datetime import date
from ejercicio8 import Empleado


class EmpleadoComision(Empleado):
    """Empleado asalariado con comision, hereda de Empleado."""

    # -------------------------------------------------------------------------
    # Inciso a) Constructor de EmpleadoComision.
    #   Recibe los mismos parametros que Empleado.con_datos() mas:
    #     - ventas_totales      : monto de ventas (debe ser >= 0)
    #     - porcentaje_comision : fraccion decimal (0.0 - 0.50)
    #                            NO puede ser mayor al 50% (0.50).
    #   Se reutiliza la logica del constructor con_datos() de Empleado
    #   mediante super() para no duplicar validaciones ya existentes.
    # -------------------------------------------------------------------------
    def __init__(
        self,
        nombre,
        apellidos,
        numero_seguridad_social,
        salario,
        ventas_totales,
        porcentaje_comision,
    ):
        """
        Lanza ValueError si ventas_totales < 0 o
        si porcentaje_comision esta fuera del rango (0, 0.50].
        """
        # Validaciones propias de EmpleadoComision (defensiva)
        if ventas_totales < 0:
            raise ValueError("Las ventas totales no pueden ser negativas.")
        if not (0 < porcentaje_comision <= 0.50):
            raise ValueError(
                f"El porcentaje de comision {porcentaje_comision:.0%} debe ser "
                "mayor a 0% y no mayor al 50% del total de ventas."
            )

        # Llama al constructor por omision de Empleado y luego aplica con_datos
        # a traves de los setters heredados para reutilizar sus validaciones.
        super().__init__()
        self.set_nombre(nombre)
        self.set_apellidos(apellidos)
        self.set_numero_seguridad_social(numero_seguridad_social)
        self.set_salario(salario)

        self.__ventas_totales = ventas_totales
        self.__porcentaje_comision = porcentaje_comision

    # -------------------------------------------------------------------------
    # Inciso b) Metodos GET y SET para los atributos propios de la clase.
    #   Los getters/setters de Empleado ya son heredados automaticamente.
    # -------------------------------------------------------------------------

    # --- ventas_totales ---
    def get_ventas_totales(self):
        return self.__ventas_totales

    def set_ventas_totales(self, ventas_totales):
        if ventas_totales < 0:
            raise ValueError("Las ventas totales no pueden ser negativas.")
        self.__ventas_totales = ventas_totales

    # --- porcentaje_comision ---
    def get_porcentaje_comision(self):
        return self.__porcentaje_comision

    def set_porcentaje_comision(self, porcentaje_comision):
        if not (0 < porcentaje_comision <= 0.50):
            raise ValueError(
                f"El porcentaje {porcentaje_comision:.0%} debe ser mayor a 0% "
                "y no mayor al 50%."
            )
        self.__porcentaje_comision = porcentaje_comision

    # -------------------------------------------------------------------------
    # Inciso c) Metodo para calcular el sueldo completo.
    #   Formula: sueldo_completo = salario + (ventas_totales * porcentaje_comision)
    # -------------------------------------------------------------------------
    def calcular_sueldo_completo(self):
        """Retorna el sueldo total: salario base + comision por ventas."""
        return self.get_salario() + (self.__ventas_totales * self.__porcentaje_comision)

    # -------------------------------------------------------------------------
    # Inciso d) Metodo para imprimir un EmpleadoComision como cadena de caracteres.
    #   Se extiende la representacion de Empleado con los datos de comision.
    # -------------------------------------------------------------------------
    def __str__(self):
        return (
            f"EmpleadoComision:\n"
            f"  Nombre              : {self.get_nombre()} {self.get_apellidos()}\n"
            f"  NSS                 : {self.get_numero_seguridad_social()}\n"
            f"  Fecha de nacimiento : "
            f"{self.get_fecha_nacimiento().strftime('%d/%m/%Y')}\n"
            f"  Edad                : {self.calcular_edad()} anios\n"
            f"  Salario base        : ${self.get_salario():,.2f}\n"
            f"  Ventas totales      : ${self.__ventas_totales:,.2f}\n"
            f"  Porcentaje comision : {self.__porcentaje_comision:.0%}\n"
            f"  Sueldo completo     : ${self.calcular_sueldo_completo():,.2f}"
        )


# =============================================================================
# Inciso e) Prueba de la clase EmpleadoComision.
#   Se muestra el uso del constructor, setters, calcular_sueldo_completo()
#   y __str__().
# =============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("  PRUEBA DEL EJERCICIO 9 - CLASE EMPLEADOCOMISION")
    print("=" * 60)

    # -- Creacion de un EmpleadoComision --
    print("\n[1] EmpleadoComision creado con constructor:")
    ec1 = EmpleadoComision(
        nombre="Maria",
        apellidos="Hernandez Torres",
        numero_seguridad_social="HETM920714GH4",
        salario=10000.0,
        ventas_totales=50000.0,
        porcentaje_comision=0.15,   # 15% de comision
    )
    ec1.set_fecha_nacimiento(date(1992, 7, 14))
    print(ec1)

    # -- Calculo explicito del sueldo completo --
    print(f"\n[2] Sueldo completo de {ec1.get_nombre()}: "
          f"${ec1.calcular_sueldo_completo():,.2f}")

    # -- Modificacion con setters --
    print("\n[3] Actualizando ventas y porcentaje con setters:")
    ec1.set_ventas_totales(80000.0)
    ec1.set_porcentaje_comision(0.20)   # 20%
    print(f"  Nuevas ventas     : ${ec1.get_ventas_totales():,.2f}")
    print(f"  Nuevo porcentaje  : {ec1.get_porcentaje_comision():.0%}")
    print(f"  Nuevo sueldo      : ${ec1.calcular_sueldo_completo():,.2f}")

    # -- Validacion defensiva: porcentaje mayor al 50% --
    print("\n[4] Prueba defensiva: porcentaje mayor al 50%")
    try:
        ec2 = EmpleadoComision("Juan", "Lopez", "LOJJ010101IJ5",
                               9000.0, 30000.0, 0.60)
    except ValueError as e:
        print(f"  Error capturado correctamente: {e}")

    # -- Validacion defensiva: ventas negativas --
    print("\n[5] Prueba defensiva: ventas totales negativas")
    try:
        ec3 = EmpleadoComision("Rosa", "Perez", "PERR030303KL6",
                               9000.0, -5000.0, 0.10)
    except ValueError as e:
        print(f"  Error capturado correctamente: {e}")

    print("\n" + "=" * 60)
