from pydantic import ValidationError

from apps.books.schema.book_schema import BookCreateSchema
from apps.utils import BaseService


class BookService(BaseService):
    collection_name = 'book'

    def __init__(self):
        self.collection = self.db[self.collection_name]

    def get(self):
        res = self.collection.find()
        return res

    def create(self, data: BookCreateSchema):
        try:
            book = BookCreateSchema.parse_obj(data)
        except ValidationError as e:
            print(e)
            return e.json(), 400
        return self.collection.insert_one(book.json())

    def get_by_id(self, _id):
        pass

    def update(self, _id, data):
        pass

    def delete(self, _id):
        pass
