# PyQt5 introduction

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test GUI")
        self.setGeometry(500, 100, 500, 100)
        self.setWindowIcon(QIcon("Lessons/52-PyQt5 GUI/AWW.png"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #292929;"
                            "background-color: #19aec2;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        
        image = QLabel(self)
        image.setGeometry(0, 0, 100, 100)

        pixmap = QPixmap("Lessons/52-PyQt5 GUI/AWW.png")
        image.setPixmap(pixmap)

        image.setScaledContents(True)

        image.setGeometry(self.width() - image.width(),
                           0, 
                           image.width(), 
                           image.height())

        # Center Image
        # image.setGeometry((self.width() - image.width()) // 2,
        #                    (self.height() - image.height()) // 2, 
        #                    image.width(), 
        #                    image.height())
        
        # label.setAlignment(Qt.AlignTop)       # vertically top
        # label.setAlignment(Qt.AlignBottom)    # vertically bottom
        # label.setAlignment(Qt.AlignVCenter)   # vertically center
        # label.setAlignment(Qt.AlignRight)     # horizontally right
        # label.setAlignment(Qt.AlignHCenter)   # horizontally center
        # label.setAlignment(Qt.AlignLeft)
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)  # center & top
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # center & bottom
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # center & center
        label.setAlignment(Qt.AlignCenter)  # center & center

        

def main():
    app = QApplication(sys.argv) 
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
