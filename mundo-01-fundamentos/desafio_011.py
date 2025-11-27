# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de 
# tinta necessaária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m quadrados
# Capacidade de cobertura: 2m² por litro
cobertura_por_litro = 2
largura = float(input("Largura da parede (metros): "))
altura = float(input("Altura da parede (metros): "))
area = largura * altura
tinta_necessaria = area / cobertura_por_litro

print(f"\nA **Área Total** é de: {area:.2f} m²")
print(f"Serão necessários **{tinta_necessaria:.2f} litros** de tinta.")
