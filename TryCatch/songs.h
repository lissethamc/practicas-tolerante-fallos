#include <iostream>
using namespace std;

class CSong {
    
    private:
        int id;
        string name;
        string artist;  

    public:
        CSong(){};
        ~CSong(){};

        void setId(const int& v) {this->id = v;}
        void setName(const string& v) {this->name = v;}
        void setArtist(const string& v) {this->artist = v;}

        int getId() {return id;}
        string getName() {return name;}
        string getArtist() {return artist;}
        

};


