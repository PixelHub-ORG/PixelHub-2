from app.modules.basedataset.repositories import BasedatasetRepository
from core.services.BaseService import BaseService


class BasedatasetService(BaseService):
    def __init__(self):
        super().__init__(BasedatasetRepository())
