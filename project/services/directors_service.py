from project.config import ITEMS_PER_PAGE
from project.dao import DirectorDAO
from project.exceptions import ItemNotFound
from project.schemas.director import DirectorSchema
from project.services.base import BaseService


class DirectorsService(BaseService):
    def get_item_by_id(self, pk):
        director = DirectorDAO(self._db_session).get_by_id(pk)
        if not director:
            raise ItemNotFound
        return DirectorSchema().dump(director)

    def get_all_directors(self):
        directors = DirectorDAO(self._db_session).get_all()
        return DirectorSchema(many=True).dump(directors)

    # def get_all_directors(self, page):
    #     directors = DirectorDAO(self._db_session).get_all().paginate(page, per_page=ITEMS_PER_PAGE, error_out=False)
    #     return DirectorSchema(many=True).dump(directors)

