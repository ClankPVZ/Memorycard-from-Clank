#создай приложение для запоминания информации
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import *
from random import shuffle

class Question():
    def __init__(
        self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

    
question_list = []
question_list.append(Question('Государственный язык Бразилии?', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
question_list.append(Question('Какого цвета нет на флаге России?', 'зеленый', 'синий', 'красный', 'белый')) 
question_list.append(Question('Национальные жилища якутов?', 'Ураса', 'Иглу', 'Юрта', 'Коробка'))


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
button = QPushButton('Ответить')
main_label = QLabel('Какой национальности не существует?')


radio_group_box = QGroupBox('Варианты ответов:')
rad_but1 = QRadioButton('Энцы')
rad_but2 = QRadioButton('Смурфы')
rad_but3 = QRadioButton('Чулымцы')
rad_but4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rad_but1)
RadioGroup.addButton(rad_but2)
RadioGroup.addButton(rad_but3)
RadioGroup.addButton(rad_but4)
hline = QHBoxLayout()
line2 = QVBoxLayout()
line3 = QVBoxLayout()

line2.addWidget(rad_but1)
line2.addWidget(rad_but2)
line3.addWidget(rad_but3)
line3.addWidget(rad_but4)
hline.addLayout(line2)
hline.addLayout(line3)

radio_group_box.setLayout(hline)

answer_group_box = QGroupBox('Результат теста')
right_or_wrong = QLabel('Прав ты или нет?')
result = QLabel('Ответ будет тут!')

Vline = QVBoxLayout()
Vline.addWidget(right_or_wrong, alignment = Qt.AlignLeft)
Vline.addWidget(result, alignment = Qt.AlignVCenter)
answer_group_box.setLayout(Vline)

H_line1 = QHBoxLayout()
H_line2 = QHBoxLayout()
H_line3 = QHBoxLayout()

H_line1.addWidget(main_label, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
H_line2.addWidget(radio_group_box)
H_line3.addWidget(button)

V_line1 = QVBoxLayout()
V_line1.addLayout(H_line1)
V_line1.addLayout(H_line2)
V_line1.addLayout(H_line3)


def show_question():
    radio_group_box.show()
    answer_group_box.hide()
    button.setText('Ответить')

def show_result():
    radio_group_box.hide()
    answer_group_box.show()
    button.setText('Следующий вопрос')

    RadioGroup.setExclusive(False)
    rad_but1.setChecked(False)
    rad_but2.setChecked(False)
    rad_but3.setChecked(False)
    rad_but4.setChecked(False)
    RadioGroup.setExclusive(True)



answer = [rad_but1, rad_but2, rad_but3, rad_but4]

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    main_label.setText(q.question)
    result.setText(q.right_answer)
    show_question()

def show_correct(res):
    right_or_wrong.setText(res)
    show_result()


def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print('Статистика\n-Всего вопросов:' , main_win.total, '\n-Правильных ответов:' , main_win.score)
        print('Рейнтинг:' , main_win.score/main_win.total * 100)
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неверно!')
            main_win.score += 1
            print('Рейнтинг:' , main_win.score/main_win.total * 100)


main_win.cur_question = -1

def next_question():
    main_win.total += 1
    print('Статистика\n-Всего вопросов:' , main_win.total, '\n-Правильных ответов:' , main_win.score)
    main_win.cur_question += 1
    if main_win.cur_question >= len(question_list):
        main_win.cur_question = 0
    q = question_list[main_win.cur_question]
    ask(q)
    

    

def click_on():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

answer_group_box.hide()

main_win.score = 0
main_win.total = 0


q = Question('Когда произошел укус?', '1983', '1987', '2012', '100000000')
ask(q)

button.clicked.connect(click_on)
next_question()
button.clicked.connect(check_answer)

main_win.resize(400, 300)
main_win.setLayout(V_line1)
main_win.show()
app.exec_()