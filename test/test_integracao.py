def test_index_ok(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert 'qualidade_software' in resp.json().get('message')