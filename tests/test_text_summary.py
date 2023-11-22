import pytest
from fastapi.testclient import TestClient

from app.main import create_app
from tests import test_data


@pytest.fixture
def client():
    app = create_app()
    return TestClient(app)


def test_summary(client):
    response = client.post(
        "/text-summary",
        json={
            'text': test_data.ARTICLE_1,
        }
    )
    assert response.status_code == 200
    assert response.json() == {'summary': test_data.SUMMARY_1}
