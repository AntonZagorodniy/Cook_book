def get_cook_book():
    cook_book = {}
    try:
        with open('List_of_recipes.txt', encoding='utf-8-sig') as file:
            lines = file.readlines()
            for line in lines:
                line = line.rstrip('\n')
                if line.isalpha():
                    name_of_the_recipe = line
                    cook_book.update({name_of_the_recipe: []})


                # if line.isdigit():
                #     for item in range(0, int(line)):
                #         cook_book[name_of_the_recipe].append({'ingridient_name': [], 'quantity': [],
                #                                           'measure': []})
                # # count = -1
                # document_type = []
                # if '|' in line:
                #     # count += 1
                #     for _ in line:
                #
                #         str = line.split(" | ")
                #         cook_book[name_of_the_recipe][0].update({'ingridient_name': str[0], 'quantity': str[1],
                #                                                 'measure': str[2]})
                if line.isdigit(): #or line.isalnum:
                    for item in range(0, int(line)):
                        cook_book[name_of_the_recipe].append({'ingridient_name': [], 'quantity': [],
                                                              'measure': []})
                        # if '|' in line:
                for it in range(0, len(cook_book[name_of_the_recipe])):
                    str = line.split(" | ")
                    cook_book[name_of_the_recipe][it].update({'ingridient_name': str[0],
                                                                                'quantity': str[1], 'measure': str[2]})
                print(cook_book)
            return cook_book
    except FileNotFoundError:
        print('Файл не найден')


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = get_cook_book()
    # print(cook_book)
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()
