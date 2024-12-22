import xmltodict
import json

def main():
    inp = open(r"E:input\schedule.xml", encoding="utf-8")
    out =  open(r"output\dop1_1.json", 'w', encoding="utf-8")
    data = xmltodict.parse(inp.read())

    json.dump(data, out, ensure_ascii=False, indent=4)
    
    inp.close()
    out.close()

if __name__ == "__main__":
    main()