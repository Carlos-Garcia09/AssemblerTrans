from multiprocessing import cpu_count
import re
from itertools import groupby



filename1='P6.asm'
filename2='p6.lst'
li=0
direc1='INH'
direc2='IMM'
direc3='DIR'
direc4='EXT'
#direc5='REL'
etiqueta=0

li1="1"
li2="2"
li3="3"

contador_operacion="4000"


suml3=hex(int(contador_operacion,16)+int(li3,16))[2:]


print("       ORG $"+str(contador_operacion))


out= open(filename2, 'w')
out.write("       ORG $"+str(contador_operacion)+"\n")

with open(filename1, 'r') as f:
    lines = f.readlines()
for line in lines:
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
                coop=89
            else:
                direct=direc3
                coop=99
            print(contador_operacion,end='   ')
            out.write(str(contador_operacion)+"   ")
            print("ADCA",end='   ')
            out.write("ADCA   ")
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
                coop='B9'
                direct=direc4
                print(contador_operacion,end='   ')
                out.write(str(contador_operacion)+"   ")
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
                print(str(contador_operacion)+"   FDR")
                out.write(str(contador_operacion)+"   FDR")
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
            gatito=bool(re.findall('#', line))
            if gatito is True:          
                direct=direc2
                coop='C3'
                li=3
            else:
                li=2
                direct=direc3
                coop='D3'
            print(contador_operacion,end='   ')
            out.write(str(contador_operacion)+"   ")
            print("ADDD",end='   ')
            out.write("ADDD   ")
            print(direct,end='   ')
            out.write(direct+"   ")
            print(f"(LI={li})",end='   ')
            out.write(f"(LI={li})   ")
            print(f"{coop} {newnumbber}")
            out.write(f"{coop} {newnumbber}\n")
            contador_operacion=contador_operacion+2    
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
            print(contador_operacion,end='   ')
            out.write(str(contador_operacion)+"   ")
            print("ADDD",end='   ')
            out.write("ADDD   ")
            print(direct,end='   ')
            out.write(direct+"   ")
            print(f"(LI={li})",end='   ')
            out.write(f"(LI={li})   ")
            print(f"{coop} {newnumbber.zfill(4)}")
            out.write(f"{coop} {newnumbber.zfill(4)}\n")
            contador_operacion=contador_operacion+3
        else:
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR")
            contador_operacion=contador_operacion+2
            
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
            contador_operacion=contador_operacion+2    
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
                contador_operacion=contador_operacion+3
            else:
                print(str(contador_operacion)+"   FDR")
                out.write(str(contador_operacion)+"   FDR")
                contador_operacion=contador_operacion+2
        else:
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR")
            contador_operacion=contador_operacion+2
            
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
            contador_operacion=contador_operacion+2    
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
                contador_operacion=contador_operacion+3
            else:
                print(str(contador_operacion)+"   FDR")
                out.write(str(contador_operacion)+"   FDR")
                contador_operacion=contador_operacion+2
        else:
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR")
            contador_operacion=contador_operacion+2
            
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
                contador_operacion=contador_operacion+2
            else:
                print(str(contador_operacion)+"   FDR")
                out.write(str(contador_operacion)+"   FDR")
                contador_operacion=contador_operacion+2
        else:
                print(str(contador_operacion)+"   FDR")
                out.write(str(contador_operacion)+"   FDR")
                contador_operacion=contador_operacion+2    
            
            
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
                contador_operacion=contador_operacion+2    
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
                    contador_operacion=contador_operacion+3
                else:
                    print(str(contador_operacion)+"   FDR")
                    out.write(str(contador_operacion)+"   FDR")
                    contador_operacion=contador_operacion+2
            else:
                print(str(contador_operacion)+"   FDR")
                out.write(str(contador_operacion)+"   FDR")
                contador_operacion=contador_operacion+2
            
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
            contador_operacion=contador_operacion+2
            
        else:
            
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR")
            contador_operacion=contador_operacion+2
                        
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
            contador_operacion=contador_operacion+2
            
        else:
            
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR")
            contador_operacion=contador_operacion+2
    
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
            contador_operacion=contador_operacion+2
            
        else:
            
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR")
            contador_operacion=contador_operacion+2
    
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
            contador_operacion=contador_operacion+2
            
        else:
            
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR")
            contador_operacion=contador_operacion+2
            
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
            contador_operacion=contador_operacion+2
            
        else:
            
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR")
            contador_operacion=contador_operacion+2
    
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
                contador_operacion=contador_operacion+3
            else:
                print(str(contador_operacion)+"   FDR")
                out.write(str(contador_operacion)+"   FDR")
                contador_operacion=contador_operacion+2
        else:
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR")
            contador_operacion=contador_operacion+2
            
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
                contador_operacion=contador_operacion+2
            else:
                print(str(contador_operacion)+"   FDR")
                out.write(str(contador_operacion)+"   FDR")
                contador_operacion=contador_operacion+3    
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
                contador_operacion=contador_operacion+3
            else:
                print(str(contador_operacion)+"   FDR")
                out.write(str(contador_operacion)+"   FDR")
                contador_operacion=contador_operacion+3
        else:
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR")
            contador_operacion=contador_operacion+3
                
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
            contador_operacion=contador_operacion+2
        else:
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR")
            contador_operacion=contador_operacion+2
                
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
            contador_operacion=contador_operacion+2
        else:
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR")
            contador_operacion=contador_operacion+2
                
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
            contador_operacion=contador_operacion+2
        else:
            print(str(contador_operacion)+"   FDR")
            out.write(str(contador_operacion)+"   FDR")
            contador_operacion=contador_operacion+2
            
    if 'END' in line:
        print(contador_operacion,end='   ')
        out.write(str(contador_operacion)+"   ")
        print("END")
        out.write("END\n")    


out.close()