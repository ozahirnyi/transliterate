from csv import reader, writer

dic = [['А', 'A'], ['У', 'Y'], ['Е', 'E'], ['Н', 'H'], ['К', 'K'],
       ['Х', 'X'], ['В', 'B'], ['А', 'A'], ['Р', 'P'], ['О', 'O'],
       ['С', 'C'], ['М', 'M'], ['Т', 'T']]


def is_cyrrylic(data, char=False, string=False):
    if char:
        return True if u'\u0400' <= data <= u'\u04FF' or u'\u0500' <= data <= u'\u052F' else False
    elif string:
        for it in data:
            if u'\u0400' <= it <= u'\u04FF' or u'\u0500' <= it <= u'\u052F':
                return True
        return False


def transliterate(data):
    for index, it in enumerate(data):
        if is_cyrrylic(it[2], string=True):
            updated_string = ""
            for char in it[2]:
                char_changed = False
                for const_char in dic:
                    if char == const_char[0]:
                        updated_string += const_char[1]
                        char_changed = True
                        break
                if not char_changed:
                    updated_string += char
            data[index][2] = updated_string
    return data


def set_new_file(data):
    with open("result.csv", 'w', newline='', encoding='utf-8') as file:
        file_writer = writer(file)
        file_writer.writerows(data)


def get_file_data(name):
    data = []

    with open(name, 'r', encoding='utf-8') as file:
        file_reader = reader(file)
        for it in file_reader:
            data.append(it)
    return data


def test(data):
    for it in data:
        if is_cyrrylic(it[2], string=True):
            print(it)
            print("ATTENTION")


if __name__ == "__main__":
    file_data = get_file_data('taxi.csv')
    print(len(file_data))
    transliterated_data = transliterate(file_data)
    print(len(transliterated_data))
    test(transliterated_data)
    set_new_file(transliterated_data)
