import sqlite3
miConexion=sqlite3.connect("base de datos primera")
miCursor=miConexion.cursor()
miCursor.execute("CREATE TABLE VENTA1 (NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER,SECCION VARCHAR(20))")
miCursor.execute("INSERT INTO VENTA VALUES ('BALON',8000,'DEPORTES')")
 
miConexion.commit()
miConexion.close()
