import yaml
import random

class Faker:

    def __init__(self):
        pass

    def city_name(self):
        city_list = self.read_yaml_file(subtopic='address', topic='city')
        return self.get_sample_to_list(city_list)

    def state_name(self, abbr=False):
        state_list = []
        if abbr is True:
           state_list = self.call_state_abbr_name()
        else:
           state_list = self.call_state_longer_name()
        return self.get_sample_to_list(state_list)

    def call_state_abbr_name(self):
        return self.read_yaml_file(subtopic='address', topic='state_abbr')

    def call_state_longer_name(self):
        return self.read_yaml_file(subtopic='address', topic='state')

    def country_name(self):
        country_list = self.read_yaml_file(subtopic='address', topic='country')
        return self.get_sample_to_list(country_list)

    def street_suffix(self):
        street_suffix_list = self.read_yaml_file(subtopic='address', topic='street_suffix')
        return self.get_sample_to_list(street_suffix_list)

    def company_sufix(self):
        company_sufix_list = self.read_yaml_file(subtopic='company', topic='suffix')
        return self.get_sample_to_list(company_sufix_list)

    def name(self):
        return f'{self.first_name()} {self.last_name()}'

    def first_name(self):
        return self.get_sample_to_list([self.male_first_name(), self.female_first_name()])

    def last_name(self):
        last_name_list = self.read_yaml_file(subtopic='name', topic='last_name')
        return self.get_sample_to_list(last_name_list)

    def male_first_name(self):
        name_list = self.read_yaml_file(subtopic='name', topic='male_first_name')
        return self.get_sample_to_list(name_list)

    def female_first_name(self):
        name_list = self.read_yaml_file(subtopic='name', topic='female_first_name')
        return self.get_sample_to_list(name_list)

    def name_prefix(self):
        prefix_list = self.read_yaml_file(subtopic='name', topic='prefix')
        return self.get_sample_to_list(prefix_list)

    def name_suffix(self):
        suffix_list = self.read_yaml_file(subtopic='name', topic='suffix')
        return self.get_sample_to_list(suffix_list)

    def gender_type(self):
        gender_type_list = self.read_yaml_file(subtopic='gender', topic='types')
        return self.get_sample_to_list(gender_type_list)

    def gender_binary_type(self):
        gender_type_list = self.read_yaml_file(subtopic='gender', topic='binary_types')
        return self.get_sample_to_list(gender_type_list)

    def color(self):
        color_list = self.read_yaml_file(subtopic='color', topic='name')
        return self.get_sample_to_list(color_list)

    def team(self):
        team_list = self.read_yaml_file(subtopic='team', topic='main_teams')
        return self.get_sample_to_list(team_list)

    def team_prefix(self):
        prefix_list = self.read_yaml_file(subtopic='team', topic='prefix')
        return self.get_sample_to_list(prefix_list)

    def team_gentile(self):
        gentile_list = self.read_yaml_file(subtopic='team', topic='gentile')
        return self.get_sample_to_list(gentile_list)

    def sport(self):
        sport_list = self.read_yaml_file(subtopic='team', topic='sport')
        return self.get_sample_to_list(sport_list)

    def food_ingredient(self):
        ingredient_list = self.read_yaml_file(subtopic='food', topic='ingredients')
        return self.get_sample_to_list(ingredient_list)

    def food_ingredient_spice(self):
        ingredient_list = self.read_yaml_file(subtopic='food', topic='spices')
        return self.get_sample_to_list(ingredient_list)

    def food_measurements(self):
        measurements_list = self.read_yaml_file(subtopic='food', topic='measurements')
        return self.get_sample_to_list(measurements_list)

    def food_measurements_sizes(self):
        measurements_list = self.read_yaml_file(subtopic='food', topic='measurement_sizes')
        return self.get_sample_to_list(measurements_list)

    def science_element(self):
        element_list = self.read_yaml_file(subtopic='science', topic='element')
        return self.get_sample_to_list(element_list)

    def space_planet(self):
        planet_list = self.read_yaml_file(subtopic='space', topic='planet')
        return self.get_sample_to_list(planet_list)

    def space_moon(self):
        moon_list = self.read_yaml_file(subtopic='space', topic='moon')
        return self.get_sample_to_list(moon_list)

    def space_distance_measurement(self):
        measurement_list = self.read_yaml_file(subtopic='space', topic='distance_measurement')
        return self.get_sample_to_list(measurement_list)

    def electrical_components_active(self):
        components_list = self.read_yaml_file(subtopic='electrical_components', topic='active')
        return self.get_sample_to_list(components_list)

    def electrical_components_passive(self):
        components_list = self.read_yaml_file(subtopic='electrical_components', topic='passive')
        return self.get_sample_to_list(components_list)

    def electrical_components_electromechanical(self):
        components_list = self.read_yaml_file(subtopic='electrical_components',
                                              topic='electromechanical')
        return self.get_sample_to_list(components_list)

    def read_yaml_file(self, locale='pt-BR', subtopic=str, topic=str):
        if subtopic is None or topic is None:
            return None

        result_list = []
        with open('locales/pt-BR.yaml') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            result_list = data['pt-BR']['faker'][subtopic][topic]
        return result_list

    def get_sample_to_list(self, list_values):
        return ''.join(random.sample(list_values, k=1))