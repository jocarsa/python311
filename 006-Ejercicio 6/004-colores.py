import matplotlib.pyplot as plt

# Data for the pie chart
etiquetas = ['Python','Java','C']
datos = [45,23,67]
colores = ["red","blue","green"]

plt.pie(datos,  labels=etiquetas, colors=colores)
plt.title('Mi gráfica')

plt.axis('equal')
plt.show()
