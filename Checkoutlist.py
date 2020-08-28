import os
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QTextBrowser, QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QIcon

t2_list = []

book_co4_1={}
book_co5_1={}
book_co6_1={}

def div(b_data):
    b_data2 = b_data.replace("-",",")
    t_list = b_data2[13:].split(",")
    for i in range(int(len(t_list)/2)):
        t2_list.append({t_list[i*2]:int(t_list[i*2+1])})
    return t2_list

def read_line(data1):
    with open(data1,'r',encoding='utf8') as f:
        fline = f.readlines()
        return fline

def read_title(data2):
    with open(data2,'r',encoding='utf8') as f2:
        fline_2 = f2.readline()
        fline_2 = fline_2[:7]
        return fline_2

if __name__=="__main__":
    lines = []
    line_title = []

    with os.scandir('Checkout') as entries:
        for entry in entries:
            line = read_line("Checkout\\%s" % entry.name)
            lines.append(line)
            line2 = read_title("Checkout\\%s" % entry.name)
            line_title.append(line2)

for data_list in lines:
    data_list2 = ",".join(data_list)
    list4= div(data_list2)

book_co4 = list4[:10]
for j in book_co4:
    book_co4_1.update(j)

book_co5 = list4[10:20]
for k in book_co5:
    book_co5_1.update(k)

book_co6 = list4[20:30]
for l in book_co6:
    book_co6_1.update(l)

list5=[book_co4_1 , book_co5_1 , book_co6_1]

book_sort=['000(총류)', '100(철학)', '200(종교)', '300(사회학)', '400(자연과학)', '500(기술과학)', '600(예술)', '700(언어)', '800(문학)', '900(역사)']
book_sum=[]
for n in book_sort:
    book_sum.append(sum(item[n] for item in list5))

save2= list(list5[0].values())
save3= list(list5[1].values())
save4= list(list5[2].values())

print(book_sort)
print(line_title[0],"=",save2)
print(line_title[1],"=",save3)
print(line_title[2],"=",save4)
print("20년도 2분기 대출현황 =",book_sum)

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl = QLabel("<b>Do you want to save?</b>",self)
        lbl.setAlignment(Qt.AlignCenter)

        font = lbl.font()
        font.setPointSize(13)

        lbl.setFont(font)

        text = QTextBrowser(self)
        text.setAcceptRichText(True)
        text.setOpenExternalLinks(True)
        text.append("4월 대출현황={0} \n5월 대출현황={1} \n6월 대출현황={2} \n20년도 2분기 대출현황={3}".format(save2, save3, save4, book_sum))

        btn1 = QPushButton('Yes', self)
        btn2 = QPushButton('No', self)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addWidget(lbl)
        vbox.addWidget(text)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        btn1.clicked.connect(self.save)
        btn2.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('Book Checkout')
        self.setWindowIcon(QIcon('save.png'))
        self.setGeometry(500, 400, 450, 150)
        self.show()

    def save(self):
        with open("Book_checkout.csv", 'w', encoding="UTF-8") as f:
            book_sort.insert(0, "분류")
            f.write(",".join(book_sort))
            f.write("\n")

            save2.insert(0, line_title[0])
            save3.insert(0, line_title[1])
            save4.insert(0, line_title[2])
            book_sum.insert(0, "20년도 2분기 대출현황")

            for i in [save2, save3, save4, book_sum]:
                temp = []
                for k in i:
                    temp.append(str(k))
                f.write(",".join(temp))
                f.write("\n")
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())



