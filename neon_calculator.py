from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class Calculator(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Neon Calculator")
        self.setFixedSize(400,600)

        self.expression=""


        self.setStyleSheet("""
        QWidget{
            background:#080808;
        }

        QLineEdit{
            background:#111;
            color:#00ffff;
            border-radius:20px;
            padding:20px;
            font-size:40px;
        }

        QPushButton{

            background:#151515;
            color:white;
            border-radius:35px;
            font-size:22px;

        }

        QPushButton:hover{

            background:#00ffff;
            color:black;

        }

        """)



        layout=QVBoxLayout()


        self.display=QLineEdit()

        self.display.setAlignment(
            Qt.AlignRight
        )

        layout.addWidget(
            self.display
        )


        buttons=[
            "AC","(",")","÷",
            "7","8","9","×",
            "4","5","6","-",
            "1","2","3","+",
            "0",".","√","="
        ]


        grid=QGridLayout()


        r=0
        c=0


        for text in buttons:

            btn=QPushButton(text)

            btn.setFixedSize(
                75,75
            )

            btn.clicked.connect(
                lambda checked=False,
                t=text:self.press(t)
            )


            grid.addWidget(
                btn,r,c
            )


            c+=1

            if c==4:
                c=0
                r+=1


        layout.addLayout(grid)

        self.setLayout(layout)



    def press(self,value):

        if value=="AC":

            self.expression=""


        elif value=="=":

            try:

                exp=self.expression

                exp=exp.replace(
                    "×","*"
                )

                exp=exp.replace(
                    "÷","/"
                )


                self.expression=str(
                    eval(exp)
                )


            except:

                self.expression="ERROR"



        elif value=="√":

            try:
                self.expression=str(
                    float(self.expression)**0.5
                )

            except:
                pass


        else:

            self.expression+=value



        self.display.setText(
            self.expression
        )



app=QApplication([])

window=Calculator()

window.show()

app.exec()