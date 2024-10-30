
import mysql.connector as mysql


db = mysql.connect(host="localhost",user ="root",password="",database="college")

command_handler = db.cursor(buffered=True)
#If we use AES cipher we can't use the program correctly, we couldn't fix the problem that mysql is not compatible with our python project. We cant Decypher the ciphered text in mysql. Although, we can cypher the text with
#AES_ENCRYPT(word,key) but we can't access the ciphered text with AES_DECRYPT(word,key) in MYSQL.

def chair_session():
     while 1:
        print("")
        print("Chair's Menu")
        print("1. View register ")
        print("2. Logout")

        user_option = input(str("Option : "))
        if user_option == "1":
            print("")
            print("Viewing all student registers")
            command_handler.execute("SELECT username, date, status FROM attendance")
            records = command_handler.fetchall()
            print("Displaying all registers")   
            for record in records :
                print(record)
        elif user_option == "3":
            break
        else:
            print("No valid Options")

def parent_session(name):
     while 1:
        print("")
        print("Parent's Menu")
        print("1. View student ")
        print("2. Logout")
        name1 = (name,)
        command_handler.execute("SELECT child FROM parents WHERE username = %s ",name1)
        child = command_handler.fetchall() 
        user_option = input(str("Option : "))
        if user_option == "1":
            print("")
            print("Viewing student register")
            command_handler.execute("SELECT username, date, status FROM attendance WHERE username = %s",child[0])
            records = command_handler.fetchall()
            print(f"Displaying all registers for student : "+ str(child[0]))
            for record in records :
                print(record)
        elif user_option == "2":
            break
        else:
            print("No valid Options")
#aes_encryption(%s, 'TJJASK23433') , aes_decryption(%s,'TJJASK23433')
def teacher_session():
     while 1:
        print("")
        print("Teacher's Menu")
        print("1. Mark student register ")
        print("2. View register ")
        print("3. Logout")

        user_option = input(str("Option : "))
        if user_option == "1":
            print("")
            print("Mark student register")
            command_handler.execute("SELECT username FROM users WHERE privilege = 'student'")
            records = command_handler.fetchall()
            date = input(str("Date : DD/MM/YYYY : "))
            for record in records :
                record = str(record).replace("'","")
                record = str(record).replace(",","")
                record = str(record).replace("(","")
                record = str(record).replace(")","")
                #Presen | Absent | Late
                status = input(str("Status for  " + str(record) + "P/A/L : "))
                query_vals = (str(record),date,status)
                command_handler.execute("INSERT INTO attendance (username, date, status) VALUES(%s,%s,%s)",query_vals)
                db.commit()
                print(record + "Marked as " + status)
        elif user_option == "2" :
            print("")
            print("Viewing all student registers")
            command_handler.execute("SELECT username, date, status FROM attendance")
            records = command_handler.fetchall()
            print("Displaying all registers")
            for record in records :
                print(record)
        elif user_option == "3":
            break
        else:
            print("No valid Options")

def student_session(username):
    while 1:
        print("")
        print("1. View Register")
        print("2. Download Register")
        print("3. Logout")

        user_option = input(str("Option : "))
        if user_option == "1":
            username = (str(username),)
            command_handler.execute("SELECT date, username, status FROM attendance WHERE username = %s ",username)
            records = command_handler.fetchall()
            for record in records:
                print(record)
        elif user_option == "2":
            print("Downloading Register")
            username = (str(username))
            command_handler.execute("SELECT date, username, status FROM attendance WHERE username = %s ",username)
            records = command_handler.fecthall()
            for record in records:
                with open("C:/sseess/register.txt","w") as f:
                    f.write(str(records)+"\n")
                f.close()
            print("All records Saved.")
        elif user_option == "3":
            break
        else:
            print("No valid option was selected.")

def chair_session():
     while 1:
        print("")
        print("Chair's Menu")
        print("1. View register ")
        print("2. Logout")

        user_option = input(str("Option : "))
        if user_option == "1":
            print("")
            print("Viewing all student registers")
            command_handler.execute("SELECT username, date, status FROM attendance")
            records = command_handler.fetchall()
            print("Displaying all registers")   
            for record in records :
                print(record)
        elif user_option == "2":
            break
        else:
            print("No valid Options")


def admin_session():
    while 1:
        print("")
        print("Admin Menu")
        print("1. Register new Student ")
        print("2. Register new Teacher ")
        print("3. Register new Chair ")
        print("4. Register new Parent ")
        print("5. Delete Existing Student")
        print("6. Delete Existing Teacher")
        print("7. Delete Existing Chair ")
        print("8. Delete Existing Parent")
        print("9. Logout")

        user_option = input(str("Option : "))
        if user_option=="1":
            print("")
            print("Register New Student")
            username = input(str("Student username: "))
            password = input(str("Student password: "))
            groups = input(str("Student group: "))
            query_vals = (username,password,groups)
            command_handler.execute("INSERT INTO users (username,password,privilege,groups) VALUES (%s,%s,'student',%s)",query_vals)
            db.commit()
            print(username + " has been registered as a student")
        elif user_option=="2":
            print("")
            print("Register New Teacher")
            username = input(str("Teacher username: "))
            password = input(str("Teacher password: "))
            groups = input(str("Student group: "))
            query_vals = (username,password,groups)
            command_handler.execute("INSERT INTO users (username,password,privilege,groups) VALUES (%s,%s,'teacher',%s)",query_vals)
            db.commit()
            print(username + " has been registered as a Teacher")
        elif user_option=="3":
            print("")
            print("Register New Chair")
            username = input(str("Chair username: "))
            password = input(str("Chair password: "))
            query_vals = (username,password)
            command_handler.execute("INSERT INTO users (username,password,privilege) VALUES (%s,%s,'chair')",query_vals)
            db.commit()
            print(username + " has been registered as a Chair")
        elif user_option=="4":
            print("")
            print("Register New Parent")
            username = input(str("Parent username: "))
            password = input(str("Parent password: "))
            childo = input(str("Child name : "))
            query_vals = (username, password,childo)
            command_handler.execute("INSERT INTO parents (username,password,child) VALUES (%s,%s,%s)",query_vals)
            db.commit()
            print(username + " has been registered as a Parent")   
        elif user_option=="5":
            print("")
            print("Delete Existing Student Account")
            username = input(str("Student username: "))
            query_vals=(username,"student")
            var = command_handler.execute("SELECT username FROM users")
            command_handler.execute("Delete FROM users WHERE username = %s AND privilege = %s ",query_vals)                        
            db.commit()
            if command_handler.rowcount < 1:
                print("User not found")
            else:
                print(username+"has been deleted")    
        elif user_option=="6":
            print("")
            print("Delete Existing Teacher Account")
            username = input(str("Teacher username: "))
            query_vals=(username,"teacher")
            command_handler.execute("Delete FROM users WHERE username = %s AND privilege = %s ",query_vals)     
            db.commit()
            if command_handler.rowcount < 1:
                print("User not found")
            else:
                print(username+"has been deleted")   
        elif user_option=="7":
            print("")
            print("Delete Existing Chair Account")
            username = input(str("Chair username: "))
            query_vals=(username,"chair")
            command_handler.execute("Delete FROM users WHERE username = %s AND privilege = %s ",query_vals)                        
            db.commit()
            if command_handler.rowcount < 1:
                print("User not found")
            else:
                print(username+" has been deleted")       
        elif user_option=="8":
            print("")
            print("Delete Existing Parent Account")
            username = input(str("Parent username: "))
            childo = input(str("Child username: "))
            query_vals=(username,childo)
            command_handler.execute("Delete FROM parents WHERE username = %s AND child = %s ",query_vals)                        
            db.commit()
            if command_handler.rowcount < 1:
                print("User not found")
            else:
                print(username+" has been deleted") 
        elif user_option == "9":
            print("")
            print("Viewing all student registers")
            command_handler.execute("SELECT username, date, status FROM attendance")
            records = command_handler.fetchall()
            print("Displaying all registers")   
            for record in records :
                print(record)    
        elif user_option =="10":
            break
        else:
            print("No valid option selected")
            
def auth_student():
    print("")
    print("Student's Login")
    print("")
    username = input(str("Username : "))
    password = input(str("Password : "))
    query_vals = (username, password, "student")
    command_handler.execute("SELECT username FROM users WHERE username = %s AND password = %s AND privilege = %s", query_vals)
    if command_handler.rowcount <= 0:
        print("Invalid Login Details")
    else:
        student_session(username)

def auth_parent():
    print("")
    print("Parent's Login")
    print("")
    username = input(str("Username : "))
    password = input(str("Password : "))
    query_vals = (username, password)
    command_handler.execute("SELECT username FROM parents WHERE username = %s AND password = %s" , query_vals)
    if command_handler.rowcount <= 0:
        print("Invalid Login Details")
    else:
        parent_session(username)        

def auth_chair(): 
    print("")
    print("Chair's Login")
    print("")
    username = input(str("Username :"))
    password = input(str("Password :"))
    query_vals = (username, password)
    command_handler.execute("SELECT * FROM users WHERE username = %s AND password = %s AND privilege = 'chair'",query_vals)       
    if command_handler.rowcount <= 0 :
        print("Login not recognized")
    else:
        chair_session()

def auth_teacher(): 
    print("")
    print("Teacher's Login")
    print("")
    username = input(str("Username :"))
    password = input(str("Password :"))
    query_vals = (username, password)
    command_handler.execute("SELECT * FROM users WHERE username = %s AND password = %s AND privilege = 'teacher'",query_vals)       
    if command_handler.rowcount <= 0 :
        print("Login not recognized")
    else:
        teacher_session()

def auth_admin():
    print("")
    print("Admin Login")
    print("")
    username = input(str("Username: "))
    password = input(str("Password: "))
    if username == "admin":
        if password =="password":
            admin_session()
        else:
            print("Incorrect password !")
    else:
            print("Login details not recognised")   
            
def auth_chair(): 
    print("")
    print("Chair's Login")
    print("")
    username = input(str("Username :"))
    password = input(str("Password :"))
    query_vals = (username, password)
    command_handler.execute("SELECT * FROM users WHERE username = %s AND password = %s AND privilege = 'chair'",query_vals)       
    if command_handler.rowcount <= 0 :
        print("Login not recognized")
    else:
        chair_session()
        
def main():
    while 1:
        print("Welcome to the college system")
        print("")
        print("1. Login as a student")
        print("2. Login as a teacher")
        print("3. Login as a chair")
        print("4. Login as a parent")
        print("5. Login as a admin")
        
        user_option = input(str("Option : "))
        
        if user_option == "1":
            auth_student()
        elif user_option == "2":
            auth_teacher()
        elif user_option=="3":
            auth_chair()
        elif user_option=="4":
            auth_parent()
        elif user_option=="5":
            auth_admin()

        else:
            print("No valid option was selected")
main()