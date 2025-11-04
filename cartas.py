# cartas.py

def aplicar_carta(numero, estado):
    # Carta 1: Dia tranquilo:
    # No ocurre nada malo.
    if numero == 1:
        return estado

    # Carta 2: Falla critica en maquinaria:
    # Pierdes 2 maquinas activas permanentemente (hasta hacer mantenimiento)
    elif numero == 2:
        return estado

    # Carta 3: Virus informatico:
    # Se pierde visibilidad del inventario y de los insumos por 1 turno
    # No puedes producir porque no sabes cuantos insumos hay.
    # No puedes vender porque no sabes cuanto invnetario hay.
    # Los clientes se enteraron y bajo la reputacion 1 nivel
    # Duración: 2 turnos
    elif numero == 3:
        return estado

    # Carta 4: Incendio en almacen
    #   - Se pierde el inventario total (al final del mes, despues de haber producido y vendido)
    elif numero == 4:
        return estado

    # Carta 5: Auditoria desfavorable
    #   - Aumentan las multas e indemnizaciones en +5000.
    # Los clientes se enteraron y bajo la reputacion 1 nivel
    elif numero == 5:
        return estado

    # Carta 6: Producto retirado del mercado
    #   - Reputacion se reduce 2 niveles.
    #   - Tuvimos que reponer mercaderia equivalente a la demanda actual (elimina el inventario equivalente a la demanda)
    #   - Luego, la demanda actual se reduce en 50%
    # Duración: 2 turnos
    elif numero == 6:
        return estado

    # Carta 7: Robo de insumos
    #   - Pierdes 30% de insumos disponibles.
    elif numero == 7:
        return estado

    # Carta 8: Fuga de talento clave
    #   - Tras la fuga de talento, operarios sin experiencia manipularon y dañaron una maquina
    #   - Pierdes 1 maquina activa (pasa a dañada).
    #   - Pierdes 1 empleado.
    elif numero == 8:
        return estado

    # Carta 9: Huelga por ambiente laboral
    #   - La proxima ronda no se produce.
    #   - Los clientes se enteran de la huelga y baja la reputación 3 niveles
    # Duración: 2 turnos
    elif numero == 9:
        return estado

    # Carta 10: Hacker secuestra datos
    #   - Pierdes 5,000 de caja (si no alcanza, la diferencia se convierte en deuda al 12%)
    #   - Reputacion baja 2 niveles
    #   - Te aplican una multa de 5,000 soles por malas practicas de seguridad de la informacion
    elif numero == 10:
        return estado

 # Carta 11: Multa ambiental
    #   - Aumentan “Multas e indemnizaciones” en +5000.
    #   - Reputacion del mercado −1 nivel.
    elif numero == 11:
        return estado

    # Carta 12: Boicot de clientes
    #   - Ventas de esta semana reducidas al 50%:
    # Duración: 2 turnos
    elif numero == 12:
        return estado

    # Carta 13: Error de etiquetado
    #   - Devuelven todas las unidades vendidas el turno actual y el turno anterior
    #     • Debes devolver el dinero obtenido por dichas ventas
    #     • Además, gastas 15,000 soles en la logística inversa
    # Duración: 3 turnos
    elif numero == 13:
        return estado

    # Carta 14: Retraso en importacion
    #   - Prohibir insumos importados las siguientes 3 rondas:
    elif numero == 14:
        return estado

    # Carta 15: Proveedores en huelga
    #   - Prohibir compras nacionales las siguientes 4 rondas:
    elif numero == 15:
        return estado

    # Carta 16: Estafa financiera
    #   - Pierdes 8,000 de caja
    elif numero == 16:
        return estado

    # Carta 17: Rumor de corrupcion
    #   - Reputacion del mercado −2 niveles.
    elif numero == 17:
        return estado

    # Carta 18: Plaga en planta
    #   - Produccion a la mitad este turno
    # Duración: 3 turnos
    elif numero == 18:
        return estado

    # Carta 19: Cliente corproativo VIP cancela pedido
    #   - Peirdes un tercio de los “Pedidos por atender”.
    elif numero == 19:
        return estado

    # Carta 20: Producto defectuoso viral
    #   - Reputacion del mercado −3 niveles.
    elif numero == 20:
        return estado

    # Carta 21: Mal clima: inundacion
    #   - No se produce la siguiente ronda:
    # Duración: 2 turnos
    elif numero == 21:
        return estado

    # Carta 22: Licencia vencida
    #   - Multas +30,000.
    #   - Prohibir produccion la siguiente ronda.
    elif numero == 22:
        return estado

    # Carta 23: Fake news en redes
    #   - Reputacion del mercado −2 niveles.
    elif numero == 23:
        return estado

    # Carta 24: Bloqueo logistico
    #   - No se venden unidades
    # Duración: 2 turnos
    elif numero == 24:
        return estado

    # Carta 25: Demanda judicial
    #   - Multas e indemnizaciones +15,000.
    elif numero == 25:
        return estado

    # Carta 26: Nuevo competidor agresivo
    #   - Ventas −40%:
    #   - Debemos pagar 5,000 por almacén
    # Duración: 3 turnos

    elif numero == 26:
        return estado

    # Carta 27: Robo interno
    #   - Caja se reduce en 10,000.
    elif numero == 27:
        return estado

    # Carta 28: Crisis economica
    #   - Todos los costos +10% por los siguientes 5 turnos:
    elif numero == 28:
        return estado

    # Carta 29: Fuga de datos
    #   - Reputacion del mercado −2 nivel.
    #   - Ventas de este mes se reducen en un 75%
    elif numero == 29:
        return estado

    # Carta 30: Huelga nacional
    #   - No ventas ni produccion
    #   - Debemos pagar 10,000 por almacén
    # Duración: 3 turnos
    elif numero == 30:
        return estado

    # Carta 31: Rechazo de exportacion
    #   - Inventario acumulado (no se vende este mes).
    #   - Debemos pagar 10,000 por almacén
    elif numero == 31:
        return estado

    # Carta 32: Error contable
    #   - Caja −7000.
    elif numero == 32:
        return estado

    # Carta 33: Error en codigo de barras
    #   - No se venden productos este mes:
    #   - reputación baja 2 niveles
    elif numero == 33:
        return estado

    # Carta 34: Mal diseño del empaque
    #   - Ventas −25%
    #   - reputación baja 2 niveles
    # Duración: 2 turnos
    elif numero == 34:
        return estado

    # Carta 35: Cliente se intoxica
    #   - Reputacion del mercado −3 niveles.
    #   - Multas +30,000.
    elif numero == 35:
        return estado

    # Carta 36: Fraude en prestamo
    #   - Caja −15,000.
    #   - Deuda pendiente +15,000.
    #   - reputación baja 2 niveles
    elif numero == 36:
        return estado

    # Carta 37: Trabajador se accidenta
    #   - Multas +4000.
    #   - Produccion −50% este mes
    #   - Temporalmente -1 trabajador por 2 turnos
    elif numero == 37:
        return estado

    # Carta 38: Derrame quimico
    #   - Inventario e Insumos = 0
    #   - No puedes producir durante este mes y el siguiente
    elif numero == 38:
        return estado

    # Carta 39: Virus contagioso
    #   Todos los empleados se quedaron en su casa por un mes
    #   No se vende ni se produce
    elif numero == 39:
        return estado

    # Carta 40: Hiring Freeze
    #   No puedes contratar empleados nuevos
    # Duración: 5 turnos
    elif numero == 40:
        return estado

    # Si el numero no coincide con ninguna carta:
    #    se considera Dia tranquilo (sin cambios).
    else:
        return estado
