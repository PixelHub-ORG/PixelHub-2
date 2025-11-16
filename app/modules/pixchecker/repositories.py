from app.modules.pixchecker.models import Pixchecker
from core.repositories.BaseRepository import BaseRepository


class PixcheckerRepository(BaseRepository):
    def __init__(self):
        super().__init__(Pixchecker)
