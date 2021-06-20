import pymysql

class DAOUsuario:

    def __init__(self):
        pass

    def connect(self):
        return pymysql.connect(host="localhost",user="root",password="",database="proyecto_db")

    def read(self,id):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM usuario order by nombre")
            else:
                cursor.execute("SELECT * FROM usuario where id = %s order by nombre",(id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self,data):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("INSERT INTO usuario(nombre, telefono, email) VALUES(%s,%s,%s)",(data['nombre'], data['telefono'], data['email'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
    
    def update(self,id,data):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE usuario SET nombre=%s, telefono=%s, email=%s where id = %s",(data['nombre'], data['telefono'], data['email'],id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def delete(self,id):
        con = DAOUsuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("delete from usuario where id = %s",(id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
