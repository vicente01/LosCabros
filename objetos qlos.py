class persona:
    def __init__(self,nombre,apellido,correo,emei):
    	self.nombre=nombre
    	self.apellido=apellido
    	self.correo=correo
    	self.emei=emei
    	self.reporte=[]

    def agregar_reporte(self,latitud,longitud,error_maximo,tiempo,actividad,probabilidad):
        que=reporte(latitud,longitud,error_maximo,tiempo,actividad,probabilidad)
        self.reporte.append(que.reporte2)

        

class reporte:
    def __init__(self,latitud,longitud,error_maximo,tiempo,actividad,probabilidad):
        self.reporte2=[latitud,longitud,error_maximo,tiempo,actividad,probabilidad]


p=persona("nicolas","aguirre","nnaguirre","chupalla")
d=reporte("12","13","10","1","fubol","0,1")


p.agregar_reporte("12","13","10","1","fubol","0,1")
p.agregar_reporte("11","14141","114121","F","f","0,2")
print (p.reporte)
