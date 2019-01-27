import pickle
def loaddata():
    try:
        with open("f:/mypython/database.pkl",'rb') as file:
            data=pickle.load(file)
            print(str(data))
    except Exception as error:
        print("打印出错！原因："+str(error))
