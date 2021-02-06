

from PyQt5 import QtCore, QtGui , QtWidgets  
from PyQt5.QtWidgets import QFileDialog  , QVBoxLayout , QWidget ,QHBoxLayout , QDialog 
from PyQt5.QtWidgets import QTableWidget, QApplication , QTableWidgetItem , QPushButton , QMainWindow
from PyQt5.QtCore import QObject


#from PyQt5.QtGui import QObject
from os.path import basename
from numpy import array
import  sys 
import numpy as np
import random
from datetime import datetime

class Ui_MWS(object):
    m=np.array([])
    filepath=None
    def openwindow(self):
        
        #app = QtWidgets.QApplication(sys.argv)
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi1(self.Dialog)
        self.Dialog.show()
       #sys.exit(app.exec_())
   
       
    def closeEvent(self,QtGui):
        MWS.close()
        
    def setupUi(self, MWS):
        MWS.setObjectName("MWS")
        MWS.resize(668, 520)
        MWS.setStyleSheet("QDialog{\n"
"background: white ;\n"
"}")
        self.frame = QtWidgets.QFrame(MWS)
        self.frame.setGeometry(QtCore.QRect(0, 0, 261, 581))
        self.frame.setStyleSheet("QFrame{\n"
"background:#f0f5f5;\n"
"font-family: Arial;\n"
"font-size: 10;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 201, 20))
        self.label_2.setStyleSheet("QLabel {\n"
"\n"
"font-size: 15px;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 60, 191, 20))
        self.label.setObjectName("label")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(20, 30, 181, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(250, 0, 20, 571))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.nombrecol = QtWidgets.QSpinBox(self.frame)
        self.nombrecol.setGeometry(QtCore.QRect(210, 60, 41, 22))
        self.nombrecol.setObjectName("nombrecol")
        self.nombrecol.setMinimum(1)
        self.nombrecol.setMaximum(20)
        self.nombrecol.valueChanged.connect(self.valChanged)###############"

        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(10, 140, 231, 171))
        self.groupBox.setObjectName("groupBox")
        self.ouvrirf = QtWidgets.QPushButton(self.groupBox)
        self.ouvrirf.setGeometry(QtCore.QRect(10, 60, 101, 21))
        self.ouvrirf.setObjectName("ouvrirf")       
        self.ouvrirf.clicked.connect(self.Singlebrowse)############

        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 161, 16))
        self.label_4.setStyleSheet("QLabel {\n"
"font-size: 11px;\n"
"}\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 111, 21))
        self.label_5.setStyleSheet("QLabel{\n"
"font-size: 11px;\n"
"font-family:Arial;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.line_3 = QtWidgets.QFrame(self.groupBox)
        self.line_3.setGeometry(QtCore.QRect(0, 90, 151, 31))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.genererm = QtWidgets.QPushButton(self.groupBox)
        self.genererm.setGeometry(QtCore.QRect(120, 130, 101, 21))
        self.genererm.setObjectName("genererm")
        self.genererm.clicked.connect(self.openwindow) #####################

        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(120, 50, 101, 31))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 330,231, 171))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(20, 20, 131, 16))
        self.label_8.setObjectName("label_8")
        self.random = QtWidgets.QCheckBox(self.groupBox_2)
        self.random.setGeometry(QtCore.QRect(60, 40, 181, 17))
        self.random.setObjectName("random")
        self.ep = QtWidgets.QCheckBox(self.groupBox_2)
        self.ep.setGeometry(QtCore.QRect(60, 80, 181, 17))
        self.ep.setObjectName("ep")
        self.ga = QtWidgets.QCheckBox(self.groupBox_2)
        self.ga.setGeometry(QtCore.QRect(60, 60,181, 17))
        self.ga.setObjectName("ga")        
        

        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(20, 110, 181, 16))
        self.label_9.setObjectName("label_9")
        self.exactm = QtWidgets.QCheckBox(self.groupBox_2)
        self.exactm.setGeometry(QtCore.QRect(60, 130, 91, 17))
        self.exactm.setObjectName("exactm")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(10, 100, 121, 20))
        self.label_7.setObjectName("label_7")
        self.iterations = QtWidgets.QSpinBox(self.frame)
        self.iterations.setGeometry(QtCore.QRect(130, 100, 91, 22))
        self.iterations.setObjectName("iteration")
        self.iterations.setMinimum(10)
        self.iterations.setMaximum(5000000)
        
        self.iterations.valueChanged.connect(self.valChanged)##############

        self.afficher = QtWidgets.QPushButton(MWS)
        self.afficher.setGeometry(QtCore.QRect(400, 450, 121, 23))
        self.afficher.setObjectName("afficher")   
        self.afficher.clicked.connect(self.choseMethode)############

        self.quitter = QtWidgets.QPushButton(MWS)
        self.quitter.setGeometry(QtCore.QRect(570, 490, 75, 23))
        self.quitter.setObjectName("resultat")
        
        self.quitter.clicked.connect(self.closeEvent)##################

        self.textEdit = QtWidgets.QTextEdit(MWS)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(280, 10, 371, 431))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(MWS)
        QtCore.QMetaObject.connectSlotsByName(MWS)
    
    def retranslateUi(self, MWS):
        
        _translate = QtCore.QCoreApplication.translate
        MWS.setWindowTitle(_translate("MWS", "MWS Solver"))
        self.label_2.setText(_translate("MWS", "Données:"))
        self.label.setText(_translate("MWS", "Nombre de colonne des sous-matrices: "))
        self.groupBox.setTitle(_translate("MWS", "Matrice Gènes-Patient"))
        self.ouvrirf.setText(_translate("MWS", "Ouvrir fichier"))
        self.label_4.setText(_translate("MWS", "Importer depuis un fichier :"))
        self.label_5.setText(_translate("MWS", "Saisir la  matrice :"))
        self.genererm.setText(_translate("MWS", "Générer "))
        self.groupBox_2.setTitle(_translate("MWS", "Méthodes"))
        self.label_8.setText(_translate("MWS", "Méthodes approximatives :"))
        self.random.setText(_translate("MWS", "Random_Algorithm"))
        self.ep.setText(_translate("MWS", "Evolutionary_Programming"))
        self.ga.setText(_translate("MWS", "Genetic_Algorithm"))
        self.label_9.setText(_translate("MWS", "Méthode Exacte:"))
        self.exactm.setText(_translate("MWS", "Exact_Method"))
        self.label_7.setText(_translate("MWS", "Nombre des itérations : "))
        self.afficher.setText(_translate("MWS", "Afficher Résultat"))
        self.quitter.setText(_translate("MWS", "Quitter"))
        
    def Singlebrowse(self):
          
           Ui_MWS.filepath, _ = QFileDialog.getOpenFileName(None ,'single file' )
           self.m=np.loadtxt(Ui_MWS.filepath)
           self.label_3.setText(basename(Ui_MWS.filepath))
           print('filepath' , Ui_MWS.filepath )
           
             
    def valChanged(self):
            
            Ui_MWS.nombrecolonnes=self.nombrecol.value()
            Ui_MWS.iteration=self.iterations.value()
            
    def choseMethode(self):
        self.textEdit.setText(" ")
        res=0
        l=[]
        if self.random.isChecked()==True:
            l=self.random_methode()
            for i in range(len(l)):
                res=l[i]
                self.textEdit.append(str(res))
        if self.ga.isChecked()==True:
            l=self.GA_mathode()
            for i in range(len(l)):
                res=l[i]
                self.textEdit.append(str(res))
        if self.ep.isChecked()==True:
            l=self.EP_mathode()
            for i in range(len(l)):
                res=l[i]
                self.textEdit.append(str(res))

        if self.exactm.isChecked()==True:
            l=self.EXACT_mathode()
            for i in range(len(l)):
                res=l[i]
                self.textEdit.append(str(res))
        if  self.m.size==0:
            self.Dialog = QtWidgets.QDialog()
            self.ui = Ui_Dialog3()
            self.ui.setupUi(self.Dialog)
            self.Dialog.show()
        
            
        else :
            if self.random.isChecked()==False and self.ga.isChecked()==False and self.ep.isChecked()==False and self.exactm.isChecked()==False:
            #self.afficher.clicked.connect(self.opendialog)
                self.Dialog = QtWidgets.QDialog()
                self.ui = Ui_Dialog2()
                self.ui.setupUi(self.Dialog)
                self.Dialog.show()
                
        #if self.exact.isChecked()==True:
         #   res=self.EXACT_mathode()
        
             
   
    ######################"
    def checkRow(self,subm):
        zeros=0
        
        sum_row=np.sum(subm,axis=1).tolist()
        for i in range(len(sum_row)):
            if sum_row[i]==0:
                zeros=zeros+1
      
        
        if int(len(self.m)) >= zeros >= self.fine()-1 :
              return True  
    #######################""
    def check(self,r,subm):
        zeros=0
        sum_row=np.sum(subm,axis=1).tolist()
        for i in range(len(sum_row)):
            if sum_row[i]==0:
                zeros=zeros+1
        if zeros!=r:
          return False
        else :
          return True
     ######################" 
    def weight(self,subm):
        a=0
        b=0
        for j in range (0,len(subm)):  
            if 1 in subm[j]:
                a+=1             #gama(M)
            for i in subm[j]:     
                if i==1:
                    b+=1         #gama(g)
        w=2*a-b          #weight
        return w 
   ########################## 
    def findE(self):
        EE=0
        it=0
        ex=0
        if Ui_MWS.iteration<1000:
            it=Ui_MWS.iteration*3
        braker=False
        for ex in range (len(self.m)):
        #while ex<=84:
             for i in range(Ui_MWS.iteration):
                b = random.sample(range(len(self.m)), Ui_MWS.nombrecolonnes)
                subm=self.m[:,b]
                if self.check(ex,subm):
                    if self.weight(subm)!=0 :
                       #print( weight(subm))
                       EE=ex
                       #print(Emax)
                       braker=True
                       break
          
             if braker:
                 break
        return EE
      
   ########################## 
    def fine(self):
        Emax=0
        ex=0
        braker=False
        for ex in range (len(self.m)+1):
        #while ex<=84:
             for i in range(Ui_MWS.iteration):
                b = random.sample(range(len(self.m[0])), Ui_MWS.nombrecolonnes)
                subm=self.m[:,b]
                if self.check(ex,subm):
                    if self.weight(subm)!=0 :
                       #print( weight(subm))
                       Emax=ex
                       #print(Emax)
                       braker=True
                       break
          
             if braker:
                 break
        return Emax
    
    ############################""  
    def checkrow(self,subm):
        zeros=0
        sum_row=np.sum(subm,axis=1).tolist()
        for i in range(len(sum_row)):
            if sum_row[i]==0:
                zeros=zeros+1
        
        return zeros  

#########################################     
    def viole(self,subm):
        zerolignes=0
        vlignes=0
        listvlignes=[]
        listv=[]
        sumrow=np.sum(subm,axis=1).tolist()
        for i in range (len(sumrow)):
            if sumrow[i]==0:
                zerolignes+=1
            if sumrow[i]>1:
               vlignes+=1
               listvlignes.append(i)
               listv.append(sumrow[i]-1)
        return ( vlignes,listvlignes,listv,zerolignes)
    
    ###########################################
    def mutation(self,b,c):  
        pos=int(random.random()*(len(b)-1))
        m1=b[:pos]+c[pos:]
        m2=c[:pos]+b[pos:]
        
        return list( np.random.choice(np.concatenate([m1,m2]),len(m1))),list( np.random.choice(np.concatenate([m1,m2]),len(m1)))
    #########################################
    def mutationEP(self,b,c):  
      
        return list( np.random.choice(np.concatenate([b,c]),len(b))),list( np.random.choice(np.concatenate([c,b]),len(b)))
    ##########################################
    def random_methode(self):
        print(self.m)
        t1=datetime.now()
        GENES=[]
        Iteration=[]
        tolerance=[] 
        G=[]
        it=0
        maxweight=0
        
        for i in range(Ui_MWS.iteration):
            b = random.sample(range(len(self.m[0])), Ui_MWS.nombrecolonnes)
            submat=self.m[:,b]
            if maxweight<self.weight(submat) and self.checkRow(submat):
               maxweight=self.weight(submat)
               gene=b
               it=i
        
        Iteration.append(it)
        GENES.append(sorted(gene))
        tolerance.append(self.checkrow(self.m[:,gene]))       
        
        for j in range(Ui_MWS.iteration): 
                
                c = random.sample(range(len(self.m[0])), Ui_MWS.nombrecolonnes)
                submatrice=self.m[:,c]
                if self.weight(submatrice)==maxweight :
                    if sorted(c) not in GENES:
                        Iteration.append(j)
                        GENES.append(sorted(c))
                        E=self.checkrow(submatrice)
                        tolerance.append(E) 
        s1='\n Méthode Random : \n'  
        s2=maxweight
        
        print("les sous-matrice trouvées,a quel iteration et leurs viole :","\n")
        for i in range (len(GENES)) :
            print( " Sous-matrice ",i+1, ":" ,GENES[i] ,"\n", "        ","-Sa viole : ",  self.viole(self.m[:,GENES[i]]),"\n" ,"        ","-A l'iteration:",Iteration[i],"\n" ,"        ","-Sa tolerance(mutual excluSivity):",tolerance[i],"\n" )
            for index in range(Ui_MWS.nombrecolonnes):
                G.append(GENES[i][index])
        print("la frequence des genes trouvés :")
        for k in set(G):
             print("      gene[",k,"]=",G.count(k))
        t2=datetime.now()
        tim=t2 - t1 
        print("time : ",tim)
        l=[]
        l.append(s1)
        l.append("Le poid maximum trouvé : "+str(s2))
        l.append("liste des gènes : "+str(GENES))
        l.append("les sous-matrice trouvées,a quel iteration et leurs viole :")
        for i in range(len(GENES)):
            l.append("\n Sous-matrice numéro "+str(i+1)+": "+str(GENES[i])+"\n"+"             Son viole est : "+
                     str(self.viole(self.m[:,GENES[i]]))+"\n"+"             à l'iteration: "+
                     str(Iteration[i])+"\n"+"             Sa tolérance(mutual exclusivity): "+str(tolerance[i]))
        l.append("\n la frequence des genes trouvés :")
        for k in set(G):
            l.append("             gene: ["+str(k)+"]="+str(G.count(k)))
        l.append("\n time : "+str(tim))
        return l
#################################
    def GA_mathode(self):
            t1=datetime.now()
            GENES=[]
            Iteration=[]
            tolerance=[]
            G=[]
            maxweight=0
        
            for i in range(Ui_MWS.iteration):
                b = random.sample(range(len(self.m[0])), Ui_MWS.nombrecolonnes)
                c = random.sample(range(len(self.m[0])), Ui_MWS.nombrecolonnes)
                for l in self.mutation(b,c):
                    submat=self.m[:,l]
                    if maxweight<self.weight(submat) and self.checkRow(submat):
                       maxweight=self.weight(submat)
                       gene=l
                       it=i
            
            Iteration.append(it)
            GENES.append(sorted(gene))
            tolerance.append(self.checkrow(self.m[:,gene]))       
            
            for j in range(Ui_MWS.iteration): 
                 b = random.sample(range(len(self.m[0])), Ui_MWS.nombrecolonnes)
                 c = random.sample(range(len(self.m[0])), Ui_MWS.nombrecolonnes)
                 for l in  self.mutation(b,c):
                    submatrice=self.m[:,l]
                    if self.weight(submatrice)==maxweight :
                        if sorted(l) not in GENES:
                            Iteration.append(j)
                            GENES.append(sorted(l))
                            E=self.checkrow(submatrice)
                            tolerance.append(E)
          
            print("le poind maximal trouve est :",maxweight,"\n") 
            
            print("les sous-matrice trouvées,a quel iteration et leurs viole :","\n")
            for i in range (len(GENES)) :
                print( " Sous-matrice ",i+1, ":" ,GENES[i] ,"\n", "        ","-Sa viole : ",  self.viole(self.m[:,GENES[i]]),"\n" ,"        ","-A l'iteration:",Iteration[i],"\n" ,"        ","-Sa tolerance(mutual excluSivity):",tolerance[i],"\n" )
                for index in range(Ui_MWS.nombrecolonnes):
                    G.append(GENES[i][index])
            print("la frequence des genes trouvés :")
            for k in set(G):
                 print("      gene[",k,"]=",G.count(k))
            t2=datetime.now()
            tim=t2 - t1 
            print("time : ",tim)
            s1='\n Méthode GA : \n'
            s2=maxweight
            l=[]
            l.append(s1)
            l.append("Le poid maximum trouvé : "+str(s2))
            l.append("liste des gènes : "+str(GENES))
            l.append("les sous-matrice trouvées,a quel iteration et leurs viole :")
            for i in range(len(GENES)):
                l.append("\n Sous-matrice numéro "+str(i+1)+": "+str(GENES[i])+"\n"+"             Son viole est : "+
                         str(self.viole(self.m[:,GENES[i]]))+"\n"+"             à l'iteration: "+
                         str(Iteration[i])+"\n"+"             Sa tolérance(mutual exclusivity): "+str(tolerance[i]))
            l.append("\n la frequence des genes trouvés :")
            for k in set(G):
                         l.append("             gene: ["+str(k)+"]="+str(G.count(k)))
            l.append("\n time : "+str(tim))
            return l
        ######################
    def EP_mathode(self):
            t1=datetime.now()
            GENES=[]
            Iteration=[]
            tolerance=[]
            G=[]
            maxweight=0
        
            for i in range(Ui_MWS.iteration):
                b = random.sample(range(len(self.m[0])), Ui_MWS.nombrecolonnes)
                c = random.sample(range(len(self.m[0])), Ui_MWS.nombrecolonnes)
                for l in self.mutationEP(b,c):
                    submat=self.m[:,l]
                    if maxweight<self.weight(submat) and self.checkRow(submat):
                       maxweight=self.weight(submat)
                       gene=l
                       it=i
            
            Iteration.append(it)
            GENES.append(sorted(gene))
            tolerance.append(self.checkrow(self.m[:,gene]))       
            
            for j in range(Ui_MWS.iteration): 
                 b = random.sample(range(len(self.m[0])), Ui_MWS.nombrecolonnes)
                 c = random.sample(range(len(self.m[0])), Ui_MWS.nombrecolonnes)
                 for l in  self.mutationEP(b,c):
                    submatrice=self.m[:,l]
                    if self.weight(submatrice)==maxweight :
                        if sorted(l) not in GENES:
                            Iteration.append(j)
                            GENES.append(sorted(l))
                            E=self.checkrow(submatrice)
                            tolerance.append(E)
          
            print("le poind maximal trouve est :",maxweight,"\n") 
            
            print("les sous-matrice trouvées,a quel iteration et leurs viole :","\n")
            for i in range (len(GENES)) :
                print( " Sous-matrice ",i+1, ":" ,GENES[i] ,"\n", "        ","-Sa viole : ",  self.viole(self.m[:,GENES[i]]),"\n" ,"        ","-A l'iteration:",Iteration[i],"\n" ,"        ","-Sa tolerance(mutual excluSivity):",tolerance[i],"\n" )
                for index in range(Ui_MWS.nombrecolonnes):
                    G.append(GENES[i][index])
            print("la frequence des genes trouvés :")
            for k in set(G):
                 print("      gene[",k,"]=",G.count(k))
            t2=datetime.now()
            tim=t2 - t1 
            print("time : ",tim)
            s1='\n Méthode EP: \n '
            s2=maxweight
            l=[]
            l.append(s1)
            l.append("Le poid maximum touvé : "+str(s2))
            l.append("liste des gènes : "+str(GENES))
            l.append("les sous-matrice trouvées,a quel iteration et leurs viole :")
            for i in range(len(GENES)):
                l.append("\n Sous-matrice numéro "+str(i+1)+": "+str(GENES[i])+"\n"+"             Son viole est : "+
                         str(self.viole(self.m[:,GENES[i]]))+"\n"+"             à l'iteration: "+
                         str(Iteration[i])+"\n"+"             Sa tolérance(mutual exclusivity): "+str(tolerance[i]))
            l.append("\n la frequence des genes trouvés :")
            for k in set(G):
                         l.append("             gene: ["+str(k)+"]="+str(G.count(k)))
            l.append("\n time : "+str(tim))
            return l
        ############################
    def EXACT_mathode(self):
        t1=datetime.now()
        GENES=[]
        Iteration=[]
        tolerance=[]
        G=[]
        maxweight=0
        #global gene
        gene=[]
    
        
        Emax=self.findE()
        print(Emax)
        if Ui_MWS.iteration<2000:
            it=4*Ui_MWS.iteration
        else:
            it=Ui_MWS.iteration
        
        for j in range(it):
        
            b = random.sample(range(len(self.m[0])), Ui_MWS.nombrecolonnes)
            c = random.sample(range(len(self.m[0])), Ui_MWS.nombrecolonnes)
            for l in self.mutationEP(b,c):
                submat=self.m[:,l]
                if maxweight<self.weight(submat) and self.check(Emax,submat):
                        maxweight=self.weight(submat)

                        gene=l
                        it=j
        #╔print(gene)
        Iteration.append(it)
        GENES.append(sorted(gene))
        tolerance.append(self.checkrow(self.m[:,gene]))       
        for i in range(3):
            for j in range(Ui_MWS.iteration): 
                #♦print(j)
                b = random.sample(range(len(self.m[0])), Ui_MWS.nombrecolonnes)
                c = random.sample(range(len(self.m[0])), Ui_MWS.nombrecolonnes)
                for l in self.mutationEP(b,c):
                    submatrice=self.m[:,l]
                    if self.weight(submatrice)==maxweight:
                        if sorted(l) not in GENES:
                            Iteration.append(j)
                            GENES.append(sorted(l))
                            E=self.checkrow(submatrice)
                            tolerance.append(E)
        print("le poind maximal trouve est :",maxweight,"\n") 
            
        print("les sous-matrice trouvées,a quel iteration et leurs viole :","\n")
        for i in range (len(GENES)) :
            print( " Sous-matrice ",i+1, ":" ,GENES[i] ,"\n", "        ","-Sa viole : ",  self.viole(self.m[:,GENES[i]]),"\n" ,"        ","-A l'iteration:",Iteration[i],"\n" ,"        ","-Sa tolerance(mutual excluSivity):",tolerance[i],"\n" )
            for index in range(Ui_MWS.nombrecolonnes):
                G.append(GENES[i][index])
        print("la frequence des genes trouvés :")
        for k in set(G):
             print("      gene[",k,"]=",G.count(k))
        t2=datetime.now()
        tim=t2 - t1 
        print("time : ",tim)
        t2=datetime.now()
        tim=t2 - t1 
        s1='\n Méthode Exate: \n '
        s2=maxweight
        l=[]
        l.append(s1)
        l.append("Le poid max: "+str(s2))
        l.append("liste des gènes : "+str(GENES))
        l.append("les sous-matrice trouvées,a quel iteration et leurs viole :")
        for i in range(len(GENES)):
            l.append("\n Sous-matrice numéro "+str(i+1)+": "+str(GENES[i])+"\n"+"             Son viole est : "+
                     str(self.viole(self.m[:,GENES[i]]))+"\n"+"             à l'iteration: "+
                     str(Iteration[i])+"\n"+"             Sa tolérance(mutual exclusivity): "+str(tolerance[i]))
        l.append("\n la frequence des genes trouvés :")
        for k in set(G):
                     l.append("             gene: ["+str(k)+"]="+str(G.count(k)))
        l.append("\n time : "+str(tim))
        return l
##############################################################################################♥
class Ui_Dialog(object):
    
   
        
    def setupUi1(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(339, 392)
        Dialog.setStyleSheet("QDialog{\n"
"background: white ;}")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(220, 350, 111, 31))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 350, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.gettext)#############""

        self.pushButton.clicked.connect(Dialog.close)#############""

        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)  
        self.textEdit_2.setGeometry(QtCore.QRect(9, 9, 321, 61))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setDisabled(True)
        self.textEdit_2.append("       Exemple à suivre : ")# (Utiliser que des espaces) ")
        #self.textEdit_2.append("Matrice de dimention 2*2 : ") 
        self.textEdit_2.append("                                            1 0 1 0 ")
        self.textEdit_2.append("                                            0 1 0 1 ")
        
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(9, 74, 321, 271))
        self.textEdit.setObjectName("textEdit")
        self.matrix=self.textEdit.toPlainText()
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
       
    def gettext(self):
       self.matrix=self.textEdit.toPlainText()
       with open('pfa.txt','w') as yourfile:
           yourfile.write(self.matrix)
       #♥self.fichier=C:\Users\USER\Desktop\s2\pfa\pfa.txt   
       
       Ui_MWS.m= np.loadtxt("pfa.txt")
       #UMWS.label_3.clear()
       print(len(Ui_MWS.m))
       print(type(Ui_MWS.m))
       print(Ui_MWS.m)
     
       
    
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Terminer"))       
        self.pushButton_2.setText(_translate("Dialog", "Valider"))
    

class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Erreur")
        Dialog.resize(329, 119)
        self.pushButton2 = QtWidgets.QPushButton(Dialog)
        self.pushButton2.setGeometry(QtCore.QRect(110, 70, 111, 23))
        self.pushButton2.setObjectName("pushButton")
        self.pushButton2.clicked.connect(Dialog.close)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 30, 271, 20))
        self.label.setObjectName("label")
        #self.pushButton.clicked.connect(self.openwindow)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Erreur", "Erreur"))
        self.pushButton2.setText(_translate("Dialog", "Quitter"))
        self.label.setText(_translate("Dialog", "      vous devez choisir une methode  !"))    
class Ui_Dialog3(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Erreur")
        Dialog.resize(329, 119)
        self.pushButton2 = QtWidgets.QPushButton(Dialog)
        self.pushButton2.setGeometry(QtCore.QRect(110, 70, 111, 23))
        self.pushButton2.setObjectName("pushButton")
        self.pushButton2.clicked.connect(Dialog.close)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 30, 271, 20))
        self.label.setObjectName("label")
        #self.pushButton.clicked.connect(self.openwindow)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        

        Dialog.setWindowTitle(_translate("Dialog", "Erreur"))
        self.pushButton2.setText(_translate("Dialog", "Quitter"))
        self.label.setText(_translate("Dialog", "  vous devez entrer votre Matrice Genes-Patients !"))    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
  
    MWS = QtWidgets.QDialog()
    ui = Ui_MWS()
    ui.setupUi(MWS)
    
    MWS.show()
    sys.exit(app.exec_())

