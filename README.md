# osscap2020

### <활용한 오픈소스>
> 크롤링 : 

> 스크롤링 led 출력 :         
https://github.com/hzeller/rpi-rgb-led-matrix/tree/master/bindings/python/samples   
https://github.com/sprach/LabRpiLed/blob/7a2db8f669e27849c2622369e0d0109e0b58830e/src/rgbledmatrix/runtext2.py


### <필요한 설치 모듈>
**RGB LED Matrix 모듈 설치**

1. git clone을 진행한다.
``` 
$ git clone https://github.com/hzeller/rpi-rgb-led-matrix
```
2. 샘플 API를 make한 뒤에 demo를 실행한다.
```
$ cd ~/rpi-rgb-led-matrix/examples-api-use
$ make
$ sudo ./demo --led-rows=32 --led-cols=64 --led-chain=1 --led-parallel=1 --led-no-hardware-pulse -D 9
```

   * 전광판 그림이 깨진다면 'led-slowdown-gpio'값을 증가시켜 본다.
```
 $ sudo ./demo --led-rows=32 --led-cols=64 --led-chain=1 --led-parallel=1 --led-no-hardware-pulse --led-slowdown-gpio=2 -D 9
```
**Python 모듈 설치**
1. 개발용 Python3를 설치한다.
```
$ sudo apt-get update
$ sudo apt-get install python3-dev python3-pillow -y
```

2. 빌더를 진행한다.
```
$ cd ~/rpi-rgb-led-matrix/bindings/python
$ make build-python PYTHON=$(which python3)
$ sudo make install-python PYTHON=$(which python3)
```

### <사용 방법>
1. git clone을 진행한다.
```
$ git clone https://github.com/ekqls3301/osscap2020.git
```

2. Final_Code에 있는 crawlKoreaData_All.py, crawlKoreaData_Seoul.py, crawlKoreaData_Gyeonggi.py를 실행한다.
```
$ cd osscap2020/Final_Code/
$ python3 crawlKoreaData_All.py
$ python3 crawlKoreaData_Seoul.py
$ python3 crawlKoreaData_Gyeonggi.py
```

3. Final_Code에 이틀 전, 어제, 오늘의 날짜가 표시된 crawlKoreaData_All_날짜.js, crawlKoreaData_Seoul_날짜.js, crawlKoreaData_Gyeonggi_날짜.js 파일이 있는지 확인한다. (3일치 파일이 없는 경우 main.py를 실행할 수 없다.)
``` 
$ ls
```

4. main.py를 실행한다.
```
$ sudo python3 ./main.py --led-no-hardware-pulse LED_NO_HARDWARE_PULSE
```

**main 실행 시**
- <시작 화면>   터미널에 메뉴가 출력되고 led matrix에 'COVID' 문구, 오늘까지의 확진자수와 함께 꽃 그림이 출력된다.
  - 키보드로 실행할 메뉴의 숫자를 입력한다.
  
- 메뉴 1을 실행할 경우
  - 터미널에 'scroll 기능 실행 시 1 입력 : '이 출력된다.
  - 1을 입력할 경우, 터미널에 'Press CTRL-C to stop sample'이라는 문구가 출력되며 led matrix에 전국 코로나 확진자 수가 스크롤링된다.
  - 스크롤링을 멈추고 싶으면 키보드의 Ctrl과 C를 동시에 누르면 된다.

- 메뉴 2를 실행할 경우
  - 터미널에 '지역을 입력하세요 (ex:종로구): '가 출력된다.
  - 만약 종로구를 입력했다면, 터미널에는 오늘, 어제, 이틀 전의 종로구의 코로나 확진자 수가 출력되고 led matrix에는 오늘, 어제, 이틀 전의 날짜와 종로구의 확진자수, 확진자 증감수가 출력된다.
  - 0을 입력할 경우, 시작 화면으로 돌아간다.
  - 1을 입력할 경우, 터미널에 'Press CTRL-C to stop sample'이라는 문구가 출력되며 led matrix에 서울 코로나 확진자 수가 스크롤링된다.
  - 스크롤링을 멈추고 싶으면 키보드의 Ctrl과 C를 동시에 누르면 된다.

- 메뉴 3을 실행할 경우
  - 터미널에 '지역을 입력하세요 (ex:수원): '이 출력된다.
  - 만약 수원을 입력했다면, 터미널에는 오늘, 어제, 이틀 전의 수원의 코로나 확진자 수가 출력되고 led matrix에는 오늘, 어제, 이틀 전의 날짜와 수원의 확진자수, 확진자 증감수가 출력된다.
  - 0을 입력할 경우, 시작 화면으로 돌아간다.
  - 1을 입력할 경우, 터미널에 'Press CTRL-C to stop sample'이라는 문구가 출력되며 led matrix에 경기도 코로나 확진자 수가 스크롤링된다.
  - 스크롤링을 멈추고 싶으면 키보드의 Ctrl과 C를 동시에 누르면 된다.
  
- 메뉴 4를 실행할 경우
  - main.py가 종료된다.
