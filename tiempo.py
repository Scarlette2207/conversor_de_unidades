"""5) Módulo tiempo.py: Este módulo debe contener funciones para convertir entre diferentes unidades de tiempo, como segundos, minutos y horas. (1 punto) """
def Segundos_a_Minutos(sec):
    min = sec / 60
    return min

def Segundos_a_Horas(sec):
    hr = sec / 3600 
    return hr

def Minutos_a_Segundos(min):
    sec = min * 60
    return sec

def Minutos_a_Horas(min):
    hr = min / 60
    return hr

def Horas_a_Segundos(hr):
    sec = hr * 3600
    return sec

def Horas_a_Minutos(hr):
    min = hr * 60
    return min

if __name__ == "__main__":
    # Ejemplos de uso
    print("Ejemplos de conversión de masa:")
    print("14 segundos a minutos:", Segundos_a_Minutos(14))
    print("20 segundos a horas:", Segundos_a_Horas(20))
    print("10 minutos a segundos:", Minutos_a_Segundos(10))
    print("18 minutos a horas:", Minutos_a_Horas(18))
    print("25 horas a segundos:",Horas_a_Segundos(25))
    print("15 horas a minutos:", Horas_a_Minutos(15))
