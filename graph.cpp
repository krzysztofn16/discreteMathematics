/*
 * napisać program w dowolnym języku programowania, który implementuje takie funkcje: 
 * wprowadznie grafów wybranego typu, podanych przez macierz sąsiedztwa lub incydentności (a dla grafów ważonych dodatkowe wprowadzenie wartości wag); 
 * implementację wybranego algorytmu dla powyższego typu grafów; 
 * zademonstrować skuteczność programu na rozszerzonej wersji jednego z poniższych grafów: 
 */

#include <iostream>
#include <vector>
#include <string>
#include <stdexcept>

using namespace std;
//definition of adjacency matrix
using Matrix = vector<vector<int>>;

class Graph
{
public:
    Graph (size_t size) : _size{size}, _matrix(size, vector<int>(size, 0))
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
    void addEdge(int i, int j, string type, bool direction=1)
    {
        if(type == "undirect"){
            _matrix[i - 1][j - 1] = 1;
            _matrix[j - 1][i - 1] = 1;
        }else if(type == "direct"){
            if(direction == 1){
                _matrix[i - 1][j - 1] = 1;
            }else if(direction == 0){
                _matrix[j - 1][i - 1] = 1;
            }else{
                throw invalid_argument("Wrong direction argument.");
            }
        }else{
            throw invalid_argument("Wrong type argument.");
        }
    }

    void display()
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

private:
    size_t _size;
    Matrix _matrix;
};

int main()
{
    Graph graph(4);
    //{direct, undirect}
    graph.addEdge(1, 2, "undirect");
    graph.addEdge(1, 3, "direct");
    graph.addEdge(2, 3, "undirect");
    graph.addEdge(3, 4, "undirect");

    graph.display();
    
    return 0;
}