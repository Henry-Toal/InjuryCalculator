from InjuryCalculator import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
import sys

    # Configuration Options
############################################################
############################################################



############################################################
############################################################





    # Main Block
############################################################
############################################################

    # Initialize Application
# ----------------------------------------------------------
Calc = QApplication(sys.argv)
# ----------------------------------------------------------

    # Set up layout
# ----------------------------------------------------------

# ----------------------------------------------------------


    # Adding Layout
# ----------------------------------------------------------

# ----------------------------------------------------------

    # Building the main system for data
# ----------------------------------------------------------

class CalcPage(QDialog):

    def __init__(self, parent=None):
        super(CalcPage, self).__init__(parent)


            # Widgets
        self.con = QLineEdit()
        con_label = QLabel("Constitution Modifier", self)
        con_layout = QHBoxLayout()
        con_layout.addWidget(self.con)
        con_layout.addWidget(con_label)

        self.level = QLineEdit()
        level_label = QLabel("Character Level", self)
        level_layout = QHBoxLayout()
        level_layout.addWidget(self.level)
        level_layout.addWidget(level_label)

        self.spill = QLineEdit()
        spill_label = QLabel("Spillover Damage", self)
        spill_layout = QHBoxLayout()
        spill_layout.addWidget(self.spill)
        spill_layout.addWidget(spill_label)

        self.sev_output = QLineEdit()
        sev_output_label = QLabel("Severity", self)
        sev_output_layout = QHBoxLayout()
        sev_output_layout.addWidget(self.sev_output)
        sev_output_layout.addWidget(sev_output_label)

        self.loc_output = QLineEdit()
        loc_output_label = QLabel("Location", self)
        loc_output_layout = QHBoxLayout()
        loc_output_layout.addWidget(self.loc_output)
        loc_output_layout.addWidget(loc_output_label)

        self.go_button = QPushButton('Go!')






        con_label.setBuddy(self.con)
        level_label.setBuddy(self.level)
        spill_label.setBuddy(self.spill)


            # Layout
        layout = QVBoxLayout()

        layout.addLayout(con_layout)
        layout.addLayout(level_layout)
        layout.addLayout(spill_layout)
        layout.addWidget(self.go_button)
        layout.addLayout(loc_output_layout)
        layout.addLayout(sev_output_layout)

        self.setLayout(layout)

        self.go_button.clicked.connect(self.display)

    def display(self):

        try:
            injury = Injury(level=self.level.text(), con=self.con.text(), spill=self.spill.text())
            self.sev_output.setText(f'{injury.severity}')
            self.loc_output.setText((f'{injury.location.name}'))
        except ValueError as e:
            ErrorBox = QDialog()
            error_text = str(e)
            error_text_box = QTextEdit()
            error_layout = QVBoxLayout()
            error_layout.addWidget(error_text_box)
            error_text_box.setText(error_text)
            ErrorBox.show()
            ErrorBox.exec_()


# ----------------------------------------------------------

    # Showing Pages
# ----------------------------------------------------------
calcpage = CalcPage()
calcpage.show()
# ----------------------------------------------------------



    # Executing
# ----------------------------------------------------------
sys.exit(Calc.exec_())
# ----------------------------------------------------------

############################################################
############################################################
