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
    private:
    public:
    vector<bool> f_result;
    Logic_func(vector<bool>function_result){
        f_result = function_result;
    }
    
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
    string basic_logic_function(vector<vector<bool>> &truth_table, vector<bool> &function_result){
        string result;
        for(int i=0;i<function_result.size();i++){
            if(function_result[i]==1){
                for(int j=0;j<am_ARG_FUNC;j++){
                    string sign;
                    switch (j)
                    {
                    case 0:
                        sign="A";
                        break;
                    case 1:
                        sign="B";
                        break;
                    case 2:
                        sign="C";
                        break;
                    default:
                        cout<<("Update functionality for more arguments !.")<<endl;
                        break;
                    }
                    if(truth_table[i][j]==1){
                        result.append(sign);
                    }
                    else{
                        result.append("n");
                        result.append(sign);
                    }
                    result.append("*");
                }
                if(i==function_result.size()-1)break;
                result.append("+");
            }
        }
        return result;
    }
    string display_simplified_logic_function(){
        return "simplified_logic_sentence";
    }
    void display_tt(vector<vector<bool>> &vec){
        cout<<"Truth table for "<<am_ARG_FUNC<<" arguments.\n";
        for (int i = 0; i < vec.size(); i++) {
            for (int j = 0; j < vec[i].size(); j++)
                cout << vec[i][j] << " ";
            cout << endl;
        }
    }
    void display_res(){
        cout<<"Result of logic function:\n";
        for(int i=0;i<f_result.size();i++){
            cout<<f_result[i]<<endl;
        }
    }
};
int main(){
    //create vector
    // vector<bool> v = {1, 0,1};

    // cout << "v= { ";
    // for(int n : v){
    //     cout <<n<<", ";
    // }
    // cout<<"}; \n";
    
    Logic_func f1({1,0,0,1,1,0,0,1});
    vector<vector<bool>> v;
    f1.generate_tt(v);
    f1.display_tt(v);
    f1.display_res();
    cout<<f1.basic_logic_function(v,f1.f_result)<<endl;

    return 0;
}