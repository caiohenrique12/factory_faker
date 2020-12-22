from factory_faker import factory_faker

def test_city_name():
    assert FactoryFaker.city_name() == 'Fortaleza'

def test_state_name():
    assert FactoryFaker.state_name() == 'Ceará'
