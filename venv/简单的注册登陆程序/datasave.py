import pickle
def datasave(user_data):
    try:
        with open("f:/mypython/database.pkl",'wb') as f:
            pickle.dump(user_data,f)
            return True
    except Exception as error:
        print("保存失败！原因："+str(error))
        return False
