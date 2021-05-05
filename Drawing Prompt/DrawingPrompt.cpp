#include <fstream>
#include <iostream>
using namespace std;


string call_file (string filename)
{
    cout << "call_file was called successfully using: " << filename << endl << endl;
    string word;

    return word;
}


string get_random_word (string wordType)
{
    cout << "get random word was called successfully using: " << wordType << endl;

    string word = call_file(wordType);

    return word;
}

int main ()
{
    string nounCall = "noun";
    string verbCall = "verb";
    string adjCall = "adjective";
    string fillerCall= "filler";

    string noun1 = get_random_word(nounCall);
    string verb1 = get_random_word(verbCall);
    string adjective1 = get_random_word(adjCall);
    string filler1 = get_random_word(fillerCall);

    return 0;
}