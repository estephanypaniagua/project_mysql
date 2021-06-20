from flask import Flask, flash, render_template, redirect, url_for, request, session
from dao.DAOUsuario import DAOUsuario

app = Flask(__name__)
app.secret_key = "Utec123"
db = DAOUsuario()

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/usuario/')
def usuario_index():
    data = db.read(None)

    return render_template('usuario/index.html',data = data)


@app.route('/usuario/add/')
def usuario_add():
    return render_template('usuario/add.html')

@app.route('/usuario/addusuario',methods=['POST','GET'])
def addusuario():
    if request.method == 'POST' and request.form['save']:
        db.insert(request.form)
        return redirect(url_for('usuario_index'))


@app.route('/usuario/update/<int:id>/')
def usuario_update(id):
    data=db.read(id)
    if len(data)==0:
        return redirect(url_for('usuario_index'))
    else:
        session['update'] = id
        return render_template('usuario/update.html',data=data)

@app.route('/usuario/updateusuario',methods=['POST'])
def updateusuario():
    if request.method == 'POST' and request.form['update']:
        db.update(session['update'],request.form)
        session.pop('delete',None)
        return redirect(url_for('usuario_index'))

@app.route('/usuario/deleteusuario',methods=['POST'])
def deleteusuario():
    if request.method == 'POST' and request.form['delete']:
        db.delete(session['delete'])
        session.pop('delete',None)
        return redirect(url_for('usuario_index'))

@app.route('/usuario/delete/<int:id>/')
def usuario_delete(id):
    data=db.read(id)
    if len(data)==0:
        return redirect(url_for('usuario_index'))
    else:
        session['delete'] = id
        return render_template('usuario/delete.html',data=data)




@app.route('/login')
def login():
    return render_template('login.html')


@app.errorhandler(404)
def page_not_found( error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True,port=3000, host="0.0.0.0")