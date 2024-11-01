# from moviepy.editor import VideoFileClip
import moviepy.editor
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import cv2


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.init_slots()
        self.video_path = ''   #视频路径
        self.init_timer()
        self.cap = cv2.VideoCapture()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(502, 439)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(57, 17, 389, 227))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 270, 481, 32))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.toolButtonInput = QtWidgets.QToolButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButtonInput.sizePolicy().hasHeightForWidth())
        self.toolButtonInput.setSizePolicy(sizePolicy)
        self.toolButtonInput.setMinimumSize(QtCore.QSize(40, 30))
        self.toolButtonInput.setObjectName("toolButtonInput")
        self.horizontalLayout.addWidget(self.toolButtonInput)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(310, 350, 181, 32))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(70, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(70, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton.setMinimumSize(QtCore.QSize(70, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(70, 30))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.label_template = QtWidgets.QLabel(self.centralwidget)
        self.label_template.setGeometry(QtCore.QRect(50, 10, 403, 241))
        self.label_template.setText("")
        self.label_template.setObjectName("label_template")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 310, 481, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.time_start = QtWidgets.QTextEdit(self.widget)
        self.time_start.setObjectName("time_start")
        self.horizontalLayout_3.addWidget(self.time_start)
        self.label_7 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(40, 30))
        self.label_7.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.textEdit_3 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_3.setObjectName("textEdit_3")
        self.horizontalLayout_3.addWidget(self.textEdit_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 502, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "视频路径："))
        self.toolButtonInput.setText(_translate("MainWindow", "..."))
        self.pushButton_2.setText(_translate("MainWindow", "关闭"))
        self.pushButton.setText(_translate("MainWindow", "切片"))
        self.label_6.setText(_translate("MainWindow", "选择视频时长：从"))
        self.label_7.setText(_translate("MainWindow", "到"))

    def init_slots(self):
        self.pushButton.clicked.connect(self.split_video_to_gifs)  # 连接切片函数
        # self.comboBoxModel.currentTextChanged.connect(self.ModelChanged)
        # self.comboBoxScale.currentTextChanged.connect(self.ScaleChanged)
        self.toolButtonInput.clicked.connect(self.InpurDir)           # 连接视频路径选择函数
        # self.toolButtonOutput.clicked.connect(self.SaveResults)
        # self.pushButton_2.clicked.connect(self.close)
        pix = QPixmap('template_1.png')
        self.label_template.setPixmap(pix)
        self.label_template.setScaledContents(True)  # 自适应QLabel大小
        #self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=Qt.KeepAspectRatio))  # 在label上显示图片
    def InpurDir(self):
        video_type = [".mp4", ".mkv", ".MOV", "avi"]
        self.video_path = QtWidgets.QFileDialog.getOpenFileName()[0]
        # if self.video_path:
        #     for vdi in video_type:
        #         if vdi in self.video_path:
        #             continue
        #         else:
        #             QtWidgets.QMessageBox.information(self, "Wrong", "不支持该格式", QtWidgets.QMessageBox.Yes,
        #                                               QtWidgets.QMessageBox.Yes)
        #             break
        print("选择的输入视频路径：", self.video_path)
        self.textEdit.setPlainText(self.video_path)
        print("videoIsOpen")
        self.cap.open(self.video_path) #打开视频
        self.timer.start(30)   #设置视频播放计时器

    def init_timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.play_video)

    def play_video(self):
        ret, img = self.cap.read()
        if ret:
            cur_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # 视频流的长和宽
            height, width = cur_frame.shape[:2]
            pixmap = QImage(cur_frame, width, height, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(pixmap)

            # 获取是视频流和label窗口的长宽比值的最大值，适应label窗口播放，不然显示不全
            ratio = max(width / self.label.width(), height / self.label.height())
            pixmap.setDevicePixelRatio(ratio)
            # 视频流置于label中间部分播放
            self.label.setAlignment(Qt.AlignCenter)
            self.label.setPixmap(pixmap)

    def split_video_to_gifs(self):
        # 读取视频文件
        video = moviepy.editor.VideoFileClip(self.video_path).subclip(0, 10)  # 取前10秒
        # video = VideoFileClip(input_video)

        # 获取视频的宽和高
        width, height = video.size

        # 计算每个部分的宽度
        segment_width = width / 5

        for i in range(5):
            # 计算每个 GIF 的起始和结束位置
            start_x = i * segment_width
            end_x = start_x + segment_width

            # 裁剪视频
            gif_segment = video.crop(x1=start_x, x2=end_x, y1=0, y2=height)

            # 生成 GIF 文件
            gif_segment.write_gif(f"{output_gif_prefix}_part{i + 1}.gif", fps=10)

        # 关闭视频文件
        video.close()
        print("ok")
        QtWidgets.QMessageBox.information(self, "Result", "Done", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.Yes)


# 使用示例
input_video = "5.mp4"  # 输入的 MP4 文件路径
output_gif_prefix = "output_gif"  # 输出 GIF 文件的前缀
# split_video_to_gifs(input_video, output_gif_prefix)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.setWindowTitle('SteamVideoCut')

    # style_file = './style.qss'
    # style_sheet = QSSLoader.read_qss_file(style_file)
    # ui.setStyleSheet(style_sheet)

    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    # app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))

    #apply_stylesheet(app, theme='dark_teal.xml')

    ui.show()
    sys.exit(app.exec_())