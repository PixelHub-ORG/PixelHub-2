from app.modules.pixchecker.repositories import PixcheckerRepository
from core.services.BaseService import BaseService


class PixcheckerService(BaseService):
    def __init__(self):
        super().__init__(PixcheckerRepository())
