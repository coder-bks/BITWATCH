from pathlib import Path
import os


def checking(data):

    os.makedirs("data", exist_ok=True)
    file_to_open = Path("data/last_price.txt")
    
    try:
        with open(file_to_open, "r",encoding="utf-8") as f:
            content=f.read()
            # print("File exists")

        if content == "":
            with open(file_to_open, "w",encoding="utf-8") as f:
             f.write(f"{data}")
            return False
        else:
            if data != content:
                with open(file_to_open, "w",encoding="utf-8") as f:
                 f.write(f'{data}')
                return True     
            else:
                return False
    

    except FileNotFoundError:
        with open(file_to_open, "w",encoding="utf-8") as f:
            f.write(f'{data}')
        return False

