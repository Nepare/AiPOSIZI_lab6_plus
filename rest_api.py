import json

from bottle import (
    debug,
    route,
    template,
    request,
    run,
    abort,
    redirect,
    Bottle,
    post,
    get
)
import logging
import settings


@get("/<model>/get/")
def get(model, db):
    data_list = db.execute(f"SELECT * FROM {settings.MODELS[model]};").fetchall()
    dict_of_models = {}
    for i in range(len(data_list)):
        dict_of_models[i] = dict(data_list[i])
    return dict_of_models


@post("/<model>/create/")
def create(model, db):
    dict_of_post_data = json.load(request.body)
    tuple_of_post_data = tuple(dict_of_post_data.values())

    match model:
        case "users":
            db.execute(
                '''
                INSERT INTO Users (name, email, password)
                VALUES (?, ?, ?);
                ''', tuple_of_post_data
            )
        case "products":
            db.execute(
                '''
                INSERT INTO Products (name, price, category_name)
                VALUES (?, ?, ?);
                ''', tuple_of_post_data
            )
        case "orders":
            db.execute(
                '''
                INSERT INTO Orders (user_id, product_name, quantity)
                VALUES (?, ?, ?);
                ''', tuple_of_post_data
            )
        case "categories":
            db.execute(
                '''
                INSERT INTO Categories (name)
                VALUES (?);
                ''', tuple_of_post_data
            )

    db.commit()


@post("/<model>/edit/")
def edit(model, db):
    dict_of_post_data = json.load(request.body)
    tuple_of_post_data = tuple(dict_of_post_data.values())

    match model:
        case "users":
            db.execute(
                '''
                UPDATE Users
                SET name = ?, email = ?, password = ?
                WHERE id = ?;
                ''', tuple_of_post_data
            )
        case "products":
            db.execute(
                '''
                UPDATE Products
                SET name = ?, price = ?, category_name = ?
                WHERE id = ?;
                ''', tuple_of_post_data
            )
        case "orders":
            db.execute(
                '''
                UPDATE Orders
                SET user_id = ?, product_name = ?, quantity = ?
                WHERE id = ?;
                ''', tuple_of_post_data
            )
        case "categories":
            db.execute(
                '''
                UPDATE Categories
                SET name = ?
                WHERE id = ?;
                ''', tuple_of_post_data
            )

    db.commit()


@post('/<model>/delete/')
def delete(model, db):
    dict_of_post_data = json.load(request.body)
    tuple_of_post_data = tuple(dict_of_post_data.values())
    db.execute(f"DELETE FROM {settings.MODELS[model]} WHERE id={tuple_of_post_data[0]};")
    db.commit()


debug(settings.DEBUG)
run(host=settings.HOST, port=settings.API_PORT, reloader=True)
