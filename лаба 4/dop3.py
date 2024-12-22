import task1

i = 0

def read_data(inp):
    global i
    i = 0
    inp.readline()
    s = inp.read()
    return read(s)
    
    

def read(s: str, open_tag = None):
    inner_str = []
    data = {}
    global i
    while i < len(s):
        c = s[i]
        if c == "<":
            i += 1
            tag = get_tag(s)
            i += 1
            if tag[0] == '/':
                if len(data) > 0:
                    return data
                else:
                    return ''.join(inner_str)
            else:
                if tag in data:
                    if not isinstance(data[tag], list):
                        data[tag] = [data[tag]] # заменяю элемент словаря на массив элементов
                    data[tag].append(read(s, tag))
                else:
                    data[tag] = read(s, tag)
        else:
            inner_str += c
        i += 1
    return data

def get_tag(s: str):
    inner_str = []
    global i
    while i < len(s):
        c = s[i]
        if c == ">":
            return ''.join(inner_str)
        else:
            inner_str.append(c)
        i += 1


def main():
    inp = open(r"input\schedule.xml", encoding="utf-8")
    out = open(r"output\dop3_1.json", 'w', encoding="utf-8")
    
    data = read_data(inp)
    task1.write_data(out, data)




if __name__ == "__main__":
    main()