from flask import Flask, request, render_template, flash, redirect, url_for
from conexion import (conect_to_db, 
                      db_params,
                      get_all_persons,
                      get_by_id,
                      delete_by_id,
                      update_person_email,
                      get_person_deptos,
                      insert_person,
                      view_persons
                     )

## servidor-23\Scripts\activate.bat
## deactivate 



app = Flask('Api Test')

app.secretkey = 'secretkey'

@app.route('/', methods=['GET', 'POST', 'PUT'])
def Index():
    response = view_persons()
    return render_template('index.html', persons=response)

@app.route('/conect')
def conect():
    conect_to_db(db_params)
    return 'Connected to the database'

@app.route('/view_persons')
def view():
    response = view_persons()
    return render_template('index.html', persons=response)


@app.route('/all_persons')
def all_persons():
    response = get_all_persons()
    return response

@app.route('/get_person_by_id')
def get_person_by_id():
    id = request.args['id']
    response = get_by_id(id)
    return response

@app.route('/get_person_deptos')
def get_person_deptos_route():
    id = request.args['id']
    response = get_person_deptos(id)
    return response

@app.route('/insert_person')
def insert_person_route(): 
    name = request.args['name']
    last_name = request.args['last_name']
    if 'email' in request.args:
        email = request.args['email']
    else:
        email = None
    insert_person(name, last_name, email)
    
    return redirect(url_for('Index'))

@app.route('/delete_person_by_id')
def delete_person_by_id():
    id = request.args['id']
    delete_by_id(id) 
    return "delete successfuly"

@app.route('/update_email_person')
def update_person_email():
    id = request.args['id']
    email = request.args['email']
    update_person_email(id, email)
    return f'email address updated'       

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)