#include <iostream>
#include <vector>
#include <bitset>
#include <string>

#define am_ARG_FUNC 3 // it should be changed by user
using namespace std;

class Logic_func{
    //access specifier
    //data members
    //member functions
    private:
    string logic_f;
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
        logic_f = result;
        return result;
    }
    string simplified_logic_function(){
        return "simplified_logic_sentence";
    }
    bool calculate_output(vector<bool> input_values){
        logic_f.replace(logic_f.begin(),logic_f.end(),"nA",!input_values[0]);//implement ASCI table
        logic_f.replace(logic_f.begin(),logic_f.end(),'A',input_values[0]);
        logic_f.replace(logic_f.begin(),logic_f.end(),"nB",!input_values[1]);
        logic_f.replace(logic_f.begin(),logic_f.end(),'B',input_values[1]);
        logic_f.replace(logic_f.begin(),logic_f.end(),"nC",!input_values[2]);
        logic_f.replace(logic_f.begin(),logic_f.end(),'C',input_values[2]);

        for(int i=0;i<logic_f.size();i+=2){
            if(logic_f[i+1]=='*'){
                if(logic_f[i]=='1'&&logic_f[i+2]=='1'){
                    logic_f[i+2]='1';
                }else{
                    logic_f[i+2]='0';
                }
            }else{
                if(logic_f[i]=='0'&&logic_f[i+2]=='0'){
                    logic_f[i+2]='0';
                }else{
                    logic_f[i+2]='1';
                }
            }
        }
        return logic_f[logic_f.size()-1]-'0';
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