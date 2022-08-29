
class recipe():
    def __init__(self,recipeDict,recipeInstructDict):
        self.recipeDict = recipeDict
        self.recipeInstructDict = recipeInstructDict

    def addRecipe(self, recipeName, ingredientsList, instructions):
        self.recipeDict[recipeName] = ingredientsList
        self.recipeInstructDict = instructions

    def outputRecipe(self, recipeName):
        if recipeName.lower() in self.recipeDict.keys():
            print(f"To make {recipeName.lower()}, you need the following ingredients:")
            for eachIngred in self.recipeDict[recipeName.lower()]:
                print(f"- {eachIngred}")
            for eachInstruct in self.recipeInstructDict[recipeName.lower()]:
                print(eachInstruct)
        else:
            print("Invalid Recipe")

    def runRecipe(self):
        userInp = str(input("Please enter the Recipe you want to make >: "))
        print("\n")
        self.outputRecipe(userInp.lower())

    def suggestRecipe(self, ingredientsList):
        self.total = 0
        self.outputListRec = []
        for key, eachRecipe in self.recipeDict.items():
            for eachIngred in ingredientsList:
                if eachIngred in eachRecipe:
                    self.total += 1
            if self.total == len(eachRecipe):
                self.outputListRec.append(key)

        return self.outputListRec

