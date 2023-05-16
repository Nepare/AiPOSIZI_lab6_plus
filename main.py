from bottle import (
    debug,
    route, 
    template, 
    request,
    run,
    abort,
    redirect,
)
import logging
import requests
import settings

API_MODE = True


@route("/")
def index():
    logging.info("go / by GET request")
    return template("index.tpl")


@route("/<model>/get/")
def get(model, db):
    logging.info("go /%s/get/ by GET request", model)
    if (model := model.lower()) not in settings.MODELS:
        logging.warning("path /%s/get/ not found", model)    
        abort(404, "Not Found")
    
    data_list = {}
    if API_MODE:
        request_str = "http://" + "localhost" + ":" + str(settings.API_PORT) + "/" + str(model) + "/get/"
        data_list = requests.get(request_str).json()
    else:
        db_table = db.execute(f"SELECT * FROM {settings.MODELS[model]};").fetchall()
        data_list = {}
        for i in range(len(db_table)):
            data_list[i] = dict(db_table[i])
    return template("get.tpl", data_list=data_list, model=model)        


@route("/<model>/create/")
@route("/<model>/create/", method="POST")
def create(model, db):
    if (model := model.lower()) not in settings.MODELS:
        logging.warning("path /%s/create/ not found", model)    
        abort(404, "Not Found")

    if request.method == "GET":
        logging.info("return create form by GET request for path /%s/create/", model)
        return template(f"create_form_{settings.MODELS[model]}.tpl")   
    
    logging.info("read form data by POST request for path /%s/create/", model)
    if API_MODE:
        request_str = "http://" + "localhost" + ":" + str(settings.API_PORT) + "/" + str(model) + "/create/"
        data_dict = {}
        match model:
            case "users":
                data_dict = {"name": request.forms.name,
                             "email": request.forms.email,
                             "password": request.forms.password}
            case "products":
                data_dict = {"name": request.forms.name,
                             "price": request.forms.price,
                             "category_name": request.forms.category_name}
            case "orders":
                data_dict = {"user_id": request.forms.user_id,
                             "product_name": request.forms.product_name,
                             "quantity": request.forms.quantity}
            case "categories":
                data_dict = {"name": request.forms.name}

        requests.post(request_str, json=data_dict)
    else:
        match model:
            case "users":
                db.execute(
                    '''
                    INSERT INTO Users (name, email, password)
                    VALUES (?, ?, ?);
                    ''', (request.forms.name, request.forms.email, request.forms.password)
                )
            case "products":
                db.execute(
                    '''
                    INSERT INTO Products (name, price, category_name)
                    VALUES (?, ?, ?);
                    ''', (request.forms.name, request.forms.price, request.forms.category_name)
                )
            case "orders":
                db.execute(
                    '''
                    INSERT INTO Orders (user_id, product_name, quantity)
                    VALUES (?, ?, ?);
                    ''', (request.forms.user_id, request.forms.product_name, request.forms.quantity)
                )
            case "categories":
                db.execute(
                    '''
                    INSERT INTO Categories (name)
                    VALUES (?);
                    ''', (request.forms.name,)
                )
        db.commit()

    logging.info("redirect to /%s/get/ path after creating object", model)
    redirect(f"/{model}/get/")

        
@route("/<model>/delete/")
@route("/<model>/delete/", method="POST")
def delete(model, db):
    if (model := model.lower()) not in settings.MODELS:
        logging.warning("path /%s/delete/ not found", model)    
        abort(404, "Not Found")

    if request.method == "GET":
        logging.info("return delete form by GET request for path /%s/delete/", model)
        return template(f"delete.tpl", model=model)

    logging.info("read form data by POST request for path /%s/delete/", model)

    if API_MODE:
        request_str = "http://" + "localhost" + ":" + str(settings.API_PORT) + "/" + str(model) + "/delete/"
        data_dict = {"id": request.forms.id}
        requests.post(request_str, json=data_dict)
    else:
        db.execute(f"DELETE FROM {settings.MODELS[model]} WHERE id={request.forms.id};")
        db.commit()
    logging.info("redirect to /%s/get/ path after deleting object", model)
    redirect(f"/{model}/get/")
        

@route("/<model>/edit/")    
@route("/<model>/edit/", method="POST")
def edit(model, db):
    if (model := model.lower()) not in settings.MODELS:
        logging.warning("path /%s/edit/ not found", model)    
        abort(404, "Not Found")

    if request.method == "GET":
        logging.info("return edit form by GET request for path /%s/edit/", model)
        return template(f"edit_form_{settings.MODELS[model]}.tpl")   

    logging.info("read form data by POST request for path /%s/edit/", model)
    if API_MODE:
        request_str = "http://" + "localhost" + ":" + str(settings.API_PORT) + "/" + str(model) + "/edit/"
        data_dict = {}
        match model:
            case "users":
                data_dict = {"new_name": request.forms.new_name,
                             "new_email": request.forms.new_email,
                             "new_password": request.forms.new_password,
                             "id": request.forms.id}
            case "products":
                data_dict = {"new_name": request.forms.new_name,
                             "new_price": request.forms.new_price,
                             "new_category": request.forms.new_category,
                             "id": request.forms.id}
            case "orders":
                data_dict = {"new_user_id": request.forms.new_user_id,
                             "new_product_name": request.forms.new_product_name,
                             "new_quantity": request.forms.new_quantity,
                             "id": request.forms.id}
            case "categories":
                data_dict = {"new_name": request.forms.new_name,
                             "id": request.forms.id}
        requests.post(request_str, json=data_dict)
    else:
        match model:
            case "users":
                db.execute(
                    '''
                    UPDATE Users
                    SET name = ?, email = ?, password = ?
                    WHERE id = ?;
                    ''', (
                        request.forms.new_name,
                        request.forms.new_email,
                        request.forms.new_password,
                        request.forms.id
                    )
                )
            case "products":
                db.execute(
                    '''
                    UPDATE Products
                    SET name = ?, price = ?, category_name = ?
                    WHERE id = ?;
                    ''', (
                        request.forms.new_name,
                        request.forms.new_price,
                        request.forms.new_category,
                        request.forms.id
                    )
                )
            case "orders":
                db.execute(
                    '''
                    UPDATE Orders
                    SET user_id = ?, product_name = ?, quantity = ?
                    WHERE id = ?;
                    ''', (
                        request.forms.new_user_id,
                        request.forms.new_product_name,
                        request.forms.new_quantity,
                        request.forms.id
                    )
                )
            case "categories":
                db.execute(
                    '''
                    UPDATE Categories
                    SET name = ?
                    WHERE id = ?;
                    ''', (
                        request.forms.new_name,
                        request.forms.id
                    )
                )

        db.commit()
    logging.info("redirect to /%s/get/ path after editing object", model)
    redirect(f"/{model}/get/")
    

if __name__ == "__main__":
    debug(settings.DEBUG)
    run(host=settings.HOST, port=settings.PORT, reloader=True)
