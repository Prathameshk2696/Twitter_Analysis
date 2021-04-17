
from MyApp import MakeCommunityGraph as mcg
import networkx as nx

def get_page_ranks(community_name):
    community_d_graph = mcg.build_community_d_graph(community_name)
    page_ranks_dict =nx.pagerank(community_d_graph, alpha=0.85, personalization=None, max_iter=100, tol=1e-06, nstart=None, weight='weight', dangling=None)
    page_rank_vis = []
    node_list = list(community_d_graph.nodes())
    edge_list = list(community_d_graph.edges())
    print(len(edge_list))
    for node in node_list:
        d = {}
        d['name'] = str(node)
        d['value'] = page_ranks_dict[node]*100
        d['tooltipText'] = page_ranks_dict[node]
        d['linkWith'] = []
        for n1,n2 in edge_list:
            if n1 == node:
                d['linkWith'].append(str(n2))
        page_rank_vis.append(d)
    return page_rank_vis

