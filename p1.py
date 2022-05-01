from operator import ne
from queue import PriorityQueue
import re
from itertools import groupby



filename1='P13.asm'
filename2='p13.lst'
filename3='Et.tabsim'
li=0
direc1='INH'
direc2='IMM'
direc3='DIR'
direc4='EXT'
direc5='REL'
direc6='IDX'
etiqueta1='0'
etiqueta2='0'
etiqueta3=0
etiqueta4=0
Equ_value=0

li1="1"
li2="2"
li3="3"
li4="4"

aux_var=0
aux_puer=0
aux_fin=0

rr='0'
signn='0'

contador_operacion="0000"





out= open(filename2, 'w')
out_et= open(filename3, 'w')


with open(filename1, 'r') as f:
    lines = f.readlines()
for line in lines:
    if 'FCB' in line:
        numbber=re.findall('[0-99999]', line)
        if len(numbber)<=1:
            newnumbber=int(numbber[0])
        elif len(numbber)<=2:
            newnumbber=int(numbber[0]+numbber[1])
        elif len(numbber)<=3:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2])
        elif len(numbber)<=4:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3])
        elif len(numbber)<=5:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3]+numbber[4])    
        else:
            print("Error, todavia no aceptamos numeros tan grandes")
        newnumbber=hex(newnumbber)[2:]
        print(contador_operacion.zfill(4),end='   ')
        out.write(str(contador_operacion.zfill(4))+"   ")
        print("FCB",end='    ')
        out.write("FCB    ")
        
        print(f"{newnumbber.zfill(2)}")
        out.write(f"{newnumbber.zfill(2)}\n")
        suml2=hex(int(contador_operacion,16)+int(li1,16))[2:]
        contador_operacion=suml2
    if 'FCC' in line:
        nssn=re.findall(r'[/](.*?)[/]', line)
        xxd=nssn[0]	
        print(contador_operacion.zfill(4)+"   FCC    ",end="")
        out.write(contador_operacion.zfill(4)+"   FCC    ")
        for ch in xxd:
            ndn=str(ord(ch))
            ndn=int(ndn)
            ndn=hex(ndn)
            print(ndn[2:],end=" ")
            out.write(ndn[2:]+" ")
            
        
        print("")
        out.write("\n")
        lim2=str(len(xxd))
        suml1=hex(int(contador_operacion,16)+int(lim2,16))[2:]
        contador_operacion=suml1
            
        
    if 'DC.W' in line:
        detect_number=bool(re.search(r'\d', line))
        if detect_number==True:
            
            s = [int(s) for s in re.findall(r'-?\d+\.?\d*', line)]
            print(contador_operacion.zfill(4)+"   DC.W   ",end="")
            out.write(contador_operacion.zfill(4)+"   DC.W   ")
            for n in range(len(s)):
                newnumbber=s[n]
                newnumbber=str(newnumbber)
                print(newnumbber.zfill(4),end=", ")
                out.write(newnumbber.zfill(4)+", ")
                
            print('')
            out.write("\n")
            lim2=str(len(s)*2)
            suml1=hex(int(contador_operacion,16)+int(lim2,16))[2:]
            contador_operacion=suml1
        else:
            print(contador_operacion.zfill(4)+"   DC.W   00 00")
            out.write(contador_operacion.zfill(4)+"   DC.W   00 00\n")
            suml1=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml1
    if 'FILL' in line:
        s = [int(s) for s in re.findall(r'-?\d+\.?\d*', line)]
        n1=s[0]
        n2=s[1]
        lii10=str(n2)
        cx=f"0{n1}"
        for k in range (0,n2-1):
            cx=cx+f" 0{n1}"
        print(contador_operacion.zfill(4)+"   "+"FILL "+"  "+str(cx))
        out.write(contador_operacion.zfill(4)+"   "+"FILL "+"  "+str(cx)+"\n")
        suml1=hex(int(contador_operacion,16)+int(lii10,16))[2:]
        contador_operacion=suml1
    if 'BSZ' in line:
        numbber=re.findall('[0-99999]', line)
        if len(numbber)<=1:
            newnumbber=int(numbber[0])
        elif len(numbber)<=2:
            newnumbber=int(numbber[0]+numbber[1])
        elif len(numbber)<=3:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2])
        elif len(numbber)<=4:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3])
        elif len(numbber)<=5:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3]+numbber[4])    
        else:
            print("Error, todavia no aceptamos numeros tan grandes")
        
        cerosnumber=newnumbber*2
        lii10=str(newnumbber)
        
        
        cx="00"
        for k in range (0,newnumbber-1):
            cx=cx+" 00"
            
        print(contador_operacion.zfill(4)+"   "+"BSZ "+"   "+str(cx))
        out.write(contador_operacion.zfill(4)+"   "+"BSZ "+"   "+str(cx)+"\n")
        suml1=hex(int(contador_operacion,16)+int(lii10,16))[2:]
        contador_operacion=suml1
    if 'DC.B' in line:
        detect_number=bool(re.search(r'\d', line))
        if detect_number==True:
            
            s = [int(s) for s in re.findall(r'-?\d+\.?\d*', line)]
            print(contador_operacion.zfill(4)+"   DC.B   ",end="")
            out.write(contador_operacion.zfill(4)+"   DC.B   ")
            for n in s:
                
                newnumbber=hex(n)[2:]
                print(newnumbber.zfill(2),end=", ")
                out.write(newnumbber.zfill(2)+", ")
                
            print('')
            out.write("\n")
            lim2=str(len(s))
            suml1=hex(int(contador_operacion,16)+int(lim2,16))[2:]
            contador_operacion=suml1
        else:
            print(contador_operacion.zfill(4)+"   DC.B   00")
            out.write(contador_operacion.zfill(4)+"   DC.B   00\n")
            suml1=hex(int(contador_operacion,16)+int(li1,16))[2:]
            contador_operacion=suml1
    if 'START' in line:
        print(str(contador_operacion)+"   Start")
        out.write(str(contador_operacion)+"   Start\n")
        contador_operacion="0000"
        
    if 'ORG' in line:
        contador_operacion="4000"
        print("       ORG $"+str(contador_operacion))
        out.write("       ORG $"+str(contador_operacion)+"\n")
    if 'VAR2' in line:
        if aux_var==0:
            etiqueta1=contador_operacion.zfill(4)
            out_et.write("VAR2 "+str(etiqueta1)+"\n")
            aux_var=1
        else:
            pass
    if 'PUERTA' in line:
        if aux_puer==0:
            etiqueta2=contador_operacion.zfill(4)
            aux_puer=1
        else:
            pass
    if 'FIN' in line:
        if aux_fin==0:
            etiqueta3='4028'
            out_et.write("FIN "+str(etiqueta3)+"\n")
            aux_fin=1
        else:
            pass 
    if 'E4' in line:
        etiqueta4=contador_operacion
                
    if 'EQU' in line:
        numbber=re.findall('[0-99999]', line)
        if len(numbber)<=2:
            newnumbber=int(numbber[0])
        elif len(numbber)<=3:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2])
        elif len(numbber)<=4:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3])
        elif len(numbber)<=5:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3])
        elif len(numbber)<=6:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3]+numbber[4])    
        else:
            print("Error, todavia no aceptamos numeros tan grandes")
        ppp=newnumbber
        arroba=bool(re.findall('@', line))
        porc=bool(re.findall('%', line))
        smps=line.find('$')
            
        if arroba is False:
            pass
            if porc is False:
                pass
                if smps == -1:
                    newnumbber=hex(newnumbber)[2:]
                        
            
        if arroba is True:
            newnumbberoc=str(newnumbber)
            d=int(newnumbberoc,8)
            h=hex(d)[2:]
            newnumbber=h
                
        elif porc is True:
                newnumbberoc=str(newnumbber)
                for digito in newnumbberoc:
                    if digito !='0' and digito !='1':
                        print('No se puede ingresar esto, ya que es binario')
                    else:
                        d=int(newnumbberoc,2)
                        h=hex(d)[2:]
                        newnumbber=h
            
        if smps != -1:
                ppp=str(newnumbber)
                newnumbber=ppp
        
        if 'PUERTA' in line:
            out_et.write("PUERTA "+str(newnumbber)+"\n")
            etiqueta2=newnumbber     
        if line[0] == 'E':
            if line[1] == '1':
                out_et.write(str(etiqueta1)+" E1 "+str(newnumbber)+"\n")
            elif line[1] == '2':
                out_et.write(str(etiqueta2)+" E2 "+str(newnumbber)+"\n")
            elif line[1] == '3':
                out_et.write(str(etiqueta3)+" E3 "+str(newnumbber)+"\n")
        print(contador_operacion+"   EQU")
        out.write(str(contador_operacion)+"   EQU\n")
    if 'ABA' in line:
        direct=direc1
        li=2
        detect_number=bool(re.search(r'\d', line))
        gatito=bool(re.findall('#', line))
        if detect_number is False and gatito is False:
            print(contador_operacion,end='   ')
            out.write(str(contador_operacion)+"   ")
            print("ABA",end='   ')
            out.write("ABA   ")
            print(f" {direc1}",end='   ')
            out.write(f" {direc1}   ")
            print("(LI=2)",end='   ')
            out.write("(LI=2)   ")
            print("18 06")
            out.write("18 06\n")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2
            
        else:
            
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR\n")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2
        
    if 'ADCA' in line:
        
        numbber=re.findall('[0-99999]', line)
        if len(numbber)<=1:
            newnumbber=int(numbber[1])
        elif len(numbber)<=2:
            newnumbber=int(numbber[1]+numbber[2])
        elif len(numbber)<=3:
            newnumbber=int(numbber[1]+numbber[2])
        elif len(numbber)<=4:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3])
        elif len(numbber)<=5:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3]+numbber[4])    
        else:
            print("Error, todavia no aceptamos numeros tan grandes")
        
        ppp=newnumbber
        arroba=bool(re.findall('@', line))
        porc=bool(re.findall('%', line))
        smps=line.find('$')
        
        if arroba is False:
            pass
            if porc is False:
                pass
                if smps == -1:
                    newnumbber=hex(newnumbber)[2:]
                    
        
        if arroba is True:
            newnumbberoc=str(newnumbber)
            d=int(newnumbberoc,8)
            h=hex(d)[2:]
            newnumbber=h
            
        elif porc is True:
                newnumbberoc=str(newnumbber)
                for digito in newnumbberoc:
                    if digito !='0' and digito !='1':
                        print('No se puede ingresar esto, ya que es binario')
                    else:
                        d=int(newnumbberoc,2)
                        h=hex(d)[2:]
                        newnumbber=h
        
        if smps != -1:
            ppp=str(newnumbber)
            newnumbber=ppp
        
        
        
        
        if len(newnumbber)<=2:
            li=2
            coop=0
            gatito=bool(re.findall('#', line))
            
            if gatito is True:          
                direct=direc2
                coop=89
            else:
                direct=direc3
                coop=99
            print(contador_operacion.zfill(4),end='   ')
            out.write(str(contador_operacion.zfill(4))+"   ")
            print("ADCA",end='   ')
            out.write("ADCA   ")
            print(direct,end='   ')
            out.write(direct+"   ")
            print(f"(LI={li})",end='   ')
            out.write(f"(LI={li})   ")
            print(f"{coop} {newnumbber.zfill(2)}")
            out.write(f"{coop} {newnumbber.zfill(2)}\n")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2   
        #falta la validacion para li3
        elif len(newnumbber)==3 or 4:
            gatito=bool(re.findall('#', line))
            if gatito is False:
                li=3
                coop='B9'
                direct=direc4
                print(contador_operacion.zfill(4),end='   ')
                out.write(str(contador_operacion.zfill(4))+"   ")
                print("ADCA",end='   ')
                out.write("ADCA   ")
                print(direct,end='   ')
                out.write(direct+"   ")
                print(f"(LI={li})",end='   ')
                out.write(f"(LI={li})   ")
                print(f"{coop} {newnumbber.zfill(4)}")
                out.write(f"{coop} {newnumbber.zfill(4)}\n")
                suml3=hex(int(contador_operacion,16)+int(li3,16))[2:]
                contador_operacion=suml3
            else:
                print(str(contador_operacion.zfill(4))+"   FDR")
                out.write(str(contador_operacion.zfill(4))+"   FDR")
                suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
                contador_operacion=suml2
            
        else:
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2
            
    if 'ADCB' in line:
        
        numbber=re.findall('[0-99999]', line)
        if len(numbber)<=1:
            newnumbber=int(numbber[0])
        elif len(numbber)<=2:
            newnumbber=int(numbber[0]+numbber[1])
        elif len(numbber)<=3:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2])
        elif len(numbber)<=4:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3])
        elif len(numbber)<=5:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3]+numbber[4])    
        else:
            print("Error, todavia no aceptamos numeros tan grandes")
        
        ppp=newnumbber
        arroba=bool(re.findall('@', line))
        porc=bool(re.findall('%', line))
        smps=line.find('$')
        
        if arroba is False:
            pass
            if porc is False:
                pass
                if smps == -1:
                    newnumbber=hex(newnumbber)[2:]
                    
        
        if arroba is True:
            newnumbberoc=str(newnumbber)
            d=int(newnumbberoc,8)
            h=hex(d)[2:]
            newnumbber=h
            
        elif porc is True:
                newnumbberoc=str(newnumbber)
                for digito in newnumbberoc:
                    if digito !='0' and digito !='1':
                        print('No se puede ingresar esto, ya que es binario')
                    else:
                        d=int(newnumbberoc,2)
                        h=hex(d)[2:]
                        newnumbber=h
        
        if smps != -1:
            ppp=str(newnumbber)
            newnumbber=ppp
        
        
        
        
        if len(newnumbber)<=2:
            li=2
            coop=''
            gatito=bool(re.findall('#', line))
            
            if gatito is True:          
                direct=direc2
                coop='C9'
            else:
                direct=direc3
                coop='D9'
            print(contador_operacion,end='   ')
            out.write(str(contador_operacion)+"   ")
            print("ADCB",end='   ')
            out.write("ADCB   ")
            print(direct,end='   ')
            out.write(direct+"   ")
            print(f"(LI={li})",end='   ')
            out.write(f"(LI={li})   ")
            print(f"{coop} {newnumbber}")
            out.write(f"{coop} {newnumbber}\n")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2    
        #falta la validacion para li3
        elif len(newnumbber)==3 or 4:
            gatito=bool(re.findall('#', line))
            if gatito is False:
                li=3
                coop='F9'
                direct=direc4
                print(contador_operacion,end='   ')
                out.write(str(contador_operacion)+"   ")
                print("ADCB",end='   ')
                out.write("ADCB   ")
                print(direct,end='   ')
                out.write(direct+"   ")
                print(f"(LI={li})",end='   ')
                out.write(f"(LI={li})   ")
                print(f"{coop} {newnumbber.zfill(4)}")
                out.write(f"{coop} {newnumbber.zfill(4)}\n")
                suml3=hex(int(contador_operacion,16)+int(li3,16))[2:]
                contador_operacion=suml3
            else:
                print(str(contador_operacion)+"   FDR")
                out.write(str(contador_operacion)+"   FDR")
                suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
                contador_operacion=suml2
        else:
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2
            
    if 'ADDA' in line:
        targ=bool(re.findall(':', line))
        if targ is True:
            etiqueta=contador_operacion
        else:
            pass
        numbber=re.findall('[0-99999]', line)
        if len(numbber)<=2:
            newnumbber=int(numbber[1])
        elif len(numbber)<=3:
            newnumbber=int(numbber[1]+numbber[2])
        elif len(numbber)<=4:
            newnumbber=int(numbber[1]+numbber[2]+numbber[3])
        elif len(numbber)<=5:
            newnumbber=int(numbber[1]+numbber[2]+numbber[3]+numbber[4])
        elif len(numbber)<=6:
            newnumbber=int(numbber[1]+numbber[2]+numbber[3]+numbber[4]+numbber[5])    
        else:
            print("Error, todavia no aceptamos numeros tan grandes")
        ppp=newnumbber
        arroba=bool(re.findall('@', line))
        porc=bool(re.findall('%', line))
        smps=line.find('$')
            
        if arroba is False:
            pass
            if porc is False:
                pass
                if smps == -1:
                    newnumbber=hex(newnumbber)[2:]
                        
            
        if arroba is True:
            newnumbberoc=str(newnumbber)
            d=int(newnumbberoc,8)
            h=hex(d)[2:]
            newnumbber=h
                
        elif porc is True:
                newnumbberoc=str(newnumbber)
                for digito in newnumbberoc:
                    if digito !='0' and digito !='1':
                        print('No se puede ingresar esto, ya que es binario')
                    else:
                        d=int(newnumbberoc,2)
                        h=hex(d)[2:]
                        newnumbber=h
            
        if smps != -1:
                ppp=str(newnumbber)
                newnumbber=ppp
            
            
            
            
        if len(newnumbber)<=2:
            li=2
            coop=''
            gatito=bool(re.findall('#', line))
                
            if gatito is True:          
                direct=direc2
                coop='8B'
            else:
                direct=direc3
                coop='9B'
            print(contador_operacion,end='   ')
            out.write(str(contador_operacion)+"   ")
            print("ADDA",end='   ')
            out.write("ADDA   ")
            print(direct,end='   ')
            out.write(direct+"   ")
            print(f"(LI={li})",end='   ')
            out.write(f"(LI={li})   ")
            print(f"{coop} {newnumbber}")
            out.write(f"{coop} {newnumbber}\n")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2    
            #falta la validacion para li3
        elif len(newnumbber)==3 or 4:
            gatito=bool(re.findall('#', line))
            if gatito is False:
                li=3
                coop='BB'
                direct=direc4
                print(contador_operacion,end='   ')
                out.write(str(contador_operacion)+"   ")
                print("ADDA",end='   ')
                out.write("ADDA   ")
                print(direct,end='   ')
                out.write(direct+"   ")
                print(f"(LI={li})",end='   ')
                out.write(f"(LI={li})   ")
                print(f"{coop} {newnumbber.zfill(4)}")
                out.write(f"{coop} {newnumbber.zfill(4)}\n")
                suml3=hex(int(contador_operacion,16)+int(li3,16))[2:]
                contador_operacion=suml3
            else:
                print(str(contador_operacion)+"   FDR")
                out.write(str(contador_operacion)+"   FDR")
                suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
                contador_operacion=suml2
        else:
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2
            
    if 'ASL' in line:
        
        numbber=re.findall('[0-99999]', line)
        if len(numbber)<=1:
            newnumbber=int(numbber[0])
        elif len(numbber)<=2:
            newnumbber=int(numbber[0]+numbber[1])
        elif len(numbber)<=3:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2])
        elif len(numbber)<=4:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3])
        elif len(numbber)<=5:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3]+numbber[4])    
        else:
            print("Error, todavia no aceptamos numeros tan grandes")
        
        ppp=newnumbber
        arroba=bool(re.findall('@', line))
        porc=bool(re.findall('%', line))
        smps=line.find('$')
        
        if arroba is False:
            pass
            if porc is False:
                pass
                if smps == -1:
                    newnumbber=hex(newnumbber)[2:]
                    
        
        if arroba is True:
            newnumbberoc=str(newnumbber)
            d=int(newnumbberoc,8)
            h=hex(d)[2:]
            newnumbber=h
            
        elif porc is True:
                newnumbberoc=str(newnumbber)
                for digito in newnumbberoc:
                    if digito !='0' and digito !='1':
                        print('No se puede ingresar esto, ya que es binario')
                    else:
                        d=int(newnumbberoc,2)
                        h=hex(d)[2:]
                        newnumbber=h
        
        if smps != -1:
            ppp=str(newnumbber)
            newnumbber=ppp
        
        
        
        elif len(newnumbber)<=4:
            gatito=bool(re.findall('#', line))
                
            if gatito is True:          
                print(str(contador_operacion)+"   FDR")
                out.write(str(contador_operacion)+"   FDR\n")
                suml3=hex(int(contador_operacion,16)+int(li3,16))[2:]
                contador_operacion=suml3
                
            else:
                li=3
                coop='78'
                direct=direc4
                print(contador_operacion,end='   ')
                out.write(str(contador_operacion)+"   ")
                print("ASL",end='   ')
                out.write("ASL   ")
                print(f" {direct}",end='   ')
                out.write(f" {direct}   ")
                print(f"(LI={li})",end='   ')
                out.write(f"(LI={li})   ")
                print(f"{coop} {newnumbber.zfill(4)}")
                out.write(f"{coop} {newnumbber.zfill(4)}\n")
                suml3=hex(int(contador_operacion,16)+int(li3,16))[2:]
                contador_operacion=suml3
        else:
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2   
            
    if 'BCC' in line:
        direct=direc1
        li=2
        
        print(contador_operacion,end='   ')
        out.write(str(contador_operacion)+"   ")
        """
        print("BCC",end='   ')
        out.write("BCC   ")
        print(" REL",end='   ')
        out.write(" REL   ")
        print("(LI=3)",end='   ')
        out.write("(LI=3)   ")
        print(f"24 {etiqueta}")
        out.write(f"24 {etiqueta}\n")
        """
        print("(Todavia no vemos este modo de direccionamiento)")
        out.write("(Todavia no vemos este modo de direccionamiento)\n")
        suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
        contador_operacion=suml2 
    
    if 'BNE' in line:
        object_code=26
        if 'VAR2' in line:
            next_code=hex(int(contador_operacion,16)+int(li2,16))[2:]
            result=hex(int(etiqueta1,16)-int(next_code,16))
            result1=hex(int(result,16) + 16**2)[2:]
            if len(result1)<=2:
                li=2
                coop=object_code
                direct=direc5
                print(contador_operacion,end='   ')
                out.write(str(contador_operacion)+"   ")
                print("BNE",end='   ')
                out.write("BNE   ")
                print(f" {direc5}",end='   ')
                out.write(f" {direc5}   ")
                print(f"(LI={li})",end='   ')
                out.write(f"(LI={li})   ")
                print(f"{coop} {result1}")
                out.write(f"{coop} {result1}\n")
                suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
                contador_operacion=suml2
            else:
                print(str(contador_operacion)+"   FDR")
                out.write(str(contador_operacion)+"   FDR"+"\n")
                suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
                contador_operacion=suml2
        if 'PUERTA' in line:
            next_code=hex(int(contador_operacion,16)+int(li2,16))[2:]
            result=hex(int(etiqueta2,16)-int(next_code,16))
            result1=hex(int(result,16) + 16**2)[2:]
            if len(result1)<=2:
                li=2
                coop=object_code
                direct=direc5
                print(contador_operacion,end='   ')
                out.write(str(contador_operacion)+"   ")
                print("BNE",end='   ')
                out.write("BNE   ")
                print(f" {direc5}",end='   ')
                out.write(f" {direc5}   ")
                print(f"(LI={li})",end='   ')
                out.write(f"(LI={li})   ")
                print(f"{coop} {result1}")
                out.write(f"{coop} {result1}\n")
                suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
                contador_operacion=suml2
            else:
                print(str(contador_operacion)+"   FDR")
                out.write(str(contador_operacion)+"   FDR"+"\n")
                suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
                contador_operacion=suml2
        if 'FIN' in line:
            next_code=hex(int(contador_operacion,16)+int(li2,16))[2:]
            result=hex(int(etiqueta3,16)-int(next_code,16))[2:]
            result1=hex(int(result,16) + 16**2)[2:]
            if len(result)<=2:
                li=2
                coop=object_code
                direct=direc5
                print(contador_operacion,end='   ')
                out.write(str(contador_operacion)+"   ")
                print("BNE",end='   ')
                out.write("BNE   ")
                print(f" {direc5}",end='   ')
                out.write(f" {direc5}   ")
                print(f"(LI={li})",end='   ')
                out.write(f"(LI={li})   ")
                print(f"{coop} {result.zfill(2)}")
                out.write(f"{coop} {result.zfill(2)}\n")
                suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
                contador_operacion=suml2
            else:
                print(str(contador_operacion)+"   FDR")
                out.write(str(contador_operacion)+"   FDR"+"\n")
                suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
                contador_operacion=suml2
        
    
    
    if 'BGND' in line:
        direct=direc1
        li=1
        detect_number=bool(re.search(r'\d', line))
        gatito=bool(re.findall('#', line))
        if detect_number is False and gatito is False:
            print(contador_operacion,end='   ')
            out.write(str(contador_operacion)+"   ")
            print("BGND",end='   ')
            out.write("BGND   ")
            print(f"{direc1}",end='   ')
            out.write(f"{direc1}   ")
            print("(LI=1)",end='   ')
            out.write("(LI=1)   ")
            print("00")
            out.write("00\n")
            suml1=hex(int(contador_operacion,16)+int(li1,16))[2:]
            contador_operacion=suml1
            
        else:
            
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR\n")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2
    
    if 'ADDD' in line:
        parc=line.find('[')
        arr = re.split('[ ,.]', line)[1]
        nonumber=any(chr.isdigit() for chr in line)
        if nonumber is False:
            if parc != -1:
                if 'D' in arr:
                    if 'X' in line:
                        rr='00'
                    if 'Y' in line:
                        rr='01'
                    if 'SP' in line:
                        rr='10'
                    if 'PC' in line:
                        rr='11'
                    numerocheto1=(str('111')+str(rr)+str('111'))[4:]
                    numerocheto2=(str('111')+str(rr)+str('111'))[:4]
                    d=int(numerocheto1,2)
                    h=hex(d)[2:]
                    nummm1=h
                    d2=int(numerocheto2,2)
                    h2=hex(d2)[2:]
                    nummm2=h2
                    numerchetau=str(nummm2)+str(nummm1)
                    direct=direc6
                    coop='E3'
                    li=2
                    print(contador_operacion.zfill(4),end='   ')
                    out.write(str(contador_operacion.zfill(4))+"   ")
                    print("ADDD",end='   ')
                    out.write("ADDD   ")
                    print(direct,end='   ')
                    out.write(direct+"   ")
                    print(f"(LI={li})",end='   ')
                    out.write(f"(LI={li})   ")
                    print(f"{coop} {numerchetau}")
                    out.write(f"{coop} {numerchetau}\n")
                    suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
                    contador_operacion=suml2
                        
                else:
                    print(str(contador_operacion.zfill(4))+"   FDR")
                    out.write(str(contador_operacion.zfill(4))+"   FDR\n")
                    suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
                    contador_operacion=suml2
            else:
                if 'A' in arr:
                    if 'X' in line:
                        rr='00'
                    if 'Y' in line:
                        rr='01'
                    if 'SP' in line:
                        rr='10'
                    if 'PC' in line:
                        rr='11'
                    aa='00'
                    numerocheto1=(str('111')+str(rr)+str('1')+str(aa))[4:]
                    numerocheto2=(str('111')+str(rr)+str('1')+str(aa))[:4]
                    d=int(numerocheto1,2)
                    h=hex(d)[2:]
                    nummm1=h
                    d2=int(numerocheto2,2)
                    h2=hex(d2)[2:]
                    nummm2=h2
                    numerchetau=str(nummm2)+str(nummm1)
                    direct=direc6
                    coop='E3'
                    li=2
                    print(contador_operacion.zfill(4),end='   ')
                    out.write(str(contador_operacion.zfill(4))+"   ")
                    print("ADDD",end='   ')
                    out.write("ADDD   ")
                    print(direct,end='   ')
                    out.write(direct+"   ")
                    print(f"(LI={li})",end='   ')
                    out.write(f"(LI={li})   ")
                    print(f"{coop} {numerchetau}")
                    out.write(f"{coop} {numerchetau}\n")
                    suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
                    contador_operacion=suml2
                elif 'B' in arr:
                    if 'X' in line:
                        rr='00'
                    if 'Y' in line:
                        rr='01'
                    if 'SP' in line:
                        rr='10'
                    if 'PC' in line:
                        rr='11'
                    aa='01'
                    numerocheto1=(str('111')+str(rr)+str('1')+str(aa))[4:]
                    numerocheto2=(str('111')+str(rr)+str('1')+str(aa))[:4]
                    d=int(numerocheto1,2)
                    h=hex(d)[2:]
                    nummm1=h
                    d2=int(numerocheto2,2)
                    h2=hex(d2)[2:]
                    nummm2=h2
                    numerchetau=str(nummm2)+str(nummm1)
                    direct=direc6
                    coop='E3'
                    li=2
                    print(contador_operacion.zfill(4),end='   ')
                    out.write(str(contador_operacion.zfill(4))+"   ")
                    print("ADDD",end='   ')
                    out.write("ADDD   ")
                    print(direct,end='   ')
                    out.write(direct+"   ")
                    print(f"(LI={li})",end='   ')
                    out.write(f"(LI={li})   ")
                    print(f"{coop} {numerchetau}")
                    out.write(f"{coop} {numerchetau}\n")
                    suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
                    contador_operacion=suml2
                elif 'D' in arr:
                    if 'X' in line:
                        rr='00'
                    if 'Y' in line:
                        rr='01'
                    if 'SP' in line:
                        rr='10'
                    if 'PC' in line:
                        rr='11'
                    aa='10'
                    numerocheto1=(str('111')+str(rr)+str('1')+str(aa))[4:]
                    numerocheto2=(str('111')+str(rr)+str('1')+str(aa))[:4]
                    d=int(numerocheto1,2)
                    h=hex(d)[2:]
                    nummm1=h
                    d2=int(numerocheto2,2)
                    h2=hex(d2)[2:]
                    nummm2=h2
                    numerchetau=str(nummm2)+str(nummm1)
                    direct=direc6
                    coop='E3'
                    li=2
                    print(contador_operacion.zfill(4),end='   ')
                    out.write(str(contador_operacion.zfill(4))+"   ")
                    print("ADDD",end='   ')
                    out.write("ADDD   ")
                    print(direct,end='   ')
                    out.write(direct+"   ")
                    print(f"(LI={li})",end='   ')
                    out.write(f"(LI={li})   ")
                    print(f"{coop} {numerchetau}")
                    out.write(f"{coop} {numerchetau}\n")
                    suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
                    contador_operacion=suml2
                else:
                    print(str(contador_operacion.zfill(4))+"   FDR")
                    out.write(str(contador_operacion.zfill(4))+"   FDR\n")
                    suml2=hex(int(contador_operacion,16)+int(li4,16))[2:]
                    contador_operacion=suml2
        else:
            numbber=re.findall('[0-99999]', line)
            if len(numbber)<=1:
                newnumbber=int(numbber[0])
                nummm=int(numbber[0])
            elif len(numbber)<=2:
                newnumbber=int(numbber[0]+numbber[1])
                nummm=int(numbber[0]+numbber[1])
            elif len(numbber)<=3:
                newnumbber=int(numbber[0]+numbber[1]+numbber[2])
                nummm=int(numbber[0]+numbber[1]+numbber[2])
            elif len(numbber)<=4:
                newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3])
                nummm=int(numbber[0]+numbber[1]+numbber[2]+numbber[3])
            elif len(numbber)<=5:
                newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3]+numbber[4])    
                nummm=int(numbber[0]+numbber[1]+numbber[2]+numbber[3]+numbber[4])    
            else:
                print("Error, todavia no aceptamos numeros tan grandes")
            
            ppp=newnumbber
            arroba=bool(re.findall('@', line))
            coma=bool(re.findall(',', line))
            porc=bool(re.findall('%', line))
            smps=line.find('$')
            neggg=line.find('-')
            parc=line.find('[')
            
            
            
            if arroba is False:
                pass
                if porc is False:
                    pass
                    if smps == -1:
                        newnumbber=hex(newnumbber)[2:]
                        
            
            if arroba is True:
                newnumbberoc=str(newnumbber)
                d=int(newnumbberoc,8)
                h=hex(d)[2:]
                newnumbber=h
                
            elif porc is True:
                    newnumbberoc=str(newnumbber)
                    for digito in newnumbberoc:
                        if digito !='0' and digito !='1':
                            print('No se puede ingresar esto, ya que es binario')
                        else:
                            d=int(newnumbberoc,2)
                            h=hex(d)[2:]
                            newnumbber=h
            
            if smps != -1:
                ppp=str(newnumbber)
                newnumbber=ppp
            
            if coma is True:
                direct=direc6
                if parc != -1:
                    if neggg != -1:
                        print(str(contador_operacion.zfill(4))+"   FDR")
                        out.write(str(contador_operacion.zfill(4))+"   FDR\n")
                        suml2=hex(int(contador_operacion,16)+int(li4,16))[2:]
                        contador_operacion=suml2
                    
                    else:
                        if 'X' in line:
                            rr='00'
                        if 'Y' in line:
                            rr='01'
                        if 'SP' in line:
                            rr='10'
                        if 'PC' in line:
                            rr='11'
                        nummm=hex(nummm)[2:]
                        numerocheto1=(str('111')+str(rr)+str('011'))[4:]
                        numerocheto2=(str('111')+str(rr)+str('011'))[:4]
                        d=int(numerocheto1,2)
                        h=hex(d)[2:]
                        nummm1=h
                        d2=int(numerocheto2,2)
                        h2=hex(d2)[2:]
                        nummm2=h2
                        numerchetau=str(nummm2)+str(nummm1)
                        direct=direc6
                        coop='E3'
                        li=4
                        print(contador_operacion.zfill(4),end='   ')
                        out.write(str(contador_operacion.zfill(4))+"   ")
                        print("ADDD",end='   ')
                        out.write("ADDD   ")
                        print(direct,end='   ')
                        out.write(direct+"   ")
                        print(f"(LI={li})",end='   ')
                        out.write(f"(LI={li})   ")
                        print(f"{coop} {numerchetau} {nummm.zfill(4)[:2]} {nummm.zfill(4)[2:]}")
                        out.write(f"{coop} {numerchetau} {nummm.zfill(4)[:2]} {nummm.zfill(4)[2:]}\n")
                        suml2=hex(int(contador_operacion,16)+int(li4,16))[2:]
                        contador_operacion=suml2
                            
                
                else:
                    
                        if neggg != -1:
                            nummm=nummm*-1
                        if nummm >= -16  and nummm <= 15:
                            if 'X' in line:
                                rr='00'
                            if 'Y' in line:
                                rr='01'
                            if 'SP' in line:
                                rr='10'
                            if 'PC' in line:
                                rr='11'
                            if nummm <0:
                                signn='1'
                                nummm=hex(nummm)
                                nummm=hex(int(nummm,16) + 16**2)[3:]
                                nummm=bin(int(nummm,16))[2:].zfill(4)
                                
                            else:
                                signn='0'
                                nummm=hex(nummm)[2:]
                                nummm=bin(int(nummm,16))[2:].zfill(4)
                            numerocheto=str(rr)+str(signn)+str(nummm)
                            numerocheto1=(str(rr)+str('0')+str(signn)+str(nummm))[4:]
                            numerocheto2=(str(rr)+str('0')+str(signn)+str(nummm))[:4]
                            d=int(numerocheto1,2)
                            h=hex(d)[2:]
                            nummm1=h
                            d2=int(numerocheto2,2)
                            h2=hex(d2)[2:]
                            nummm2=h2
                            numerchetau=str(nummm2)+str(nummm1)
                            direct=direc6
                            coop='E3'
                            li=2
                            print(contador_operacion.zfill(4),end='   ')
                            out.write(str(contador_operacion.zfill(4))+"   ")
                            print("ADDD",end='   ')
                            out.write("ADDD   ")
                            print(direct,end='   ')
                            out.write(direct+"   ")
                            print(f"(LI={li})",end='   ')
                            out.write(f"(LI={li})   ")
                            print(f"{coop} {numerchetau}")
                            out.write(f"{coop} {numerchetau}\n")
                            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
                            contador_operacion=suml2
                            
                        elif (nummm >= -256  and nummm <= -17) or (nummm >=16 and nummm <=255):
                            if 'X' in line:
                                rr='00'
                            if 'Y' in line:
                                rr='01'
                            if 'SP' in line:
                                rr='10'
                            if 'PC' in line:
                                rr='11'
                            if nummm <0:
                                signn='1'
                                nummm=hex(nummm)
                                nummm=hex(int(nummm,16) + 16**2)[2:]
                                numerocheto1=(str('111')+str(rr)+str('0')+str('0')+str(signn))[4:]
                                numerocheto2=(str('111')+str(rr)+str('0')+str('0')+str(signn))[:4]
                                d=int(numerocheto1,2)
                                h=hex(d)[2:]
                                nummm1=h
                                d2=int(numerocheto2,2)
                                h2=hex(d2)[2:]
                                nummm2=h2
                                numerchetau=str(nummm2)+str(nummm1)
                                direct=direc6
                                coop='E3'
                                li=3
                                print(contador_operacion.zfill(4),end='   ')
                                out.write(str(contador_operacion.zfill(4))+"   ")
                                print("ADDD",end='   ')
                                out.write("ADDD   ")
                                print(direct,end='   ')
                                out.write(direct+"   ")
                                print(f"(LI={li})",end='   ')
                                out.write(f"(LI={li})   ")
                                print(f"{coop} {numerchetau} {nummm}")
                                out.write(f"{coop} {numerchetau} {nummm}\n")
                                suml2=hex(int(contador_operacion,16)+int(li3,16))[2:]
                                contador_operacion=suml2
                            else:
                                signn='0'
                                nummm=hex(nummm)[2:]
                                numerocheto1=(str('111')+str(rr)+str('0')+str('0')+str(signn))[4:]
                                numerocheto2=(str('111')+str(rr)+str('0')+str('0')+str(signn))[:4]
                                d=int(numerocheto1,2)
                                h=hex(d)[2:]
                                nummm1=h
                                d2=int(numerocheto2,2)
                                h2=hex(d2)[2:]
                                nummm2=h2
                                numerchetau=str(nummm2)+str(nummm1)
                                direct=direc6
                                coop='E3'
                                li=3
                                print(contador_operacion.zfill(4),end='   ')
                                out.write(str(contador_operacion.zfill(4))+"   ")
                                print("ADDD",end='   ')
                                out.write("ADDD   ")
                                print(direct,end='   ')
                                out.write(direct+"   ")
                                print(f"(LI={li})",end='   ')
                                out.write(f"(LI={li})   ")
                                print(f"{coop} {numerchetau} {nummm}")
                                out.write(f"{coop} {numerchetau} {nummm}\n")
                                suml2=hex(int(contador_operacion,16)+int(li3,16))[2:]
                                contador_operacion=suml2
                        elif (nummm >= -32768  and nummm <= -257) or (nummm >=256 and nummm <=65535):
                            if 'X' in line:
                                rr='00'
                            if 'Y' in line:
                                rr='01'
                            if 'SP' in line:
                                rr='10'
                            if 'PC' in line:
                                rr='11'
                            if nummm <0:
                                signn='1'
                                nummm=hex(nummm)
                                nummm=hex(int(nummm,16) + 16**4)[2:]
                                numerocheto1=(str('111')+str(rr)+str('0')+str('1')+str(signn))[4:]
                                numerocheto2=(str('111')+str(rr)+str('0')+str('1')+str(signn))[:4]
                                d=int(numerocheto1,2)
                                h=hex(d)[2:]
                                nummm1=h
                                d2=int(numerocheto2,2)
                                h2=hex(d2)[2:]
                                nummm2=h2
                                numerchetau=str(nummm2)+str(nummm1)
                                direct=direc6
                                coop='E3'
                                li=4
                                print(contador_operacion.zfill(4),end='   ')
                                out.write(str(contador_operacion.zfill(4))+"   ")
                                print("ADDD",end='   ')
                                out.write("ADDD   ")
                                print(direct,end='   ')
                                out.write(direct+"   ")
                                print(f"(LI={li})",end='   ')
                                out.write(f"(LI={li})   ")
                                print(f"{coop} {numerchetau} {nummm.zfill(4)[:2]} {nummm.zfill(4)[2:]}")
                                out.write(f"{coop} {numerchetau} {nummm.zfill(4)[:2]} {nummm.zfill(4)[2:]}\n")
                                suml2=hex(int(contador_operacion,16)+int(li4,16))[2:]
                                contador_operacion=suml2
                            else:
                                signn='0'
                                nummm=hex(nummm)[2:]
                                numerocheto1=(str('111')+str(rr)+str('0')+str('1')+str(signn))[4:]
                                numerocheto2=(str('111')+str(rr)+str('0')+str('1')+str(signn))[:4]
                                d=int(numerocheto1,2)
                                h=hex(d)[2:]
                                nummm1=h
                                d2=int(numerocheto2,2)
                                h2=hex(d2)[2:]
                                nummm2=h2
                                numerchetau=str(nummm2)+str(nummm1)
                                direct=direc6
                                coop='E3'
                                li=4
                                print(contador_operacion.zfill(4),end='   ')
                                out.write(str(contador_operacion.zfill(4))+"   ")
                                print("ADDD",end='   ')
                                out.write("ADDD   ")
                                print(direct,end='   ')
                                out.write(direct+"   ")
                                print(f"(LI={li})",end='   ')
                                out.write(f"(LI={li})   ")
                                print(f"{coop} {numerchetau} {nummm.zfill(4)[:2]} {nummm.zfill(4)[2:]}")
                                out.write(f"{coop} {numerchetau} {nummm.zfill(4)[:2]} {nummm.zfill(4)[2:]}\n")
                                suml2=hex(int(contador_operacion,16)+int(li4,16))[2:]
                                contador_operacion=suml2
            else:
                if len(newnumbber)<=2:
                    gatito=bool(re.findall('#', line))
                    if gatito is True:          
                        direct=direc2
                        coop='C3'
                        li=3
                        print(contador_operacion.zfill(4),end='   ')
                        out.write(str(contador_operacion.zfill(4))+"   ")
                        print("ADDD",end='   ')
                        out.write("ADDD   ")
                        print(direct,end='   ')
                        out.write(direct+"   ")
                        print(f"(LI={li})",end='   ')
                        out.write(f"(LI={li})   ")
                        print(f"{coop} {newnumbber.zfill(4)}")
                        out.write(f"{coop} {newnumbber.zfill(4)}\n")
                        suml3=hex(int(contador_operacion,16)+int(li3,16))[2:]
                        contador_operacion=suml3
                    else:
                        li=2
                        direct=direc3
                        coop='D3'
                        print(contador_operacion.zfill(4),end='   ')
                        out.write(str(contador_operacion.zfill(4))+"   ")
                        print("ADDD",end='   ')
                        out.write("ADDD   ")
                        print(direct,end='   ')
                        out.write(direct+"   ")
                        print(f"(LI={li})",end='   ')
                        out.write(f"(LI={li})   ")
                        print(f"{coop} {newnumbber.zfill(2)}")
                        out.write(f"{coop} {newnumbber.zfill(2)}\n")
                        suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
                        contador_operacion=suml2   
                #falta la validacion para li3
                elif len(newnumbber)==3 or 4:
                    li=3
                    gatito=bool(re.findall('#', line))
                    
                    if gatito is True:          
                        direct=direc2

                        coop='C3'
                    else:
                        direct=direc4
                        coop='F3'
                    print(contador_operacion.zfill(4),end='   ')
                    out.write(str(contador_operacion.zfill(4))+"   ")
                    print("ADDD",end='   ')
                    out.write("ADDD   ")
                    print(direct,end='   ')
                    out.write(direct+"   ")
                    print(f"(LI={li})",end='   ')
                    out.write(f"(LI={li})   ")
                    print(f"{coop} {newnumbber.zfill(4)}")
                    out.write(f"{coop} {newnumbber.zfill(4)}\n")
                    suml3=hex(int(contador_operacion,16)+int(li3,16))[2:]
                    contador_operacion=suml3    
                else:
                    print(str(contador_operacion.zfill(4))+"   FDR")
                    out.write(str(contador_operacion.zfill(4))+"   FDR")
                    suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
                    contador_operacion=suml2
            
    if 'ANDA' in line: 
        numbber=re.findall('[0-99999]', line)
        if len(numbber)<=1:
            newnumbber=int(numbber[0])
        elif len(numbber)<=2:
            newnumbber=int(numbber[0]+numbber[1])
        elif len(numbber)<=3:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2])
        elif len(numbber)<=4:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3])
        elif len(numbber)<=5:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3]+numbber[4])    
        else:
            print("Error, todavia no aceptamos numeros tan grandes")
        
        ppp=newnumbber
        arroba=bool(re.findall('@', line))
        porc=bool(re.findall('%', line))
        smps=line.find('$')
        
        if arroba is False:
            pass
            if porc is False:
                pass
                if smps == -1:
                    newnumbber=hex(newnumbber)[2:]
                    
        
        if arroba is True:
            newnumbberoc=str(newnumbber)
            d=int(newnumbberoc,8)
            h=hex(d)[2:]
            newnumbber=h
            
        elif porc is True:
                newnumbberoc=str(newnumbber)
                for digito in newnumbberoc:
                    if digito !='0' and digito !='1':
                        print('No se puede ingresar esto, ya que es binario')
                    else:
                        d=int(newnumbberoc,2)
                        h=hex(d)[2:]
                        newnumbber=h
        
        if smps != -1:
            ppp=str(newnumbber)
            newnumbber=ppp
        
        
        
        
        if len(newnumbber)<=2:
            li=2
            coop=0
            gatito=bool(re.findall('#', line))
            
            if gatito is True:          
                direct=direc2
                coop='84'
            else:
                direct=direc3
                coop='94'
            print(contador_operacion,end='   ')
            out.write(str(contador_operacion)+"   ")
            print("ANDA",end='   ')
            out.write("ANDA   ")
            print(direct,end='   ')
            out.write(direct+"   ")
            print(f"(LI={li})",end='   ')
            out.write(f"(LI={li})   ")
            print(f"{coop} {newnumbber}")
            out.write(f"{coop} {newnumbber}\n")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2    
        #falta la validacion para li3
        elif len(newnumbber)==3 or 4:
            gatito=bool(re.findall('#', line))
            if gatito is False:
                li=3
                coop='B4'
                direct=direc4
                print(contador_operacion,end='   ')
                out.write(str(contador_operacion)+"   ")
                print("ANDA",end='   ')
                out.write("ANDA   ")
                print(direct,end='   ')
                out.write(direct+"   ")
                print(f"(LI={li})",end='   ')
                out.write(f"(LI={li})   ")
                print(f"{coop} {newnumbber.zfill(4)}")
                out.write(f"{coop} {newnumbber.zfill(4)}\n")
                suml3=hex(int(contador_operacion,16)+int(li3,16))[2:]
                contador_operacion=suml3
            else:
                print(str(contador_operacion)+"   FDR")
                out.write(str(contador_operacion)+"   FDR")
                suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
                contador_operacion=suml2
        else:
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2
            
    if 'ANDB' in line: 
        numbber=re.findall('[0-99999]', line)
        if len(numbber)<=1:
            newnumbber=int(numbber[0])
        elif len(numbber)<=2:
            newnumbber=int(numbber[0]+numbber[1])
        elif len(numbber)<=3:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2])
        elif len(numbber)<=4:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3])
        elif len(numbber)<=5:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3]+numbber[4])    
        else:
            print("Error, todavia no aceptamos numeros tan grandes")
        
        ppp=newnumbber
        arroba=bool(re.findall('@', line))
        porc=bool(re.findall('%', line))
        smps=line.find('$')
        
        if arroba is False:
            pass
            if porc is False:
                pass
                if smps == -1:
                    newnumbber=hex(newnumbber)[2:]
                    
        
        if arroba is True:
            newnumbberoc=str(newnumbber)
            d=int(newnumbberoc,8)
            h=hex(d)[2:]
            newnumbber=h
            
        elif porc is True:
                newnumbberoc=str(newnumbber)
                for digito in newnumbberoc:
                    if digito !='0' and digito !='1':
                        print('No se puede ingresar esto, ya que es binario')
                    else:
                        d=int(newnumbberoc,2)
                        h=hex(d)[2:]
                        newnumbber=h
        
        if smps != -1:
            ppp=str(newnumbber)
            newnumbber=ppp
        
        
        
        
        if len(newnumbber)<=2:
            li=2
            coop=0
            gatito=bool(re.findall('#', line))
            
            if gatito is True:          
                direct=direc2
                coop='C4'
            else:
                direct=direc3
                coop='D4'
            print(contador_operacion,end='   ')
            out.write(str(contador_operacion)+"   ")
            print("ANDB",end='   ')
            out.write("ANDB   ")
            print(direct,end='   ')
            out.write(direct+"   ")
            print(f"(LI={li})",end='   ')
            out.write(f"(LI={li})   ")
            print(f"{coop} {newnumbber}")
            out.write(f"{coop} {newnumbber}\n")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2    
        #falta la validacion para li3
        elif len(newnumbber)==3 or 4:
            gatito=bool(re.findall('#', line))
            if gatito is False:
                li=3
                coop='F4'
                direct=direc4
                print(contador_operacion,end='   ')
                out.write(str(contador_operacion)+"   ")
                print("ANDB",end='   ')
                out.write("ANDB   ")
                print(direct,end='   ')
                out.write(direct+"   ")
                print(f"(LI={li})",end='   ')
                out.write(f"(LI={li})   ")
                print(f"{coop} {newnumbber.zfill(4)}")
                out.write(f"{coop} {newnumbber.zfill(4)}\n")
                suml3=hex(int(contador_operacion,16)+int(li3,16))[2:]
                contador_operacion=suml3
            else:
                print(str(contador_operacion)+"   FDR")
                out.write(str(contador_operacion)+"   FDR")
                suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
                contador_operacion=suml2
        else:
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2
            
    if 'ANDCC' in line:
        numbber=re.findall('[0-99999]', line)
        if len(numbber)<=1:
            newnumbber=int(numbber[0])
        elif len(numbber)<=2:
            newnumbber=int(numbber[0]+numbber[1])
        elif len(numbber)<=3:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2])
        elif len(numbber)<=4:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3])
        elif len(numbber)<=5:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3]+numbber[4])    
        else:
            print("Error, todavia no aceptamos numeros tan grandes")
        
        ppp=newnumbber
        arroba=bool(re.findall('@', line))
        porc=bool(re.findall('%', line))
        smps=line.find('$')
        
        if arroba is False:
            pass
            if porc is False:
                pass
                if smps == -1:
                    newnumbber=hex(newnumbber)[2:]
                    
        
        if arroba is True:
            newnumbberoc=str(newnumbber)
            d=int(newnumbberoc,8)
            h=hex(d)[2:]
            newnumbber=h
            
        elif porc is True:
                newnumbberoc=str(newnumbber)
                for digito in newnumbberoc:
                    if digito !='0' and digito !='1':
                        print('No se puede ingresar esto, ya que es binario')
                    else:
                        d=int(newnumbberoc,2)
                        h=hex(d)[2:]
                        newnumbber=h
        
        if smps != -1:
            ppp=str(newnumbber)
            newnumbber=ppp
        
        
        
        
        if len(newnumbber)<=2:
            li=2
            coop=10
            gatito=bool(re.findall('#', line))
            
            if gatito is True:          
                direct=direc2
                print(contador_operacion,end='   ')
                out.write(str(contador_operacion)+"   ")
                print("ANDCC",end='  ')
                out.write("ANDCC  ")
                print(f"{direct}",end='   ')
                out.write(f"{direct}   ")
                print("(LI=2)",end='   ')
                out.write("(LI=2)   ")
                print(f"10 {newnumbber}")
                out.write(f"10 {newnumbber}\n")
                suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
                contador_operacion=suml2
            else:
                print(str(contador_operacion)+"   FDR")
                out.write(str(contador_operacion)+"   FDR")
                suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
                contador_operacion=suml2
        else:
                print(str(contador_operacion)+"   FDR")
                out.write(str(contador_operacion)+"   FDR")
                suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
                contador_operacion=suml2    
            
            
    if 'ADDB' in line:
            numbber=re.findall('[0-99999]', line)
            if len(numbber)<=1:
                newnumbber=int(numbber[0])
            elif len(numbber)<=2:
                newnumbber=int(numbber[0]+numbber[1])
            elif len(numbber)<=3:
                newnumbber=int(numbber[0]+numbber[1]+numbber[2])
            elif len(numbber)<=4:
                newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3])
            elif len(numbber)<=5:
                newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3]+numbber[4])    
            else:
                print("Error, todavia no aceptamos numeros tan grandes")
            
            ppp=newnumbber
            arroba=bool(re.findall('@', line))
            porc=bool(re.findall('%', line))
            smps=line.find('$')
            
            if arroba is False:
                pass
                if porc is False:
                    pass
                    if smps == -1:
                        newnumbber=hex(newnumbber)[2:]
                        
            
            if arroba is True:
                newnumbberoc=str(newnumbber)
                d=int(newnumbberoc,8)
                h=hex(d)[2:]
                newnumbber=h
                
            elif porc is True:
                    newnumbberoc=str(newnumbber)
                    for digito in newnumbberoc:
                        if digito !='0' and digito !='1':
                            print('No se puede ingresar esto, ya que es binario')
                        else:
                            d=int(newnumbberoc,2)
                            h=hex(d)[2:]
                            newnumbber=h
            
            if smps != -1:
                ppp=str(newnumbber)
                newnumbber=ppp
            
            
            
            
            if len(newnumbber)<=2:
                li=2
                coop=''
                gatito=bool(re.findall('#', line))
                
                if gatito is True:          
                    direct=direc2
                    coop='CB'
                else:
                    direct=direc3
                    coop='DB'
                print(contador_operacion,end='   ')
                out.write(str(contador_operacion)+"   ")
                print("ADDB",end='   ')
                out.write("ADDB   ")
                print(direct,end='   ')
                out.write(direct+"   ")
                print(f"(LI={li})",end='   ')
                out.write(f"(LI={li})   ")
                print(f"{coop} {newnumbber}")
                out.write(f"{coop} {newnumbber}\n")
                suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
                contador_operacion=suml2    
            #falta la validacion para li3
            elif len(newnumbber)==3 or 4:
                gatito=bool(re.findall('#', line))
                if gatito is False:
                    li=3
                    coop='FB'
                    direct=direc4
                    print(contador_operacion,end='   ')
                    out.write(str(contador_operacion)+"   ")
                    print("ADDB",end='   ')
                    out.write("ADDB   ")
                    print(direct,end='   ')
                    out.write(direct+"   ")
                    print(f"(LI={li})",end='   ')
                    out.write(f"(LI={li})   ")
                    print(f"{coop} {newnumbber.zfill(4)}")
                    out.write(f"{coop} {newnumbber.zfill(4)}\n")
                    suml3=hex(int(contador_operacion,16)+int(li3,16))[2:]
                    contador_operacion=suml3
                else:
                    print(str(contador_operacion)+"   FDR")
                    out.write(str(contador_operacion)+"   FDR")
                    suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
                    contador_operacion=suml2
            else:
                print(str(contador_operacion)+"   FDR")
                out.write(str(contador_operacion)+"   FDR")
                suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
                contador_operacion=suml2
            
    if 'ASLA' in line:
        direct=direc1
        li=2
        detect_number=bool(re.search(r'\d', line))
        gatito=bool(re.findall('#', line))
        if detect_number is False and gatito is False:
            print(contador_operacion,end='   ')
            out.write(str(contador_operacion)+"   ")
            print("ASLA",end='   ')
            out.write("ASLA   ")
            print(f" {direc1}",end='   ')
            out.write(f" {direc1}   ")
            print("(LI=2)",end='   ')
            out.write("(LI=2)   ")
            print("00 48")
            out.write("00 48\n")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2
            
        else:
            
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2
                        
    if 'ASLB' in line:
        direct=direc1
        li=2
        detect_number=bool(re.search(r'\d', line))
        gatito=bool(re.findall('#', line))
        if detect_number is False and gatito is False:
            print(contador_operacion,end='   ')
            out.write(str(contador_operacion)+"   ")
            print("ASLB",end='   ')
            out.write("ASLB   ")
            print(f" {direc1}",end='   ')
            out.write(f" {direc1}   ")
            print("(LI=2)",end='   ')
            out.write("(LI=2)   ")
            print("00 58")
            out.write("00 58\n")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2
            
        else:
            
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2
    
    if 'ASLD' in line:
        direct=direc1
        li=2
        detect_number=bool(re.search(r'\d', line))
        gatito=bool(re.findall('#', line))
        if detect_number is False and gatito is False:
            print(contador_operacion,end='   ')
            out.write(str(contador_operacion)+"   ")
            print("ASLD",end='   ')
            out.write("ASLD   ")
            print(f" {direc1}",end='   ')
            out.write(f" {direc1}   ")
            print("(LI=2)",end='   ')
            out.write("(LI=2)   ")
            print("00 59")
            out.write("00 59\n")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2
            
        else:
            
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2
    
    if 'ASRA' in line:
        direct=direc1
        li=2
        detect_number=bool(re.search(r'\d', line))
        gatito=bool(re.findall('#', line))
        if detect_number is False and gatito is False:
            print(contador_operacion,end='   ')
            out.write(str(contador_operacion)+"   ")
            print("ASRA",end='   ')
            out.write("ASRA   ")
            print(f" {direc1}",end='   ')
            out.write(f" {direc1}   ")
            print("(LI=2)",end='   ')
            out.write("(LI=2)   ")
            print("00 47")
            out.write("00 47\n")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2
            
        else:
            
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2
            
    if 'ASRB' in line:
        direct=direc1
        li=2
        detect_number=bool(re.search(r'\d', line))
        gatito=bool(re.findall('#', line))
        if detect_number is False and gatito is False:
            print(contador_operacion,end='   ')
            out.write(str(contador_operacion)+"   ")
            print("ASRB",end='   ')
            out.write("ASRB   ")
            print(f" {direc1}",end='   ')
            out.write(f" {direc1}   ")
            print("(LI=2)",end='   ')
            out.write("(LI=2)   ")
            print("00 57")
            out.write("00 57\n")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2
            
        else:
            
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2
    
    if 'ASR' in line:
        
        numbber=re.findall('[0-99999]', line)
        if len(numbber)<=1:
            newnumbber=int(numbber[0])
        elif len(numbber)<=2:
            newnumbber=int(numbber[0]+numbber[1])
        elif len(numbber)<=3:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2])
        elif len(numbber)<=4:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3])
        elif len(numbber)<=5:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3]+numbber[4])    
        else:
            print("Error, todavia no aceptamos numeros tan grandes")
        
        ppp=newnumbber
        arroba=bool(re.findall('@', line))
        porc=bool(re.findall('%', line))
        smps=line.find('$')
        
        if arroba is False:
            pass
            if porc is False:
                pass
                if smps == -1:
                    newnumbber=hex(newnumbber)[2:]
                    
        
        if arroba is True:
            newnumbberoc=str(newnumbber)
            d=int(newnumbberoc,8)
            h=hex(d)[2:]
            newnumbber=h
            
        elif porc is True:
                newnumbberoc=str(newnumbber)
                for digito in newnumbberoc:
                    if digito !='0' and digito !='1':
                        print('No se puede ingresar esto, ya que es binario')
                    else:
                        d=int(newnumbberoc,2)
                        h=hex(d)[2:]
                        newnumbber=h
        
        if smps != -1:
            ppp=str(newnumbber)
            newnumbber=ppp
        
        
        
        elif len(newnumbber)<=4:
            gatito=bool(re.findall('#', line))
            if gatito is False:
                li=3
                coop='77'
                direct=direc4
                print(contador_operacion,end='   ')
                out.write(str(contador_operacion)+"   ")
                print("ASR",end='   ')
                out.write("ASR   ")
                print(f" {direct}",end='   ')
                out.write(f" {direct}   ")
                print(f"(LI={li})",end='   ')
                out.write(f"(LI={li})   ")
                print(f"{coop} {newnumbber.zfill(4)}")
                out.write(f"{coop} {newnumbber.zfill(4)}\n")
                suml3=hex(int(contador_operacion,16)+int(li3,16))[2:]
                contador_operacion=suml3
            else:
                print(str(contador_operacion)+"   FDR")
                out.write(str(contador_operacion)+"   FDR")
                suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
                contador_operacion=suml2
        else:
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2
            
    if 'BCLR' in line:
        
        numbber=re.findall('[0-99999]', line)
        if len(numbber)<=1:
            newnumbber=int(numbber[0])
        elif len(numbber)<=2:
            newnumbber=int(numbber[0]+numbber[1])
        elif len(numbber)<=3:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2])
        elif len(numbber)<=4:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3])
        elif len(numbber)<=5:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3]+numbber[4])    
        else:
            print("Error, todavia no aceptamos numeros tan grandes")
        
        ppp=newnumbber
        arroba=bool(re.findall('@', line))
        porc=bool(re.findall('%', line))
        smps=line.find('$')
        
        if arroba is False:
            pass
            if porc is False:
                pass
                if smps == -1:
                    newnumbber=hex(newnumbber)[2:]
                    
        
        if arroba is True:
            newnumbberoc=str(newnumbber)
            d=int(newnumbberoc,8)
            h=hex(d)[2:]
            newnumbber=h
            
        elif porc is True:
                newnumbberoc=str(newnumbber)
                for digito in newnumbberoc:
                    if digito !='0' and digito !='1':
                        print('No se puede ingresar esto, ya que es binario')
                    else:
                        d=int(newnumbberoc,2)
                        h=hex(d)[2:]
                        newnumbber=h
        
        if smps != -1:
            ppp=str(newnumbber)
            newnumbber=ppp
        
        
        
        
        if len(newnumbber)<=4:
            gatito=bool(re.findall('#', line))
            if gatito is False:
                li=3
                direct=direc3
                coop='4D'
                print(contador_operacion,end='   ')
                out.write(str(contador_operacion)+"   ")
                print("BCLR",end='   ')
                out.write("BCLR   ")
                print(direct,end='   ')
                out.write(f" {direct}   ")
                print(f"(LI={li})",end='   ')
                out.write(f"(LI={li})   ")
                print(f"{coop} {newnumbber.zfill(4)}")
                out.write(f"{coop} {newnumbber.zfill(4)}\n")
                suml2=hex(int(contador_operacion,16)+int(li3,16))[2:]
                contador_operacion=suml3
            else:
                print(str(contador_operacion)+"   FDR")
                out.write(str(contador_operacion)+"   FDR")
                suml3=hex(int(contador_operacion,16)+int(li3,16))[2:]
                contador_operacion=suml3    
        #falta la validacion para li3
        elif len(newnumbber)==5 or 6:
            gatito=bool(re.findall('#', line))
            if gatito is False:
                li=4
                coop='1D'
                direct=direc4
                print(contador_operacion,end='   ')
                out.write(str(contador_operacion)+"   ")
                print("BCLR",end='   ')
                out.write("BCLR   ")
                print(direct,end='   ')
                out.write(f" {direct}   ")
                print(f"(LI={li})",end='   ')
                out.write(f"(LI={li})   ")
                print(f"{coop} {newnumbber.zfill(6)}")
                out.write(f"{coop} {newnumbber.zfill(6)}\n")
                suml4=hex(int(contador_operacion,16)+int(li4,16))[2:]
                contador_operacion=suml4
            else:
                print(str(contador_operacion)+"   FDR")
                out.write(str(contador_operacion)+"   FDR")
                suml3=hex(int(contador_operacion,16)+int(li3,16))[2:]
                contador_operacion=suml3
        else:
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR")
            suml3=hex(int(contador_operacion,16)+int(li3,16))[2:]
            contador_operacion=suml3
                
    if 'BCS' in line:
        numbber=re.findall('[0-99999]', line)
        if len(numbber)<=1:
            newnumbber=int(numbber[0])
        elif len(numbber)<=2:
            newnumbber=int(numbber[0]+numbber[1])
        elif len(numbber)<=3:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2])
        elif len(numbber)<=4:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3])
        elif len(numbber)<=5:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3]+numbber[4])    
        else:
            print("Error, todavia no aceptamos numeros tan grandes")
        
        ppp=newnumbber
        arroba=bool(re.findall('@', line))
        porc=bool(re.findall('%', line))
        smps=line.find('$')
        
        if arroba is False:
            pass
            if porc is False:
                pass
                if smps == -1:
                    newnumbber=hex(newnumbber)[2:]
                    
        
        if arroba is True:
            newnumbberoc=str(newnumbber)
            d=int(newnumbberoc,8)
            h=hex(d)[2:]
            newnumbber=h
            
        elif porc is True:
                newnumbberoc=str(newnumbber)
                for digito in newnumbberoc:
                    if digito !='0' and digito !='1':
                        print('No se puede ingresar esto, ya que es binario')
                    else:
                        d=int(newnumbberoc,2)
                        h=hex(d)[2:]
                        newnumbber=h
        
        if smps != -1:
            ppp=str(newnumbber)
            newnumbber=ppp
        
        
        
        
        if len(newnumbber)<=2:
            li=2
            coop=25
            
            print(contador_operacion,end='   ')
            out.write(str(contador_operacion)+"   ")
            print("BCS",end='   ')
            out.write("BCS   ")
            print("REL",end='   ')
            out.write("REL   ")
            print(f"(LI={li})",end='   ')
            out.write(f"(LI={li})   ")
            print(f"{coop} {newnumbber}")
            out.write(f"{coop} {newnumbber}\n")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2
        else:
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2
                
    if 'BEQ' in line:
        numbber=re.findall('[0-99999]', line)
        if len(numbber)<=1:
            newnumbber=int(numbber[0])
        elif len(numbber)<=2:
            newnumbber=int(numbber[0]+numbber[1])
        elif len(numbber)<=3:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2])
        elif len(numbber)<=4:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3])
        elif len(numbber)<=5:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3]+numbber[4])    
        else:
            print("Error, todavia no aceptamos numeros tan grandes")
        
        ppp=newnumbber
        arroba=bool(re.findall('@', line))
        porc=bool(re.findall('%', line))
        smps=line.find('$')
        
        if arroba is False:
            pass
            if porc is False:
                pass
                if smps == -1:
                    newnumbber=hex(newnumbber)[2:]
                    
        
        if arroba is True:
            newnumbberoc=str(newnumbber)
            d=int(newnumbberoc,8)
            h=hex(d)[2:]
            newnumbber=h
            
        elif porc is True:
                newnumbberoc=str(newnumbber)
                for digito in newnumbberoc:
                    if digito !='0' and digito !='1':
                        print('No se puede ingresar esto, ya que es binario')
                    else:
                        d=int(newnumbberoc,2)
                        h=hex(d)[2:]
                        newnumbber=h
        
        if smps != -1:
            ppp=str(newnumbber)
            newnumbber=ppp
        
        
        
        
        if len(newnumbber)<=2:
            li=2
            coop=27
            
            print(contador_operacion,end='   ')
            out.write(str(contador_operacion)+"   ")
            print("BEQ",end='   ')
            out.write("BEQ   ")
            print("REL",end='   ')
            out.write("REL   ")
            print(f"(LI={li})",end='   ')
            out.write(f"(LI={li})   ")
            print(f"{coop} {newnumbber}")
            out.write(f"{coop} {newnumbber}\n")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2
        else:
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2
                
    if 'BGE' in line:
        numbber=re.findall('[0-99999]', line)
        if len(numbber)<=1:
            newnumbber=int(numbber[0])
        elif len(numbber)<=2:
            newnumbber=int(numbber[0]+numbber[1])
        elif len(numbber)<=3:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2])
        elif len(numbber)<=4:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3])
        elif len(numbber)<=5:
            newnumbber=int(numbber[0]+numbber[1]+numbber[2]+numbber[3]+numbber[4])    
        else:
            print("Error, todavia no aceptamos numeros tan grandes")
        
        ppp=newnumbber
        arroba=bool(re.findall('@', line))
        porc=bool(re.findall('%', line))
        smps=line.find('$')
        
        if arroba is False:
            pass
            if porc is False:
                pass
                if smps == -1:
                    newnumbber=hex(newnumbber)[2:]
                    
        
        if arroba is True:
            newnumbberoc=str(newnumbber)
            d=int(newnumbberoc,8)
            h=hex(d)[2:]
            newnumbber=h
            
        elif porc is True:
                newnumbberoc=str(newnumbber)
                for digito in newnumbberoc:
                    if digito !='0' and digito !='1':
                        print('No se puede ingresar esto, ya que es binario')
                    else:
                        d=int(newnumbberoc,2)
                        h=hex(d)[2:]
                        newnumbber=h
        
        if smps != -1:
            ppp=str(newnumbber)
            newnumbber=ppp
        
        
        
        
        if len(newnumbber)<=2:
            li=2
            coop='2C'
            
            print(contador_operacion,end='   ')
            out.write(str(contador_operacion)+"   ")
            print("BGE",end='   ')
            out.write("BGE   ")
            print("REL",end='   ')
            out.write("REL   ")
            print(f"(LI={li})",end='   ')
            out.write(f"(LI={li})   ")
            print(f"{coop} {newnumbber}")
            out.write(f"{coop} {newnumbber}\n")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2
        else:
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR")
            suml2=hex(int(contador_operacion,16)+int(li2,16))[2:]
            contador_operacion=suml2
            
    if 'END' in line:
        print(contador_operacion.zfill(4),end='   ')
        out.write(str(contador_operacion.zfill(4))+"   ")
        print("END")
        out.write("END\n")    



out.close()