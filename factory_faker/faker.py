import yaml
import random

class Faker:

    def __init__(self):
        pass

    def city_name(self):
        city_list = []
        with open('locales/pt-BR.yaml') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            city_list = data['pt-BR']['faker']['address']['city']
        return print(random.sample(city_list, k=1)[0])

    def state_name(self, abbr=False):
        state_list = []
        with open('locales/pt-BR.yaml') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            if abbr is True:
                state_list = data['pt-BR']['faker']['address']['state_abbr']
            else:
                state_list = data['pt-BR']['faker']['address']['state']
        return print(random.sample(state_list, k=1)[0])
    
    def country_name(self):
        country_list = []
        with open('locales/pt-BR.yaml') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            country_list = data['pt-BR']['faker']['address']['country']
        return print(random.sample(country_list, k=1)[0])
    
    def street_suffix(self):
        street_suffix_list = []
        with open('locales/pt-BR.yaml') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            street_suffix_list = data['pt-BR']['faker']['address']['street_suffix']
        return print(random.sample(street_suffix_list, k=1)[0])

    def company_sufix(self):
        company_sufix_list = []
        with open('locales/pt-BR.yaml') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            company_sufix_list = data['pt-BR']['faker']['company']['suffix']
        return print(random.sample(company_sufix_list, k=1)[0])

# if __name__ == "__main__":
#     f = Faker()
#     f.company_sufix()


