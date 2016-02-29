from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_MainWindow
import sys,requests,threading,subprocess,os,shutil,time
from bs4 import BeautifulSoup;
import you_get
import you_get.common


class Mywin(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Mywin,self).__init__()
        self.setupUi(self);
        self.search.clicked.connect(self.getLinks);
        self.exit.clicked.connect(self.downloadJ)
        self.line1.returnPressed.connect(self.getLinks)
        self.bar1.setValue(0);

        self.list1.itemDoubleClicked.connect(self.playTv);
        # self.tread =


    def GetLink(self):
        self.th = threading.Thread(target=self.getLinks);
        self.th.start()

    def playTv(self):
        self.th = threading.Thread(target=self.PlayTv);
        self.th.start()

    def downloads(self):
        self.bar1.setValue(0)
        self.th = threading.Thread(target=self.downloadJ);
        self.th.start()

        # QtCore.QThread()

    def downloadJ(self):
        urls1 = self.downloadlist.values()
        self.o1 = 100/len(urls1);
        self.count = 0
        self.tt = foo().tt;

        if (not os.path.exists(os.getcwd()+'/'+self.flodName)):
            os.mkdir(os.getcwd()+'/'+self.flodName)
        self.app = Work(urls1,self.flodName);
        self.app.start()
        self.app.pp.connect(self.setval);

    def setval(self):
        self.count = self.count + 1;
        self.bar1.setValue(self.o1*self.count);

    def getLinks(self):
        url = self.line1.text();
        content = requests.get(url).text;
        html = BeautifulSoup(content,'html.parser');
        self.playlist = [];
        self.flodName = html.find("div",{"class":'v-title'}).h1.string;
        print(self.flodName)
        self.downloadlist = {};
        for i in html.find_all("option"):
            self.playlist.append(i.text);
            self.downloadlist[i.string] = 'http://www.bilibili.com'+i['value'];
        self.list1.clear();
        self.playlist.sort()
        self.list1.addItems(self.playlist);
        #self.webView();
    def PlayTv(self):
        row = self.list1.currentRow();
        row = self.list1.item(row)
        row = row.text()
        url = subprocess.Popen(['you-get','-u',self.downloadlist[row]],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        self.playLink = ''
        for i in url.stdout.readlines():
            i = i.decode("utf-8").replace("\n","");
            if i.find("http") != -1:
                self.playLink = self.playLink + i + ' ';
        subprocess.Popen(['deepin-movie',self.playLink])
        self.playLink = '';

class Work(QtCore.QThread):
    pp = QtCore.pyqtSignal()
    def __init__(self,urls,flodName):
        super(Work,self).__init__();
        self.urls = urls
        self.flodName = flodName
    def run(self):
        self.o1 = 100/len(self.urls);
        self.count = 0
        self.tt = foo().tt;
        for i in self.urls:
            self.count = self.count+1;
            # subprocess.call(['you-get',i])
            you_get.common.any_download(i,caption="1");
            self.pp.emit()
        for i in os.walk(os.getcwd()):
            if i[0] != os.getcwd():
                #print('OK')
                continue
            for i1 in i[2]:
                if i1.find('.flv') > 0 or i1.find('.mp4') > 0 or i1.find('.avi') >0 :
                    print(i1);
                    try:
                        shutil.move(i[0]+'/'+i1,os.getcwd()+'/'+self.flodName+'/');
                    except:
                        os.remove(os.getcwd()+'/'+self.flodName+'/'+i1)
                        shutil.move(i[0]+'/'+i1,os.getcwd()+'/'+self.flodName+'/');
                if i1.find('.xml') > 0:
                    os.remove(i[0]+'/'+i1);

class foo(QtCore.QObject):
    tt = QtCore.pyqtSignal()

app = QtWidgets.QApplication(sys.argv);
win = Mywin();
win.show();
sys.exit(app.exec_())