command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True            
            print("car is starting...")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("car is stopping")
    elif command == "help":
        print("""
    start - car is starting
    stop - car is stopping
    quit - end the game
              """)  
    elif command == "quit":
     break
    else:
        print("sorry i don't understand that...")         