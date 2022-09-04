command = ""
started = False
while True:
    command = input('> ').lower()
    if command == "help":
        print(''' 
    start = start the car
    stop = stop the car
    quit = exit the game''')
    elif command == "start":
        if started:
            print('the car is already started!')
        else:
            started = True
            print('the car has started')
    elif command == "stop":
        if not started:
            print('the car is already stopped')
        else:
            started = False
            print('the car is stopped')
    elif command == "quit":
        break
    else:
        print('i dont understand')
