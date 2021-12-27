from _pytest.monkeypatch import MonkeyPatch
from src.db import DB
from test.mock_util import MockDynamo, MockUserTable
from test.expexted_data import expected_users

monkeypatch = MonkeyPatch()
db = DB()


def test_db_query():
    mock_dynamo = MockDynamo()
    monkeypatch.setattr(mock_dynamo, "Table", MockUserTable)
    monkeypatch.setattr(db, "dynamo", mock_dynamo)
    actual_users = db.query("1234")
    assert  actual_users == expected_users

