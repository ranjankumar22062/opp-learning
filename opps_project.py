class chatbook:
    def __init__(self):
        self.username =''
        self.password =''
        self.loggedin =False
        self.menu()

    def menu(self):
        user_input = input("""welcome to chatbook !! how would you like to proced?
                           1.press 1 to signup
                           2.press 2 to signin
                           3.press 3 to write a post
                           4.press 4 to message a friend
                           5.press any other key to exit
                           
                           """)
        if user_input =="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.my_post()
        elif user_input=="4":
            self.sendmsg()
        else:
            exit()
    def signup(self):
        email =input("enter your email address")
        pwd=input("setup your password")
        self.username=email
        self.password=pwd
        print("you have signup sucessfully")
        print("\n")
        self.menu()
    def signin(self):
        if self.username=='' and  self.password=='':
            print("please signup first by pressing 1 ")
        else:
            uname= input("enter your email/username here")
            pwd= input("Enter your password")
            if self.username==uname and self.password==pwd:
                print("you have sucessfully signin")
                self.loggedin=True
                
            else:
                print("please give correct crendentials")
            print("\n")
            self.menu()        
    def my_post(self):
        if self.loggedin==True:
            txt=input("enter your message here")
            print(f"following content has been posted -> {txt}")
        else:
            print("you need to signin first to post something")
        print("\n")
        self.menu()

    def sendmsg(self):
        if self.loggedin==True:
            txt =input("enter your message here -->")
            frnd=input ("whom to send -->")
            print(f"Your message has been sent to {frnd}")
        else:
            print("you need to signin first to post something ...")
        print("\n")
        self.menu()            


            


    
obj=chatbook()
