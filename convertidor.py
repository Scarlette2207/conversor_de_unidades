"""1) Módulo temperatura.py: Este módulo debe contener funciones para convertir entre diferentes unidades de temperatura, como Celsius, Fahrenheit y Kelvin.(0.5 puntos) """
"""2) Módulo masa.py: Este módulo debe contener funciones para convertir entre diferentes unidades de masa, como kilogramos, libras y onzas.(0.5 puntos) """
"""3) Crear el primer versionamiento con git de los dos módulos creados de temperatura y masa (usar git add y git commit ). (0.5 puntos) """
"""4) Crear una nueva rama llamada “desarrollo” y en esta nueva rama agregar los módulos tiempo.py y convertidor.py (recuerda usar git branch ). (0.5 puntos) """
"""5) Módulo tiempo.py: Este módulo debe contener funciones para convertir entre diferentes unidades de tiempo, como segundos, minutos y horas. (1 punto) """
"""6) Módulo convertidor.py: Este módulo importa los módulos de masa, temperatura y tiempo. Actúa como el punto de entrada del programa. Debe permitir a los usuarios seleccionar la categoría de conversión deseada (temperatura, masa o tiempo), ingresar el valor a convertir y las unidades de origen y destino, y obtener el resultado de la conversión.(2 puntos) """
"""7) Versionar esta rama “desarrollo” con git add y git commit para luego fusionar con la rama master (para fusionar, usar: git merge). (1 punto) """
""" Desde la rama main o master subir al nuevo repositorio de github llamado conversor_de_unidades. (1 punto) """

""" Recuerda que cada uno de los módulos, deben incluir el bloque if __name__ == "__main__" para sus pruebas en cada módulo. """
import temperatura
import masa
import tiempo
def main():
    while True:
        # Muestra el menú principal
        print("Menú Principal:")
        print("[1] Convertir celsius a fahrenheit")
        print("[2] Convertir celsius a Kelvin")
        print("[3] Convertir Fahrenheit a Celsius")
        print("[4] Convertir Fahrenheit a Kelvin")
        print("[5] Convertir Kelvin a Celsius")
        print("[6] Convertir Kelvin a Fahrenheit")
        print("[7] Convertir Kilogramos a Gramos")
        print("[8] Convertir Kilogramos a Toneladas")
        print("[9] Convertir Gramos a Kilogramos")
        print("[10] Convertir Gramos a Toneladas")
        print("[11] Convertir Toneladas a Kilogramos")
        print("[12] Convertir Toneladas a Gramos ")
        print("[13] Convertir Segundos a Minutos")
        print("[14] Convertir Segundos a Horas")
        print("[15] Convertir Minutos a Segundos")
        print("[16] Convertir Minutos a Horas")
        print("[17] Convertir Horas a Segundos")
        print("[18] Convertir Horas a Minutos")

        
        # Solicita al usuario que ingrese una opción
        opcion = input("Ingrese una opción: ")
        valorInicial=int(input("Ingrese valor inicial: "))
        try:
            opcion = int(opcion)
            if opcion == 0:
                print("Saliendo del programa. ¡Hasta luego!")
                break
            elif opcion == 1:
                resultado = temperatura.celsius_a_fahrenheit(valorInicial)
                print("El resultado es: ", resultado)
            elif opcion == 2:
                resultado = temperatura.Celsius_a_kelvin(valorInicial)
                print("El resultado es: ", resultado)
            elif opcion == 3:
                resultado = temperatura.Fahrenheit_a_Celsius(valorInicial)
                print("El resultado es: ", resultado)
            elif opcion == 4:
                resultado = temperatura.Kelvin_a_Kelvin(valorInicial)
                print("El resultado es: ", resultado)
            elif opcion == 5:
                resultado = temperatura.Fahrenheit_a_Celsius(valorInicial)
                print("El resultado es: ", resultado)
            elif opcion == 6:
                resultado = temperatura.Kelvin_a_Fahrenheits(valorInicial)
                print("El resultado es: ", resultado)
            elif opcion == 7:
                resultado = masa.Kilogramos_a_Gramos(valorInicial)
                print("El resultado es: ", resultado)
            elif opcion == 8:
                resultado = masa.Kilogramos_a_Tonelada(valorInicial)
                print("El resultado es: ", resultado)
            elif opcion == 9:
                resultado = masa.Gramos_a_Kilogramos(valorInicial)
                print("El resultado es: ", resultado)
            elif opcion == 10:
                resultado = masa.Gramos_a_Toneladas(valorInicial)
                print("El resultado es: ", resultado)
            elif opcion == 11:
                resultado = masa.Toneladas_a_Kilogramos(valorInicial)
                print("El resultado es: ", resultado)
            elif opcion == 12:
                resultado = masa.Toneladas_a_Gramos(valorInicial)
                print("El resultado es: ", resultado)
            elif opcion == 13:
                resultado = tiempo.Segundos_a_Minutos(valorInicial)
                print("El resultado es: ", resultado)
            elif opcion == 14:
                resultado = tiempo.Segundos_a_Horas(valorInicial)
                print("El resultado es: ", resultado)
            elif opcion == 15:
                resultado = tiempo.Minutoss_a_Segundos(valorInicial)
                print("El resultado es: ", resultado)
            elif opcion == 16:
                resultado = tiempo.Minutoss_a_Horas(valorInicial)
                print("El resultado es: ", resultado)
            elif opcion == 17:
                resultado = tiempo.Horas_a_Segundos(valorInicial)
                print("El resultado es: ", resultado)
            elif opcion == 18:
                resultado = tiempo.Horas_a_Minutos(valorInicial)
                print("El resultado es: ", resultado)
            else:
                print("Opción no válida. Por favor, ingrese una opción válida.")
        except ValueError:
            print("Solo puede ingresar valores numéricos.")

if __name__ == "__main__":
    main()
    #https://github.com/Scarlette2207/conversor_de_unidades/