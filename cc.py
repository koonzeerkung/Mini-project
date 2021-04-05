#!/usr/bin/env python
# coding: utf-8

# In[15]:


import os
os.system("")
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    ORANGE='\33[33m'
def read(): #เปิดfileชื่อสินค้าและราคาออกมา แล้วเก็บเป็นdict.
    with open('menu.txt') as file:
        text = file.readlines()
    d = dict()
    for each in text:
        each = each.split('  ')
        product = each[0]
        price = each[1].strip()
        d[product]= float(price)
    return d
def vat(): #counter mode
    z=[]
    i=1
    with open('rn.txt','a+') as g:#ไว้ใช้ใส่และตั้งชื่อใบกำกับภาษี
        try:
            g.seek(0)
            k = len(g.read())
            n=int(k)
        except:
            g.write('1')
            g.seek(0)
            k = len(g.read())
            n=int(k)
        finally:
            g.write('1')
        with open('A/{}.txt'.format(n),'a+') as g:
                        g.write('-'*50)
                        g.write("\n"+' \t\t    บริษัท จุฬาภรณราชวิทยาลัยจำกัด')
                        g.write("\n"+' \t\t51 หมู่ 6 บ่อเงิน ลาดหลุมแก้ว ปทุมธานี')
                        g.write("\n"+'----------------------------------------')
                        g.write('ใบกำกับภาษีแบบย่อ')
                        g.write('----------------------------------------')
                        g.write("\n"+'_'*50)
    while True:
        a=input(style.BLUE+'กด 1 เพื่อบันทึกรายการสินค้า '+style.GREEN+' กด 2 เพื่อแสดงใบเสร็จเบื้องต้นกด'+style.MAGENTA+' 3 เพื่อprintใบเสร็จ'+style.RED+' กด 0 เพื่อกลับสู่หน้าเลือกโหมด'+style.BLACK+' : ')
        if a=='1':
            while True:
                b=input('ใส่ชื่อสินค้า(ใส่ 0 เพื่อหยุด) : ')
                if b=='0':
                    break
                list_of_products = read()
                c = False  #ถ้ามีข้อมูลของสินค้าอยู่แล้ว จะดึงราคามาเลย
                for product in list_of_products:
                    if b == product:
                        c = list_of_products[product]
                if not c:  #ถ้าไม่มีก็ใส่เอง
                    try:
                        c=float(input('ใส่ราคา : '))
                    except:
                        print('โปรดใส่ราคาเป็นตัวเลข')
                    else : #แล้วบันทึกด้วย
                        with open ("menu.txt","a") as f :
                            f.write('{}  {}'.format(b, c))
                            z.append(c)
                else:
                    print('{} ราคา {} บาท'.format(b, c))
                    z.append(c)
                with open('A/{}.txt'.format(n),'a') as g:
                    g.write("\n"+'\t%d.%s\t %f\tบาท'%(i,b,c))
                i+=1
        elif a=='2':
            y=tuple(z)
            d=sum(y)
            e=(d*7/100)
            f=d+e
            try:
                print('ราคาสินค้า %f บาท'%d )
                print('ภาษี %f บาท'%e)
                print('รวมทั้งหมด %f บาท'%f)
            except UnboundLocalError:
                print('ยังไม่ได้ใส่รายการสินค้า')
        elif a=='3':
            with open('A/{}.txt'.format(n),'a') as g :
                g.write("\n"+'_'*50)
                g.write("\n"+'\tรวม\t\t%f\tบาท'%(d))
                g.write("\n"+'\tภาษี 7%')
                g.write('\t\t%f\tบาท'%(e))
                g.write("\n"+'_'*50)
                g.write("\n"+'\tราคารวมทั้งหมด\t%f\tบาท'%(f))
                g.write('\n'+'\tหมายเลขใบกำกับภาษี : {}'.format(n))
                g.write("\n"+'_'*50)
            f= open('A/{}.txt' .format(n), "r")
            print(f.read())
            break
        elif a=='0':
            print(style.RED+'กำลังกลับสู่หน้าเลือกโหมด'+style.BLACK)
            print('\n')
            break
        else:
            print(style.ORANGE+'โปรดพิมพ์ตัวอักษรตามเงื่อนไข'+style.BLACK)
    print('\n')





