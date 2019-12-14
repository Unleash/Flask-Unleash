

def test_check_userId1(client):
    response = client.get('/check?userId=1')
    assert "True" in response.json


def test_check_userId3(client):
    response = client.get('/check?userId=3')
    assert "False" in response.json
