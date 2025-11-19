import logging

from flask import render_template

from app.modules.dataset.services import DataSetService
from app.modules.filemodel.services import FilemodelService
from app.modules.public import public_bp

logger = logging.getLogger(__name__)


@public_bp.route("/")
def index():
    logger.info("Access index")
    dataset_service = DataSetService()
    file_model_service = FilemodelService()

    # Statistics: total datasets and feature models
    datasets_counter = dataset_service.count_synchronized_datasets()
    file_models_counter = file_model_service.count_file_models()
    # Statistics: total downloads
    total_dataset_downloads = dataset_service.total_dataset_downloads()
    total_file_model_downloads = file_model_service.total_file_model_downloads()

    # Statistics: total views
    total_dataset_views = dataset_service.total_dataset_views()
    total_file_model_views = file_model_service.total_file_model_views()
    return render_template(
        "public/index.html",
        datasets=dataset_service.latest_synchronized(),
        datasets_counter=datasets_counter,
        file_models_counter=file_models_counter,
        total_dataset_downloads=total_dataset_downloads,
        total_file_model_downloads=total_file_model_downloads,
        total_dataset_views=total_dataset_views,
        total_file_model_views=total_file_model_views,
    )
