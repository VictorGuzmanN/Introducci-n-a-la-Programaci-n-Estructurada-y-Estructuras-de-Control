# def calcular_aumento(horas, sueldo_hora):
#     """Calcula el aumento según las horas trabajadas"""
#     if horas == 10:
#         porcentaje = 0.20
#     elif horas == 15:
#         porcentaje = 0.30
#     elif horas == 20:
#         porcentaje = 0.15
#     elif horas > 25:
#         porcentaje = 0.08
#     else:
#         porcentaje = 0.0
#     return porcentaje

# def procesar_trabajador():
#     """Lee los datos de un trabajador y devuelve sueldo neto"""
#     nombre = input("Nombre del trabajador: ").strip().title()
#     horas = int(input("Número de horas trabajadas: "))
#     sueldo_hora = float(input("Sueldo por hora: "))

#     sueldo_base = horas * sueldo_hora
#     aumento = sueldo_base * calcular_aumento(horas)
#     sueldo_neto = sueldo_base + aumento

#     print(f"\nTrabajador: {nombre}")
#     print(f"Sueldo base: ${sueldo_base:.2f}")
#     print(f"Aumento: ${aumento:.2f}")
#     print(f"Sueldo neto: ${sueldo_neto:.2f}\n")

#     return sueldo_neto

# def main():
#     total_trabajadores = 0
#     total_sueldos = 0.0

#     while True:
#         sueldo_neto = procesar_trabajador()
#         total_trabajadores += 1
#         total_sueldos += sueldo_neto

#         continuar = input("¿Desea ingresar otro trabajador? (s/n): ").lower()
#         if continuar != "s":
#             break

#     print("\n--- Resumen Final ---")
#     print(f"Total de trabajadores ingresados: {total_trabajadores}")
#     print(f"Monto total de sueldos netos: ${total_sueldos:.2f}")

# # Ejecutar el programa
# main()


def sueldoTrabajadores(horas_trab,sueldo):
    sueldo_base=sueldo*horas_trab   
    return sueldo_base


print("\033c")
trabajadores=0
acum_sueldo_neto=0
opc="S"
while opc=="S":
    nombre=input("Nombre: ")
    horas_trab=int(input("Horas trabajadas: "))
    sueldo=float(input("Sueldo por Horas trabajadas: "))
    aumento=0
    sueldo_base=sueldoTrabajadores(horas_trab,sueldo)

    if horas_trab==10:
        aumento=0.20
    elif horas_trab==15:
        aumento=0.30
    elif horas_trab==20:
        aumento=0.15
    elif horas_trab>25:
        aumento=0.08
        
    aumento_pagar=aumento*sueldo_base
    suel_neto=sueldo_base+aumento_pagar
    
    trabajadores+=1
    acum_sueldo_neto+=suel_neto
    
    print(f"El aumento es: {aumento_pagar}\n Y el sueldo neto cobrado es: {suel_neto}")
    
    opc=input("¿Desea ingresar mas trabajadores (S/N)").upper().strip()
print(f"El total de trabajadores es: {trabajadores}\nY monto total del sueldo neto cobrado es: {acum_sueldo_neto}")