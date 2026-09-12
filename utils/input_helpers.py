from re import search
def ask_for_choice(prompt: str, minimum: int, maximum: int) -> int:
    while True:
       try :
        choice = int(input(prompt))
        if choice in range(minimum,maximum +1):
           return choice
        else:
           print("Enter an integer in the correct range")
       except ValueError:
          print("Enter a valid integer")

def ask_for_integer(prompt: str) -> int:
    while True:
       try :
        integer = int(input(prompt))
        return integer
       except ValueError:
          print("Enter a valid integer")

def ask_for_text(prompt: str) -> str:
    while True:
        text = input(prompt)
        if text.strip() != "":
            return text.strip()
        else:
             print("Text cannot be empty")

def ask_for_email(prompt: str) -> str:
    while True :
        email = ask_for_text(prompt)
        is_email = search(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", email)
        if is_email:
            return email
        else:
            print("Enter a valid email")