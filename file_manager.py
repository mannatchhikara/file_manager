def func():
    user_input=input('enter filename: ')
    try:
        with open(user_input):
            pass
        print("""For Reading:- r
        For Re-Writing- w
        For Adding- a""")
        mode=input("What you want to do:- ")
        with open(user_input,mode) as f:
            if mode=="r":
                print(f.read())
            elif mode=="w":
                f.write(input("What to re-write:- "))
            elif mode=="a":
                f.write(input("What to add:- "))
            else:
                print("Enter valid thing to do!!")
    except FileNotFoundError:
        print('File doesnt found. Pls enter correct file name')
        func()
    except Exception as e:
        print('Enter valid filename')
        func()
func()
