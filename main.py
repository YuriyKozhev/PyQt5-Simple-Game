from scene import Scene

from PyQt5.QtWidgets import QApplication

import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    scene = Scene()
    sys.exit(app.exec_())