
import networkx as nx
from MyApp import GraphMain as gm

def get_shortest_path_graph_vis(n1,n2):
    nx_u_graph = gm.nx_u_graph
    try:
        path = nx.shortest_path(nx_u_graph,n1,n2)
        print(path)
        path_edges = [(path[i],path[i+1]) for i in range(len(path)-1)]
        path_vis = []
        for n1,n2 in path_edges:
            d = {}
            d['name'] = str(n1)
            d['linkWith'] = [str(n2)]
            path_vis.append(d)
        path_vis.append({'name':path_vis[-1]['linkWith']})
        return path_vis
    except nx.exception.NodeNotFound as nnf:
        print('No Path')
    

