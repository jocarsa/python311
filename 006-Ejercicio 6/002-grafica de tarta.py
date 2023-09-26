import matplotlib.pyplot as plt

# Data for the pie chart
etiquetas = ['Python','Java','C']
datos = [45,23,67]  

plt.pie(datos,  labels=etiquetas)
plt.title('Mi gráfica')

plt.axis('equal')  # Equal aspect ratio ensures that the pie is circular
plt.show()
