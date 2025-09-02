class Aparato:
    def __init__(self, nombre, potencia_w, horas_dia, dias_mes):
        self.nombre = nombre
        self.potencia_w = potencia_w
        self.horas_dia = horas_dia
        self.dias_mes = dias_mes

    def consumo_mensual_kwh(self):
        """
        Calcula el consumo mensual en kWh
        Fórmula: (potencia en W * horas/día * días/mes) / 1000
        """
        return (self.potencia_w * self.horas_dia * self.dias_mes) / 1000

    def costo_mensual(self, tarifa):
        """Calcula el costo mensual según la tarifa en $/kWh"""
        return self.consumo_mensual_kwh() * tarifa

