# from pymongo import MongoClient
# def get_database():
 
#    # Provide the mongodb atlas url to connect python to mongodb using pymongo
#    CONNECTION_STRING = "mongodb+srv://user:pass@cluster.mongodb.net/myFirstDatabase"
 
#    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
#    client = MongoClient(CONNECTION_STRING)
 
#    # Create the database for our example (we will use the same database throughout the tutorial
#    return client['user_shopping_list']
  
# # This is added so that many files can reuse the function get_database()
# if __name__ == "__main__":   
  
#    # Get the database
#    dbname = get_database()

# from datetime import date

# print(date.today().strftime('%d-%m-%Y'))

# from PySide.QtGui import *

# def main():
#     app = QApplication([])

#     window = QMainWindow()
#     bar = QMenuBar(window)
#     window.setMenuBar(bar)
#     m = QMenu('menu', bar)
#     bar.addMenu(m)
#     action = QAction('action', m, checkable=True)
#     m.addAction(action)

#     window.show()
#     app.exec_()
#     print(action.isChecked())

# if __name__ == '__main__':
#     main()

x = [{}]

