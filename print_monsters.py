#Import SQL intrepeter
import sqlite3
#Select ghef.db as the database that we are going to use in this program
DATABASE = 'MHWI_Data.db'
#define a function that can print out all monsters
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
#define a function that can print out all elder dragons
def print_all_elder():
    '''Each section of in all the defined function below is exactly same as the print_all_monster()'''
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()    
        '''At the query below we will add "WHERE Classes == 1" at the end of the query to find all elder dragon.'''
        elder = f"SELECT Monsters_name.MonstersNames, Monster_classes.Monster_Classes, e1.Elements_And_Status, e2.Elements_And_Status, e3.Elements_And_Status, e4.Elements_And_Status, e5.Elements_And_Status FROM Monsters_name JOIN Monster_classes ON Monsters_name.Classes = Monster_classes.ID LEFT JOIN Elements_And_Abnormal_Status as e1 ON Monsters_name.Type1 = e1.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e2 ON Monsters_name.Type2 = e2.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e3 ON Monsters_name.Type3 = e3.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e4 ON Monsters_name.Type4 = e4.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e5 ON Monsters_name.Type5 = e5.Elements_ID WHERE Classes = 1;"
        cursor.execute(elder)
        result = cursor.fetchall()
        for SMD in result:
            print_data = [SMD[0], SMD[1], SMD[2]] 
            for i in range(3, 7):  
                if SMD[i] is not None:
                    print_data.append(SMD[i])
            print("________________________________________________________________")
            print("Monster: ",print_data[0],"\n","Class: ",print_data[1],"\n","Elements Or Status Effect: ",print_data[2:])
        print("________________________________________________________________")
#define a function that can print out all flynig wyverns.
def print_all_flying():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()   
        '''At the query below we will add "WHERE Classes == 2" at the end of the query to find all flying wyverns'''
        flying = f"SELECT Monsters_name.MonstersNames, Monster_classes.Monster_Classes, e1.Elements_And_Status, e2.Elements_And_Status, e3.Elements_And_Status, e4.Elements_And_Status, e5.Elements_And_Status FROM Monsters_name JOIN Monster_classes ON Monsters_name.Classes = Monster_classes.ID LEFT JOIN Elements_And_Abnormal_Status as e1 ON Monsters_name.Type1 = e1.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e2 ON Monsters_name.Type2 = e2.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e3 ON Monsters_name.Type3 = e3.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e4 ON Monsters_name.Type4 = e4.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e5 ON Monsters_name.Type5 = e5.Elements_ID WHERE Classes = 2;"
        cursor.execute(flying)
        result = cursor.fetchall()
        for SMD in result:
            print_data = [SMD[0], SMD[1], SMD[2]] 
            for i in range(3, 7):  
                if SMD[i] is not None:
                    print_data.append(SMD[i])
            print("________________________________________________________________")
            print("Monster: ",print_data[0],"\n","Class: ",print_data[1],"\n","Elements Or Status Effect: ",print_data[2:])
        print("________________________________________________________________")
#define a function that can print out all fanged wyverns
def print_all_fanged():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()  
        '''At the query below we will add "WHERE Clsses == 3" at the end of the query to find all fanged wyverns.'''
        fanged = f"SELECT Monsters_name.MonstersNames, Monster_classes.Monster_Classes, e1.Elements_And_Status, e2.Elements_And_Status, e3.Elements_And_Status, e4.Elements_And_Status, e5.Elements_And_Status FROM Monsters_name JOIN Monster_classes ON Monsters_name.Classes = Monster_classes.ID LEFT JOIN Elements_And_Abnormal_Status as e1 ON Monsters_name.Type1 = e1.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e2 ON Monsters_name.Type2 = e2.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e3 ON Monsters_name.Type3 = e3.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e4 ON Monsters_name.Type4 = e4.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e5 ON Monsters_name.Type5 = e5.Elements_ID WHERE Classes = 3;"
        cursor.execute(fanged)
        result = cursor.fetchall()
        for SMD in result:
            print_data = [SMD[0], SMD[1], SMD[2]] 
            for i in range(3, 7):  
                if SMD[i] is not None:
                    print_data.append(SMD[i])
            print("________________________________________________________________")
            print("Monster: ",print_data[0],"\n","Class: ",print_data[1],"\n","Elements Or Status Effect: ",print_data[2:])
        print("________________________________________________________________")
#define a program that can print out all brute wyverns
def print_all_brute():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()    
        '''At the query below we will add "WHERE Classes == 5" at the end of the query to find all brute wyverns'''
        brute = f"SELECT Monsters_name.MonstersNames, Monster_classes.Monster_Classes, e1.Elements_And_Status, e2.Elements_And_Status, e3.Elements_And_Status, e4.Elements_And_Status, e5.Elements_And_Status FROM Monsters_name JOIN Monster_classes ON Monsters_name.Classes = Monster_classes.ID LEFT JOIN Elements_And_Abnormal_Status as e1 ON Monsters_name.Type1 = e1.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e2 ON Monsters_name.Type2 = e2.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e3 ON Monsters_name.Type3 = e3.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e4 ON Monsters_name.Type4 = e4.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e5 ON Monsters_name.Type5 = e5.Elements_ID WHERE Classes = 5;"
        cursor.execute(brute)
        result = cursor.fetchall()
        for SMD in result:
            print_data = [SMD[0], SMD[1], SMD[2]] 
            for i in range(3, 7):  
                if SMD[i] is not None:
                    print_data.append(SMD[i])
            print("________________________________________________________________")
            print("Monster: ",print_data[0],"\n","Class: ",print_data[1],"\n","Elements Or Status Effect: ",print_data[2:])
        print("________________________________________________________________")
#define a function that can print out all piscnie wyverns
def print_all_piscine():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()    
        '''At the query below we will add "WHERE Classes == 6" at the end of the query to find all piscine wyverns'''
        piscine = f"SELECT Monsters_name.MonstersNames, Monster_classes.Monster_Classes, e1.Elements_And_Status, e2.Elements_And_Status, e3.Elements_And_Status, e4.Elements_And_Status, e5.Elements_And_Status FROM Monsters_name JOIN Monster_classes ON Monsters_name.Classes = Monster_classes.ID LEFT JOIN Elements_And_Abnormal_Status as e1 ON Monsters_name.Type1 = e1.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e2 ON Monsters_name.Type2 = e2.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e3 ON Monsters_name.Type3 = e3.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e4 ON Monsters_name.Type4 = e4.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e5 ON Monsters_name.Type5 = e5.Elements_ID WHERE Classes = 6;"
        cursor.execute(piscine)
        result = cursor.fetchall()
        for SMD in result:
            print_data = [SMD[0], SMD[1], SMD[2]] 
            for i in range(3, 7):  
                if SMD[i] is not None:
                    print_data.append(SMD[i])
            print("________________________________________________________________")
            print("Monster: ",print_data[0],"\n","Class: ",print_data[1],"\n","Elements Or Status Effect: ",print_data[2:])
        print("________________________________________________________________")

#define a function that can print out all bird wyverns
def print_all_Bird():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()    
        '''At the query below we will add "WHERE Classes == 7" at the end of the query to find all bird wyverns'''
        bird = f"SELECT Monsters_name.MonstersNames, Monster_classes.Monster_Classes, e1.Elements_And_Status, e2.Elements_And_Status, e3.Elements_And_Status, e4.Elements_And_Status, e5.Elements_And_Status FROM Monsters_name JOIN Monster_classes ON Monsters_name.Classes = Monster_classes.ID LEFT JOIN Elements_And_Abnormal_Status as e1 ON Monsters_name.Type1 = e1.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e2 ON Monsters_name.Type2 = e2.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e3 ON Monsters_name.Type3 = e3.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e4 ON Monsters_name.Type4 = e4.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e5 ON Monsters_name.Type5 = e5.Elements_ID WHERE Classes = 7;"
        cursor.execute(bird)
        result = cursor.fetchall()
        for SMD in result:
            print_data = [SMD[0], SMD[1], SMD[2]] 
            for i in range(3, 7):  
                if SMD[i] is not None:
                    print_data.append(SMD[i])
            print("________________________________________________________________")
            print("Monster: ",print_data[0],"\n","Class: ",print_data[1],"\n","Elements Or Status Effect: ",print_data[2:])
        print("________________________________________________________________")
#define a function that can print out all relicts monster.
def print_all_Relicts():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()    
        '''At the query below we will add "WHERE Classes == 8"at the end of the query to find all Relicts monster'''
        Relicts = f"SELECT Monsters_name.MonstersNames, Monster_classes.Monster_Classes, e1.Elements_And_Status, e2.Elements_And_Status, e3.Elements_And_Status, e4.Elements_And_Status, e5.Elements_And_Status FROM Monsters_name JOIN Monster_classes ON Monsters_name.Classes = Monster_classes.ID LEFT JOIN Elements_And_Abnormal_Status as e1 ON Monsters_name.Type1 = e1.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e2 ON Monsters_name.Type2 = e2.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e3 ON Monsters_name.Type3 = e3.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e4 ON Monsters_name.Type4 = e4.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e5 ON Monsters_name.Type5 = e5.Elements_ID WHERE Classes = 8;"
        cursor.execute(Relicts)
        result = cursor.fetchall()
        for SMD in result:
            print_data = [SMD[0], SMD[1], SMD[2]] 
            for i in range(3, 7):  
                if SMD[i] is not None:
                    print_data.append(SMD[i])
            print("________________________________________________________________")
            print("Monster: ",print_data[0],"\n","Class: ",print_data[1],"\n","Elements Or Status Effect: ",print_data[2:])
        print("________________________________________________________________")

#Define a function that can print all fanged beast  
def print_all_beast():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()    
        '''At the query below we will add "WHERE Classes == 4"at the end of the query to find all fanged beast.'''
        beast = f"SELECT Monsters_name.MonstersNames, Monster_classes.Monster_Classes, e1.Elements_And_Status, e2.Elements_And_Status, e3.Elements_And_Status, e4.Elements_And_Status, e5.Elements_And_Status FROM Monsters_name JOIN Monster_classes ON Monsters_name.Classes = Monster_classes.ID LEFT JOIN Elements_And_Abnormal_Status as e1 ON Monsters_name.Type1 = e1.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e2 ON Monsters_name.Type2 = e2.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e3 ON Monsters_name.Type3 = e3.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e4 ON Monsters_name.Type4 = e4.Elements_ID LEFT JOIN Elements_And_Abnormal_Status as e5 ON Monsters_name.Type5 = e5.Elements_ID WHERE Classes = 4;"
        cursor.execute(beast)
        result = cursor.fetchall()
        for SMD in result:
            print_data = [SMD[0], SMD[1], SMD[2]] 
            for i in range(3, 7):  
                if SMD[i] is not None:
                    print_data.append(SMD[i])
            print("________________________________________________________________")
            print("Monster: ",print_data[0], "\n","Class: ",print_data[1],"\n","Elements Or Status Effect: ",print_data[2:])
        print("________________________________________________________________")


#check if this program was used as main program or not.
if __name__ == "__main__":
    #Verify the user
    #Set Accessbility to True
    Accessbility = True
    #Set Admin username and admin password
    ADMIN_USERNAME = 'OSS'
    ADMIN_PASSWORD = 'BOSS'
    #Limit the tries
    tries = 0
    print("""Type "I don't know" if you don't know the admin username or password.""")
    print(f"You still have {3 -  tries} tries left")
    while True:
        username = input("Please input Admin username.\n")
        password = input("Please input Admin password.\n")
        #Limit the number of tries.
        if tries == 2:
            #Set Accessbility to False if tries = 2
            Accessbility = False
            break
        if username != ADMIN_USERNAME and username.lower() != "i don't know":
            tries += 1
            print('That is not the correct Admin username.')
            print(f"You still have {3 -  tries} tries left")
            print("""Type " I don't know " in both input if you don't know the admin username or password.\n""")
        elif password != ADMIN_PASSWORD and password.lower() != "i don't know":
            tries += 1
            print("That is not the correct Admin password.")
            print(f"You still have {3 - tries} tries left")
            print("""Type " I don't know "  in both input if you don't know the admin username or password.\n""")
            #Ask the user a question if he/she input "I don't know"
        elif username.lower() == "i don't know" or password.lower() == "i don't know":
            #Create a list for the multiple answer for the fact question.
            Special_Access = ["duck", 'duck!', 'little duck!', "ducky!", "ducky", "little ducky!"]
            Identify = input("What can help improve your programming skills?\n")
            #If user input is not in the list created above then the access for this prorgam will be denied
            if Identify.lower() not in Special_Access:
                print("No, you don't have any access for this program")
                #Set Accessbility to False if the user don't know the correct answer.
                Accessbility = False
                break
            else:
                #If user's input is in the list created above" then he/she has the access for this program
                print("Yes, you have the access for this progress.")
                Accessbility = True
                break
        else:
            break
    #Ask for user's input
    if Accessbility == False:
        print("Access Denied")
    if Accessbility == True:
        print("LOGIN SUCCESSFULL\n")
        print("""\nWhat classes of monster you want to look for?\n Input "ALL" for all monster\n Input "Elder" for Elder Dragon\n Input "Flying" for Flying Wyverns\n Input "Fanged" for Fanged Wyverns\n Input "Beast" for Fanged Beast\n Input "Brute" for Brute Wyverns\n Input "Piscine" for Piscine Wyverns\n Input "Bird" for Bird Wyverns\n Input "Relicts" for Relicts\n Input "Stop" to close the program""")
        #Keep asking for input from user
        while True:
                Q = input("\nSelect the classes:\n")
                #run different defined function depends on user input.
                #Use .lower() function to prevents user input some capital letter.
                if Q.lower()  == 'all':
                    print_all_monsters()
                elif Q.lower() == 'elder':
                    print_all_elder()
                elif Q.lower() == 'flying':
                    print_all_flying()
                elif Q.lower() == 'fanged':
                    print_all_fanged()
                elif Q.lower() == 'beast': 
                    print_all_beast()
                elif Q.lower() == 'brute':
                    print_all_brute()
                elif Q.lower() == 'piscine':
                    print_all_piscine()
                elif Q.lower() == 'bird':
                    print_all_Bird()
                elif Q.lower() == 'relicts':
                    print_all_Relicts()
                elif Q.lower() == 'stop':
                    break
                else:
                    print("Please follow the instruction below:\n")
                    print("""What classes of monster you want to look for?\n Input "ALL" for all monster\n Input "Elder" for Elder Dragon\n Input "Flying" for Flying Wyverns\n Input "Fanged" for Fanged Wyverns\n Input "Beast" for Fanged Beast\n Input "Brute" for Brute Wyverns\n Input "Piscine" for Piscine Wyverns\n Input "Bird" for Bird Wyverns\n Input "Relicts" for Relicts\n Input "Stop" to close the program""")