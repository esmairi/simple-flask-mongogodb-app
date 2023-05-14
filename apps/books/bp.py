from apps.books.views.book_view import bp_welcome


def register_welcome_app(app):
    """
    TODO
    :param app:
    :return:
    """
    app.register_blueprint(bp_welcome, url_prefix='/books')