class Persona:
    def __init__(self,nombre,apellido,correo,emei):
    	self.nombre=nombre
    	self.apellido=apellido
    	self.correo=correo
    	self.emei=emei
    	self.reporte=[]
    	self.persona=[nombre,apellido,correo,emei]

    def agregar_reporte(self,latitud,longitud,error_maximo,tiempo,actividad,probabilidad):
        que=reporte(latitud,longitud,error_maximo,tiempo,actividad,probabilidad)
        self.reporte.append(que.reporte2)

    def promedio_errores(self):
        promedioerrores=0
        for i in range (0,len(self.reporte)):
            error_maximo=self.reporte[i][2]
            promedioerrores+=int(error_maximo)
            
        return promedioerrores/len(self.reporte)

    def tiempo_promedio_entre_mediciones(self):
        contador=0
        promedio=0
        for i in range(0,len(self.reporte)-1):
            tiempo1=self.reporte[i][3]
            tiempo2=self.reporte[i+1][3]
            promedio+=(int(tiempo1)+int(tiempo2))/2
            contador+=1
            
        promedio_final=promedio/contador
            
        return promedio_final

class reporte:
    def __init__(self,latitud,longitud,error_maximo,tiempo,actividad,probabilidad):
        self.reporte2=[latitud,longitud,error_maximo,tiempo,actividad,probabilidad]

class Pais:
    def __init__(self,nombre):
        self.nombre = nombre
        self.lista_personas = []

    def agregar_persona(self,persona):
        self.lista_personas.append(persona)
            

class Menu:
    def __init__(self):
        self.opciones={
                        "1": self.agregar_persona,"2": self.agregar_pais, "3": self.print_todo}
        self.lista_paises = []
        
    def display_menu(self):
        print(""" 1: agregar_persona al pais  \n 2: agregar_pais   \n 3: printear todo""")           
        
    def run(self):
        
        while True:
            self.display_menu()
            eleccion=input("Ingrese opcion: ")
            accion=self.opciones.get(eleccion)
            if accion:
                accion()
            
    def agregar_persona(self):       
        lista=input("ingrese tags separados por espacios y el utimo es el pais ")
        lista=lista.split()
        person=Persona(lista[0],lista[1],lista[2],lista[3])

        for i in self.lista_paises:
            if i.nombre == lista[4]:
                i.lista_personas.append(person)
            

    def agregar_pais(self):
        input_usuario = input("ingrese pais que quiere agregar")
        nuevo_pais = Pais(input_usuario);
        self.lista_paises.append(nuevo_pais)

    def print_todo(self):
        for i in self.lista_paises:
            for j in i.lista_personas:
                print(i.nombre + " " + "las personas de este pais son" + " " + j.nombre+ "\n")
            
        
if __name__ == "__main__":#esto es para que corra en la consola
    Menu().run()
    

      
