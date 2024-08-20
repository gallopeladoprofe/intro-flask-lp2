# Data access object - DAO
from conexion.Conexion import Conexion

class CiudadDao:

    def getCiudades(self):

        ciudadSQL = """
        SELECT id, descripcion
        FROM ciudades
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(ciudadSQL)
            # trae datos de la bd
            lista_ciudades = cur.fetchall()
            # retorno los datos
            return lista_ciudades
        except con.Error as e:
            print(e)
        finally:
            cur.close()
            con.close()

    def guardarCiudad(self, descripcion):

        insertCiudadSQL = """
        INSERT INTO ciudades(descripcion) VALUES(%s)
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertCiudadSQL, (descripcion,))
            # se confirma la insercion
            con.commit()

            return True

        # Si algo fall entra aqui
        except con.Error as e:
            print(e)

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

        return False