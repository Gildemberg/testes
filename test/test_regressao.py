import json

def test_regressao_soma(client):
    resp = client.post('/soma/', data=json.dumps({'a': 2, 'b': 3}), content_type='application/json')
    assert resp.status_code == 200
    assert resp.json()['resultado'] == 5