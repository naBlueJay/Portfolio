#include <iostream>
#include <ctime>
using namespace std;


string getWord (string neededWord)
{
    string randomWord;
    int randomNumber;
    // In the furure I wuld like to  replace the premade arrays with arrays generated from CSV files
    string nouns[10] = {"group", "party", "man", "woman", "table", "animal", "figure", "president", "friend", "couple"};
    string verbs[10] = {"comparing", "clening", "copying", "wrapping", "running", "existing", "waiting", "traversing", "floating", "failing"};
    string adjective[10] = {"aged", "adept", "common", "complex", "fearless", "fickle", "impish", "lanky", "murky", "slimy"};
    string filler[10] = {"next to", "on", "under", "over", "behind", "infront of", "across from", "below", "above", "far from"};

    if (neededWord == "noun")
    {
        // The randomNumber is used to pull a random vlue from the wor arrays.
        randomNumber = (rand()%10);
        randomWord = nouns[randomNumber];
        // cout << randomWord << endl;
    }

    else if (neededWord == "verb")
    {
        randomNumber = (rand()%10);
        randomWord = verbs[randomNumber];
        // cout << randomWord << endl;
    }

    else if (neededWord == "adjective")
    {
        randomNumber = (rand()%10);
        randomWord = adjective[randomNumber];
        // cout << randomWord << endl;
    }

    else if (neededWord == "filler")
    {
        randomNumber = (rand()%10);
        randomWord = filler[randomNumber];
        // cout << randomWord << endl;
    }

    else
    {
        cout << "Something went wrong calling your word" << endl;
    }

    return randomWord;
}


void runGame()
{
    // These variables are sent to the getWord function to tell it what word needs to be generated.
    string nounCall = "noun", verbCall = "verb", adjCall = "adjective", fillerCall = "filler";

    // This calls the getWord function and sets the word values to the random words from the arrays.
    string noun1 = getWord(nounCall), noun2 = getWord(nounCall), verb1 = getWord(verbCall), verb2 = getWord(verbCall), filler1 = getWord(fillerCall);

    // This section prints out the prompt.
    cout << "Here's your prompt! Enjoy!" << endl << endl;
    cout << "A " << noun1 << " " << verb1 << " " << filler1 << " a/an "  << verb2 << " " << noun2 << endl << endl;

    // This is a paus section that allows the user to read the prompt before continuing.
    cout << "Press ENTER to continue" << endl;
    cin.ignore();
}


int main ()
{
    string playGame = "y";
    srand(time(NULL));
    
    // The while loop will be entered automatically due to the fact that playGames starts as "y"
    while (playGame == "y")
    {
        cout << "Hello! Would you like a new drawing prompt?" << endl << "Pleasy type (y/n): ";
        cin  >> playGame;
        cout << endl;

        // This is where the generator is either started or aborted.
        if (playGame == "y")
        {
            runGame();
        }

        else if (playGame == "n")
        {
            // I put this here so that the program didn't end as soon as you typed in "n"
            cout << "Thanks for playing" << endl << "Please press ENTER to close program";
            cin.ignore();
        }
    }

    return 0;
}
