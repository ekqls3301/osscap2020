from runtext import RunText
import json
import time
import datetime
from datetime import date, timedelta



today = date.today()
yesterday = date.today() - timedelta(1)
a = str(today)

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
run_text.my_text =getdata('koreaData_All_'+ a +'.js')
run_text.process()
