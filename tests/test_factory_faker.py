from factory_faker import Faker
import re

def test_city_name():
    assert re.match("[a-zA-Z]", Faker().city_name())

def test_state_name_not_abbreviated():
    assert re.match("[a-zA-Z]", Faker().state_name())

def test_state_name_abbreviated():
    assert re.match("[a-zA-Z]", Faker().state_name(abbr=True))

def test_country_name():
    assert re.match("[a-zA-Z]", Faker().country_name())

def test_street_name():
    assert re.match("[A-Za-z0-9]", Faker().street_name())

def test_street_number():
    assert re.match("[0-9]", f'{Faker().street_number()}')

def test_street_suffix():
    assert re.match("[a-zA-Z]", Faker().street_suffix())

def test_company_name():
    assert re.match("[a-zA-Z]", Faker().company_name())

def test_company_suffix():
    assert re.match("[a-zA-Z]", Faker().company_suffix())

def test_name():
    assert re.match("[a-zA-Z]", Faker().name())

def test_first_name():
    assert re.match("[a-zA-Z]", Faker().first_name())

def test_last_name():
    assert re.match("[a-zA-Z]", Faker().last_name())

def test_male_first_name():
    assert re.match("[a-zA-Z]", Faker().male_first_name())

def test_female_first_name():
    assert re.match("[a-zA-Z]", Faker().female_first_name())

def test_name_prefix():
    assert re.match("[a-zA-Z].", Faker().name_prefix())

def test_name_suffix():
    assert re.match("[a-zA-Z].", Faker().name_suffix())

def test_gender_type():
    assert re.match("[a-zA-Z]", Faker().gender_type())

def test_gender_binary_type():
    assert re.match("[a-zA-Z]", Faker().gender_binary_type())

def test_color():
    assert re.match("[a-zA-Z]", Faker().color())

def test_team():
    assert re.match("[a-zA-Z]", Faker().team())

def test_team_prefix():
    assert re.match("[a-zA-Z]", Faker().team_prefix())

def test_team_gentile():
    assert re.match("[a-zA-Z]", Faker().team_gentile())

def test_sport():
    assert re.match("[a-zA-Z]", Faker().sport())

def test_food_ingredient():
    assert re.match("[a-zA-Z]", Faker().food_ingredient())

def test_food_ingredient_spice():
    assert re.match("[a-zA-Z]", Faker().food_ingredient_spice())

def test_food_measurements():
    assert re.match("[a-zA-Z]", Faker().food_measurements())

def test_food_measurements_sizes():
    assert re.match("[A-Za-z0-9]", Faker().food_measurements_sizes())

def test_science_element():
    assert re.match("[A-Za-z]", Faker().science_element())

def test_space_planet():
    assert re.match("[A-Za-z]", Faker().space_planet())

def test_space_moon():
    assert re.match("[A-Za-z]", Faker().space_moon())

def test_space_distance_measurement():
    assert re.match("[A-Za-z]", Faker().space_distance_measurement())

def test_electrical_components_passive():
    assert re.match("[A-Za-z]", Faker().electrical_components_passive())

def test_electrical_components_active():
    assert re.match("[A-Za-z]", Faker().electrical_components_active())

def electrical_components_electromechanical():
    assert re.match("[A-Za-z]", Faker().electrical_components_electromechanical())

def test_read_yml_file():
    result = Faker().read_yaml_file(subtopic='name', topic='last_name')
    assert type(result) == list