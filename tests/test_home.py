def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200
    expected = '<h1>Hello</h1>'
    assert expected in res.get_data(as_text=True)