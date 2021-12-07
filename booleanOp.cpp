
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

    return 0;
}