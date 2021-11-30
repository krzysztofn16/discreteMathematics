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
#include <iostream>
#include <vector>
#include <bitset>
//#include <booleanOp.h>
using namespace std;
#define am_ARG_FUNC 3 // it should be changed by user

class Logic_func{
    //access specifier
    //data members
    //member functions
    public:
    bool to_bool(char const& s) {
        return s != '0';
    }
    int max_val_bits(int b){
        return (1<<b)-1;
    }
    void generate_tt(vector<vector<bool>> &vec){
        int max_val = max_val_bits(am_ARG_FUNC);
        for (int i=0;i<=max_val;i++){//also ROWs
            string s = bitset<am_ARG_FUNC>(i).to_string();
            vector<bool> v1;
            for(int j=0;j<am_ARG_FUNC;j++){
                bool tmp = to_bool(s[j]);
                v1.push_back(tmp);
            }
            vec.push_back(v1);
        }
    }
    void display_tt(vector<vector<bool>> &vec){
        for (int i = 0; i < vec.size(); i++) {
            for (int j = 0; j < vec[i].size(); j++)
                cout << vec[i][j] << " ";
            cout << endl;
        }
    }
};
// void generate(int n, std::vector< std::vector<int> >& vec) {
//     vec.resize(n, std::vector<int>(1 << n, 0));
// }

// int main() {
//     std::vector< std::vector<int> > v;
//     generate(10, v);
// }
int main(){
    //create vector
    // vector<bool> v = {1, 0,1};

    // cout << "v= { ";
    // for(int n : v){
    //     cout <<n<<", ";
    // }
    // cout<<"}; \n";
    
    Logic_func f1;
    vector<vector<bool>> v;
    f1.generate_tt(v);
    f1.display_tt(v);

    return 0;
}