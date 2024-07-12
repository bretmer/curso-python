"""creando variables y funcion"""
saludo:str="hola a todos "

numero:int=45

verdadero:bool=True

alumnos:list=["jorge","jose","ana","percy","ruth"]

mascotas:tuple=(
    {
        "nombre":"alvarez",
        "edad":36,
        "curso":"programacion"
    },
    {
       "nombre":"salvador",
        "edad":40,
        "curso":"mantenimiento" 
    }
)

def promedio(alum1,alum2,alum3):
    """funcion para promediar notas"""
    suma:int=alum1+alum2+alum3
    media:float=suma/3
    return media
