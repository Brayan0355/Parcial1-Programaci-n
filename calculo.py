def calcular_totales(aparatos, tarifa):
    total_consumo = sum(a.consumo_mensual_kwh() for a in aparatos)
    total_costo = sum(a.costo_mensual(tarifa) for a in aparatos)
    return total_consumo, total_costo


def ordenar_por_consumo(aparatos):
    """Ordena los aparatos de mayor a menor consumo"""
    return sorted(aparatos, key=lambda a: a.consumo_mensual_kwh(), reverse=True)