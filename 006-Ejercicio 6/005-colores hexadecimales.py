import matplotlib.pyplot as plt

# Data for the pie chart
etiquetas = ['Python','Java','C']
datos = [45,23,67]
colores = ["#ff0000","#00ff00","#0000ff"]

plt.pie(datos,  labels=etiquetas, colors=colores)
plt.title('Mi gráfica')

plt.axis('equal')
plt.show()
