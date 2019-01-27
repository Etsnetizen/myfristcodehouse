import pickle
def open_database():
    try:
        with open("f:/mypython/database.pkl",'rb') as f:
            return pickle.load(f)
    #except Exception as error:
      #  print("文件读取失败！原因："+str(error))
      #  return False
    #except IOError as e:
     #   return False
    #except Exception as e:
     #   raise e
    except EOFError:
        return None