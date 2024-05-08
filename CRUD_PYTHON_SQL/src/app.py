from flask import  Flask, render_template,request, redirect,url_for
import  os
import database as db

template_dir= os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir= os.path.join(template_dir,'src','template')

app=Flask(__name__,template_folder=template_dir)

#ruta de la aplicacion
@app.route('/')
def home():
    cursor=db.database.cursor()
    cursor.execute("SELECT * FROM tabla_api")
    myresult=cursor.fetchall()
    #Convertir datos a diccionarios
    insertObject=[]
    columNames=[column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columNames,record)))
    cursor.close()
    return render_template('index.html',data=insertObject)

#Agregar
@app.route('/datos',methods=['POST'])
def addUs():
    placa=request.form['placa']
    pos_ini=request.form['pos_ini']
    pos_fin=request.form['pos_fin']

    if  placa and pos_ini and pos_fin:
        cursor=db.database.cursor()
        sql="INSERT INTO tabla_api(placa, pos_ini, pos_fin) VALUES (%s, %s, %s)"
        data=(placa, pos_ini, pos_fin)
        cursor.execute(sql,data)
        db.database.commit()
    return redirect(url_for('home'))

#ELIMNIAR
@app.route('/delete/<string:id_vehiculo>')
def delete(id_vehiculo):
    cursor = db.database.cursor()
    sql="DELETE FROM tabla_api WHERE id_vehiculo= %s"
    data = (id_vehiculo,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))

#ACTUALIZAR
@app.route('/editar/<string:id_vehiculo>',methods=['POST'])
def EditUs(id_vehiculo):
    placa=request.form['placa']
    pos_ini=request.form['pos_ini']
    pos_fin=request.form['pos_fin']

    if  placa and pos_ini and pos_fin:
        cursor=db.database.cursor()
        sql="UPDATE tabla_api SET placa=%s, pos_ini=%s, pos_fin=%s WHERE id_vehiculo=%s"
        data=(placa, pos_ini, pos_fin,id_vehiculo)
        cursor.execute(sql,data)
        db.database.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, port=4000)