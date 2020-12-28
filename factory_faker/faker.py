import yaml
from random import randint, sample
import re

class Faker:

    def __init__(self):
        pass

    def city_name(self):
        city_list = self.read_yaml_file(topic='address', subtopic='city')
        return self.get_sample_to_list(list_values=city_list)

    def state_name(self, abbr=False):
        state_list = []
        if abbr is True:
            state_list = self.call_state_abbr_name()
        else:
           state_list = self.call_state_longer_name()
        return self.get_sample_to_list(list_values=state_list)

    def call_state_abbr_name(self):
        return self.read_yaml_file(topic='address', subtopic='state_abbr')

    def call_state_longer_name(self):
        return self.read_yaml_file(topic='address', subtopic='state')

    def country_name(self):
        country_list = self.read_yaml_file(topic='address', subtopic='country')
        return self.get_sample_to_list(list_values=country_list)

    def street_name(self):
        return f'{self.street_suffix()} {self.first_name()} {self.last_name()}, {self.street_number()}'

    def street_complement(self):
        complement_list = self.read_yaml_file(topic='address', subtopic='secondary_address')
        complement_sample = self.get_sample_to_list(list_values=complement_list)
        return complement_sample.replace('#', f'{self.street_number()}')

    def street_suffix(self):
        street_suffix_list = self.read_yaml_file(topic='address', subtopic='street_suffix')
        return self.get_sample_to_list(list_values=street_suffix_list)

    def street_number(self):
        return randint(1, 9)

    def postcode(self):
        postcode_list = self.read_yaml_file(topic='address', subtopic='postcode')
        postcode_str = self.get_sample_to_list(list_values=postcode_list)
        return self.replace_postcode_with_number(postcode_str)

    def postcode_by_state(self, state_abbrevieted=''):
        if state_abbrevieted != '':
            state_abbr = state_abbrevieted.upper()
        else:
            state_abbr = self.state_name(abbr=True)
        postcode_by_state_abbr = self.read_yaml_file(topic='address', subtopic='postcode_by_state')
        postcodes = postcode_by_state_abbr[state_abbr]

        if type(postcodes) == list:
            postcode_sample = self.get_sample_to_list(list_values=postcodes)
            return self.replace_postcode_with_number(postcode_sample)
        else:
            return self.replace_postcode_with_number(postcodes)

    def replace_postcode_with_number(self, postcode):
        result = re.sub('\W', '', postcode)
        for char in postcode:
            if char == '#':
                rand_number = randint(1, 9)
                result = result + f'{rand_number}'
            elif char == '-':
                result = result + '-'
        return result

    def company_name(self):
        return f'{self.last_name()} {self.company_suffix()}'

    def company_suffix(self):
        company_suffix_list = self.read_yaml_file(topic='company', subtopic='suffix')
        return self.get_sample_to_list(list_values=company_suffix_list)

    def university_name(self):
        return f'{self.university_prefix()} {self.university_region()} {self.last_name()} {self.university_suffix()}'

    def university_region(self):
        region_list = self.read_yaml_file(topic='university', subtopic='region')
        return self.get_sample_to_list(list_values=region_list)

    def university_prefix(self):
        prefix_list = self.read_yaml_file(topic='university', subtopic='prefix')
        return self.get_sample_to_list(list_values=prefix_list)

    def university_suffix(self):
        suffix_list = self.read_yaml_file(topic='university', subtopic='suffix')
        return self.get_sample_to_list(list_values=suffix_list)

    def internet_free_email(self):
        email_domain_list = self.read_yaml_file(topic='internet', subtopic='free_email')
        return self.get_sample_to_list(list_values=email_domain_list)

    def internet_domain_suffix(self):
        domain_suffix_list = self.read_yaml_file(topic='internet', subtopic='domain_suffix')
        return self.get_sample_to_list(list_values=domain_suffix_list)

    def lorem_words(self):
        word_list = self.read_yaml_file(topic='lorem', subtopic='words')
        return self.get_sample_to_list(list_values=word_list)

    def lorem_text(self):
        word_list = self.read_yaml_file(topic='lorem', subtopic='words')
        return self.get_sample_to_list(list_values=word_list, k=100, whitespace=True)

    def job_title(self):
        return f'{self.job_position()} de {self.job_field()} {self.job_seniority()}'

    def job_field(self):
        field_list = self.read_yaml_file(topic='job', subtopic='field')
        return self.get_sample_to_list(list_values=field_list)

    def job_seniority(self):
        seniority_list = self.read_yaml_file(topic='job', subtopic='seniority')
        return self.get_sample_to_list(list_values=seniority_list)

    def job_position(self):
        position_list = self.read_yaml_file(topic='job', subtopic='position')
        return self.get_sample_to_list(list_values=position_list)

    def job_key_skill(self):
        key_skill_list = self.read_yaml_file(topic='job', subtopic='key_skills')
        return self.get_sample_to_list(list_values=key_skill_list)

    def job_employment_type(self):
        employment_type_list = self.read_yaml_file(topic='job', subtopic='employment_type')
        return self.get_sample_to_list(list_values=employment_type_list)

    def job_education_level(self):
        education_level_list = self.read_yaml_file(topic='job', subtopic='education_level')
        return self.get_sample_to_list(list_values=education_level_list)

    def name(self):
        return f'{self.first_name()} {self.last_name()}'

    def first_name(self):
        return self.get_sample_to_list(list_values=[self.male_first_name(), self.female_first_name()])

    def last_name(self):
        last_name_list = self.read_yaml_file(topic='name', subtopic='last_name')
        return self.get_sample_to_list(list_values=last_name_list)

    def male_first_name(self):
        name_list = self.read_yaml_file(topic='name', subtopic='male_first_name')
        return self.get_sample_to_list(list_values=name_list)

    def female_first_name(self):
        name_list = self.read_yaml_file(topic='name', subtopic='female_first_name')
        return self.get_sample_to_list(list_values=name_list)

    def name_prefix(self):
        prefix_list = self.read_yaml_file(topic='name', subtopic='prefix')
        return self.get_sample_to_list(list_values=prefix_list)

    def name_suffix(self):
        suffix_list = self.read_yaml_file(topic='name', subtopic='suffix')
        return self.get_sample_to_list(list_values=suffix_list)

    def gender_type(self):
        gender_type_list = self.read_yaml_file(topic='gender', subtopic='types')
        return self.get_sample_to_list(list_values=gender_type_list)

    def gender_binary_type(self):
        gender_type_list = self.read_yaml_file(topic='gender', subtopic='binary_types')
        return self.get_sample_to_list(list_values=gender_type_list)

    def color(self):
        color_list = self.read_yaml_file(topic='color', subtopic='name')
        return self.get_sample_to_list(list_values=color_list)

    def team(self):
        team_list = self.read_yaml_file(topic='team', subtopic='main_teams')
        return self.get_sample_to_list(list_values=team_list)

    def team_prefix(self):
        prefix_list = self.read_yaml_file(topic='team', subtopic='prefix')
        return self.get_sample_to_list(list_values=prefix_list)

    def team_gentile(self):
        gentile_list = self.read_yaml_file(topic='team', subtopic='gentile')
        return self.get_sample_to_list(list_values=gentile_list)

    def sport(self):
        sport_list = self.read_yaml_file(topic='team', subtopic='sport')
        return self.get_sample_to_list(list_values=sport_list)

    def phone_number_area_code(self):
        area_code_list = self.read_yaml_file(topic='phone_number', subtopic='area_code')
        return self.get_sample_to_list(list_values=area_code_list)

    def food_ingredient(self):
        ingredient_list = self.read_yaml_file(topic='food', subtopic='ingredients')
        return self.get_sample_to_list(list_values=ingredient_list)

    def food_ingredient_spice(self):
        ingredient_list = self.read_yaml_file(topic='food', subtopic='spices')
        return self.get_sample_to_list(list_values=ingredient_list)

    def food_measurements(self):
        measurements_list = self.read_yaml_file(topic='food', subtopic='measurements')
        return self.get_sample_to_list(list_values=measurements_list)

    def food_measurements_sizes(self):
        measurements_list = self.read_yaml_file(topic='food', subtopic='measurement_sizes')
        return self.get_sample_to_list(list_values=measurements_list)

    def science_element(self):
        element_list = self.read_yaml_file(topic='science', subtopic='element')
        return self.get_sample_to_list(list_values=element_list)

    def space_planet(self):
        planet_list = self.read_yaml_file(topic='space', subtopic='planet')
        return self.get_sample_to_list(list_values=planet_list)

    def space_moon(self):
        moon_list = self.read_yaml_file(topic='space', subtopic='moon')
        return self.get_sample_to_list(list_values=moon_list)

    def space_distance_measurement(self):
        measurement_list = self.read_yaml_file(topic='space', subtopic='distance_measurement')
        return self.get_sample_to_list(list_values=measurement_list)

    def electrical_components_active(self):
        components_list = self.read_yaml_file(topic='electrical_components', subtopic='active')
        return self.get_sample_to_list(list_values=components_list)

    def electrical_components_passive(self):
        components_list = self.read_yaml_file(topic='electrical_components', subtopic='passive')
        return self.get_sample_to_list(list_values=components_list)

    def electrical_components_electromechanical(self):
        components_list = self.read_yaml_file(topic='electrical_components',
                                              subtopic='electromechanical')
        return self.get_sample_to_list(list_values=components_list)

    def read_yaml_file(self, locale='pt-BR', topic=str, subtopic=str):
        if  topic is None or subtopic is None:
            return None

        result_list = []
        with open('locales/pt-BR.yaml') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            result_list = data['pt-BR']['faker'][topic][subtopic]
        return result_list

    def get_sample_to_list(self, list_values=list, k=1, whitespace=False):
        txt = ''
        if whitespace is True:
            txt = ' '

        return txt.join(sample(list_values, k=k))