from app.modules.basedataset.models import Basedataset
from core.repositories.BaseRepository import BaseRepository


class BasedatasetRepository(BaseRepository):
    def __init__(self):
        super().__init__(Basedataset)
