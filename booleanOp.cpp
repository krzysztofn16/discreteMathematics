/*
napisać program w dowolnym języku programowania, który implementuje takie funkcje: 
wprowadznie funkcji boolowskich n zmiennych podanych w tabelach; 
konstruowanie wyrażenia boolowskiego, które odpowiada wprowadzonej funkcji boolowskiej; 
optymalizowanie wyrażeń boolowskich; 
konstruowanie sieci logicznych, które realizują optymalizowane wyrażenia boolowskie (konstruowanie sieci logicznych dla zoptymalizowanych wyrażeń 
może być wykonywane w dostępnym oprogramowaniu). 

zademonstrować skuteczność programu w stosunku do swego wariantu 5 zadania. 
0 0    0 0 0 - 1  0 0 0 0
0 1    0 0 1 - 0  0 0 0 1
1 0    0 1 0 - 0  0 0 1 0
1 1    0 1 1 - 1  0 0 1 1
       1 0 0 - 1  0 1 0 0 
       1 0 1 - 0  0 1 0 1
       1 1 0 - 0  0 1 1 0
       1 1 1 - 1  0 1 1 1
                  1 0 0 0
                  1 0 0 1
                  1 0 1 0
                  1 0 1 1
                  1 1 0 0
                  1 1 0 1
                  1 1 1 0
                  1 1 1 1
*/  

#include "Logic_func.h"
using namespace std;

int main(){
    Logic_func f1({1,0,0,1,1,0,0,1});
    vector<vector<bool>> v;
    f1.generate_tt(v);
    f1.display_tt(v);
    f1.display_res();
    cout<<f1.basic_logic_function(v,f1.f_result)<<endl; 
    int res = f1.calculate_output({0,0,0});
    cout<<"result of 0,0,0 values: "<<res<<endl;
    cout<<f1.logic_f<<endl;

    return 0;
}