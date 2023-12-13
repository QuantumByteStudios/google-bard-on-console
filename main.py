import utils
import bard as b
from datetime import datetime

utils.clear_screen()

while True:

    utils.print_header()

    user_prompt = input(f"{utils.colors.CYAN}Enter a prompt: {utils.colors.END}")

    if user_prompt == "exit()":
        break

    utils.clear_screen()
    print(f"\nYou  : {utils.colors.BOLD}{user_prompt}{utils.colors.END}")
    response = b.askBard(user_prompt)
    if response == "" or response == None:
        print(f"Bard : {utils.colors.RED}No response{utils.colors.END}")
    else:
        print(f"Bard : {utils.colors.GREEN}Response: {utils.colors.END}\n{utils.colors.BLUE}{b.askBard(user_prompt)}{utils.colors.END}")
    print(f"\n{utils.colors.END}")

    action = input("Type 'save()' to save this conversation. Press enter to continue. If you want to exit, type 'exit()': ")
    if action == "save()":
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H-%M")
        file_name = "conversations/Google Bard On Console - Conversation " + str(formatted_datetime) + ".txt"
        file = open(file_name, "a")
        file.write("  Google Bard On Console - Conversation " + str(formatted_datetime) + "\n\n")
        file.write("  You : " + user_prompt + "\n")
        file.write("  Bard: Response:\n\n" + response + "\n\n")
        file.write("  - https://github.com/QuantumByteStudios/google-bard-on-console" + "\n")
        file.close()
    if action == "exit()":
        break

    utils.clear_screen()


# Google Bard Console
