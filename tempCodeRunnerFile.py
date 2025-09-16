from pathlib import Path

def readfileandfolder():
    path=Path('')
    items=list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")

def createfile():
    try:
        readfileandfolder()
        name=input("please tell your file name:- ")
        p=Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data=input("what you want to write in this file:- ")
                fs.write(data)

            print(F"File Created Successfully")
        else:
            print("this file is already exists..")        
    except Exception as err:
        print(f"An error occured as {err}")



print("press 1 for creating a file")
print("press 2 for reading file")
print("press 3 for updating a file")
print("press 4 for deletion a file")

check=int(input("Please tell your response:- "))

if check==1:
    createfile()
