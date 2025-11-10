import sys
import os
from PyQt5 import QtWidgets, QtCore, QtGui

class SnippingWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.setWindowTitle("Snipping Tool")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowState(QtCore.Qt.WindowFullScreen)
        QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())
        print(f"Snipped area: ({x1}, {y1}) to ({x2}, {y2})")

        self.close()
        QtWidgets.QApplication.restoreOverrideCursor()

        # Use Qt's grabWindow for Linux
        screen = QtWidgets.QApplication.primaryScreen()
        screenshot = screen.grabWindow(0, x1, y1, x2 - x1, y2 - y1)
        save_path = os.path.join(os.path.dirname(__file__), "snip.png")
        screenshot.save(save_path, "png")
        print(f"Saved screenshot: {save_path} ({x2 - x1}x{y2 - y1})")

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            QtWidgets.QApplication.restoreOverrideCursor()
            self.close()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        # Draw semi-transparent overlay
        painter.fillRect(self.rect(), QtGui.QColor(0, 0, 0, 100))
        # Draw snipping rectangle if dragging
        if not self.begin.isNull() and not self.end.isNull():
            rect = QtCore.QRect(self.begin, self.end)
            painter.setPen(QtGui.QPen(QtGui.QColor(255, 0, 0), 2))
            painter.drawRect(rect)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = SnippingWidget()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()