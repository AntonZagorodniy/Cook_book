
def get_cook_book():
    cook_book = dict()
    with open('List_of_recipes.txt', encoding='utf-8-sig') as file:


        dish = ""
        for l in file:
            tempstr = l.strip()
            if '|' in tempstr:
                ingrs = tempstr.split("|")
                for i, ingr in enumerate(ingrs):
                    ingrs[i] = ingrs[i].strip()
                tempdict = dict()
                tempdict["ingridient_name"] = ingrs[0].lower()
                tempdict["quantity"] = int(ingrs[1])
                tempdict["measure"] = ingrs[2]
                cook_book[dish].append(tempdict)
            elif len(tempstr) == 0:
                continue
            elif tempstr.isdigit():
                pass
            else:
                dish = tempstr.lower()
                cook_book[dish] = list()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = get_cook_book()
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
