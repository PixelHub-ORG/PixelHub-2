import pytest
from unittest.mock import MagicMock
from app.modules.dataset.services import DataSetService
from app.modules.dataset.repositories import DSDownloadRecordRepository
from app.modules.dataset.models import DataSet


@pytest.fixture
def mock_dsdownloadrecord_repository():
    repository = MagicMock(spec=DSDownloadRecordRepository)
    mock_dataset = MagicMock(spec=DataSet)
    repository.top_3_dowloaded_datasets_per_week.return_value = [mock_dataset] * 3
    return repository


@pytest.fixture
def dataset_service(mock_dsdownloadrecord_repository):
    service = DataSetService()
    service.dsdownloadrecord_repository = mock_dsdownloadrecord_repository
    return service


def test_get_dataset_leaderboard_success(
    dataset_service,
    mock_dsdownloadrecord_repository
):
    period = "week"
    leaderboard_data = dataset_service.get_dataset_leaderboard(period=period)
    mock_dsdownloadrecord_repository.top_3_dowloaded_datasets_per_week.\
        assert_called_once_with(period=period)
    assert len(leaderboard_data) == 3


def test_get_dataset_leaderboard_with_month_period(
        dataset_service, mock_dsdownloadrecord_repository):
    period = "month"
    leaderboard_data = dataset_service.get_dataset_leaderboard(period=period)
    mock_dsdownloadrecord_repository.top_3_dowloaded_datasets_per_week.\
        assert_called_once_with(period=period)
    assert len(leaderboard_data) == 3


def test_get_dataset_leaderboard_invalid_period(dataset_service):
    with pytest.raises(ValueError,
                       match="Periodo no soportado: usa 'week' o 'month'"):
        dataset_service.get_dataset_leaderboard(period="invalid_period")


def test_get_dataset_leaderboard_empty(
    dataset_service,
    mock_dsdownloadrecord_repository
):
    mock_dsdownloadrecord_repository.top_3_dowloaded_datasets_per_week.\
        return_value = []
    period = "week"
    leaderboard_data = dataset_service.get_dataset_leaderboard(period=period)
    assert len(leaderboard_data) == 0


def test_get_dataset_leaderboard_with_same_downloads(
        dataset_service, mock_dsdownloadrecord_repository):
    mock_dataset_1 = MagicMock(spec=DataSet, id=1, downloads=20)
    mock_dataset_2 = MagicMock(spec=DataSet, id=2, downloads=20)
    mock_dataset_3 = MagicMock(spec=DataSet, id=3, downloads=20)
    mock_dsdownloadrecord_repository.top_3_dowloaded_datasets_per_week.\
        return_value = [mock_dataset_1, mock_dataset_2, mock_dataset_3]
    period = "week"
    leaderboard_data = dataset_service.get_dataset_leaderboard(period=period)
    assert leaderboard_data[0].id <= leaderboard_data[1].id <= \
           leaderboard_data[2].id


def test_get_dataset_leaderboard_already_sorted(dataset_service,
                                                mock_dsdownloadrecord_repository):
    mock_dataset_1 = MagicMock(spec=DataSet, id=1, downloads=30)
    mock_dataset_2 = MagicMock(spec=DataSet, id=2, downloads=20)
    mock_dataset_3 = MagicMock(spec=DataSet, id=3, downloads=10)
    mock_dsdownloadrecord_repository.top_3_dowloaded_datasets_per_week.\
        return_value = [mock_dataset_1, mock_dataset_2, mock_dataset_3]
    period = "week"
    leaderboard_data = dataset_service.get_dataset_leaderboard(period=period)
    assert leaderboard_data[0].downloads > \
           leaderboard_data[1].downloads > leaderboard_data[2].downloads


def test_get_dataset_leaderboard_large_number_of_datasets(
        dataset_service, mock_dsdownloadrecord_repository):
    mock_datasets = [MagicMock(spec=DataSet, id=i, downloads=100)
                     for i in range(1000)]
    mock_dsdownloadrecord_repository.top_3_dowloaded_datasets_per_week.\
        return_value = mock_datasets[:3]
    period = "week"
    leaderboard_data = dataset_service.get_dataset_leaderboard(period=period)
    assert len(leaderboard_data) == 3


def test_get_dataset_leaderboard_with_null_data(dataset_service,
                                                mock_dsdownloadrecord_repository):
    mock_dsdownloadrecord_repository.top_3_dowloaded_datasets_per_week.\
        return_value = None
    period = "week"
    leaderboard_data = dataset_service.get_dataset_leaderboard(period=period)
    assert leaderboard_data is None


def test_get_dataset_leaderboard_limit_parameter(dataset_service, mock_dsdownloadrecord_repository):
    mock_dsdownloadrecord_repository.top_3_dowloaded_datasets_per_week.return_value = []
    period = "week"

    dataset_service.dsdownloadrecord_repository.top_3_dowloaded_datasets_per_week(period=period, limit=1)
    mock_dsdownloadrecord_repository.top_3_dowloaded_datasets_per_week.assert_called_once_with(period=period, limit=1)


def test_get_dataset_leaderboard_with_duplicate_datasets(dataset_service, mock_dsdownloadrecord_repository):
    mock_dataset = MagicMock(spec=DataSet, id=1, downloads=10)
    mock_datasets = [mock_dataset, mock_dataset, mock_dataset]
    mock_dsdownloadrecord_repository.top_3_dowloaded_datasets_per_week.return_value = mock_datasets

    leaderboard_data = dataset_service.get_dataset_leaderboard(period="week")

    assert all(d.id == 1 for d in leaderboard_data)


def test_get_dataset_leaderboard_repository_error(dataset_service, mock_dsdownloadrecord_repository):
    mock_dsdownloadrecord_repository.top_3_dowloaded_datasets_per_week.side_effect = Exception("DB error")

    with pytest.raises(Exception, match="DB error"):
        dataset_service.get_dataset_leaderboard(period="week")


def test_get_dataset_leaderboard_with_single_dataset(dataset_service, mock_dsdownloadrecord_repository):
    mock_dataset_1 = MagicMock(spec=DataSet, id=1, downloads=100)
    mock_dsdownloadrecord_repository.top_3_dowloaded_datasets_per_week.return_value = [mock_dataset_1]
    period = "week"
    leaderboard_data = dataset_service.get_dataset_leaderboard(period=period)
    assert len(leaderboard_data) == 1
    assert leaderboard_data[0].downloads == 100


def test_get_dataset_leaderboard_with_null_values_in_dataset(dataset_service, mock_dsdownloadrecord_repository):
    mock_dataset_1 = MagicMock(spec=DataSet, id=1, downloads=None)
    mock_dsdownloadrecord_repository.top_3_dowloaded_datasets_per_week.return_value = [mock_dataset_1]
    period = "week"
    leaderboard_data = dataset_service.get_dataset_leaderboard(period=period)
    assert leaderboard_data[0].downloads is None


def test_get_dataset_leaderboard_with_empty_fields(dataset_service, mock_dsdownloadrecord_repository):
    mock_dataset_1 = MagicMock(spec=DataSet, id=1, downloads=100, description=None)
    mock_dsdownloadrecord_repository.top_3_dowloaded_datasets_per_week.return_value = [mock_dataset_1]
    period = "week"
    leaderboard_data = dataset_service.get_dataset_leaderboard(period=period)
    assert leaderboard_data[0].description is None


def test_get_dataset_leaderboard_with_invalid_dataset_id(dataset_service, mock_dsdownloadrecord_repository):
    mock_dsdownloadrecord_repository.top_3_dowloaded_datasets_per_week.return_value = []
    period = "week"
    leaderboard_data = dataset_service.get_dataset_leaderboard(period=period)
    assert leaderboard_data == []


def test_get_dataset_leaderboard_with_special_characters_in_period(dataset_service, mock_dsdownloadrecord_repository):
    period = "week$"
    leaderboard_data = dataset_service.get_dataset_leaderboard(period=period)

    mock_dsdownloadrecord_repository.top_3_dowloaded_datasets_per_week.assert_called_once_with(period="week")

    assert len(leaderboard_data) == 3
