import json

def test_regressao_soma(client):
    resp = client.post('/soma/', data=json.dumps({'a': 2, 'b': 3}), content_type='application/json')
    assert resp.status_code == 200
    assert resp.json()['resultado'] == 5

def test_regressao_subtracao(client):
    resp = client.post('/subtracao/', data=json.dumps({'a': 21, 'b': 3}), content_type='application/json')
    assert resp.status_code == 200
    assert resp.json()['resultado'] == 18

def test_regressao_multiplicacao(client):
    resp = client.post('/multiplicacao/', data=json.dumps({'a': 5, 'b': 5}), content_type='application/json')
    assert resp.status_code == 200
    assert resp.json()['resultado'] == 25

def test_regressao_divisao(client):
    resp = client.post('/divisao/', data=json.dumps({'a': 6, 'b': 3}), content_type='application/json')
    assert resp.status_code == 200
    assert resp.json()['resultado'] == 2
    
def test_regressao_divisao_por_zero(client):
    resp = client.post('/divisao/', data=json.dumps({'a': 6, 'b': 0}), content_type='application/json')
    assert resp.status_code == 400
    assert resp.json()['erro'] == 'Divisão por zero não é permitida'