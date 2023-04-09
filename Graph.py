"""
Graph V1.00
created by Nima
email: Nima81ghasemi@proton.me

notes: 
    in this version you need to create a list first then run program
    program will create a graph (adjacency list) for you
"""

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dictionary = dict()

    def create_graph_dictionary(self, list):
        for i in range(len(list)):
            first_item = list[i][0]
            second_item = list[i][1]
            if first_item not in self.graph_dictionary.keys():
                self.graph_dictionary[first_item] = []
                self.graph_dictionary[first_item].append(second_item)
            else:
                self.graph_dictionary[first_item].append(second_item)
        return self.graph_dictionary

routes = [
    ('Kerman', 'Yazd'),
    ('Kerman', 'Esfahan'),
    ('Esfahan', 'Mashhad'),
    ('Yazd', 'Mashhad'),
    ('Yazd', 'Esfahan'),
    ('Mashhad', 'Tehran')
]

# testing program

test = Graph(1)
print(test.create_graph_dictionary(routes))
"""
result will be this:

    {
        'Kerman': ['Yazd', 'Esfahan'],
        'Esfahan': ['Mashhad'],
        'Yazd': ['Mashhad', 'Esfahan'],
        'Mashhad': ['Tehran']
    }

"""