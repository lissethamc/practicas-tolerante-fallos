#include <iostream>
#include <exception>
#include <vector>
#include <fstream>
#include <cstdlib>
#include <string>
#include <ctype.h>


#include "songs.h"

using namespace std;

struct MyException : public exception {
   const char * what () const throw () {
      return "Parsing error: expected int value";
   }
};

bool isNumber(const string& s);
 
int main() {

    vector<CSong> songList;
    CSong currentSong;
    ifstream inputFile;
    string temporaryString;
    int temporaryInt;
    int checkPosition;
    inputFile.open("songlist.txt");

    if(inputFile.is_open()){
        while(inputFile.good()){
            
            temporaryString = " ";
            getline(inputFile,temporaryString,'/');
            try{
                if(!isNumber(temporaryString)){
                    throw MyException();
                }
                temporaryInt = stoi(temporaryString);
                currentSong.setId(temporaryInt);
                //aqui lanzo la excepcion si el valor no es numerico 
            }
            catch(const invalid_argument& ia){

                cout << "Invalid Argument custom exception" << std::endl;
                cout <<  ia.what() << std::endl;
            }
            catch(const MyException& e){

                cout << "MyException Caught" << std::endl;
                cout <<  e.what() << std::endl;
                currentSong.setName(temporaryString);
                
            }
            songList.push_back(currentSong);

        }
    }



//    try {
//       throw MyException();
//    } catch(MyException& e) {
//       std::cout << "MyException caught" << std::endl;
//       std::cout << e.what() << std::endl;
//    } catch(std::exception& e) {
//       Other errors
//    }


    
}

bool isNumber(const string& s){
    string::const_iterator it = s.begin();
    while(it !=s.end() && isdigit(*it)) ++it;
    return !s.empty() && it == s.end();
} 