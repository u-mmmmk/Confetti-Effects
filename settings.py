'''
For settings UI and configuration
'''

from aqt import mw
from aqt.qt import *

from .config import CONFIG, save_config

class ConfettiSettings(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        #widget settings
        self.setWindowTitle("Confetti Settings")

        self.date_setting = QDateEdit()
        self.date_setting.setCalendarPopup(True)
        qdate = QDate.fromString(CONFIG["Test_Date"], "MM-dd-yyyy")
        self.date_setting.setDate(qdate)

        self.confetti_box = QCheckBox(text="Confetti")
        self.confetti_box.setChecked(CONFIG["Confetti"])

        self.mature_box = QCheckBox(text="Confetti when card matures")
        self.mature_box.setChecked(CONFIG["Mature_Cards"])

        #put together widgets
        layout = QVBoxLayout()

        date_layout = QHBoxLayout()
        date_layout.addWidget(QLabel("Test date:"))
        date_layout.addWidget(self.date_setting)

        layout.addLayout(date_layout)
        layout.addWidget(self.confetti_box)
        layout.addWidget(self.mature_box)

        self.setLayout(layout)

    def closeEvent(self, event):
        qdate = self.date_setting.date()
        CONFIG["Test_Date"] = qdate.toString("MM-dd-yyyy")
        CONFIG["Confetti"] = self.confetti_box.isChecked()
        CONFIG["Mature_Cards"] = self.mature_box.isChecked()
        save_config()

        super().closeEvent(event)

def open_settings():
    dialog = ConfettiSettings(mw)
    dialog.exec()

