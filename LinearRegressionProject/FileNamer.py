class SetFileName:
    global extension
    global fileName

    @staticmethod
    def getExtension():
        return extension

    @staticmethod
    def getFileName():
        return fileName

    @staticmethod
    def fileNamer():
        global fileName
        global extension
        fileName = input("Enter .csv File Name: ")

        if ".csv" == fileName[len(fileName) - 4:len(fileName)]:  # Removes .txt extension if user adds it
            fileName = fileName[0:len(fileName) - 4]
            extension = '.csv'
        else:
            extension = input("Is your file a .csv file? (Y/N)")
            if extension.lower() == 'n':
                print("Only .csv files are currently supported. Please try again.")
                quit()
            elif extension.lower() != 'y':
                print("Invalid input. Punishment: You have to redo the process because I'm currently on a plane, and"
                      " I'm waaaaay too tired to add a simple loop...")

        try:
            test = open(fileName + ".csv")
            test.close()
        except FileNotFoundError:
            print("File not found. Make sure that the File is in the same folder as this program.")
            fileNamer()
