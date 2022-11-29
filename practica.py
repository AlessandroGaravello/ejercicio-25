#crea una clase llamada Producto
class Producto:
#nombre, unidades y precio
    def __init__(self,nombre,unidades,precio):
        self.nombre=nombre
        self.unidades=unidades
        self.precio=precio
#crea un método de infoProducto. Muestra el nombre, unidades, precio y inventario valorado (uxp)
    def infoProducto(self):
        print(f'El producto se llama {self.nombre}, hay {self.unidades} unidades, cuesta {self.precio} y el inventario valorado es {self.unidades*self.precio}')
#creas un producto camisa, 10, 9.95 de precio
c1=Producto('camisa',10,9.95)
#muestra el nombre de producto por consola
print(f'El producto se llama {c1.nombre}')
print(f'{c1.infoProducto()}')

#práctica de sobreescritura.
#crea una clase llamada Servicio
class Servicio:
    def __init__(self,nombre):
        self.nombre=nombre
#tiene un método llamado consultarDetalle que muestra. el servicio es básico.
    def consultarDetalle(self):
        print('El servicio es básico')
#la empresa tiene dos servicios. estándar y premium. Son dos clases que derivan de Servicio
class Estandar(Servicio):
    def consultarDetalle(self):#sobrecarga
        print('El servicio es estandar')

class Premium(Servicio):
    def consultarDetalle(self):#sobrecarga
        print('El servicio es premium')
#la clase Estandar y Premium tienen un método llamado consultarDetalle y explican que son
#servicio estándar y premium respectivamente.
#pide por consola un servicio. Elegimos premium y te muestra el resultado de consultarDetalle
e1=Estandar('estandar')
e2=Premium('premium')
empresa=input('Dime un servicio: ')
if empresa == 'estandar':
    e1.consultarDetalle()
if empresa == 'premium':
    e2.consultarDetalle()