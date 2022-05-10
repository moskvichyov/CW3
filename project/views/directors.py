from flask_restx import abort, Namespace, Resource

from project.exceptions import ItemNotFound
from project.services import DirectorsService
from project.setup_db import db
from project.config import ITEMS_PER_PAGE
import paginate

directors_ns = Namespace("directors")


@directors_ns.route("/")
class DirectorsView(Resource):
    @directors_ns.response(200, "OK")
    def get(self, page=1):
        """Get all directors"""
        return DirectorsService(db.session).get_all_directors()
            # .paginate(page, per_page=ITEMS_PER_PAGE, error_out=False)


# @directors_ns.route("/<int: page>")
# class DirectorsView(Resource):
#     @directors_ns.response(200, "OK")
#     def get(self, page):
#         """Get all directors"""
#         return DirectorsService(db.session).get_all_directors(page)


@directors_ns.route("/<int:director_id>")
class DirectorView(Resource):
    @directors_ns.response(200, "OK")
    @directors_ns.response(404, "Director not found")
    def get(self, director_id: int):
        """Get director by id"""
        try:
            return DirectorsService(db.session).get_item_by_id(director_id)
        except ItemNotFound:
            abort(404, message="Director not found")
