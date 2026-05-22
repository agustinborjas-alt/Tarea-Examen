# =============================================================================
# Ejercicio 8 - Clase Empleado
# Tarea-Examen Programacion
#
# Se modela a un Empleado con los atributos:
#   nombre, apellidos, numero_seguridad_social, fecha_nacimiento, salario
#
# Se aplica programacion a la defensiva en constructores y setters.
# =============================================================================

from datetime import date


class Empleado:
    """Modela a un empleado de una empresa."""

    # -------------------------------------------------------------------------
    # Inciso a) Constructor por omision.
    #   - salario por defecto: $8,000.0
    #   - fecha de nacimiento por defecto: 19 de noviembre de 1990
    #   - El resto de atributos se inicializan como cadenas vacias.
    # -------------------------------------------------------------------------
    def __init__(self):
        self.__nombre = ""
        self.__apellidos = ""
        self.__numero_seguridad_social = ""
        self.__fecha_nacimiento = date(1990, 11, 19)
        self.__salario = 8000.0

    # -------------------------------------------------------------------------
    # Inciso b) Constructor con parametros.
    #   Recibe: nombre, apellidos, numero_seguridad_social, salario.
    #   Restriccion defensiva: el salario no puede ser menor a $1,000.0.
    #   La fecha de nacimiento se conserva con el valor por omision (19/11/1990)
    #   ya que el enunciado no la incluye como parametro de este constructor.
    # -------------------------------------------------------------------------
    @classmethod
    def con_datos(cls, nombre, apellidos, numero_seguridad_social, salario):
        """
        Construye un Empleado con datos especificos.
        Lanza ValueError si el salario es menor a $1,000.0.
        """
        if not nombre or not apellidos:
            raise ValueError("El nombre y los apellidos no pueden estar vacios.")
        if not numero_seguridad_social:
            raise ValueError("El numero de seguridad social no puede estar vacio.")
        if salario < 1000.0:
            raise ValueError(
                f"El salario ${salario:,.1f} no puede ser menor a $1,000.0."
            )

        emp = cls()                               # usa constructor por omision
        emp.__nombre = nombre
        emp.__apellidos = apellidos
        emp.__numero_seguridad_social = numero_seguridad_social
        emp.__salario = salario
        # fecha_nacimiento queda con el valor por defecto (19/11/1990)
        return emp

    # -------------------------------------------------------------------------
    # Inciso c) Metodos GET y SET para cada atributo.
    #   Se valida en cada setter siguiendo programacion a la defensiva.
    # -------------------------------------------------------------------------

    # --- nombre ---
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        if not nombre:
            raise ValueError("El nombre no puede estar vacio.")
        self.__nombre = nombre

    # --- apellidos ---
    def get_apellidos(self):
        return self.__apellidos

    def set_apellidos(self, apellidos):
        if not apellidos:
            raise ValueError("Los apellidos no pueden estar vacios.")
        self.__apellidos = apellidos

    # --- numero_seguridad_social ---
    def get_numero_seguridad_social(self):
        return self.__numero_seguridad_social

    def set_numero_seguridad_social(self, nss):
        if not nss:
            raise ValueError("El numero de seguridad social no puede estar vacio.")
        self.__numero_seguridad_social = nss

    # --- fecha_nacimiento ---
    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento

    def set_fecha_nacimiento(self, fecha):
        if not isinstance(fecha, date):
            raise TypeError("La fecha de nacimiento debe ser un objeto date.")
        if fecha > date.today():
            raise ValueError("La fecha de nacimiento no puede ser futura.")
        self.__fecha_nacimiento = fecha

    # --- salario ---
    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        if salario < 1000.0:
            raise ValueError(
                f"El salario ${salario:,.1f} no puede ser menor a $1,000.0."
            )
        self.__salario = salario

    # -------------------------------------------------------------------------
    # Inciso d) Metodo para calcular la edad del Empleado.
    #   Se calcula en base a la fecha actual usando date.today().
    # -------------------------------------------------------------------------
    def calcular_edad(self):
        """Retorna la edad actual del empleado en anos completos."""
        hoy = date.today()
        edad = hoy.year - self.__fecha_nacimiento.year
        # Se resta 1 si aun no ha llegado el cumpleanos este ano
        if (hoy.month, hoy.day) < (
            self.__fecha_nacimiento.month,
            self.__fecha_nacimiento.day,
        ):
            edad -= 1
        return edad

    # -------------------------------------------------------------------------
    # Inciso e) Metodo para imprimir un Empleado como cadena de caracteres.
    # -------------------------------------------------------------------------
    def __str__(self):
        return (
            f"Empleado:\n"
            f"  Nombre              : {self.__nombre} {self.__apellidos}\n"
            f"  NSS                 : {self.__numero_seguridad_social}\n"
            f"  Fecha de nacimiento : {self.__fecha_nacimiento.strftime('%d/%m/%Y')}\n"
            f"  Edad                : {self.calcular_edad()} anios\n"
            f"  Salario             : ${self.__salario:,.2f}"
        )


# =============================================================================
# Inciso f) Prueba de la clase Empleado.
#   Se muestra el uso de ambos constructores, getters/setters y los metodos
#   calcular_edad() y __str__().
# =============================================================================
if __name__ == "__main__":
    print("=" * 55)
    print("  PRUEBA DEL EJERCICIO 8 - CLASE EMPLEADO")
    print("=" * 55)

    # -- Constructor por omision --
    print("\n[1] Empleado creado con constructor por omision:")
    emp1 = Empleado()
    print(emp1)

    # -- Uso de setters para completar datos --
    print("\n[2] Completando datos con setters:")
    emp1.set_nombre("Ana")
    emp1.set_apellidos("Garcia Lopez")
    emp1.set_numero_seguridad_social("GALA901119AB1")
    emp1.set_salario(12000.0)
    emp1.set_fecha_nacimiento(date(1990, 11, 19))
    print(emp1)

    # -- Constructor con parametros --
    print("\n[3] Empleado creado con constructor con_datos():")
    emp2 = Empleado.con_datos(
        nombre="Luis",
        apellidos="Martinez Ruiz",
        numero_seguridad_social="MARL850305CD2",
        salario=15500.0,
    )
    emp2.set_fecha_nacimiento(date(1985, 3, 5))
    print(emp2)

    # -- Getter de edad --
    print(f"\n[4] Edad de {emp2.get_nombre()}: {emp2.calcular_edad()} anios")

    # -- Validacion defensiva: salario menor al minimo --
    print("\n[5] Prueba defensiva: salario menor a $1,000.0")
    try:
        emp3 = Empleado.con_datos("Pedro", "Ramos", "RAMP000101EF3", 500.0)
    except ValueError as e:
        print(f"  Error capturado correctamente: {e}")

    print("\n" + "=" * 55)
