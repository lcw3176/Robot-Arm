from tkinter import *
import serial
import time
import struct
ard = serial.Serial('COM3', 9600)


class Arm:
    def __init__(self, win):
        self.win = win
        self.can = Canvas(self.win, height='600', width='800')
        self.can.pack()
        self.font = 'consolas 20'
        self.button = Button(self.win, text='LEFT', background='violet', font=self.font, command=self.left)
        self.button.place(x='250', y='250')
        self.button = Button(self.win, text='RIGHT', background='violet', font=self.font, command=self.right)
        self.button.place(x='450', y='250')
        self.button = Button(self.win, text=' UP ', background='violet', font=self.font, command=self.up)
        self.button.place(x='350', y='150')
        self.button = Button(self.win, text='DOWN', background='violet', font=self.font, command=self.down)
        self.button.place(x='350', y='350')

        self.button = Button(self.win, text='PICK UP', background='green', font=self.font, command=self.pick)
        self.button.place(x='100', y='450')
        self.button = Button(self.win, text='LAY DOWN', background='green', font=self.font, command=self.lay)
        self.button.place(x='550', y='450')

        self.button = Button(self.win, text='RECORD', background='red', font=self.font, command=self.record)
        self.button.place(x='100', y='50')

        self.button = Button(self.win, text='SAVE', background='yellow', font=self.font, command=self.save)
        self.button.place(x='550', y='50')

        self.button = Button(self.win, text='START', font=self.font, background='blue', command=self.start)
        self.button.place(x='350', y='50')

        self.button = Button(self.win, text='STOP', font=self.font, background='yellow', command=self.stop)
        self.button.place(x='350', y='250')

        self.rec = False
        self.i = 0
        self.count = 0

        self.moving = []
        self.timing = []
        self.time = 0
        self.now_time = 0

    def left(self):
        ard.write(struct.pack('>B', 1))  # 포맷 B == C: unsigned char , Python : integer
        if self.rec is True:  # 녹화 시작 시 작동
            self.moving.append('1')  # moving 리스트에 데이터 추가
            self.time = time.time()  # 버튼이 눌린 시점의 시간 저장

    def right(self):
        ard.write(struct.pack('>B', 2))
        if self.rec is True:
            self.moving.append('2')
            self.time = time.time()

    def up(self):
        ard.write(struct.pack('>B', 3))
        if self.rec is True:
            self.moving.append('3')
            self.time = time.time()

    def down(self):
        ard.write(struct.pack('>B', 4))
        if self.rec is True:
            self.moving.append('4')
            self.time = time.time()

    def pick(self):
        ard.write(struct.pack('>B', 5))
        if self.rec is True:
            self.moving.append('5')
            self.time = time.time()

    def lay(self):
        ard.write(struct.pack('>B', 6))
        if self.rec is True:
            self.moving.append('6')
            self.time = time.time()

    def stop(self):
        ard.write(struct.pack('>B', 7))
        self.now_time = time.time()  # 작동 중지 명령 때의 시간 저장
        self.now_time = self.now_time - self.time  # 시간차 계산
        self.timing.append(round(self.now_time, 3))  # timing 리스트에 소수점 3자리 시간까지 데이터 저장

    def record(self):
        ard.write(struct.pack('>B', 8))  # 8번 명령: 각도 초기값 세팅
        del self.moving[:]  # 남아있는 이전 기록 제거
        del self.timing[:]
        self.rec = True  # 녹화 시작

    def save(self):
        self.rec = False  # 녹화 중지

    def start(self):
        ard.write(struct.pack('>B', 8))  # 각도 초기값 세팅
        time.sleep(0.5)
        while 1:
            self.i = self.moving[0]          # 리스트 값 맨 앞에서부터 하나씩 추출
            del self.moving[0]               # 추출한 값 삭제
            self.i = int(self.i)             # integer 형으로 변환
            ard.write(struct.pack('>B', self.i))
            time.sleep(self.timing[0])       # 시리얼 통신 후 저장된 시간만큼 정지
            ard.write(struct.pack('>B', 7))  # 7번 명령: 정지
            del self.timing[0]               # 추출한 값 삭제
            self.count = len(self.moving)    # 저장된 리스트 길이 측정
            if self.count is 0:              # 모든 저장된 값 소멸시 정지
                break


root = Tk()
root.geometry('800x600+350+100')
root.title('로봇 팔 제어')


if __name__ == '__main__':
    arm = Arm(root)
    root.mainloop()
