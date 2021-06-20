import random
import csv

min = 1
max = 6


def rollDice(numberOfDice, fileName):
    dice = []
    newString = ""

    for i in range(numberOfDice):
        dice.append(random.randint(min, max))
        # print(dice[i])

    for number in str(dice):
        newString += number

    newString = newString.strip("[]").replace(",", "").replace(" ", "")

    outfile = open(fileName, 'a', newline='')
    out = csv.writer(outfile)
    out.writerow(newString)
    outfile.close


def main():
    numberOfRolls = 10000
    numberOfDice = 5
    fileName = "diceSimulation10k.csv"
    newFileName = "cleaned10k.csv"

    for i in range(numberOfRolls):
        rollDice(numberOfDice, fileName)


if __name__ == '__main__':
    main()
