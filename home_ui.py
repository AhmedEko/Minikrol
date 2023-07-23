# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSplitter, QTabWidget, QToolBox,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1313, 754)
        icon = QIcon()
        icon.addFile(u":/icons/Icons/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(0)
        self.menu_wg = QWidget(self.splitter)
        self.menu_wg.setObjectName(u"menu_wg")
        self.menu_wg.setMinimumSize(QSize(150, 0))
        font = QFont()
        font.setPointSize(10)
        self.menu_wg.setFont(font)
        self.menu_wg.setStyleSheet(u"background-color:#06162d;\n"
"color:#fff;\n"
"border:none;")
        self.gridLayout = QGridLayout(self.menu_wg)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(4, 4, 4, 15)
        self.toolBox = QToolBox(self.menu_wg)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"#toolBox {\n"
"	color: #fff;\n"
"}\n"
"\n"
"#toolBox::tab {\n"
"	padding-left:5px;\n"
"	text-align:left;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"\n"
"#toolBox::tab:selected {\n"
"	background-color: #2d9cdb;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"#toolBox QPushButton {\n"
"	padding:5px 0px 5px 20px;\n"
"	text-align:left;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"#toolBox QPushButton:hover {\n"
"	background-color: #85C1E9;\n"
"}\n"
"\n"
"#toolBox QPushButton:checked {\n"
"	background-color: #3498DB;\n"
"}\n"
"\n"
"")
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.page1.setGeometry(QRect(0, 0, 397, 223))
        self.verticalLayout = QVBoxLayout(self.page1)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.new_project_btn = QPushButton(self.page1)
        self.new_project_btn.setObjectName(u"new_project_btn")
        self.new_project_btn.setFocusPolicy(Qt.NoFocus)
        self.new_project_btn.setCheckable(False)

        self.verticalLayout.addWidget(self.new_project_btn)

        self.new_concept_btn = QPushButton(self.page1)
        self.new_concept_btn.setObjectName(u"new_concept_btn")
        self.new_concept_btn.setFocusPolicy(Qt.NoFocus)
        self.new_concept_btn.setCheckable(False)

        self.verticalLayout.addWidget(self.new_concept_btn)

        self.new_role_btn = QPushButton(self.page1)
        self.new_role_btn.setObjectName(u"new_role_btn")
        self.new_role_btn.setFocusPolicy(Qt.NoFocus)
        self.new_role_btn.setCheckable(False)

        self.verticalLayout.addWidget(self.new_role_btn)

        self.verticalSpacer = QSpacerItem(20, 102, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/new-badge-2-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page1, icon1, u"New")
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.page2.setGeometry(QRect(0, 0, 397, 223))
        self.page2.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.page2)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.open_project_btn = QPushButton(self.page2)
        self.open_project_btn.setObjectName(u"open_project_btn")
        self.open_project_btn.setFocusPolicy(Qt.NoFocus)
        self.open_project_btn.setCheckable(False)

        self.verticalLayout_2.addWidget(self.open_project_btn)

        self.open_concept_btn = QPushButton(self.page2)
        self.open_concept_btn.setObjectName(u"open_concept_btn")
        self.open_concept_btn.setFocusPolicy(Qt.NoFocus)
        self.open_concept_btn.setCheckable(False)

        self.verticalLayout_2.addWidget(self.open_concept_btn)

        self.open_role_btn = QPushButton(self.page2)
        self.open_role_btn.setObjectName(u"open_role_btn")
        self.open_role_btn.setFocusPolicy(Qt.NoFocus)
        self.open_role_btn.setCheckable(False)

        self.verticalLayout_2.addWidget(self.open_role_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 102, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/open-in-browser-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page2, icon2, u"open")
        self.page3 = QWidget()
        self.page3.setObjectName(u"page3")
        self.verticalLayout_3 = QVBoxLayout(self.page3)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.run_project_btn = QPushButton(self.page3)
        self.run_project_btn.setObjectName(u"run_project_btn")
        self.run_project_btn.setFocusPolicy(Qt.NoFocus)
        self.run_project_btn.setCheckable(True)

        self.verticalLayout_3.addWidget(self.run_project_btn)

        self.verticalSpacer_3 = QSpacerItem(20, 174, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/code-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page3, icon3, u"Run")
        self.page4 = QWidget()
        self.page4.setObjectName(u"page4")
        self.verticalLayout_4 = QVBoxLayout(self.page4)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.save_project_btn = QPushButton(self.page4)
        self.save_project_btn.setObjectName(u"save_project_btn")
        self.save_project_btn.setFocusPolicy(Qt.NoFocus)
        self.save_project_btn.setCheckable(False)

        self.verticalLayout_4.addWidget(self.save_project_btn)

        self.save_concept_btn = QPushButton(self.page4)
        self.save_concept_btn.setObjectName(u"save_concept_btn")
        self.save_concept_btn.setFocusPolicy(Qt.NoFocus)
        self.save_concept_btn.setCheckable(False)

        self.verticalLayout_4.addWidget(self.save_concept_btn)

        self.save_role_btn = QPushButton(self.page4)
        self.save_role_btn.setObjectName(u"save_role_btn")
        self.save_role_btn.setFocusPolicy(Qt.NoFocus)
        self.save_role_btn.setCheckable(False)

        self.verticalLayout_4.addWidget(self.save_role_btn)

        self.verticalSpacer_4 = QSpacerItem(20, 102, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        icon4 = QIcon()
        icon4.addFile(u":/icons/Icons/save-as-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page4, icon4, u"Save")

        self.gridLayout.addWidget(self.toolBox, 0, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 1, 1, 1, 1)

        self.exit_btn = QPushButton(self.menu_wg)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setMinimumSize(QSize(150, 50))
        self.exit_btn.setMaximumSize(QSize(1000, 1000))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        self.exit_btn.setFont(font1)
        self.exit_btn.setStyleSheet(u"#QPushButton {\n"
"	padding:5px 0px 5px 20px;\n"
"	text-align:left;\n"
"	border-radius: 3px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color:#85C1E9;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/Icons/x-mark-4-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_btn.setIcon(icon5)
        self.exit_btn.setCheckable(False)
        self.exit_btn.setChecked(False)

        self.gridLayout.addWidget(self.exit_btn, 2, 1, 1, 1)

        self.splitter.addWidget(self.menu_wg)
        self.main_wg = QWidget(self.splitter)
        self.main_wg.setObjectName(u"main_wg")
        self.gridLayout_2 = QGridLayout(self.main_wg)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.search_widget = QWidget(self.main_wg)
        self.search_widget.setObjectName(u"search_widget")
        self.search_widget.setStyleSheet(u"#search_widget {background-color: #ABB2B9;}")
        self.horizontalLayout_2 = QHBoxLayout(self.search_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_11 = QPushButton(self.search_widget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(30, 30))
        self.pushButton_11.setMaximumSize(QSize(30, 30))
        icon6 = QIcon()
        icon6.addFile(u":/icons/Icons/arrow-96-48.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon6)
        self.pushButton_11.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.pushButton_11)

        self.horizontalSpacer = QSpacerItem(241, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.search_frame = QFrame(self.search_widget)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setMinimumSize(QSize(300, 0))
        self.search_frame.setMaximumSize(QSize(300, 16777215))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.search_frame.setFont(font2)
        self.search_frame.setStyleSheet(u"#search_frame {\n"
"	border:  1px solid #aa7e6f;\n"
"	border-radius: 15px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#search_btn {\n"
"	padding:5px 5px;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"#search_btn:pressed {\n"
"	padding-left: 10px;\n"
"}")
        self.search_frame.setFrameShape(QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.search_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.wellcome_lbl = QLabel(self.search_frame)
        self.wellcome_lbl.setObjectName(u"wellcome_lbl")
        font3 = QFont()
        font3.setFamilies([u"Harlow Solid Italic"])
        font3.setPointSize(15)
        font3.setBold(False)
        font3.setItalic(True)
        self.wellcome_lbl.setFont(font3)

        self.horizontalLayout.addWidget(self.wellcome_lbl)


        self.horizontalLayout_2.addWidget(self.search_frame)

        self.horizontalSpacer_2 = QSpacerItem(241, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.user_label = QLabel(self.search_widget)
        self.user_label.setObjectName(u"user_label")
        self.user_label.setMinimumSize(QSize(30, 30))
        self.user_label.setMaximumSize(QSize(30, 30))
        self.user_label.setStyleSheet(u"#user_label {\n"
"	background-color: #fff;\n"
"	border: 1px solid #F2F4F4;\n"
"	padding: 5px 5px;\n"
"	border-radius: 15%;\n"
"}")
        self.user_label.setPixmap(QPixmap(u":/icons/Icons/user-48.ico"))
        self.user_label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.user_label)


        self.gridLayout_2.addWidget(self.search_widget, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.main_wg)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFont(font1)

        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.splitter.addWidget(self.main_wg)

        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_11.toggled.connect(self.menu_wg.setHidden)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MiniKrol", None))
        self.new_project_btn.setText(QCoreApplication.translate("MainWindow", u"Project", None))
        self.new_concept_btn.setText(QCoreApplication.translate("MainWindow", u"Concept", None))
        self.new_role_btn.setText(QCoreApplication.translate("MainWindow", u"Role", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page1), QCoreApplication.translate("MainWindow", u"New", None))
        self.open_project_btn.setText(QCoreApplication.translate("MainWindow", u"Project", None))
        self.open_concept_btn.setText(QCoreApplication.translate("MainWindow", u"Concept", None))
        self.open_role_btn.setText(QCoreApplication.translate("MainWindow", u"Role", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page2), QCoreApplication.translate("MainWindow", u"open", None))
        self.run_project_btn.setText(QCoreApplication.translate("MainWindow", u"Project", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page3), QCoreApplication.translate("MainWindow", u"Run", None))
        self.save_project_btn.setText(QCoreApplication.translate("MainWindow", u"Project", None))
        self.save_concept_btn.setText(QCoreApplication.translate("MainWindow", u"Concept", None))
        self.save_role_btn.setText(QCoreApplication.translate("MainWindow", u"Role", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page4), QCoreApplication.translate("MainWindow", u"Save", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.pushButton_11.setText("")
        self.wellcome_lbl.setText(QCoreApplication.translate("MainWindow", u"   Wellcome to MiniKrol", None))
        self.user_label.setText("")
    # retranslateUi

