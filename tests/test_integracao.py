def test_index_ok(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert 'Aplicação está no ar - OK' in resp.json().get('message')