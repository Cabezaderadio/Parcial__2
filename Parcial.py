class CCsalud:
    
    def __init__ (self, numero_identidicacion, nombre_completo, edad, sintomas, diagnostico_medico):
        
        self.numero = numero_identidicacion
        self.nombre = nombre_completo
        self.edad = edad
        self.sintomas = sintomas
        self.diagnostico = diagnostico_medico
        self.anterior = None
        self.siguiente = None
        
class Listacircular:
    
    def __init__(self):
        
        self.primero = None
        self.ultimo = None
    
    def vacia(self):
        return self.primero == None
        
    def registrar(self, numero_identidicacion, nombre_completo, edad, sintomas, diagnostico_medico):
    
        if self.vacia():
            self.primero = CCsalud(numero_identidicacion, nombre_completo, edad, sintomas, diagnostico_medico)
            self.ultimo = self.primero
            
        else: 
            aux = CCsalud(numero_identidicacion, nombre_completo, edad, sintomas, diagnostico_medico)
            aux.siguiente = self.primero
            self.primero = aux
            
    def Eliminar(self, numero_identidicacion):
        nodo_actual = self.vacia
        
        if nodo_actual is not None and nodo_actual.numero_identificacion == numero_identidicacion:
            nodo_actual = nodo_actual.siguiente
        else:
            print("El número de identificación ingresado no se encuentra en la base de datos")

    def buscar_paciente(self, numero_identidicacion):
        nodo_actual = self.vacia
        
        if nodo_actual is not None and nodo_actual.numero_identificacion == numero_identidicacion:
            print(f"Nombre: {nodo_actual.nombre} \n Edad: {nodo_actual.edad}\n Número de identificación: {nodo_actual.numero_identificacion}\n Sintomas: {nodo_actual.sintomas}\n Diagnostico: {nodo_actual.diagnostico}")
        else:
            print("El número de identificación ingresado no se encuentra en la base de datos")
            
    def mostrar_pacientes():
        
        nodo_actual = self.vacia
        
        while nodo_actual+