import json
import crawlKoreaData_All as crawl1
import crawlKoreaData_Gyeonggi as crawl2
import crawlKoreaData_Seoul as crawl3
import LED_Display as LMD
import threading
from datetime import date, timedelta
import datetime
from matrix import *
from runtext import RunText

today = date.today()
oneday = datetime.timedelta(days=1)
yesterday = today - oneday
third = today - oneday - oneday
a = str(today)
b = str(yesterday)
c = str(third)


def LED_init():
    thread=threading.Thread(target=LMD.main, args=())
    thread.setDaemon(True)
    thread.start()
    return

crawl1.run()
crawl2.run()
crawl3.run()

def draw_matrix(array):
    for x in range(16):
        for y in range(32):
            if array[x][y] == 1:
                LMD.set_pixel(x,y,4) #BLUE
            elif array[x][y] == 2:
                LMD.set_pixel(x,y,2) #GREEN
            elif array[x][y] == 3:
                LMD.set_pixel(x,y,3) #YELLOW
            elif array[x][y] == 4:
                LMD.set_pixel(x,y,1) #RED
            elif array[x][y] == 5:
                LMD.set_pixel(x,y,5) #PINK
            elif array[x][y] == 6:
                LMD.set_pixel(x,y,6) #CYAN
            elif array[x][y] == 7:
                LMD.set_pixel(x,y,7) #WHITE

            elif array[x][y] == 0:
                LMD.set_pixel(x,y,0)
            else:
                continue
        print()

array_screen = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

number_array = [
    [[1,1,1,0],
     [1,0,1,0],
     [1,0,1,0],
     [1,0,1,0],
     [1,1,1,0]], #0
    [[0,1,0,0],
     [0,1,0,0],
     [0,1,0,0],
     [0,1,0,0],
     [0,1,0,0]], #1
    [[1,1,1,0],
     [0,0,1,0],
     [1,1,1,0],
     [1,0,0,0],
     [1,1,1,0]], #2
    [[1,1,1,0],
     [0,0,1,0],
     [1,1,1,0],
     [0,0,1,0],
     [1,1,1,0]], #3
    [[1,0,1,0],
     [1,0,1,0],
     [1,1,1,0],
     [0,0,1,0],
     [0,0,1,0]], #4
    [[1,1,1,0],
     [1,0,0,0],
     [1,1,1,0],
     [0,0,1,0],
     [1,1,1,0]], #5
    [[1,1,1,0],
     [1,0,0,0],
     [1,1,1,0],
     [1,0,1,0],
     [1,1,1,0]], #6
    [[1,1,1,0],
     [0,0,1,0],
     [0,1,0,0],
     [0,1,0,0],
     [0,1,0,0]], #7
    [[1,1,1,0],
     [1,0,1,0],
     [1,1,1,0],
     [1,0,1,0],
     [1,1,1,0]], #8
    [[1,1,1,0],
     [1,0,1,0],
     [1,1,1,0],
     [0,0,1,0],
     [0,0,1,0]], #9
]

covid_array = [
    #########RED#########
    [[0, 4, 4, 0],
     [4, 0, 0, 0],
     [4, 0, 0, 0],
     [4, 0, 0, 0],
     [0, 4, 4, 0]], # C
    [[0, 4, 0, 0],
     [4, 0, 4, 0],
     [4, 0, 4, 0],
     [4, 0, 4, 0],
     [0, 4, 0, 0]], # O
    [[4, 0, 4, 0],
     [4, 0, 4, 0],
     [4, 0, 4, 0],
     [4, 0, 4, 0],
     [0, 4, 0, 0]], # V
    [[4, 4, 4, 0],
     [0, 4, 0, 0],
     [0, 4, 0, 0],
     [0, 4, 0, 0],
     [4, 4, 4, 0]], # I
    [[4, 4, 0, 0],
     [4, 0, 4, 0],
     [4, 0, 4, 0],
     [4, 0, 4, 0],
     [4, 4, 0, 0]]  # D
]

arrow_array = [
    [[0,1,0],
     [1,1,1],
     [0,1,0],
     [0,1,0],
     [0,1,0]]
]

comma_array = [
    [[0,0],
     [1,0],
     [0,0],
     [1,0],
     [0,0]]
]

flower = [
    [[0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 0, 0, 0],
    [0, 7, 0, 7, 0, 7, 0],
    [0, 0, 7, 3, 7, 0, 0],
    [7, 7, 3, 3, 3, 7, 7],
    [0, 0, 7, 3, 7, 0, 0],
    [0, 7, 0, 7, 0, 7, 0],
    [0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0],
    [2, 0, 0, 2, 0, 0, 2],
    [0, 2, 0, 2, 0, 2, 0],
    [0, 0, 2, 2, 2, 0, 0],
    [0, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0]]
]

LED_init()
draw_matrix(array_screen); print()

################################TODAY###################################################
def today_compare_data(js_file1, js_file2, search_region ,confirmed_cmp, array):
    with open(js_file1, "r", encoding="utf-8") as f1:
        with open(js_file2, "r", encoding="utf-8") as f2:
            json_data_1 = json.load(f1)
            json_data_2 = json.load(f2)
            for i in range(0, len(json_data_1) - 1):
                region = json_data_1[i]['지역이름']
                confirmed_1 = json_data_1[i]['확진자수']
                confirmed_2 = json_data_2[i]['확진자수']
                cmp_data = confirmed_1 - confirmed_2

                confirmed_cmp.append({
                    '지역이름' : region,
                    '전날비교' : cmp_data
                 })
            for i in range(0,len(confirmed_cmp)):
                if (confirmed_cmp[i]['지역이름']) == search_region:
                    list = [int(i) for i in str(confirmed_cmp[i]['전날비교'])]
                    for j in range(0,len(list)):
                        for x in range(5):
                            for y in range(22+4*j, 26+4*j):
                                array[x][y] = number_array[list[j]][x][y-22-4*j]
                    for x in range(5):
                        for y in range(21+4*len(list),21+4*len(list)+3):
                            array[x][y] = arrow_array[0][x][y-21-4*len(list)]
            return confirmed_cmp

# 지역별 확진자 수 검색 함수 (LED구현)
def today_search_count(js_file,search_region,array):
    with open (js_file,"r",encoding="utf-8") as f:
        json_data = json.load(f)
        for i in range(0,len(json_data)-1):
            if (json_data[i]['지역이름']) == search_region:
                print(json_data[i]['확진자수'])
                list =[int(i) for i in str(json_data[i]['확진자수'])]
                for j in range(0,len(list)):
                    for x in range(5):
                        for y in range(10+4*j,13+4*j):
                            array[x][y] = number_array[list[j]][x][y-4*j-10]

def today_date_print(array):
    a_list = a[8:10]
    list = [int(i) for i in str(a_list)]
    for j in range(0,len(list)):
        for x in range(5):
            for y in range(0+4*j,4+4*j):
                array[x][y] = number_array[list[j]][x][y-4*j]
    for j in range(1):
        for x in range(5):
            for y in range(8,10):
                array[x][y] = comma_array[0][x][y-8]


####################################################################################

################################YESTERDAY###################################################
def yesterday_compare_data(js_file1, js_file2, search_region ,confirmed_cmp, array):
    with open(js_file1, "r", encoding="utf-8") as f1:
        with open(js_file2, "r", encoding="utf-8") as f2:
            json_data_1 = json.load(f1)
            json_data_2 = json.load(f2)
            for i in range(0, len(json_data_1) - 1):
                region = json_data_1[i]['지역이름']
                confirmed_1 = json_data_1[i]['확진자수']
                confirmed_2 = json_data_2[i]['확진자수']
                cmp_data = confirmed_1 - confirmed_2

                confirmed_cmp.append({
                    '지역이름' : region,
                    '전날비교' : cmp_data
                 })
            for i in range(0,len(confirmed_cmp)):
                if (confirmed_cmp[i]['지역이름']) == search_region:
                    list = [int(i) for i in str(confirmed_cmp[i]['전날비교'])]
                    for j in range(0,len(list)):
                        for x in range(6,11):
                            for y in range(22+4*j, 26+4*j):
                                array[x][y] = number_array[list[j]][x-6][y-22-4*j]
                    for x in range(6,11):
                        for y in range(21+4*len(list),21+4*len(list)+3):
                            array[x][y] = arrow_array[0][x-6][y-21-4*len(list)]
            return confirmed_cmp

# 지역별 확진자 수 검색 함수 (LED구현)
def yesterday_search_count(js_file,search_region,array):
    with open (js_file,"r",encoding="utf-8") as f:
        json_data = json.load(f)
        for i in range(0,len(json_data)-1):
            if (json_data[i]['지역이름']) == search_region:
                print(json_data[i]['확진자수'])
                list =[int(i) for i in str(json_data[i]['확진자수'])]
                for j in range(0,len(list)):
                    for x in range(6,11):
                        for y in range(10+4*j,13+4*j):
                            array[x][y] = number_array[list[j]][x-6][y-4*j-10]

def yesterday_date_print(array):
    b_list = b[8:10]
    list = [int(i) for i in str(b_list)]
    for j in range(0,len(list)):
        for x in range(6,11):
            for y in range(0+4*j,4+4*j):
                array[x][y] = number_array[list[j]][x-6][y-4*j]
    for j in range(1):
        for x in range(6,11):
            for y in range(8,10):
                array[x][y] = comma_array[0][x-6][y-8]


################################BEFORE_YESTERDAY###################################

def b_yesterday_compare_data(js_file1, js_file2, search_region ,confirmed_cmp, array):
    with open(js_file1, "r", encoding="utf-8") as f1:
        with open(js_file2, "r", encoding="utf-8") as f2:
            json_data_1 = json.load(f1)
            json_data_2 = json.load(f2)
            for i in range(0, len(json_data_1) - 1):
                region = json_data_1[i]['지역이름']
                confirmed_1 = json_data_1[i]['확진자수']
                confirmed_2 = json_data_2[i]['확진자수']
                cmp_data = confirmed_1 - confirmed_2

                confirmed_cmp.append({
                    '지역이름' : region,
                    '전날비교' : cmp_data
                 })
            for i in range(0,len(confirmed_cmp)):
                if (confirmed_cmp[i]['지역이름']) == search_region:
                    list = [int(i) for i in str(confirmed_cmp[i]['전날비교'])]
                    for j in range(0,len(list)):
                        for x in range(11,16):
                            for y in range(22+4*j, 26+4*j):
                                array[x][y] = number_array[list[j]][x-11][y-22-4*j]
                    for x in range(11,16):
                        for y in range(21+4*len(list),21+4*len(list)+3):
                            array[x][y] = arrow_array[0][x-11][y-21-4*len(list)]
            return confirmed_cmp

# 지역별 확진자 수 검색 함수 (LED구현)
def b_yesterday_search_count(js_file,search_region,array):
    with open (js_file,"r",encoding="utf-8") as f:
        json_data = json.load(f)
        for i in range(0,len(json_data)-1):
            if (json_data[i]['지역이름']) == search_region:
                print(json_data[i]['확진자수'])
                list =[int(i) for i in str(json_data[i]['확진자수'])]
                for j in range(0,len(list)):
                    for x in range(11,16):
                        for y in range(10+4*j,13+4*j):
                            array[x][y] = number_array[list[j]][x-11][y-4*j-10]

def b_yesterday_date_print(array):
    c_list = c[8:10]
    list = [int(i) for i in str(c_list)]
    for j in range(0,len(list)):
        for x in range(11,16):
            for y in range(0+4*j,4+4*j):
                array[x][y] = number_array[list[j]][x-11][y-4*j]
    for j in range(1):
        for x in range(11,16):
            for y in range(8,10):
                array[x][y] = comma_array[0][x-11][y-8]


def main_UI(array):
    for j in range(0,5):
        for x in range(2,7):
            for y in range(1+4*j,5+4*j):
                array[x][y] = covid_array[j][x-2][y-4*j-1]

def all_count(js_file,array):
    with open (js_file,"r",encoding="utf-8") as f:
        json_data = json.load(f)
        list = [int(i) for i in str(json_data[0]['확진자수'])]
        for j in range(0,len(list)):
            for x in range(10,15):
                for y in range(1+4*j,5+4*j):
                    array[x][y] = number_array[list[j]][x-10][y-4*j-1]

def flower_print(array):
    for x in range(1,16):
        for y in range(23,30):
            array[x][y] = flower[0][x-1][y-23]

# 지역별 전날대비 확진자 수 증감 검색 함수
def count_change(js_file,search_region):
    with open (js_file,"r",encoding="utf-8") as f:
        json_data = json.load(f)
        for i in range(0,len(json_data)-1):
            if (json_data[i]['지역이름']) == search_region:
                return json_data[i]['전날비교']

def clear_array(array):
    for i in range(16):
        for j in range(32):
            array[i][j] = 0
            
            
def getdata(js_file):
    with open (js_file,"r",encoding="utf-8") as f:
        json_data = json.load(f)
        text =''
        for i in range(0,len(json_data)-1):
            data_name = json_data[i]['지역이름']
            data_num = json_data[i]['확진자수']
            text = text + data_name + " : " + str(data_num) + "  "
        return text

    
main_menu = 0
menu = 1
while(menu):
    print("*****Menu*****")
    print("1.All")
    print("2.Seoul")
    print("3.Gyeonggi")
    print("4.Exit")
    print("**************")
    if main_menu == 0:
        main_UI(array_screen)
        file = 'koreaData_All' + '_' + a + '.js'
        all_count(file, array_screen)
        flower_print(array_screen)
        draw_matrix(array_screen);print()
    compare_cmp = []
    y_compare_cmp = []
    b_y_compare_cmp = []
    menu_choice = int(input("Select menu: "))

    # while > 뒤로가기 입력전까지 menu 반복시행
    while menu_choice == 1:  # 전국 확진자 수 검색
        js_file = 'koreaData_All'+ '_'+ a +'.js'
        while(1):
            search_region = input("scroll 기능 실행 시 1 입력 : ");
            if search_region == '1':
                run_text = RunText()
                run_text.my_text = getdata(js_file)
                run_text.process()
            if search_region == '0': # 0을 입력하면 메뉴로 복귀
                main_menu = 0
                break
        


    while menu_choice == 2: # 서울 세부지역 확진자 수 검색
        sum_today = 0
        sum_yesterday = 0
        sum_today_array = []
        sum_yesterday_array = []
        js_file = 'koreaData_Seoul'+ '_' + a + '.js'
        js_file_yesterday = 'koreaData_Seoul'+ '_' + b + '.js'
        js_file_b_yesterday = 'koreaData_Seoul'+ '_' + c + '.js'
        search_region = input("지역을 입력하세요 (ex:종로구): ")
        clear_array(array_screen)
        draw_matrix(array_screen);print()
        today_date_print(array_screen)
        today_search_count(js_file,search_region,array_screen)
        for x in range(5):
            for y in range(22):
                if array_screen[x][y] == 1:
                    array_screen[x][y] += 6
        today_compare_data(js_file, js_file_yesterday, search_region, compare_cmp, array_screen)

        for i in range(0,len(compare_cmp)):
            sum_today += compare_cmp[i]['전날비교']
            sum_today_array.append(compare_cmp[i]['전날비교'])
        avg_today = sum_today/len(compare_cmp)
        max1 = (max(sum_today_array)+avg_today) / 2
        min1 = (min(sum_today_array)+avg_today) / 2

        for i in range(0,len(compare_cmp)):
            if compare_cmp[i]['지역이름'] == search_region:
                list = [int(i) for i in str(compare_cmp[i]['전날비교'])]
                if compare_cmp[i]['전날비교'] >= max1:
                    for x in range(5):
                        for y in range(22,32):
                            if array_screen[x][y] == 1:
                                array_screen[x][y] += 3
                if compare_cmp[i]['전날비교'] >= min1 and compare_cmp[i]['전날비교'] < max1:
                    for x in range(5):
                        for y in range(22,32):
                            if array_screen[x][y] == 1:
                                array_screen[x][y] += 2
                if compare_cmp[i]['전날비교'] >= 0 and compare_cmp[i]['전날비교'] < min1:
                    for x in range(5):
                        for y in range(22,32):
                            if array_screen[x][y] == 1:
                                array_screen[x][y] += 1
        yesterday_date_print(array_screen)
        yesterday_search_count(js_file_yesterday,search_region,array_screen)
        for x in range(6,11):
            for y in range(22):
                if array_screen[x][y] == 1:
                    array_screen[x][y] += 5
        yesterday_compare_data(js_file_yesterday, js_file_b_yesterday, search_region, y_compare_cmp, array_screen)

        for i in range(0,len(y_compare_cmp)):
            sum_yesterday += y_compare_cmp[i]['전날비교']
            sum_yesterday_array.append(y_compare_cmp[i]['전날비교'])
        avg_yesterday = sum_yesterday/len(y_compare_cmp)
        max2 = (max(sum_yesterday_array)+avg_yesterday) / 2
        min2 = (min(sum_yesterday_array)+avg_yesterday) / 2

        for i in range(0,len(y_compare_cmp)):
            if y_compare_cmp[i]['지역이름'] == search_region:
                list = [int(i) for i in str(y_compare_cmp[i]['전날비교'])]
                if y_compare_cmp[i]['전날비교'] >= max2:
                    for x in range(6,11):
                        for y in range(22,32):
                            if array_screen[x][y] == 1:
                                array_screen[x][y] += 3
                if y_compare_cmp[i]['전날비교'] >= min2 and y_compare_cmp[i]['전날비교'] < max2:
                    for x in range(6,11):
                        for y in range(22,32):
                            if array_screen[x][y] == 1:
                                array_screen[x][y] += 2
                if y_compare_cmp[i]['전날비교'] >= 0 and y_compare_cmp[i]['전날비교'] < min2:
                    for x in range(6,11):
                        for y in range(22,32):
                            if array_screen[x][y] == 1:
                                array_screen[x][y] += 1
        b_yesterday_date_print(array_screen)
        b_yesterday_search_count(js_file_b_yesterday,search_region,array_screen)
        for x in range(11,16):
            for y in range(22):
                if array_screen[x][y] == 1:
                    array_screen[x][y] += 6
        draw_matrix(array_screen);print()
        if search_region == '1':
            run_text = RunText()
            run_text.my_text = getdata(js_file)
            run_text.process()
            
        if search_region == '0': # 0을 입력하면 메뉴로 복귀
            compare_cmp = []
            y_compare_cmp = []
            b_y_compare_cmp = []
            main_menu = 0
            clear_array(array_screen)
            break

    while menu_choice == 3: # 경기 세부지역 확진자 수 검색
        sum_today = 0
        sum_yesterday = 0
        sum_today_array = []
        sum_yesterday_array = []
        js_file = 'koreaData_Gyeonggi'+ '_'+ a + '.js'
        js_file_yesterday = 'koreaData_Gyeonggi'+ '_'+ b + '.js'
        js_file_b_yesterday = 'koreaData_Gyeonggi'+ '_' + c + '.js'
        search_region = input("지역을 입력하세요 (ex:수원): ")
        clear_array(array_screen)
        draw_matrix(array_screen);print()
        today_date_print(array_screen)
        today_search_count(js_file,search_region,array_screen)
        for x in range(5):
            for y in range(22):
                if array_screen[x][y] == 1:
                    array_screen[x][y] += 6
        today_compare_data(js_file, js_file_yesterday, search_region, compare_cmp, array_screen)

        for i in range(0,len(compare_cmp)):
            sum_today += compare_cmp[i]['전날비교']
            sum_today_array.append(compare_cmp[i]['전날비교'])
        avg_today = sum_today/len(compare_cmp)
        max1 = (max(sum_today_array)+avg_today) / 2
        min1 = (min(sum_today_array)+avg_today) / 2

        for i in range(0,len(compare_cmp)):
            if compare_cmp[i]['지역이름'] == search_region:
                list = [int(i) for i in str(compare_cmp[i]['전날비교'])]
                if compare_cmp[i]['전날비교'] >= max1:
                    for x in range(5):
                        for y in range(22,32):
                            if array_screen[x][y] == 1:
                                array_screen[x][y] += 3
                if compare_cmp[i]['전날비교'] >= min1 and compare_cmp[i]['전날비교'] < max1:
                    for x in range(5):
                        for y in range(22,32):
                            if array_screen[x][y] == 1:
                                array_screen[x][y] += 2
                if compare_cmp[i]['전날비교'] >= 0 and compare_cmp[i]['전날비교'] < min1:
                    for x in range(5):
                        for y in range(22,32):
                            if array_screen[x][y] == 1:
                                array_screen[x][y] += 1
        yesterday_date_print(array_screen)
        yesterday_search_count(js_file_yesterday,search_region,array_screen)
        for x in range(6,11):
            for y in range(22):
                if array_screen[x][y] == 1:
                    array_screen[x][y] += 5
        yesterday_compare_data(js_file_yesterday, js_file_b_yesterday, search_region, y_compare_cmp, array_screen)

        for i in range(0,len(y_compare_cmp)):
            sum_yesterday += y_compare_cmp[i]['전날비교']
            sum_yesterday_array.append(y_compare_cmp[i]['전날비교'])
        avg_yesterday = sum_yesterday/len(y_compare_cmp)
        max2 = (max(sum_yesterday_array)+avg_yesterday) / 2
        min2 = (min(sum_yesterday_array)+avg_yesterday) / 2

        for i in range(0,len(y_compare_cmp)):
            if y_compare_cmp[i]['지역이름'] == search_region:
                list = [int(i) for i in str(y_compare_cmp[i]['전날비교'])]
                if y_compare_cmp[i]['전날비교'] >= max2:
                    for x in range(6,11):
                        for y in range(22,32):
                            if array_screen[x][y] == 1:
                                array_screen[x][y] += 3
                if y_compare_cmp[i]['전날비교'] >= min2 and y_compare_cmp[i]['전날비교'] < max2:
                    for x in range(6,11):
                        for y in range(22,32):
                            if array_screen[x][y] == 1:
                                array_screen[x][y] += 2
                if y_compare_cmp[i]['전날비교'] >= 0 and y_compare_cmp[i]['전날비교'] < min2:
                    for x in range(6,11):
                        for y in range(22,32):
                            if array_screen[x][y] == 1:
                                array_screen[x][y] += 1
        b_yesterday_date_print(array_screen)
        b_yesterday_search_count(js_file_b_yesterday,search_region,array_screen)
        for x in range(11,16):
            for y in range(22):
                if array_screen[x][y] == 1:
                    array_screen[x][y] += 6
       
        draw_matrix(array_screen);print()
        if search_region == '1':
            run_text = RunText()
            run_text.my_text = getdata(js_file)
            run_text.process()
            
        if search_region == '0': # 0을 입력하면 메뉴로 복귀
            compare_cmp = []
            y_compare_cmp = []
            b_y_compare_cmp = []
            main_menu = 0
            clear_array(array_screen)
            break

    if menu_choice == 4: # 메뉴 종료
        menu = 0


