import login
import register
import loaddata
if __name__=='__main__':
    user_choose=input("请输入你要的操作：1.注册 2.登陆 3.退出 0.打印当前用户信息")
    if user_choose=='1':
        register.register()
    elif user_choose=='2':
        login.login()
    elif user_choose=='3':
        exit()
    elif user_choose=='0':
        loaddata.loaddata()
    else:
        print("无效指令")