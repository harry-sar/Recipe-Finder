from recipe import recipe

class runRecpieProgram(recipe):

    def __init__(self,recipeDict,recipeInstructDict):
        super().__init__(recipeDict,recipeInstructDict)
        self.ingredInputList = []
        self.flag = True

    def menu(self):
        while self.flag:
            print(
                "-----------------------------------------\nWelcome to The Recipe Creator 1.0\n-----------------------------------------")
            print(
                "-Please select what you want to do-\n\n1. Enter Ingredients to suggest Recipe\n2. Enter Recipe to view Instructions\n3. Enter Time Restraint to find Recipe\n4. Quit")
            try:
                uChoice = int(input(">: "))
                if uChoice in [1, 2, 3, 4]:
                    if uChoice == 1:
                        amount = int(input("Enter Amount of ingredients you have >: "))
                        for x in range(0, amount):
                            inInput = str(input(f"Enter Ingredient {x + 1} >: "))
                            self.ingredInputList.append(inInput.lower())
                        if len(self.suggestRecipe(self.ingredInputList))!=0:
                            print("You can make the following Recipes:")
                            for eachR in self.suggestRecipe(self.ingredInputList):
                                print(eachR)
                        else:
                            print("You can't make any Recipes")
                        self.flag = False
                        break
                    elif uChoice == 2:
                        self.runRecipe()
                        self.flag=False
                        break
                    elif uChoice == 3:
                        print("[WIP]")
                        exit(0)
                    elif uChoice == 4:
                        self.flag=False
                        exit(0)
                else:
                    print("Invalid Input")
            except:
                if self.flag!=False:
                    print("Invalid Input")
