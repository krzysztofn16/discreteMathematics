/*
napisać program w dowolnym języku programowania, który implementuje takie funkcje: 
wprowadznie funkcji boolowskich n zmiennych podanych w tabelach; 
konstruowanie wyrażenia boolowskiego, które odpowiada wprowadzonej funkcji boolowskiej; 
optymalizowanie wyrażeń boolowskich; 
konstruowanie sieci logicznych, które realizują optymalizowane wyrażenia boolowskie (konstruowanie sieci logicznych dla zoptymalizowanych wyrażeń 
może być wykonywane w dostępnym oprogramowaniu). 

zademonstrować skuteczność programu w stosunku do swego wariantu 5 zadania. 
000 - 1
001 - 0
010 - 0
011 - 1 
100 - 1
101 - 0
110 - 0
111 - 1
*/
#include <iostream>
#include <vector>
//#include <booleanOp.h>
using namespace std;
int main(){
    //create vector
    vector<bool> v = {1, 0,1};

    cout << "v= { ";
    for(int n : v){
        cout <<n<<", ";
    }
    cout<<"}; \n";

    return 0;
}