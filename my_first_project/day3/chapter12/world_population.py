# world_population.py
import json


if __name__ == '__main__':

    filename = 'population_data.json'
    with open(filename) as file_p:
        # pop_date = json.load(file_p)
        file_str = file_p.read()
        pop_date = json.loads(file_str)

    for pop_dict in pop_date:
        country_name = pop_dict['Country Name']
        population = pop_dict['Value']
        print(country_name, ':', population)
