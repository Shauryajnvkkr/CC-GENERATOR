from random import randint as rint
from os import system
import datetime
p=str(datetime.datetime.now().time())
system("color 0A")
system("title CC GENERATOR BY QUIETKILLER" )
print("CC GENERATOR By QUIETKILLER ")
bien=input("Enter The Bin : ")
ngen=(input("NO. OF GENERATED CC : "))
bienlen=(input("ENTER CC LENGTH BY DEFAULT 16 : "))
try:
    ngen=int(ngen)
except:
    ngen=100
R=""
for i in p:
    if  i==":":
        R+="_"
    else:
        R+=i
file=open(("CC Generated"+R+".txt"),"w")
try :
    bienlen=int(bienlen)
except:
    bienlen=16
while len(bien)<bienlen:
    bien+="x"
amex=None
if int(bien[0])==3:
    amex=True
else:
    amex=False
mm=input("MM FOR RANDOM PRESS ENTER :")
yy=input("YY FOR RANDOM PRESS ENTER : ")
cvc=input("CVC FOR RANDOM PRESS ENTER : ")
n=0
while n!=ngen:
    ccgen=""
    for i in bien:
        if (i=="x") or (i=="X"):
            ccgen+=str(rint(0,9))
        else:
            ccgen+=i
        if (mm=="") or (mm==" ") :
            MM=rint(1,12)
            if len(str(MM))<2:
                MM=("0"+str(MM))
            else:
                pass
        else:
            MM=mm
        if (yy=="") or (yy==" ") :
            YY=rint(21,26)
        else:
            YY=yy
       
        if amex:
            if (cvc=="") or (cvc==" ") :
                CVV=rint(1,9999)
                if len(str(CVV))==1:
                    CVV=("000"+str(CVV))
                elif len(str(CVV))==2:
                    CVV=("00"+str(CVV))
                elif len(str(CVV))==3:
                    CVV=("0"+str(CVV))
                else:
                    pass
            else:
                CVV=cvc
            
        elif (cvc=="") or (cvc==" ") :
            CVV=rint(1,999)
            if len(str(CVV))==1:
                CVV=("00"+str(CVV))
            elif len(str(CVV))==2:
                CVV=("0"+str(CVV))
            else:
                pass
        else:
            CVV=cvc
       
    cc=ccgen+"|"+str(MM)+"|"+str(YY)+"|"+str(CVV)
    print(cc)
    file.write(cc+"\n")
    file.flush()
    O="title CC GENERATOR BY ⋆ 🕊  🎀  𝒬𝒰𝐼𝐸𝒯𝒦𝐼𝐿𝐿𝐸𝑅  🎀  🕊 ⋆"+ "GENERATED : "+str(n)
    system(O)
    n+=1
file.write("JOIN US @CONFIGS_GRAM @CONFIG_HUB @JSON_SEC \n")
file.write("CC GENERATOR BY QUIETKILLER \n")
file.close()
print("JOIN US @CONFIGS_GRAM @CONFIG_HUB @JSON_SEC")
endinput=input("Press Any Key To Continue")