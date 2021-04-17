
from MyApp import GraphMain as gm

def get_children(node_name):
    dendro_list = gm.dendro_list
    if node_name[0]=='L':
        L = node_name[1]
    else:
        L=len(dendro_list)-1
    children_list = dendro_list[int(L)][node_name]['children']
    children_list2 = []
    for d in children_list:
        children_list2.append({})
        for key in d:
            if key != 'children':
                children_list2[-1][key] = d[key]
    return children_list2

def get_leaves(node_name):
    dendro_list = gm.dendro_list
    level_number = int(node_name[1])
    node_name_list = [node_name]
    node_name_list2 = []
    while True:
        for node_name in node_name_list:
            children_list = get_children(node_name)
            for d in children_list:
                node_name_list2.append(d['name'])
        node_name_list = node_name_list2
        node_name_list2 = []
        level_number += 1
        if level_number == (len(dendro_list)-1):
            break
    return node_name_list

def build_community_u_graph(community_name):
    nx_u_graph = gm.nx_u_graph
    leaves_list = get_leaves(community_name)
    leaves_list = [int(s) for s in leaves_list]
    return (nx_u_graph.subgraph(leaves_list))

def build_community_d_graph(community_name):
    nx_d_graph = gm.nx_d_graph
    leaves_list = get_leaves(community_name)
    leaves_list = [int(s) for s in leaves_list]
    return (nx_d_graph.subgraph(leaves_list))