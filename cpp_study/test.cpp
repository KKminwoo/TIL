#include <iostream>
#include <cctype>
int main() {
    using namespace std;
    cout << "input text, end with @\n";
    char ch;
    int whitespace = 0;
    int digits = 0;
    int chars = 0;
    int punct = 0;
    int others = 0;

    cin.get(ch);
    while (ch != '@')
    {
        if (isalpha(ch))
            chars++;
        else if (isspace(ch))
            whites
    }
    
 }