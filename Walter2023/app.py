from flask import Flask, request, render_template, flash, redirect, url_for
from conexion import (conect_to_db, 
                      db_params,
                      get_all_persons,
                      get_by_id,
                      delete_person_by_id,
                      update_person_email,
                      get_person_deptos,
                      insert_person,
                      view_persons,
                      get_for_id,
                      update_person
                     )

## servidor-23\Scripts\activate.bat
## deactivate 



app = Flask('Api Test')

app.secretkey = 'secretkey'

@app.route('/', methods=['GET', 'POST', 'PUT'])
def Index():
    return render_template('index.html')

@app.route('/conect')
def conect():
    conect_to_db(db_params)
    return 'Connected to the database'

# ? new methods render templates
@app.route('/list_of_persons')
def view_list():
    response = view_persons()
    return render_template('list_of_persons.html', persons=response)
    
@app.route('/delete_person/', methods=['GET','POST'])
def delete_person():
    if request.method == 'GET':
        response = view_persons()
        return render_template('delete_person.html', persons=response)

@app.route('/delete/<id>')
def delete(id): 
    delete_person_by_id(id)
    return redirect(url_for('view_list'))

    
# @app.route('/delete_person_by_id')
# def delete_person_by_id():
#     id = request.args['id']
#     delete_by_id(id) 
#     return "delete successfuly"




@app.route('/set_person_in_db')
def view_form():
    return render_template('set_person_in_db.html')

@app.route('/update_person', methods=['GET'])
def view_update():
    if request.method == 'GET':
        response = view_persons()
        return render_template('update_person.html', persons=response)
  
  

    
@app.route('/form_update_person/<id>', methods=['GET','POST'])
def update_person_by_id(id):
    if request.method == 'GET':
        response = get_for_id(id)
        print(response[0])
        return render_template('form_update_person.html', person=response[0])
    else:
        name = request.form['name']
        last_name = request.form['last_name']
        email = request.form['email']
        update_person(id,name,last_name,email)
        return redirect(url_for('view_list'))
        

        
#  ? ----------------------------------------------

@app.route('/all_persons')
def all_persons():
    if request.form == 'GET':
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



# # ! view person
# @app.route('/view_insert_person')
# def form_insert_person():
#     return render_template('all_persons.html')


@app.route('/insert_person', methods=['GET','POST'])
def insert_person_route(): 
    if request.method == 'POST':
        name = request.form['name']
        last_name = request.form['last_name']
        if 'email' in request.form:
            email = request.form['email']
        else:
            email = None
        print(request.form)
        insert_person(name, last_name, email)
        return redirect(url_for('list_of_persons'))     
    elif request.method == 'GET':
        return redirect(url_for('list_of_persons'))
    else:
        print('error')


# @app.route('/insert_person')
# def insert_person_route(): 
#     name = request.args['name']
#     last_name = request.args['last_name']
#     if 'email' in request.args:
#         email = request.args['email']
#     else:
#         email = None
#     insert_person(name, last_name, email)
    
#     return redirect(url_for('Index'))

# @app.route('/delete_person_by_id')
# def delete_person_by_id():
#     id = request.args['id']
#     delete_by_id(id) 
#     return "delete successfuly"

@app.route('/update_email_person')
def update_person_email():
    id = request.args['id']
    email = request.args['email']
    update_person_email(id, email)
    return f'email address updated'       

# @app.route('/update_person/<id>', methods=['POST','GET'])
# def update(id):
#     if request.method == 'GET':
#         data = get_for_id(id)
#         print(data)
#         return render_template('form_update_person.html', person=data[0])
        

    

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)