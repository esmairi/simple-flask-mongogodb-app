import os
from flask import Blueprint, render_template, jsonify, request
from flask.views import MethodView
from apps.books.schema.book_schema import BookCreateSchema
from apps.books.services.book_service import BookService

bp_welcome = Blueprint('books', __name__, template_folder=os.path.join(os.pardir, "templates"))


class BaseService:
    def __init__(self):
        self.book_service = BookService()


class WelcomeGetterAPI(MethodView, BaseService):
    init_every_request = False

    def get(self, id):
        return self.book_service.get_by_id(id)

    def patch(self, id):
        return self.book_service.update(id, request.json)

    def delete(self, id):
        self.book_service.delete(id)
        return "", 204


class WelcomeDispatcherAPI(MethodView, BaseService):
    init_every_request = False

    def get(self):
        return self.book_service.get()

    def post(self):
        return self.book_service.create(request.json)


def register_api(app, name):
    getter = WelcomeGetterAPI.as_view(f"{name}-getter")
    dispatcher = WelcomeDispatcherAPI.as_view(f"{name}-dispatcher")
    app.add_url_rule(f"/<int:id>", view_func=getter)
    app.add_url_rule(f"/", view_func=dispatcher)


register_api(bp_welcome, 'books')
