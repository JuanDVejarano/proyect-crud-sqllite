#Gestion de datos
import sqlite3 as sql

#Crear base de datos
def crearDB():
    conn = sql.connect("/home/juanj/Projects-Python/proyect-crud-sqllite/src/Estudiantes.db")
    conn.commit()
    conn.close()

#enviar instruccion
def setDataBase(instruccion):
    conn = sql.connect("/home/juanj/Projects-Python/proyect-crud-sqllite/src/Estudiantes.db")
    cursor = conn.cursor()
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

#Obtener datos segun instruccion
def getDataBase(instruccion):
    conn = sql.connect("/home/juanj/Projects-Python/proyect-crud-sqllite/src/Estudiantes.db")
    cursor = conn.cursor()
    cursor.execute(instruccion)
    registros = cursor.fetchall()
    conn.close()
    return registros

#Crear tabla
def crear_tabla():
    setDataBase("""CREATE TABLE T_Estudiantes(
                    ID integer,
                    nombre text,
                    correo text
                    )
                    """)

#Insertar registros
def insertarRegistro(ID,nombre,correo):
    instruccion = f"INSERT INTO T_Estudiantes VALUES ('{ID}',' {nombre}',' {correo}')" 
    setDataBase(instruccion)

#Consultar registros
def consultarRegistros():
    instruccion = f"SELECT * FROM T_Estudiantes"
    return getDataBase(instruccion)

#Actualizar registros
def actualizarRegistro(ID,nombre,correo):
    instruccion = f"UPDATE T_Estudiantes SET nombre = '{nombre}', correo = '{correo}' WHERE ID = '{ID}'"
    setDataBase(instruccion)

#Eliminar registros
def eliminarRegistro(ID):
    instruccion = f"DELETE FROM T_Estudiantes WHERE ID = '{ID}'"
    setDataBase(instruccion)

def buscarRegistro(ID):
    instruccion = f"SELECT * FROM T_Estudiantes WHERE ID = '{ID}'"
    return getDataBase(instruccion)

#buscar por nombre
def buscarRegistroNombre(nombre):
    instruccion = f"SELECT nombre FROM T_Estudiantes WHERE nombre like '%{nombre}%'"
    return getDataBase(instruccion)
    

#PP
if __name__ == "__main__":
    #crearDB()
    #crear_tabla()
    #insertarRegistro(123,"Carolina Ruiz","Carolina@gmail.com")
    #insertarRegistro(777,"Pedro Demalas","pdemalas@gmail.com")
    #actualizarRegistro(777,"Carolina Ruiz","correonuevo@gmail.com")
    #insertarRegistro(888,"Claudia torres","pdemalas@gmail.com")
    #insertarRegistro(999,"Roberto de Niro","rdeniro@gmail.com")
    #insertarRegistro(555,"Fernando Ramirez","framirez@gmail.com")
    #insertarRegistro(666,"Angie Gomez","agonmez@gmail.com")
    #print(consultarRegistros())
    #print(buscarRegistro(555))
    print(buscarRegistroNombre("o"))
