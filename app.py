from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = '54.234.8.98'
app.config['MYSQL_USER'] = 'support'
app.config['MYSQL_PASSWORD'] = 'ratkiller1'
app.config['MYSQL_DB'] = 'TP'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Albergue')
    dataA=cur.fetchall()
    cur.execute('SELECT * FROM Desahuciado')
    dataD=cur.fetchall()
    return render_template('index.html', als=dataA, ds=dataD)

@app.route('/albergues',methods=['GET','POST'])
def albergues():

    if request.method == 'GET':
        data = {}
        cursor = mysql.connection.cursor()
        
        sql1 = "SELECT * FROM Albergue"
        cursor.execute(sql1)
        albergues = cursor.fetchall()
        data['albergues'] = albergues
        
        return jsonify(data)
	
    if request.method == 'POST':
        try:
            cursor = mysql.connection.cursor()
            
            sql1="""INSERT INTO Albergue (Nombre,Ciudad,Direccion,Telefono,Disponibilidad) VALUES ('{0}','{1}','{2}',{3},'{4}')""".format(request.form['1'],request.form['2'],request.form['3'],request.form['4'],request.form['5'])
            
            cursor.execute(sql1)
            mysql.connection.commit()
            #return jsonify({'mensaje':'Albergue registrado'})
            return redirect(url_for('index')) 
        except Exception as ex:
            return jsonify({'mensaje':'Error'})
        
		
def obtener_un_albergue(codigo):
    cursor = mysql.connection.cursor()
    sql="SELECT * FROM Albergue WHERE Id = {0}".format(codigo)
    cursor.execute(sql)
    albergue = cursor.fetchall()
    return jsonify(albergue)

def obtener_un_albergue2(codigo):
    cursor = mysql.connection.cursor()
    sql="SELECT * FROM Albergue WHERE Id = {0}".format(codigo)
    cursor.execute(sql)
    albergue = cursor.fetchall()
    return albergue

@app.route('/eliminaralbergue/<codigo>')
def albergue_eliminar(codigo):
    try:
        curso = obtener_un_albergue(codigo)
        if curso != None:
            cursor = mysql.connection.cursor()
            sql = "DELETE FROM Albergue WHERE Id = {0}".format(codigo)
            cursor.execute(sql)
            mysql.connection.commit()
            #return jsonify({'mensaje': "Albergue eliminado.", 'exito': True})
            return redirect(url_for('index')) 
        else:
            return jsonify({'mensaje': "Albergue no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})

@app.route('/editalbergue/<codigo>')
def albergue_editar(codigo):
    a = obtener_un_albergue2(codigo)
    print(a)
    return render_template('edit-a.html', a=a[0])

@app.route('/actualizaralbergue/<codigo>', methods=['POST'])
def albergue_actualizar(codigo):
    try:
        curso = obtener_un_albergue(codigo)
        if curso != None:
            cursor = mysql.connection.cursor()
            sql = """UPDATE Albergue SET Nombre = '{0}', Ciudad = '{1}' , Direccion = '{2}' , Telefono = {3} , Disponibilidad = '{4}' WHERE Id = {5}""".format(request.form['1'],request.form['2'],request.form['3'],request.form['4'],request.form['5'],codigo)
            cursor.execute(sql)
            mysql.connection.commit()
            #return jsonify({'mensaje': "Albergue actualizado.", 'exito': True})
            return redirect(url_for('index')) 
        else:
            return jsonify({'mensaje': "Albergue no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje':'Error'})

@app.route('/desahuciados',methods=['GET','POST'])
def desahuciados():

    if request.method == 'GET':
		
        data = {}
        cursor = mysql.connection.cursor()		
        sql2 = "SELECT * FROM Desahuciado"
        cursor.execute(sql2)
        desahuciados = cursor.fetchall()
        data['desahuciados'] = desahuciados		
        return jsonify(data)   

    if request.method == 'POST':
        try:
            cursor = mysql.connection.cursor()
            
            sql2="""INSERT INTO Desahuciado (Nombre,Ciudad,Telefono,Edad,Distrito,Sexo) VALUES ('{0}','{1}',{2},{3},'{4}','{5}')""".format(request.form['1'],request.form['2'],request.form['3'],request.form['4'],request.form['5'],request.form['6'])
            
            cursor.execute(sql2)
            mysql.connection.commit()
            #return jsonify({'mensaje':'Desahuciado registrado'})
            return redirect(url_for('index')) 
        except Exception as ex:
            return jsonify({'mensaje':'Error'})		
        

def obtener_un_desahuciado(codigo):
    cursor = mysql.connection.cursor()
    sql="SELECT * FROM Desahuciado WHERE Id = {0}".format(codigo)
    cursor.execute(sql)
    desahuciado = cursor.fetchall()
    return jsonify(desahuciado)
def obtener_un_desahuciado2(codigo):
    cursor = mysql.connection.cursor()
    sql="SELECT * FROM Desahuciado WHERE Id = {0}".format(codigo)
    cursor.execute(sql)
    desahuciado = cursor.fetchall()
    return desahuciado

@app.route('/eliminardesahuciado/<codigo>')
def desahuciado_eliminar(codigo):  
    try:
        curso = obtener_un_desahuciado(codigo)
        if curso != None:
            cursor = mysql.connection.cursor()
            sql = "DELETE FROM Desahuciado WHERE Id = {0}".format(codigo)
            cursor.execute(sql)
            mysql.connection.commit()
            #return jsonify({'mensaje': "Desahuciado eliminado.", 'exito': True})
            return redirect(url_for('index')) 
        else:
            return jsonify({'mensaje': "Desahuciado no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})  
    
@app.route('/editdesahuciado/<codigo>')
def desahuciado_editar(codigo):
    d = obtener_un_desahuciado2(codigo)
    return render_template('edit-d.html', d=d[0])

@app.route('/actualizardesahuciado/<codigo>', methods=['POST'])
def desahuciado_actualizar(codigo):
    try:
        curso = obtener_un_desahuciado2(codigo)
        if curso != None:
            cursor = mysql.connection.cursor()
            sql = """UPDATE Desahuciado SET Nombre = '{0}', Ciudad = '{1}' , Telefono = {2} , Edad = {3} , Distrito = '{4}' , Sexo = '{5}' WHERE Id = {6}""".format(request.form['1'],request.form['2'],request.form['3'],request.form['4'],request.form['5'],request.form['6'],codigo)
            cursor.execute(sql)
            mysql.connection.commit()
            #return jsonify({'mensaje': "Desahuciado actualizado.", 'exito': True})
            return redirect(url_for('index')) 
        else:
            return jsonify({'mensaje': "Desahuciado no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje':'Error'})

if __name__ == '__main__':
    app.run(debug=True, port=5050)     
