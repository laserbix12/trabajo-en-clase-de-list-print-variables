from datetime import datetime

# Encabezado
print("="*60)
print("    SURTITODO         FACTURA DE COMPRA")
print("="*60)
cliente = "Jhojan Silva"   # Nombre del cliente
fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print(f"Cliente: {cliente}")
print(f"Fecha:   {fecha}")
print("Nit:123456789-0")
print("="*60)


# Listas con datos
productos = ["aguacate", "papa", "Azúcar", "Pan", "Leche", "Huevos", "Queso", "Jamón", "Carne", "Tomate", "Cebolla", "Lechuga", "Manzana", "Plátano", "Naranja", "Uvas", "Pera", "Piña", "Melón", "Sandía", "Mango"]
cantidades = [2, 1, 3, 1, 12, 6, 4, 2, 5, 3, 1, 4, 6, 3, 2, 5, 1, 1, 1, 2, 3]
precios = [3000, 8500, 2800, 1500, 1200, 8000, 5000, 20000, 4000, 2500, 3000, 3500, 4000, 4500, 6000, 7000, 8000, 9000, 10000, 11000, 12000]

# IVA por producto (19%)
ivas = []
subtotales = []
totales = []

# Calcular IVA, subtotal y total por producto
for i in range(len(productos)):
    subtotal = cantidades[i] * precios[i]
    iva = precios[i] * 0.19
    total = subtotal + (iva * cantidades[i])

    subtotales.append(subtotal)
    ivas.append(iva)
    totales.append(total)

# Mostrar factura
print("{:<30} {:<50} {:<25} {:<20} {:<40}".format("Producto", "Cantidad", "Precio", "IVA", "Total"))
print("-"*60)

total_general = 0
for i in range(len(productos)):
    print("{:<12} {:<10} {:<15} {:<15} {:<15}".format(
        productos[i],
        cantidades[i],
        f"${precios[i]:,}".replace(",", "."),
        f"${ivas[i]:,.0f}".replace(",", "."),
        f"${totales[i]:,.0f}".replace(",", ".")
    ))
    total_general += totales[i]

print("-"*60)
print(f"{'TOTAL A PAGAR':<45} ${total_general:,.0f}".replace(",", "."))
print("="*60)
print("Gracias por su compra!")