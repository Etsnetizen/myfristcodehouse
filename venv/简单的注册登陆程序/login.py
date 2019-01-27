import getpass
import opendatabase
def login():
    count=0
    while count<3:
        your_name=input("请输入你的用户名：")
        your_pws=input("请输入你的密码：")
        database=opendatabase.open_database()
        uesr_pws=database.get(your_name)
        if uesr_pws is None:
            print("此用户不存在")
            break
        if your_pws !=uesr_pws:
            print("密码错误，你还可以输入"+str(2-count)+"次")
            count+=1
            continue
        print("密码正确")
        break
    else:
        print("你已经尝试了三次！")
