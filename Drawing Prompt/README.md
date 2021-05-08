# Drawing Prompt Generator
## Overview

I created a program that generated randomized drawing prompts. It pulls from various lists of nouns, verbs, adjectives, and filler words to make unique prompts. I made this software to combat writers-block, or rather artist’s block. By writing this software I hoped to learn more about other software languages and the similarities between them.

[Random Prompt Generator](https://youtu.be/i58LQz00YB8)

## Development Environment

I used the programming language C++ for this project.  To do the coding I used Visual Studio Code with the C++ addon and compiler.

The library that I used was ‘iostream’ and ‘ctime’. The ‘iostream’ library allows for basic input and output functions while the ‘ctime’ allows access to the system time. The system time is used for a simple pseudo-random number generator.

The random number generator is used to pull random numbers from the word arrays that I use.



## Useful Websites

{Make a list of websites that you found helpful in this project}

* [CPlusPlus](https://www.cplusplus.com/)
* [w3schools](https://www.w3schools.com/cpp/)

## Future Work

```
* I need to add a feature for reading form CSV files for the random words so that I'm not limited to 10 words.
* I would like to add a feature of writing the promts to a txt file instead of to a terminal.
* I have some repeated code that could probably be cut down to reduce the total line count.
```