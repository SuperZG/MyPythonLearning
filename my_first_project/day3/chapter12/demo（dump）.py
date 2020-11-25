# world_population.py
import json


if __name__ == '__main__':

    filename = 'test.json'
    # with open(filename,'w') as file_p:
        # dump
        # test_list = ["xiaoming","xiaomei"]
        # pop_date = json.dump(test_list,file_p)

    test_dict = {"name":"xiaoming","age":"18"}
    result_str = json.dumps(test_dict)
    print(result_str)
    print(type(result_str))
