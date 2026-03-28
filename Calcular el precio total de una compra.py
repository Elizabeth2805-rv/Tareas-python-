def calcular_total(precio, cantidad, descuento):
    """ Calcula el total a pagar aplicando descuento.
    precio: valor unitario del producto
    cantidad: número de productos
    descuento: porcentaje de descuento (ej: 10 para 10%)
    """
    subtotal = precio * cantidad
    valor_descuento = subtotal * (descuento / 100)
    total = subtotal - valor_descuento
    return total
def main():
    print("=== CÁLCULO DEL PRECIO TOTAL DE UNA COMPRA ===")
    try:
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad de productos: "))
        descuento = float(input("Ingrese el porcentaje de descuento (%): "))
        if precio < 0 or cantidad < 0 or descuento < 0:
            print("Error: No se permiten valores negativos.")
            return
        total_pagar = calcular_total(precio, cantidad, descuento)
        print(f"Subtotal: {precio * cantidad}")
        print(f"Descuento aplicado: {descuento}%")
        print(f"Total a pagar: {total_pagar}")
    except ValueError:
        print("Error: Debe ingresar valores numéricos válidos.")
main()
 
