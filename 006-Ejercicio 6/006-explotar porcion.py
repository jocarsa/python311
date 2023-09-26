import matplotlib.pyplot as plt

# Data for the pie chart
etiquetas = ['Python','Java','C']
datos = [45,23,67]
colores = ["#ff0000","#00ff00","#0000ff"]
explotar = (0.1, 0, 0)  

plt.pie(
    datos,
    labels=etiquetas,
    colors=colores,
    explode = explotar
    )
plt.title('Mi gráfica')

plt.axis('equal')
plt.show()
