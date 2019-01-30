from PyQt4 import QtCore, QtGui, QtWebKit
import sys

class Browser(QtGui.QMainWindow):
    def __init__(self):
        """
            Initialize the browser GUI and connect the events
            self.html.settings -> QtWebKit.QWebSettings
        """

        QtGui.QMainWindow.__init__(self)
        self.resize(800,600)
        self.centralwidget = QtGui.QWidget(self)

        self.mainLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setMargin(1)

        self.frame = QtGui.QFrame(self.centralwidget)

        self.gridLayout = QtGui.QVBoxLayout(self.frame)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)

        self.horizontalLayout = QtGui.QHBoxLayout()
        self.tb_url = QtGui.QLineEdit(self.frame)
        self.bt_back = QtGui.QPushButton(self.frame)
        self.bt_ahead = QtGui.QPushButton(self.frame)

        self.bt_back.setIcon(QtGui.QIcon().fromTheme("go-previous"))
        self.bt_ahead.setIcon(QtGui.QIcon().fromTheme("go-next"))

        self.horizontalLayout.addWidget(self.bt_back)
        self.horizontalLayout.addWidget(self.bt_ahead)
        self.horizontalLayout.addWidget(self.tb_url)
        self.gridLayout.addLayout(self.horizontalLayout)

        self.html = QtWebKit.QWebView()
        self.html.loadFinished.connect(self.get_html)
        self.gridLayout.addWidget(self.html)
        self.mainLayout.addWidget(self.frame)
        self.setCentralWidget(self.centralwidget)

        self.connect(self.tb_url, QtCore.SIGNAL("returnPressed()"), self.browse)
        self.connect(self.bt_back, QtCore.SIGNAL("clicked()"), self.html.back)
        self.connect(self.bt_ahead, QtCore.SIGNAL("clicked()"), self.html.forward)

        self.default_url = "http://google.com"
        self.tb_url.setText(self.default_url)
        self.browse()
    
    def get_html(self):
        # page_url = self.html.url()
        # if 'maps.php' in page_url ....
        page = self.html.page()
        frame = page.mainFrame()
        html_code = unicode(frame.toHtml())
        return html_code

    def browse(self):
        """
            Make a web browse on a specific url and show the page on the
            Webview widget.
        """

        url = self.tb_url.text() if self.tb_url.text() else self.default_url
        self.html.load(QtCore.QUrl(url))
        self.html.show()

if __name__ == '__main__':
    qapp = QtGui.QApplication(sys.argv)
    w = Browser()
    w.show()
    sys.exit(qapp.exec_())