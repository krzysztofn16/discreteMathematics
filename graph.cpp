
#include <iostream>
#include <vector>
#include <string>
#include <stdexcept>

using namespace std;
//definition of adjacency matrix
using Matrix = vector<vector<int>>;
using Weight_matrix = vector<vector<double>>;

class Graph
{
public:
    Graph (size_t size) : _size{size}, _matrix(size, vector<int>(size, 0)),_weight_matrix(size, vector<double>(size,0))
    {
    }
    /**
     * @brief Add connection betwen 2 nodes of the graph
     *   TO DO - remove fourth arg and define direction based sequence of passed nodes.
     * @param i node 1
     * @param j node 2
     * @param type undirect or direct connection
     * @param direction 1 for left2right
     *                  0 for right2left
     */
    void addEdge(int i, int j, string type, bool direction=1, double weight=1.0)
    {
        if(type == "undirect"){
            _matrix[i - 1][j - 1] = 1;
            _weight_matrix[i - 1][j - 1] = 1;
            _matrix[j - 1][i - 1] = 1;
            _weight_matrix[j - 1][i - 1] = 1;
        }else if(type == "direct"){
            if(direction == 1){
                _matrix[i - 1][j - 1] = 1;
                _weight_matrix[i - 1][j - 1] = 1;
            }else if(direction == 0){
                _matrix[j - 1][i - 1] = 1;
                _weight_matrix[j - 1][i - 1] = 1;
            }else{
                throw invalid_argument("Wrong direction argument.");
            }
        }else{
            throw invalid_argument("Wrong type argument.");
        }
    }

    void display_matrix()
    {
        for (int i = 0; i < _size; ++i)
        {
            for (int j = 0; j < _size; ++j)
            {
                cout<<_matrix[i][j]<<" ";
            }
            cout<<endl;
        }
    }
    void display_weight()
    {
        for (int i = 0; i < _size; ++i)
        {
            for (int j = 0; j < _size; ++j)
            {
                cout<<_weight_matrix[i][j]<<" ";
            }
            cout<<endl;
        }
    }

private:
    size_t _size;
    Matrix _matrix;
    Weight_matrix _weight_matrix;
};

int main()
{
    Graph graph(4);
    //{direct, undirect}
    graph.addEdge(1, 2, "undirect");
    graph.addEdge(1, 3, "direct");
    graph.addEdge(2, 3, "undirect");
    graph.addEdge(3, 4, "undirect");

    cout<<"Adjucent matrix"<<endl;
    graph.display_matrix();
    cout<<"Weight for connection"<<endl;
    graph.display_weight();
    
    return 0;
}