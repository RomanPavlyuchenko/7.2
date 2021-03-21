import os
from pprint import pprint


file_path = os.path.join(os.getcwd(), 'files', 'file.txt')
cook_book = {}
with open(file_path) as file:
    name = file.readline().strip()
    while name != '':
        cook_book[name] = []
        ingr_count = int(file.readline())
        for i in range(ingr_count):
            ingedient = file.readline().strip()
            splited = [j for j in ingedient.split(' | ')]
            cook_book[name].append({'ingredient_name': splited[0],
                                    'quantity': int(splited[1]),
                                    'measure': splited[2]})
        file.readline()
        name = file.readline().strip()

pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        for ingr in cook_book[dish]:
            if ingr['ingredient_name'] in result:
                result[ingr['ingredient_name']]['quantity'] += ingr['quantity'] * person_count
            else:
                result[ingr['ingredient_name']] = {}
                result[ingr['ingredient_name']]['quantity'] = ingr['quantity'] * person_count
                result[ingr['ingredient_name']]['measure'] = ingr['measure']
    return result


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 5))
