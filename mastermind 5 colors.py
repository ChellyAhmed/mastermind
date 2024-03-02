from logic import *
import random

#create a class "Chelly'sOr" that inherits from Or, which is just an improved
#version of Or since the predefined Or class does not have an add method
class ChellysOr(Or):
    #Extend the Or class by the add method
    def add(self, disjunct): 
        Sentence.validate(disjunct)
        self.disjuncts.append(disjunct)


# Create an empty set of tuples and name it guesses:
guesses = set()

def createRandomCombination():
    global guesses
    colors = ["red", "blue", "green", "yellow", "white"]
    combination = []
    for i in range(len(colors)):
        color = random.choice(colors)
        colors.remove(color)
        combination.append(color)
    combination_tuple = tuple(combination)  # Convert list to tuple
    if combination_tuple not in guesses:
        guesses.add(combination_tuple)
        return combination
    else:
        return createRandomCombination()

colors = ["red", "blue", "green", "yellow", "black"]
correctGuess = [""] * len(colors)
symbols = []
for i in range(len(colors)):
    for color in colors:
        symbols.append(Symbol(f"{color}{i}"))

knowledge = And()

# Each color has a position.
for color in colors:
    knowledge.add(Or(
        Symbol(f"{color}0"),
        Symbol(f"{color}1"),
        Symbol(f"{color}2"),
        Symbol(f"{color}3"),
        Symbol(f"{color}4"),
    ))

# Only one position per color.
for color in colors:
    for i in range(len(colors)):
        for j in range(len(colors)):
            if i != j:
                knowledge.add(Implication(
                    Symbol(f"{color}{i}"), Not(Symbol(f"{color}{j}"))
                ))

# Only one color per position.
for i in range(len(colors)):
    for c1 in colors:
        for c2 in colors:
            if c1 != c2:
                knowledge.add(Implication(
                    Symbol(f"{c1}{i}"), Not(Symbol(f"{c2}{i}"))
                ))

correctPositions = 0
while correctPositions<len(colors) :
    guess = createRandomCombination()
    print(guess)
    correctPositions = int(input("How many correct positions? "))
    if (correctPositions == 0):
        for i in range(len(colors)):
            knowledge.add(Not(Symbol(f"{guess[i]}{i}")))

    elif (correctPositions == len(colors)):
        for i in range(len(colors)):
            knowledge.add(Symbol(f"{guess[i]}{i}"))

    elif (correctPositions == 1): #A more general, but fun way to handle this case
        orredConditinos = ChellysOr()
        for iCorrect in range(len(colors)):
            andedConditions = And(Symbol(f"{guess[iCorrect]}{iCorrect}"))
            for iIncorrect in range(len(colors)):
                if iCorrect != iIncorrect:
                    andedConditions.add(Not(Symbol(f"{guess[iIncorrect]}{iIncorrect}")))
            orredConditinos.add(andedConditions)
        knowledge.add(orredConditinos)
           
    elif (correctPositions == 2):
        knowledge.add(Or(   
            And(Symbol(f"{guess[0]}0"), Symbol(f"{guess[1]}1"), Not(Symbol(f"{guess[2]}2")), Not(Symbol(f"{guess[3]}3")), Not(Symbol(f"{guess[4]}4"))),
            And(Symbol(f"{guess[0]}0"), Not(Symbol(f"{guess[1]}1")), Symbol(f"{guess[2]}2"), Not(Symbol(f"{guess[3]}3")), Not(Symbol(f"{guess[4]}4"))),
            And(Symbol(f"{guess[0]}0"), Not(Symbol(f"{guess[1]}1")), Not(Symbol(f"{guess[2]}2")), Symbol(f"{guess[3]}3"), Not(Symbol(f"{guess[4]}4"))),
            And(Symbol(f"{guess[0]}0"), Not(Symbol(f"{guess[1]}1")), Not(Symbol(f"{guess[2]}2")), Not(Symbol(f"{guess[3]}3")), Symbol(f"{guess[4]}4")),
            And(Not(Symbol(f"{guess[0]}0")), Symbol(f"{guess[1]}1"), Symbol(f"{guess[2]}2"), Not(Symbol(f"{guess[3]}3")), Not(Symbol(f"{guess[4]}4"))),
            And(Not(Symbol(f"{guess[0]}0")), Symbol(f"{guess[1]}1"), Not(Symbol(f"{guess[2]}2")), Symbol(f"{guess[3]}3"), Not(Symbol(f"{guess[4]}4"))),
            And(Not(Symbol(f"{guess[0]}0")), Symbol(f"{guess[1]}1"), Not(Symbol(f"{guess[2]}2")), Not(Symbol(f"{guess[3]}3")), Symbol(f"{guess[4]}4")),
            And(Not(Symbol(f"{guess[0]}0")), Not(Symbol(f"{guess[1]}1")), Symbol(f"{guess[2]}2"), Symbol(f"{guess[3]}3"), Not(Symbol(f"{guess[4]}4"))), 
            And(Not(Symbol(f"{guess[0]}0")), Not(Symbol(f"{guess[1]}1")), Symbol(f"{guess[2]}2"), Not(Symbol(f"{guess[3]}3")), Symbol(f"{guess[4]}4")),
            And(Not(Symbol(f"{guess[0]}0")), Not(Symbol(f"{guess[1]}1")), Not(Symbol(f"{guess[2]}2")), Symbol(f"{guess[3]}3"), Symbol(f"{guess[4]}4")),
                ))
        
    elif (correctPositions == 3):
        knowledge.add(Or(
            And(Not(Symbol(f"{guess[0]}0")), Not(Symbol(f"{guess[1]}1")), Symbol(f"{guess[2]}2"), Symbol(f"{guess[3]}3"), Symbol(f"{guess[4]}4")),
            And(Not(Symbol(f"{guess[0]}0")), Symbol(f"{guess[1]}1"), Not(Symbol(f"{guess[2]}2")), Symbol(f"{guess[3]}3"), Symbol(f"{guess[4]}4")),
            And(Not(Symbol(f"{guess[0]}0")), Symbol(f"{guess[1]}1"), Symbol(f"{guess[2]}2"), Not(Symbol(f"{guess[3]}3")), Symbol(f"{guess[4]}4")),
            And(Not(Symbol(f"{guess[0]}0")), Symbol(f"{guess[1]}1"), Symbol(f"{guess[2]}2"), Symbol(f"{guess[3]}3"), Not(Symbol(f"{guess[4]}4"))),
            And(Symbol(f"{guess[0]}0"), Not(Symbol(f"{guess[1]}1")), Not(Symbol(f"{guess[2]}2")), Symbol(f"{guess[3]}3"), Symbol(f"{guess[4]}4")),
            And(Symbol(f"{guess[0]}0"), Not(Symbol(f"{guess[1]}1")), Symbol(f"{guess[2]}2"), Not(Symbol(f"{guess[3]}3")), Symbol(f"{guess[4]}4")),
            And(Symbol(f"{guess[0]}0"), Not(Symbol(f"{guess[1]}1")), Symbol(f"{guess[2]}2"), Symbol(f"{guess[3]}3"), Not(Symbol(f"{guess[4]}4"))),
            And(Symbol(f"{guess[0]}0"), Symbol(f"{guess[1]}1"), Not(Symbol(f"{guess[2]}2")), Not(Symbol(f"{guess[3]}3")), Symbol(f"{guess[4]}4")), 
            And(Symbol(f"{guess[0]}0"), Symbol(f"{guess[1]}1"), Not(Symbol(f"{guess[2]}2")), Symbol(f"{guess[3]}3"), Not(Symbol(f"{guess[4]}4"))),
            And(Symbol(f"{guess[0]}0"), Symbol(f"{guess[1]}1"), Symbol(f"{guess[2]}2"), Not(Symbol(f"{guess[3]}3")), Not(Symbol(f"{guess[4]}4"))),
                 ))
        
    elif (correctPositions == 4):
        print("You must be mistaken! There are five colors, therefore there cannot be four correct positions.")
        break

    else:
        for i in range(len(colors)):
            knowledge.add(Symbol(f"{guess[i]}{i}"))      
                   
                         
    correctPositions = 0 
    for symbol in symbols:
        if model_check(knowledge, symbol):
            correctGuess[int(symbol.name[-1])] = symbol.name[:-1]
            correctPositions += 1

print("The secret combination is: ", correctGuess)
