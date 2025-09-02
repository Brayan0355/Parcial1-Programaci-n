"""
En El Salvador, muchas familias desean controlar su gasto eléctrico mensual.
Cada hogar utiliza distintos aparatos eléctricos, como refrigeradores,
televisores, aire acondicionado o iluminación, durante diferentes cantidades
de horas. Sin un registro, es difícil saber qué aparato genera mayor consumo
y cómo optimizar el gasto mensual de electricidad.
"""

from aparato import Aparato
import calculo

def Ejercicio1Parcial():
    aparatos = []
    tarifa = float(input("Ingrese la tarifa de electricidad ($/kWh): "))

    n = int(input("¿Cuántos aparatos desea registrar? "))
    for i in range(n):
        print(f"\n--- Aparato {i+1} ---")
        nombre = input("Nombre del aparato: ")
        potencia = float(input("Potencia (W): "))
        horas = float(input("Horas de uso al día: "))
        dias = int(input("Días de uso al mes: "))
        aparatos.append(Aparato(nombre, potencia, horas, dias))

    # Ordenar aparatos por consumo
    aparatos_ordenados = calculo.ordenar_por_consumo(aparatos)

    # Totales
    total_consumo, total_costo = calculo.calcular_totales(aparatos, tarifa)

    # Reporte
    print("\n REPORTE DE CONSUMO (Ordenado de mayor a menor consumo)")
    for a in aparatos_ordenados:
        print(f"- {a.nombre}: {a.consumo_mensual_kwh():.2f} kWh, "
              f"Costo: ${a.costo_mensual(tarifa):.2f}")

    print("\n RESUMEN")
    print(f" Consumo total: {total_consumo:.2f} kWh")
    print(f" Gasto mensual total: ${total_costo:.2f}")

if __name__ == "__main__":
    Ejercicio1Parcial()

