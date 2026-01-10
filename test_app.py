from app import app

def test_name():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data ==b'If You Are Reading This you are going to hell with me :(' 