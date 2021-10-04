import os

cook_book = dict()

def add_cook_book(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            dish_name = line.strip()
            counter = int(file.readline())
            temp_list = []
            for item in range(counter):
                ingredient_name, quantity, measure = file.readline().split("|")
                temp_list.append(
                    {"ingredient_name": ingredient_name.strip(), "quantity": int(quantity), "measure": measure.strip()}
                )
                cook_book[dish_name] = temp_list
            file.readline()
    return(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    cook_book_person = dict()
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient["ingredient_name"] in cook_book_person:
                    cook_book_person[ingredient["ingredient_name"]]["quantity"] \
                        += int(ingredient["quantity"]) * person_count
                else:
                    temp = {"quantity": int(ingredient["quantity"]) * person_count, "measure": ingredient["measure"]}
                    cook_book_person[ingredient["ingredient_name"]] = temp
    return cook_book_person

add_cook_book("recipes.txt")

print(get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 2))

def write_file(result_file):
    str_dict = dict()
    temp_dict = dict()
    path = '2.4.files/sorted'
    path_1 = '2.4.files'
    res = sorted(os.listdir(path))
    with open(os.path.join(path_1, result_file), "a", encoding="utf-8") as file_1:
        for name_file in res:
            temp_list = list()
            count = 0
            with open(os.path.join(path, name_file), "r", encoding="utf-8") as file:
                for count, line in enumerate(file):
                     temp_list.append(line)
                str_dict[name_file] = temp_list
                count += 1
                temp_dict[count] = name_file
        list_keys = list(temp_dict.keys())
        list_keys.sort()
        for item in list_keys:
            file_1.write(f'{temp_dict[item]}\n {item}\n{"".join(str_dict[temp_dict[item]])}\n\n')

write_file('4.txt')
