import matplotlib.pyplot as plt
import sqlite3

conexion = sqlite3.connect("registros.db")
cursor = conexion.cursor()
cursor.execute('''
SELECT COUNT(extra3),extra3
FROM logs
WHERE extra3 != ''
GROUP BY extra3
ORDER BY COUNT(extra3) DESC
LIMIT 10
''')

datos = cursor.fetchall()

print(datos)

etiquetas = ['Python','Java','C']
datos = [45,23,67]
colores = ["#ff0000","#00ff00","#0000ff"]
explotar = (0.1, 0, 0)
anguloinicial = 90

plt.pie(
    datos,
    labels=etiquetas,
    colors=colores,
    explode = explotar,
    startangle = anguloinicial,
    shadow=True
    )
plt.title('Mi gráfica')

plt.axis('equal')
plt.show()
