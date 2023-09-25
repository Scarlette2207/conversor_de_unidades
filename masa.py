"""2) Módulo masa.py: Este módulo debe contener funciones para convertir entre diferentes unidades de masa, como kilogramos, libras y onzas.(0.5 puntos) """
def Kilogramos_a_Gramos(kg):
    g = kg * 1000
    return g

def Kilogramos_a_Toneladas(kg):
    t = kg / 1000
    return t

def Gramos_a_Kilogramos(g):
    kg = g / 1000
    return kg

def Gramos_a_Toneladas(g):
    t = g / 1000000
    return g

def Toneladas_a_Kilogramos(t):
    kg = t * 1000
    return t

def Toneladas_a_Gramos(t):
    g = t * 1000000
    return t

if __name__ == "__main__":
    # Ejemplos de uso
    print("Ejemplos de conversión de masa:")
    print("14kg a g:", Kilogramos_a_Gramos(14))
    print("20kg a t:", Kilogramos_a_Toneladas(20))
    print("10g a kg:", Gramos_a_Kilogramos(10))
    print("18g a t:", Gramos_a_Toneladas(18))
    print("25t a kg:", Toneladas_a_Kilogramos(25))
    print("15t a g:", Toneladas_a_Gramos(15))

