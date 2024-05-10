"""
En este código, hemos definido la clase SimpleOperations, que contiene los métodos apply_discount y
calculate_tax. Luego, creamos una instancia de esta clase llamada operations.
Utilizando functools.partial, hemos configurado dos funciones especializadas: twenty_percent_discount
y vat_tax. twenty_percent_discount está configurada para aplicar un descuento del 20% usando el método 
apply_discount de operations, mientras que vat_tax está configurada para calcular el impuesto del 21% 
utilizando el método calculate_tax de operations.
Finalmente, utilizamos estas funciones preconfiguradas para calcular el precio después del descuento y
 después de aplicar el impuesto sobre el precio original.
"""
import functools

class SimpleOperations:
    def apply_discount(self, price, discount):
        """Aplica un descuento al precio dado y retorna el nuevo precio."""
        discounted_price = price - (price * discount)
        return discounted_price

    def calculate_tax(self, price, tax_rate):
        """Calcula y agrega el impuesto al precio dado."""
        taxed_price = price + (price * tax_rate)
        return taxed_price

# Crear una instancia de SimpleOperations
operations = SimpleOperations()

# Configurar funciones con descuentos y tasas de impuestos predefinidos utilizando functools.partial.
twenty_percent_discount = functools.partial(operations.apply_discount, discount=0.20)
vat_tax = functools.partial(operations.calculate_tax, tax_rate=0.21)

# Usar las funciones preconfiguradas.
original_price = 100
price_after_discount = twenty_percent_discount(original_price)
price_after_tax = vat_tax(original_price)

print("Precio original:", original_price)
print("Precio después de descuento del 20%:", price_after_discount)
print("Precio después de aplicar el IVA (21%):", price_after_tax)
