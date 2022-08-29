from RecipeRunner import runRecpieProgram

if __name__=="__main__":
    runnerObj = runRecpieProgram({"pizza": ["pizza base", "tomato sauce", "pepperoni"]},{
            "pizza": ["Step 1: Flatten Pizza Base", "Step 2: Add Tomato Sauce", "Step 3: Add Pepperoni",
                      "Step 4: Cook at gas mark 5 for 30 mins"]})
    runnerObj.menu()