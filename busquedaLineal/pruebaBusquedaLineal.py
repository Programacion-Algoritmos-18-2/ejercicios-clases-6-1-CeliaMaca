# Se importa la clase a ejecutar
from paquete_archivos.miarchivo import MiArchivo
from modelado.arregloLineal import ArregloLineal, OperacionesArregloLineal

m = MiArchivo()
enteroBusqueda = 3

lista = m.obtener_informacion()
data_lista = []
for l in lista:
  lista = l.split(",")
  for li in lista:
    data_lista.append(int(li))

data_lista.sort()
print("ListaInicial ", data_lista)

operaciones = OperacionesArregloLineal(data_lista)

print("El elemento %s se encontró en la posicion %s" %(enteroBusqueda, operaciones.busquedaLineal(enteroBusqueda)))
