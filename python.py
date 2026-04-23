# GUEESING GAME
# counter=1
# num=8
# while counter<=3:
#     guess=int(input("Guess the number: "))
#     if guess == num:
#         print("Congratulations! You guessed the number.")
#         break
#     counter+=1
#     if guess != num:
#         print("Try again.")


# CAR GAME
# is_started = False
# status = ""
# while True:
#     message=input("Enter a message: ").lower()
#     if message == "start":
#         if is_started:
#             print("Machine is already running.")
#         else:
#             print("Machine started.")
#             is_started = True
#             status = "running"
#     elif message == "stop":
#         if not is_started:
#             print("Machine is already stopped.")
#         else:
#             print("Machine stopped.")
#             is_started = False
#             status = "stopped"
#     elif message == "help":
#         print("Available commands: Start, Stop, Exit, Help, Status")
#     elif message == "status":
#         if status == "running":
#             print("Machine is running.")
#         elif status == "stopped":
#             print("Machine is stopped.")
#         else:
#             print("Machine status unknown.")
#     elif message == "exit":
#         print("Exiting the program.")
#         break

#     else:
#         print("Invalid command.")