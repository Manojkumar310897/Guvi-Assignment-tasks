def register():
    db = open("hello.txt", "r")
    Email_username=input("create a username:")
    def check(Email_username):
     import re
     regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' 
     if(re.fullmatch(regex, Email_username)):
         print("Valid Email_username")
     else:
         print("Invalid Email_username")
         register()
    check(Email_username)
    d = []
    f = []
    for i in db:
               a,b= i.split(",") 
               b = b.strip()
               c = a,b
               d.append(a)
               f.append(b)
               data = dict(zip(d, f))
    #print(data)
    if Email_username in d:
        print("user name already exists")
        return(register())
    
    password=input('Enter ur password:') 
    #Password check
    import re
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,16}$"
    pat = re.compile(reg)
    mat = re.search(pat, password)
    if mat:
      print('valid password')
    else:
      print("""Password must contain minimum 
              one special character 
              one digitone uppercase 
              one lowercase character
              and must be of 5 to 16 characters""")
      access()
    db = open("hello.txt", "a")
    db.write(Email_username+", "+str(password)+"\n")
    print("User created successfully!")  
 
    
def login():
    Email_username=input("Enter username:")
    password=input("Enter ur password")
    db = open("hello.txt", "r")
    d = []
    f = []
    for i in db:
               a,b = i.split(",")
               b = b.strip()
               c = a,b
               d.append(a)
               f.append(b)
               data = dict(zip(d, f))
    if  password in f:
        print("you are logged in successfully")
    if Email_username in d:
        print("you are logged in successfully")
    else:
         print('wrong password or username not available go to registration or signup')
         access()
     
def forgot_password():
    Email_username=input(" Enter ur username:")
    db = open("hello.txt", "r")
    d = []
    f = []
    for i in db:
               a,b = i.split(",")
               b = b.strip()
               c = a,b
               d.append(a)
               f.append(b)
               data = dict(zip(d, f))
    if Email_username in d:
        print('Provide a new password')
        New_password=input('Enter ur New password:')
        import re
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,16}$"
        pat = re.compile(reg)
        mat = re.search(pat, New_password)
        if mat:
          print('valid password')
          print('New passowrd created now You can login')
        else:
          print("""Password must contain minimum 
                  one special character 
                  one digitone uppercase 
                  one lowercase character
                  and must be of 5 to 16 characters""")
        forgot_password()
    else:
       if Email_username not in d:
           print('username not available go to registration')
           access()
        
    db = open("hello.txt", "a")
    db.write(Email_username+", "+str(New_password)+"\n")
         
def access():
    while(1):
        print("1.signup\n2.login\n3.forgot password")
        option=int(input())
        if option==1:
            register()
            break
        if option==2:
            login()
            break
        if option==3:
            forgot_password()
            break
        else:
            print("Enter the correct option")
access()
     
         
 
        
 
    
   
    
