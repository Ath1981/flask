from flask import Flask,jsonify,request
import pymysql.cursors

app = Flask(__name__)


def connection_mysql():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 database='ddd',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

personas = ["brayan","juan","pablo"]


@app.route("/")
def hello_world():
    return jsonify(personas)



@app.route('/personas', methods=['GET'])
def index():
    lista_personas = [
        {'name': 'Adriana Torres Hoyos'},
        {'name': 'Danilo Mendoza'},
        {'name': 'Carlos Toscano'},
        {'name': 'Julio Castillo'}

    ]
    return jsonify(lista_personas)



@app.route('/usuarios', methods=["POST"])
def create():
    
    data = request.get_json()
    connection = connection_mysql()

    with connection:
        with connection.cursor() as cursor:

            sql = "INSERT INTO personas (NOMBRE, APELLIDO, CELULAR, EMAIL) VALUES (%s, %s,%s, %s)"
            cursor.execute(sql, (data['NOMBRE'], data ['APELLIDO'],data ['CELULAR'],data ['EMAIL'])) 

        connection.commit()

    return jsonify({
    'message': 'Creacion exitosa'
 }), 201      
    
@app.route('/usuarios', methods=["GET"])
def mostrar():

    connection = connection_mysql()

    with connection:
        with connection.cursor() as cursor:

            sql = "SELECT * FROM personas" 
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
    return jsonify(result)

@app.route('/update/<id>', methods=["PUT"])
def update(id):
    
    data = request.get_json()
    connection = connection_mysql()

    with connection:
        with connection.cursor() as cursor:

            sql = "UPDATE personas SET NOMBRE = %s, APELLIDO = %s, CELULAR= %s, EMAIL= %s WHERE id = %s"
            cursor.execute(sql, (data['NOMBRE'], data ['APELLIDO'],data ['CELULAR'],data ['EMAIL'],id)) 

        connection.commit()

    return jsonify({
    'message': 'update exitoso'
 }), 201      

@app.route('/delete/<id>', methods=["DELETE"])
def delecte(id):
    
    connection = connection_mysql()

    with connection:
        with connection.cursor() as cursor:

            sql = "DELETE FROM personas WHERE id = %s"
            cursor.execute(sql,(id,)) 

        connection.commit()
    return jsonify({'message': 'Eliminado con exito'})
    
if __name__ == '__main__':
    app.run(debug=True)    
    