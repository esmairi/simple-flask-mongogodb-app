import json


def test_1_get(app, client):
    res = client.get('/books/')
    assert res.status_code == 200
    expected = [[{"name": "foo"}, {"name": "bar"}]]
    assert expected == json.loads(res.get_data(as_text=True))


def test_2_get_by_id(app, client):
    res = client.get('/books/0')
    assert res.status_code == 200
    expected = {"name": "foo"}
    assert expected == json.loads(res.get_data(as_text=True))


def test_3_create(app, client):
    data = {"name": "adel"}
    res = client.post('/books/', json=data)
    print('status_codestatus_code',res.status_code)
    print(res)
    assert res.status_code == 201
    assert data == json.loads(res.get_data(as_text=True))
    res = client.get('/books/2')
    assert data == json.loads(res.get_data(as_text=True))


def test_3_update(app, client):
    data = {'name': 'mounir'}
    res = client.patch('/books/0', json=data)
    assert res.status_code == 202
    assert data == json.loads(res.get_data(as_text=True))
    res = client.get('/books/0')
    assert data == json.loads(res.get_data(as_text=True))


def test_4_delete(app, client):
    res = client.delete('/books/0')
    assert res.status_code == 204

