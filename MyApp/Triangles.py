
from MyApp import MakeCommunityGraph as mcg
from MyApp import GraphMain as gm
import networkx as nx

def get_triangles(community_name):
    nx_u_graph = gm.nx_u_graph
    community_u_graph = mcg.build_community_u_graph(community_name)
    tr = nx.triangles(community_u_graph)
    tr_nonzero = {k:v for k,v in tr.items() if v != 0}
    triangles_vis = []
    edge_list = list(community_u_graph.edges())
    for node in tr_nonzero:
        d = {}
        d['name'] = str(node)
        d['value'] = tr[node]
        d['linkWith'] = []
        for n1,n2 in edge_list:
            if n1 == node and n2 in tr_nonzero:
                d['linkWith'].append(str(n2))
            elif n2 == node and n1 in tr_nonzero:
                d['linkWith'].append(str(n1))
        triangles_vis.append(d)
    return triangles_vis