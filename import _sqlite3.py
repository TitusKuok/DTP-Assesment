#Import SQL intrepeter
import sqlite3
#Select ghef.db as the database that we are going to use in this program
DATABASE = 'ghef.db'
#Use def to define print_all_monsters()
def print_all_monsters():
    #Connect ghef.db with SQL intrepeter
    with sqlite3.connect(DATABASE) as db:
        #Use .cursor() function as the operator of this program.
        cursor = db.cursor()    
        #Write a query
        a = f"SELECT Monsters_name.MonstersNames, Monster_classes.Monster_Classes, e1.Elements_And_Status, e2.Elements_And_Status, e3.Elements_And_Status, e4.Elements_And_Status, e5.Elements_And_Status FROM Monsters_name JOIN Monster_classes ON Monsters_name.Classes = Monster_classes.ID LEFT JOIN Elements_And_Abnormal_Status as e1 ON Monsters_name.Type1 = e1.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e2 ON Monsters_name.Type2 = e2.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e3 ON Monsters_name.Type3 = e3.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e4 ON Monsters_name.Type4 = e4.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e5 ON Monsters_name.Type5 = e5.Elements_ID;"#Uses JOIN and LEFT JOIN function to let the outcome showing words and not numbers
        #Use cursor.execute() to run the query above
        cursor.execute(a)
        #Use cursor.fetchall() to gain all of the information from the query
        result = cursor.fetchall()
        #Remove useless elements in the outcome
        for SMD in result:
            print_data = [SMD[0], SMD[1], SMD[2]] 
            for i in range(3, 7):  
                if SMD[i] is not None:
                    print_data.append(SMD[i])
            print("________________________________________________________________")
            print("Monster: ",print_data[0],"\n","Class: ",print_data[1],"\n","Elements Or Status Effect: ",(print_data[2:]))
        print("________________________________________________________________")
def print_all_elder():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()    
        #Add "WHERE" to find all elder dragon
        a = f"SELECT Monsters_name.MonstersNames, Monster_classes.Monster_Classes, e1.Elements_And_Status, e2.Elements_And_Status, e3.Elements_And_Status, e4.Elements_And_Status, e5.Elements_And_Status FROM Monsters_name JOIN Monster_classes ON Monsters_name.Classes = Monster_classes.ID LEFT JOIN Elements_And_Abnormal_Status as e1 ON Monsters_name.Type1 = e1.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e2 ON Monsters_name.Type2 = e2.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e3 ON Monsters_name.Type3 = e3.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e4 ON Monsters_name.Type4 = e4.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e5 ON Monsters_name.Type5 = e5.Elements_ID WHERE Classes = 1;"
        cursor.execute(a)
        result = cursor.fetchall()
        for SMD in result:
            print_data = [SMD[0], SMD[1], SMD[2]] 
            for i in range(3, 7):  
                if SMD[i] is not None:
                    print_data.append(SMD[i])
            print("________________________________________________________________")
            print("Monster: ",print_data[0],"\n","Class: ",print_data[1],"\n","Elements Or Status Effect: ",print_data[2:])
        print("________________________________________________________________")
            
def print_all_flying():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()   
        #Add "WHERE" to find all flying wyverns
        a = f"SELECT Monsters_name.MonstersNames, Monster_classes.Monster_Classes, e1.Elements_And_Status, e2.Elements_And_Status, e3.Elements_And_Status, e4.Elements_And_Status, e5.Elements_And_Status FROM Monsters_name JOIN Monster_classes ON Monsters_name.Classes = Monster_classes.ID LEFT JOIN Elements_And_Abnormal_Status as e1 ON Monsters_name.Type1 = e1.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e2 ON Monsters_name.Type2 = e2.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e3 ON Monsters_name.Type3 = e3.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e4 ON Monsters_name.Type4 = e4.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e5 ON Monsters_name.Type5 = e5.Elements_ID WHERE Classes = 2;"
        cursor.execute(a)
        result = cursor.fetchall()
        for SMD in result:
            print_data = [SMD[0], SMD[1], SMD[2]] 
            for i in range(3, 7):  
                if SMD[i] is not None:
                    print_data.append(SMD[i])
            print("________________________________________________________________")
            print("Monster: ",print_data[0],"\n","Class: ",print_data[1],"\n","Elements Or Status Effect: ",print_data[2:])
        print("________________________________________________________________")

def print_all_fanged():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()  
        #Add "WHERE" to find all fanged wyverns
        a = f"SELECT Monsters_name.MonstersNames, Monster_classes.Monster_Classes, e1.Elements_And_Status, e2.Elements_And_Status, e3.Elements_And_Status, e4.Elements_And_Status, e5.Elements_And_Status FROM Monsters_name JOIN Monster_classes ON Monsters_name.Classes = Monster_classes.ID LEFT JOIN Elements_And_Abnormal_Status as e1 ON Monsters_name.Type1 = e1.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e2 ON Monsters_name.Type2 = e2.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e3 ON Monsters_name.Type3 = e3.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e4 ON Monsters_name.Type4 = e4.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e5 ON Monsters_name.Type5 = e5.Elements_ID WHERE Classes = 3;"
        cursor.execute(a)
        result = cursor.fetchall()
        for SMD in result:
            print_data = [SMD[0], SMD[1], SMD[2]] 
            for i in range(3, 7):  
                if SMD[i] is not None:
                    print_data.append(SMD[i])
            print("________________________________________________________________")
            print("Monster: ",print_data[0],"\n","Class: ",print_data[1],"\n","Elements Or Status Effect: ",print_data[2:])
        print("________________________________________________________________")

def print_all_brute():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()    
        #Add "WHERE" to find all brute wyverns
        a = f"SELECT Monsters_name.MonstersNames, Monster_classes.Monster_Classes, e1.Elements_And_Status, e2.Elements_And_Status, e3.Elements_And_Status, e4.Elements_And_Status, e5.Elements_And_Status FROM Monsters_name JOIN Monster_classes ON Monsters_name.Classes = Monster_classes.ID LEFT JOIN Elements_And_Abnormal_Status as e1 ON Monsters_name.Type1 = e1.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e2 ON Monsters_name.Type2 = e2.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e3 ON Monsters_name.Type3 = e3.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e4 ON Monsters_name.Type4 = e4.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e5 ON Monsters_name.Type5 = e5.Elements_ID WHERE Classes = 5;"
        cursor.execute(a)
        result = cursor.fetchall()
        for SMD in result:
            print_data = [SMD[0], SMD[1], SMD[2]] 
            for i in range(3, 7):  
                if SMD[i] is not None:
                    print_data.append(SMD[i])
            print("________________________________________________________________")
            print("Monster: ",print_data[0],"\n","Class: ",print_data[1],"\n","Elements Or Status Effect: ",print_data[2:])
        print("________________________________________________________________")

def print_all_piscine():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()    
        #Add "WHERE" to find all piscine wyverns
        a = f"SELECT Monsters_name.MonstersNames, Monster_classes.Monster_Classes, e1.Elements_And_Status, e2.Elements_And_Status, e3.Elements_And_Status, e4.Elements_And_Status, e5.Elements_And_Status FROM Monsters_name JOIN Monster_classes ON Monsters_name.Classes = Monster_classes.ID LEFT JOIN Elements_And_Abnormal_Status as e1 ON Monsters_name.Type1 = e1.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e2 ON Monsters_name.Type2 = e2.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e3 ON Monsters_name.Type3 = e3.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e4 ON Monsters_name.Type4 = e4.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e5 ON Monsters_name.Type5 = e5.Elements_ID WHERE Classes = 6;"
        cursor.execute(a)
        result = cursor.fetchall()
        for SMD in result:
            print_data = [SMD[0], SMD[1], SMD[2]] 
            for i in range(3, 7):  
                if SMD[i] is not None:
                    print_data.append(SMD[i])
            print("________________________________________________________________")
            print("Monster: ",print_data[0],"\n","Class: ",print_data[1],"\n","Elements Or Status Effect: ",print_data[2:])
        print("________________________________________________________________")


def print_all_Bird():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()    
        #Add "WHERE" to find all bird wyverns
        a = f"SELECT Monsters_name.MonstersNames, Monster_classes.Monster_Classes, e1.Elements_And_Status, e2.Elements_And_Status, e3.Elements_And_Status, e4.Elements_And_Status, e5.Elements_And_Status FROM Monsters_name JOIN Monster_classes ON Monsters_name.Classes = Monster_classes.ID LEFT JOIN Elements_And_Abnormal_Status as e1 ON Monsters_name.Type1 = e1.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e2 ON Monsters_name.Type2 = e2.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e3 ON Monsters_name.Type3 = e3.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e4 ON Monsters_name.Type4 = e4.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e5 ON Monsters_name.Type5 = e5.Elements_ID WHERE Classes = 7;"
        cursor.execute(a)
        result = cursor.fetchall()
        for SMD in result:
            print_data = [SMD[0], SMD[1], SMD[2]] 
            for i in range(3, 7):  
                if SMD[i] is not None:
                    print_data.append(SMD[i])
            print("________________________________________________________________")
            print("Monster: ",print_data[0],"\n","Class: ",print_data[1],"\n","Elements Or Status Effect: ",print_data[2:])
        print("________________________________________________________________")


def print_all_Relicts():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()    
        #Add "WHERE" to find all Relicts monster
        a = f"SELECT Monsters_name.MonstersNames, Monster_classes.Monster_Classes, e1.Elements_And_Status, e2.Elements_And_Status, e3.Elements_And_Status, e4.Elements_And_Status, e5.Elements_And_Status FROM Monsters_name JOIN Monster_classes ON Monsters_name.Classes = Monster_classes.ID LEFT JOIN Elements_And_Abnormal_Status as e1 ON Monsters_name.Type1 = e1.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e2 ON Monsters_name.Type2 = e2.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e3 ON Monsters_name.Type3 = e3.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e4 ON Monsters_name.Type4 = e4.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e5 ON Monsters_name.Type5 = e5.Elements_ID WHERE Classes = 8;"
        cursor.execute(a)
        result = cursor.fetchall()
        for SMD in result:
            print_data = [SMD[0], SMD[1], SMD[2]] 
            for i in range(3, 7):  
                if SMD[i] is not None:
                    print_data.append(SMD[i])
            print("________________________________________________________________")
            print("Monster: ",print_data[0],"\n","Class: ",print_data[1],"\n","Elements Or Status Effect: ",print_data[2:])
        print("________________________________________________________________")


def print_all_beast():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()    
        #Add "WHERE" to find all fanged beast
        a = f"SELECT Monsters_name.MonstersNames, Monster_classes.Monster_Classes, e1.Elements_And_Status, e2.Elements_And_Status, e3.Elements_And_Status, e4.Elements_And_Status, e5.Elements_And_Status FROM Monsters_name JOIN Monster_classes ON Monsters_name.Classes = Monster_classes.ID LEFT JOIN Elements_And_Abnormal_Status as e1 ON Monsters_name.Type1 = e1.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e2 ON Monsters_name.Type2 = e2.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e3 ON Monsters_name.Type3 = e3.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e4 ON Monsters_name.Type4 = e4.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e5 ON Monsters_name.Type5 = e5.Elements_ID WHERE Classes = 4;"
        cursor.execute(a)
        result = cursor.fetchall()
        for SMD in result:
            print_data = [SMD[0], SMD[1], SMD[2]] 
            for i in range(3, 7):  
                if SMD[i] is not None:
                    print_data.append(SMD[i])
            print("________________________________________________________________")
            print("Monster: ",print_data[0],"\n","Class: ",print_data[1],"\n","Elements Or Status Effect: ",print_data[2:])
        print("________________________________________________________________")
#check if this program was used as main program or not.
if __name__ == "__main__":
    #Ask for user's input
    print("""What classes of monster you want to look for?\n Input 1 for all monster\n Input 2 for Elder Dragon\n Input 3 for Flying Wyverns\n Input 4 for Fanged Wyverns\n Input 5 for Fanged Beast\n Input 6 for Brute Wyverns\n Input 7 for Piscine Wyverns\n Input 8 for Bird Wyverns\n Input 9 for Relicts\n Input 0 to close the program""")
#Keep asking for input from user
while True:
        Q = input("Select the classes:\n")
        #run different def depends on user input.
        if Q == '1':
            print_all_monsters()
        elif Q == '2':
            print_all_elder()
        elif Q == '3':
            print_all_flying()
        elif Q == '4':
            print_all_fanged()
        elif Q == '5':
            print_all_beast()
        elif Q == '6':
            print_all_brute()
        elif Q == '7':
            print_all_piscine()
        elif Q == '8':
            print_all_Bird()
        elif Q == '9':
            print_all_Relicts()
        elif Q == '0':
            break
        else:
            print("Please type a number from 0 to 9")
            print("""What classes of monster you want to look for?\n Input 1 for all monster\n Input 2 for Elder Dragon\n Input 3 for Flying Wyverns\n Input 4 for Fanged Wyverns\n Input 5 for Fanged Beast\n Input 6 for Brute Wyverns\n Input 7 for Piscine Wyverns\n Input 8 for Bird Wyverns\n Input 9 for Relicts\n Input 0 to close the program""")