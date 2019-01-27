import getpass
import pickle
import datasave
import opendatabase
def register():
    try:
        user_name=input("请输入要注册的用户名：")
        #获取字典数据
        database=opendatabase.open_database()if opendatabase.open_database()else {}
        if user_name in database.keys():
            print("用户已存在，请登陆")
            return False
        user_pws = input("请输入你的密码：")
        database[user_name]=user_pws#往字典中添加此用户
        save=datasave.datasave(database)#保存字典到文件中
        if save:#保存成功的话
            print("注册成功")
        else:
            raise IOError
    except Exception as error:
        print("注册失败！原因："+str(error))



