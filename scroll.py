from runtext import RunText
import json

def getdata(js_file):
    with open (js_file,"r",encoding="utf-8") as f:
        json_data = json.load(f)
        text =''
        for i in range(0,len(json_data)-1):
            data_name = json_data[i]['지역이름']
            data_num = json_data[i]['확진자수']
            text = text + data_name + " : " + str(data_num) + "  "
        return text


run_text = RunText()
run_text.my_text =getdata('koreaData_All_2020-11-26.js')
run_text.process()