import codecs


def read_data(inp):
    data = {}
    stack = [data]
    inp.readline()

    for s in inp.readlines():
        if "<" in s:
            tag1_start = s.index("<") + 1
            tag1_end = s.index(">")
            tag1 = s[tag1_start:tag1_end]

            if tag1[0] != '/':
                if tag1 in stack[-1]:
                    if not isinstance(stack[-1][tag1], list):
                        stack[-1][tag1] = [stack[-1][tag1]]  # заменяю элемент словаря на массив элементов
                    stack.append(stack[-1][tag1])

                s = s[tag1_end + 1:]

                if "<" in s:
                    tag2_start = s.index("<") + 1
                    tag2_end = s.index(">")
                    tag2 = s[tag2_start:tag2_end]

                    content = s[:tag2_start - 1]

                    stack[-1][tag1] = content
                else:
                    if isinstance(stack[-1], list):
                        stack[-1].append({})
                        stack.append(stack[-1][-1])
                    else:
                        stack[-1][tag1] = {}
                        stack.append(stack[-1][tag1])
            else:
                stack.pop()
                if isinstance(stack[-1], list):
                    stack.pop()

    return data


def write_data(out, data, spase=0, is_arr_el=False):
    if isinstance(data, list):
        if is_arr_el:
            out.write("\t" * spase + "[\n")
        else:
            out.write("[\n")

        for i in range(len(data)):
            write_data(out, data[i], spase + 1, True)
            if i != len(data) - 1:
                out.write(",\n")
            else:
                out.write("\n")
        out.write("\t" * spase + "]")

    elif isinstance(data, dict):
        if is_arr_el:
            out.write("\t" * spase + "{\n")
        else:
            out.write("{\n")

        i = 0
        for key in data:
            out.write("\t" * (spase + 1) + f'"{key}": ')
            write_data(out, data[key], spase + 1)
            if i != len(data) - 1:
                out.write(",\n")
            else:
                out.write("\n")
            i += 1
        out.write("\t" * spase + "}")

    elif isinstance(data, str):
        if is_arr_el:
            out.write("\t" * spase + f'"{data}"')
        else:
            out.write(f'"{data}"')


def main():
    inp = open(r"input\schedule.xml", encoding="utf-8")
    out = open(r"output\task_0.json", 'w', encoding="utf-8")

    data = read_data(inp)
    write_data(out, data)


if __name__ == "__main__":
    main()