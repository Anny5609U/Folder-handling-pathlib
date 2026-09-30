from pathlib import Path 

def readfileandfolder():
    path = Path('') #is the current directory
    items= list(path.rglob("*"))
    for i, item in enumerate(items):
        print(f"{i + 1}: {item.name}") #if i write same name then windowspath thing comes (item is different from, items )
    return items

def createfolder(): #what if i dont want to create a new folder rather just a file inside an existing folder? (done)
    try:
        readfileandfolder()
        name =input("tell us the name of the folder you want to create")
        p = Path(name)
        if not p.exists():
            p.mkdir(parents = True)
            print(f"folder '{name}' created succuesfully")
        else:
            print("folder already exist")

        add_file = input("do you want to add file in this folder ? Yes/No") # why this new file is being created seprately and not inside the folder (solved, bcz i was using file_path rather than)
        if add_file == "yes" or add_file == "Yes":
            filename= input("name your file:- ")
            file_path = p/ filename #here p is folder and filename is file created by the user, this is done bcz the  file needs to be generated inside the folder and not outside it. 
            data = input("enter file content: ")
            file_path.write_text(data) #⭐ here i wrote p.write_text as this is correct 
            print(f"file'{filename}' created inside '{name}")
        elif add_file == "no" or add_file == "No":
            print("folder successfully created")

    except Exception as err:
        print(f"An error has occured as {err}")

def readfolder():
    try:
        path = Path('')
        item = list(path.rglob("*"))
        #list name and loop name should be different otherwise windowspath error occurs

        
        for i, path_item in enumerate(item, start = 1):
                print(i , path_item) #displaying the list
        
        number= int(input("which folder do you want to read?"))
        p = item[number - 1] #this is the folder

            
        if p.is_dir():
            folder_items = list(p.iterdir()) #accessing the folder
        else:
            print("this is not a folder")
            return 

        for i, item in enumerate(folder_items, start=1):
                print(i, item) #accessing the folder items

        if not folder_items :#to check whether a file exists is folder to read
            print("no file exist in folder to read")
            return

        access= int(input("which file do you want to read?"))
        selected_file = folder_items[access - 1] #accessing the file from folder items, with index 1, here we defined what selected_file is and so we can also use it later

        
        with open(selected_file, 'r') as fs: #opening and reading the file
                    data= fs.read()
                    print(data)
        
    
    except Exception as err:
        print(f"An error has occured as {err}")




def updatefolder(): #check why the updatefolder is not working(solved)
    try:
        folders = readfileandfolder() #i just changed line 78, 80 & 81 to solve int not accepting issue. and also the duplication folder problem 
        number= int(input("which folder do you want to update"))#what if i dont want to write whole foldername rather the number --add this
        folder_name = folders[number -1 ]
        p = Path(folder_name)

        if p.exists():
            print("press 1 to rename folder")
            print("press 2 for appending something in your files")


            res = int(input("tell your response:-"))
            if res== 1: #this is working fine
                name2 = input("new name of the folder") #why does this create a duplicate folder with the changed name and now change the name of that folder only (solved)?
                p2= Path(name2) 
                p.rename(p2)
                print("Folder name updated succuessfully")

            # elif res == 2:
            #     filename = input("tell the file name:- ")
            #     file_path= Path(name)/ filename
            #     data= input("enter file content")
            #     file_path.write_text(data) # ⭐path does not have(.write) feature so add (_text) after this to make this work
            #     print(f"file '{filename}' created successfully ")

            elif res == 2: #new concept, i was making a mistake which led to creation of new file automaticallyin folder to append add the appending part even if file existed and not bring in changesin the file
                folder_items = [item for item in p.iterdir() if item.is_file()] #correct version where it excludes sub folders and focus on files only 

                if not folder_items:
                    print("no files in this folder to append to.")
                    return

                for i, items in enumerate(folder_items, start = 1):
                    print(f"{i}: {items.name}") #item.name prints only the name with no extention

                filenum =int(input("which file you wanna edit")) #try adding file names of that folder and this also creates a new file by default
                selected_file = folder_items[filenum-1] 
                
                data = input("what do you wanna add")
                with open(selected_file, 'a') as fs:
                    fs.write(data + "\n")
                    print("data added successfully")


        

    except Exception as err:
        print(f"An error has occured as {err}")    


def deletefolder():
    try: 
        readfileandfolder()
        path = Path('')
        item = list(path.rglob("*"))

        for i, path_item in enumerate (item , start =1 ):
            print(i, path_item)


        number= int(input("which folder do you want to delete (index of the folder)"))
        p = item[number -1]

            
        if p.is_dir():
            folder_items = list(p.iterdir())
        else:
            print("this is not a folder")
            return 

        for i, item in enumerate(folder_items, start =1):
            print(i,item)
            
        if not folder_items :#to check whether a file exists is folder to delete
            print("no file exist in folder to delete")
            return    
    

        del_file= int(input("which file do you want to delete"))
        selected_file = folder_items[del_file -1]

       

        confirm= input(f"are you sure you want to delete{selected_file}? (yes/no):")
        if confirm.lower () in ("yes" , "y"):
            selected_file.unlink()
            print("file deleted successfully")
        else:
            print("deletion cancelled")
    except Exception as err: 
        print(f"An error has occured as {err}")


def createfile():
    try:
        path = Path('') #a folder
        items= list(path.rglob("*"))
        # readfolder(p.is_dir())
        
        for i,path_item in enumerate(items, start = 1):
            print(i, path_item)
        #from 140 - 145 - we have displayed the list for user to choose a folder in which he wants to add the new file
        
        num = int(input("in which folder you want to create a file in(select folder only not file)"))
        path = items[num -1]

        if not path.is_dir():
            print("this is not a folder, please pick a folder")
            return

        filename= input("name your file:- ")
        file_path = path/ filename 
        data = input("what do you wanna add in the file")
        file_path.write_text(data) #here i earlier wrote path instead of file_path which was creating a prob as path was the folder, and file_path is the file
        print("file successfully created")
    
        

    except Exception as err:
        print(f"An error has occured as {err}")


if __name__ == "__main__":  # menu code here #menu code is a guard line, as it protects menu code from running when it should'nt
    print("press 1 for creating a folder")
    print("press 2 for reading a folder")
    print("press 3 for updating a folder")
    print("press 4 for deleting a folder")
    print("press 5 for creating a file in a already exisiting folder")

    check = int(input("please tell your response"))

    if check == 1:
        createfolder()

    elif check == 2:
        readfolder()

    elif check == 3:
        updatefolder()

    elif check == 4:
        deletefolder()

    elif check == 5:
        createfile()
    else:
        print("invalid choice, please pick a number from 1-5")

   


# folder_path.write_text(data)   # "I'm writing to the folder" — wrong, you can hear it
# file_path.write_text(data)     # "I'm writing to the file" — right
