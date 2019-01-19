# Se crea la clase ArregloLineal
class ArregloLineal(object):

  '''def __init__(self):
    self.datos = []

  #Metodos set y get


  # Método para imprimir
  def __str__(self):

    for elemento in self.datos:
      return "%s" % (elemento)'''

class OperacionesArregloLineal(object):
  def __init__(self, datos):
    self.listaElementos = datos

  def arregloLineal(self, valores):
      self.listaElementos = valores

  def busquedaLineal(self, claveBusqueda):
      i = 0
      for z in self.listaElementos:
        if (z == claveBusqueda):
          return i
        i = i + 1
      return -1

  def __str__(self):
    cadena = ""
    for n in self.listaElementos:
      cadena = "%d" %(self.busquedaLineal())
    return cadena