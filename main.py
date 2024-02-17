#Simple calculator

π=3.1415926535
import math
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
Window.clearcolor=(1,1,1,1)
layout=GridLayout(cols=4)
adtools=GridLayout(cols=8,size_hint=(1,0.07))
layout0=BoxLayout(orientation='horizontal',size_hint=(1,0.18))
layout1=BoxLayout(orientation='vertical')
label=Label(text="0",size_hint=(1,0.28),halign='right',valign='bottom',color=(0,1,0    ,1),font_size='50')
label1=Label(text="",size_hint=(1,0.041),halign='right',valign='top',color=(0,1,0,1),font_size='40')
label2=Label(text="",size_hint=(1,0.041),halign='right',valign='top',color=(0,1,0,1),font_size='40')

layout1.add_widget(label2)
layout1.add_widget(label)
layout1.add_widget(label1)

def lblnth(n):
    shrt=str(eval("10**len(label.text[1:])"))
    if len(label.text)>30 and sub(label.text):
        if label.text[0]!="-":
            label.text=str(eval(label.text+"/"+shrt))+f"*10^{len(label.text[1:])}"
            #label1.text=label.text

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def root(a):
    if a[0]!="√":
        ad=[]
    else:
        ad=[""]
    l=a.split("√")
    for j in l:
        cnt=0
        if j!='':
            if j[0]!="(" and j[0]!="-":
                for p in j:
                    cnt+=1
                    if p not in "0123456789.":
                        ad.append("("+j[0:cnt-1]+")"+j[cnt-1:])
                        break
                    elif cnt==len(j):
                        ad.append("("+j[0:cnt]+")"+j[cnt:])
                        break
                
            else:
                ad.append(j)
    if a==label.text:
        label.text="math.sqrt".join(ad)
        ch()
    else:
        pass
def pi():
    if "0π" in label.text:
        label.text=label.text.replace("0π","0*π")
    if "1π" in label.text:
        label.text=label.text.replace("1π","1*π")
    if "2π" in label.text:
        label.text=label.text.replace("2π","2*π")
    if "3π" in label.text:
        label.text=label.text.replace("3π","3*π")
    if "4π" in label.text:
        label.text=label.text.replace("4π","4*π")
    if "5π" in label.text:
        label.text=label.text.replace("5π","5*π")
    if "6π" in label.text:
        label.text=label.text.replace("6π","6*π")
    if "7π" in label.text:
        label.text=label.text.replace("7π","7*π")
    if "8π" in label.text:
        label.text=label.text.replace("8π","8*π")
    if "9π" in label.text:
        label.text=label.text.replace("9π","9*π")

def fct():
    cntr=0
    adl=[]
    lst1=label.text.split("!")
    for jp in lst1:
        
        if jp!="":
            if jp[len(jp)-1]!=")":
                for rj in jp[::-1]:
                    cntr-=1
                    if rj not in "0123456789.":
                        if (jp.index(rj))!=0:
                            adl.append(jp[0:cntr+1]+"factorial("+str(round(float(jp[cntr+1:len(jp)])))+")")
                            break
                        else:
                            adl.append(jp[0]+"factorial("+str(round(float(jp[1:])))+")")
                            break
                    elif cntr==-len(jp):
                        adl.append("factorial("+str(round(float(jp)))+")")
            else:
               centr=0
               sent1=0
               sent2=0
               for rj in jp[::-1]:
                   centr-=1
                   if rj==")":
                       sent1+=1
                   elif rj=="(":
                       sent2+=1
                       if sent2==sent1:
                           adl.append(jp[0:centr]+"factorial"+"("+str(round(float(eval(jp[centr:]))))+")")
                           break
                       
                       
                         
    label.text="".join(adl)
    if label.text.count("(")>label.text.count(")"):
        label.text=label.text+")"
    
                        
                        
            

def sub(a):
    res=True
    for t in a:
        if t not in "0123456789.-":
            res=False
        else:
            pass
    return res
def ch():
    if ")math" in label.text:
        label.text=label.text.replace(")math",")*math")
    if "0math" in label.text:
        label.text=label.text.replace("0math","0*math")
    if "1math" in label.text:
        label.text=label.text.replace("1math","1*math")
    if "2math" in label.text:
        label.text=label.text.replace("2math","2*math")
    if "3math" in label.text:
        label.text=label.text.replace("3math","3*math")
    if "4math" in label.text:
        label.text=label.text.replace("4math","4*math")
    if "5math" in label.text:
        label.text=label.text.replace("5math","5*math")
    if "6math" in label.text:
        label.text=label.text.replace("6math","6*math")
    if "7math" in label.text:
        label.text=label.text.replace("7math","7*math")
    if "8math" in label.text:
        label.text=label.text.replace("8math","8*math")
    if "9math" in label.text:
        label.text=label.text.replace("9math","9*math")

def em():
    if "0(" in label.text:
        label.text=label.text.replace("0(","0*(")
    if "1(" in label.text:
        label.text=label.text.replace("1(","1*(")
    if "2(" in label.text:
        label.text=label.text.replace("2(","2*(")
    if "3(" in label.text:
        label.text=label.text.replace("3(","3*(")
    if "4(" in label.text:
        label.text=label.text.replace("4(","4*(")
    if "5(" in label.text:
        label.text=label.text.replace("5(","5*(")
    if "6(" in label.text:
        label.text=label.text.replace("6(","6*(")
    if "7(" in label.text:
        label.text=label.text.replace("7(","7*(")
    if "8(" in label.text:
        label.text=label.text.replace("8(","8*(")
    if "9(" in label.text:
        label.text=label.text.replace("9(","9*(")
    if ")fa" in label.text:
        label.text=label.text.replace(")fa",")*fa")
class myapp(App):
			def build(self):
				bnt1=Button(text='√',color=(0,1,0,1),on_press=self.skroy)
				bnt2=Button(text='^',color=(0,1,0,1),font_size='40',on_press=self.power)
				bnt3=Button(text='!',color=(0,1,0,1),on_press=self.skroy)
				bnt4=Button(text='π',color=(0,1,0,1),on_press=self.skroy)
				bnt5=Button(text="I'm here",color=(0,1,0,1))
				adtools.add_widget(bnt1)
				adtools.add_widget(bnt2)
				adtools.add_widget(bnt3)
				adtools.add_widget(bnt4)
				adtools.add_widget(bnt5)

				layout1.add_widget(adtools)
				lst=[['1','2','3','+'],['4','5','6','-'],['7','8','9','*'],['.','0','cl.','/']]
				for i in lst:
					for j in i:
						if j!='cl.' and j!='+' and j!='-' and j!='*' and j!='/':
							btn=Button(text=j,on_press=self.skroy,color=(0,0,0.6,1),font_size='50',background_color=(0,255,255,0.5))
						
							layout.add_widget(btn)
						elif j=='cl.':
							btn=Button(text=j,on_press=self.skroy2,color=(0,0,0.6,1),background_color=(0,255,255,0.5),font_size='40')
							layout.add_widget(btn)
						else:
							btn=Button(text=j,on_press=self.skroy,color=(0,0,0.6,1),font_size='80',background_color=(182/255,0,180/255,0.3))
							layout.add_widget(btn)
				btn1=Button(text='=',on_press=self.skroy1,size_hint=(0.5,1),color=(0,1,0.3,1),font_size='70',background_color=(0.5,0,2,0.5))
				btn2=Button(text='Del.',on_press=self.skroy3,size_hint=(0.25,1),color=(0,1,0.3,1),font_size='70',background_color=(0.5,0,2,0.5))
				btn3=Button(text='( )',on_press=self.skroy0,size_hint=(0.25,1),color=(0,1,0.3,1),font_size='70',background_color=(0.5,0,2,0.5))
				layout1.add_widget(layout)
				layout0.add_widget(btn1)
				layout0.add_widget(btn3)
				layout0.add_widget(btn2)
				layout1.add_widget(layout0)
				return layout1
			def skroy0(self,btn):
			    if label.text[len(label.text)-1]=="√":
			        label.text+="("
			    else:
			        if "(" not in label.text:
			            if label.text!="0":
			                label.text+="("
			            else:
			                label.text="("
			        else:
			            if label.text[len(label.text)-1]=="(":
			                if label.text!="0":
			                    label.text+="("
			            else:
			                c=label.text
			                if c.count("(")>c.count(")"):
			                    label.text+=")"
			                else:
			                    if label.text!=0:
			                        label.text+="("
			def skroy(self,btn):
				if label.text=='0':
					label.text=btn.text
					if label.text=='+' or label.text=='-' or label.text=='*' or label.text=='/' or label.text=='.':
						label.text='0'
				
				
				else:
					label.text=label.text+btn.text
			def skroy2(self,btn):
				label1.text=""
				label.text='0'
				if " ( Error!!! )" in label.text:
					label.color=(1,0,0,1)
				else:
					label.color=(0,1,0,1)
					
			def skroy1(self,btn1):
			    pi()
			    
			    if "√" in label.text:
			        root(label.text)
			        if "rt-" in label.text:
			            pk=label.text.split("t")
			            lst=[]
			            for tk in pk:
			                if tk[0]=="-":
			                    lst.append(f"({tk})")
			                else:
			                    lst.append(tk)
			            label.text="t".join(lst)
			        
			    if "!" in label.text:
			        fct()
			    em()
			    if '^' in label.text:
			        if '^' in label.text:
			            label.text=label.text.replace("^","**")
			            

			            try:
			                em()
			            except:
			                pass
			        

			                    
			    if True:
			            try:
			                try:
			                    if ")(" not in label.text:
			                        em()
			                        label.text=str(eval(label.text))
			                    else:
			                        label.text=label.text.replace(")(",")*(")
			                        em()
			                        label.text=str(eval(label.text))
			                
			                except ValueError:
			                    cnt=0
			                    label.text=str(eval(label.text[9:]+"**(1/2)"))
			            except OverflowError:
			                           if "*10**" in label.text:
			                               cnt=0
			                               for sch in label.text:
			                                   cnt+=1
			                                   if sch=="*":
			                                       if label.text[cnt:cnt+4]=="10**":
			                                           lblst=label.text.split("*10**")
			                                           lblst[0]=str(round(float(lblst[0])))
			                                           label.text="*10**".join(lblst)
			            except:
			                label.text=label.text+(" ( Error!!! )")
			                label.color=(1,0,0,1)
			    if len(label.text)>25:
			        label1.text=str(eval(label.text))
			    if len(label.text)>30:
			        lblnth(label.text)
			    elif len(label.text)<25:
			        label1.text=""
			    if len(label1.text)>730:
			        label1.text=""
			def power(self,bnt2):
			    label.text=label.text+bnt2.text
			    
			def skroy3(self,btn1):
			    if len(label.text)>=13:
			        chk=label.text[len(label.text)-13:len(label.text)]
			        if chk==" ( Error!!! )":
			            label.text=label.text[0:len(label.text)-13]
			            if " ( Error!!! )" in label.text:
			                label.color=(1,0,0,1)
			            else:
			                label.color=(0,1,0,1)
			        else:
			            label.text=label.text[0:len(label.text)-1]
			            if " ( Error!!! )" in label.text:
			                label.color=(1,0,0,1)
			            else:
			                label.color=(0,1,0,1)
			    else:
			        label.text=label.text[0:len(label.text)-1]
			        if label.text=='':
			            label.text='0'
			            if " ( Error!!! )" in label.text:
			                label.color=(1,0,0,1)
			            else:
			                label.color=(0,1,0,1)
			        
			    
			
myapp().run()
