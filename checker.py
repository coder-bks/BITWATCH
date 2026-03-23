from pathlib import Path
from scraper import data
def checking(data):

    relative_folder_path = Path("../stock alert/data") 
    file_to_open = relative_folder_path / "last_price.txt"
    
    try:
        with open(file_to_open, "r") as f:
            content=f.read()
            print("File exists")

        if content == "":
            with open(file_to_open, "w") as f:
             f.write(f"{data}")
            return False
        else:
            if data != content:
                with open(file_to_open, "w") as f:
                 f.write(f'{data}')
                return True     
            else:
                print("same data")
                return False
    

    except FileNotFoundError:
        with open(file_to_open, "w") as f:
            f.write(f'{data}')
        return False

check=checking(data)
