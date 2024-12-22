import csv
import dop3


def write_dictianoris(file, data, keys, separator = ';'):
    file.write(separator.join(keys) + "\n")
    
    for couple in data:
        values = []
        for key in keys:
            values.append(couple[key])
        file.write(separator.join(values) + "\n")


def main():
    inp = open(r"input\schedule_for_task5.xml", encoding="utf-8")
    out = open(r"output\task.json", 'w', encoding="utf-8")
    data = dop3.read_data(inp)
    
    data = data["schedule"]["lesson"]
    keys = list(data[0].keys())
    
    write_dictianoris(out, data, keys, ';')
    inp.close()
    out.close()



if __name__ == "__main__":
    main()  
