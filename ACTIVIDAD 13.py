class repartidor:
    def init (self, nombre, paquetes,zona):
        self.nombre=nombre
        self.paquetes=paquetes
        self.zona=zona

    def init (self):
        return (f"{self.nombre} - {self.paquetes} paquetes - zona {self.zona}")

class mensajes:
    def init (self):
        self.repartidores=[]

    def nuevo(self,repartidor):
        for r in self.repartidores:
            if r.nombre ==repartidor.nombre:
                return False
        if repartidor.paquetes<0 or repartidor.zona.strip()=="":
             return False
        self.repartidores.append(repartidor)
        return True
    def quick_sort(self,lista):
        if len(lista)<=1:
            return lista
        pivote = lista[0]
        mayores=[x for x in lista[1:] if x.paquetes > pivote.paquetes]
        menores = [x for x in lista[1:] if x.paquetes == pivote.paquetes]
        iguales = [x for x in lista[1:] if x.paquetes < pivote.paquetes]
        return self.quick_sort(mayores)+[pivote]+iguales+self.quick_sort(menores)
    def ordenar(self):
        self.repartidores = self.quick_sort(self.repartidores)

    def buscar(self, nombre):
        for r in self.repartidores:
            if r.nombre()== nombre():
                return r
        return None
    def ranking(self):
        for r in self.repartidores:
            print(r)

    def estadisticas(self):
        total =sum(r.paquetes for r in self.repartidores)
        promedio = total / len(self.repartidores) if self.repartidores else 0
        max_entrega=max(r.paquetes for r in self.repartidores)
        min_entrega = min(r.paquetes for r in self.repartidores)
        max_repartidores=[r.nombre for r in self.repartidores if r.paquetes == max_repartidores]
        min_repartidores = [r.nombre for r in self.repartidores if r.paquetes == min_repartidores]

        print(f"Total de paquetes: {total}")
        print(f"Promedio de paquetes: {promedio:}")
        print(f"Mayor número de entregas: {', '.join(max_repartidores)} ({max_entrega})")
        print(f"Menor número de entregas: {', '.join(min_repartidores)} ({min_entrega})")

empresa = empresaEnvios()
n=int(input("cantida de repartidores"))
for i in range(n):
    print(f"ingrese datos del repartidor")
    nombre = input("nombre")
    paquetes=int(input("paquetes"))
    zona = input("zona")
    r = Repartidor(nombre, paquetes, zona)
    if not empresa.agregar_repartidor(r):
        print("Datos inválidos o nombre repetido. Intente nuevamente.")
        continue

for r in empresa.repartidores:
    print(r)

empresa.ordenar_por_paquetes()
empresa.mostrar_ranking()

nombre_buscar = input("\nBuscar repartidor: ")
encontrado = empresa.buscar_repartidor(nombre_buscar)
if encontrado:
    print(encontrado)
else:
    print("Repartidor no encontrado.")

print("\n--- Estadísticas ---")
empresa.estadisticas()



