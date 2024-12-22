import task1
import re


def read_data(inp):
    data = {}
    stack = [data]
    inp.readline()

    for s in inp.readlines():
        tags = re.findall("(?<=<)[\\w]+(?=>)", s)
        content = re.findall("(?<=>).+(?=<)", s)

        if len(tags) == 1:
            tag1 = tags[0]
            if tag1[0] != '/':
                if tag1 in stack[-1]:
                    if not isinstance(stack[-1][tag1], list):
                        stack[-1][tag1] = [stack[-1][tag1]]  # заменяю элемент словаря на массив элементов
                    stack.append(stack[-1][tag1])

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

        if len(tags) == 2:
            tag1 = tags[0]
            content = re.findall("(?<=>).+(?=<)", s)
            stack[-1][tag1] = content[0]
    return data


def main():
    inp = open(r"input\schedule.xml", encoding="utf-8")
    out = open(r"output\dop2_1.json", 'w', encoding="utf-8")

    data = read_data(inp)
    task1.write_data(out, data)


if __name__ == "__main__":
    main()