# Lista de productos y precios
menu = {
    1: {'nombre': 'Café Americano', 'precio': 2.50},
    2: {'nombre': 'Café con Leche', 'precio': 3.00},
    3: {'nombre': 'Capuchino', 'precio': 3.50},
    4: {'nombre': 'Té', 'precio': 2.00},
    5: {'nombre': 'Sándwich', 'precio': 4.00},
    6: {'nombre': 'Pastel', 'precio': 3.75},
}

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Menú de la Cafetería ---")
    for clave, producto in menu.items():
        print(f"{clave}. {producto['nombre']} - ${producto['precio']:.2f}")
    print("----------------------------")

# Función para hacer un pedido
def hacer_pedido():
    pedido = []
    total = 0.0
    opcion = None  # Inicializar la opción

    while opcion != 0:
        mostrar_menu()
        opcion = int(input("Selecciona el número del producto que deseas (o escribe '0' para finalizar el pedido): "))

        if opcion == 0:
            break
        elif opcion in menu:
            cantidad = int(input(f"¿Cuántas unidades de {menu[opcion]['nombre']} deseas? "))
            total_producto = menu[opcion]['precio'] * cantidad
            pedido.append({'producto': menu[opcion]['nombre'], 'cantidad': cantidad, 'total': total_producto})
            total += total_producto
            print(f"Agregaste {cantidad} de {menu[opcion]['nombre']} al pedido. Subtotal: ${total_producto:.2f}")
        else:
            print("Opción no válida.")

    return pedido, total

# Función para procesar el pago
def procesar_pago(total):
    pago = float(input(f"\nTotal a pagar: ${total:.2f}\nIngresa la cantidad con la que vas a pagar: $"))

    while pago < total:
        print("El monto es insuficiente, intenta de nuevo.")
        pago = float(input("Ingresa la cantidad con la que vas a pagar: $"))

    cambio = pago - total
    print(f"Pago exitoso. Tu cambio es: ${cambio:.2f}")

# Función principal
def main():
    print("¡Bienvenido a la Cafetería Virtual!\n")
    pedido, total = hacer_pedido()

    if pedido:
        print("\n--- Resumen del Pedido ---")
        for item in pedido:
            print(f"{item['cantidad']} x {item['producto']} - Total: ${item['total']:.2f}")
        print(f"Total del pedido: ${total:.2f}")

        procesar_pago(total)
    else:
        print("No realizaste ningún pedido.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
