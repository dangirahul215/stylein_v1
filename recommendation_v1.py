import pandas as pd
# import networkx as nx
from networkx import Graph
import glob


def read_all_files(path=r"asos"):
    allFiles = glob.glob(path + "/*.csv")
    list_ = []

    for file_ in allFiles:
        df = pd.read_csv(file_, header=0)
        list_.append(df)

    frame = pd.concat(list_)
    return frame


# def blabla(g, passed_prod_ids):
#     try:
#         passed_prod_ids_ = passed_prod_ids.split('|')
#         adjacency_list_1 = [(prod_id, int(similar_prod_id)) for similar_prod_id in passed_prod_ids_]
#         g.add_edges_from(adjacency_list_1)
#
#         return g
#     except:
#         raise TypeOneException
class CustomGraph(Graph):
    def __init__(self, **attr):
        super(CustomGraph, self).__init__(**attr)

    def add_edges_from(self, adjacency_list, **kwargs):
        #try:
        super(CustomGraph, self).add_edges_from(adjacency_list, **kwargs)
        #except:
        #    pass


class Operation:
    def __init__(self, frame):
        # Part A
        self.G_similar_products = CustomGraph()

        # Part B
        self.G_pair_with = CustomGraph()

        self.frame = frame

    def algo(self):
        for prod_id, pair_with_ids, similar_prod_ids in zip(self.frame['prodId'], self.frame['pairWithProducts'],
                                                            self.frame['similarProducts']):
            # TODO Part A
            # create an adjacency list and pass fw
            try:
                similar_prod_ids = similar_prod_ids.split('|')
                adjacency_list_a = [(prod_id, int(similar_prod_id)) for similar_prod_id in similar_prod_ids]
            #adjacency_list_a = create_list_a(passed_prod_ids=similar_prod_ids)
                self.G_similar_products.add_edges_from(adjacency_list=adjacency_list_a)
            except:
                pass
            finally:
                try:
            # TODO Part B
            # create an adjacency list and pass fw
                    pair_with_ids=pair_with_ids.split('|')
                    adjacency_list_b=[(prod_id,int(pair_with_id)) for pair_with_id in pair_with_ids]
            #adjacency_list_b = create_list_b(passed_prod_ids=pair_with_ids)
                    self.G_pair_with.add_edges_from(adjacency_list=adjacency_list_b)
                except:
                    pass
    def recommended_products_similar(self, prod_id):
        return list(self.G_similar_products.adj[prod_id])

    def recommended_products_pair_with(self, prod_id):
        return list(self.G_pair_with.adj[prod_id])

'''
def main():
    frame = read_all_files()
    node = Operation(frame)
    node.algo()
    print(node.recommended_products_similar(prod_id=9786234))
    print(node.recommended_products_pair_with(9786234))


if __name__ == '__main__':
    main()
'''