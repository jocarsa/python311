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

datosdb = cursor.fetchall()


etiquetas = []
datos = []
for dato in datosdb:
    print(dato)
    etiquetas.append(dato[1])
    datos.append(dato[0])
print(etiquetas)
    
anguloinicial = 90

plt.pie(
    datos,
    labels=etiquetas,
    startangle = anguloinicial,
    shadow=True
    )
plt.title('Mi gráfica')

plt.axis('equal')
plt.show()
