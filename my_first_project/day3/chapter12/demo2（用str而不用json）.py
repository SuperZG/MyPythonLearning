import json


if __name__ == '__main__':

    filename = 'test.json'
    with open(filename,'w') as file_p:
        # dump
        # test_list = ["xiaoming","xiaomei"]
        # pop_date = json.dump(test_list,file_p)

        test_dict = {"name":"xiaoming","age":"18"}
        result_str = str(test_dict)
        print(result_str)
        file_p.write(result_str)

    with open(filename) as file_p:
        # pop_date = json.load(file_p)
        file_str = file_p.read()
        # json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
        # 注意:json 不能用单引号!!!
        pop_date = json.loads(file_str)
        print(type(pop_date))