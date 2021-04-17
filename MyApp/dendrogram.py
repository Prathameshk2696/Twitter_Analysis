
import pickle
from copy import deepcopy as dc

def get_root():
    global data
    f = open(r'F:\Fall 2020\Massive Data Storage and retrieval\TwitterAnalysis\MyApp\dendro_1M_list.pkl','rb')
    data = pickle.load(f)
    root_node_with_children = data[0]['L0C0']
    root_node = {}
    for key in root_node_with_children:
        if key != 'children':
            root_node[key] = root_node_with_children[key]
    return root_node

def get_children(node_name):
    print('node_name',node_name)
    #f = open(r'F:\Fall 2020\Massive Data Storage and retrieval\TwitterAnalysis\MyApp\dendro_1M_list.pkl','rb')
    #data = pickle.load(f)
    if node_name[0]=='L':
        L = node_name[1]
    else:
        L=len(data)-1
    #print(data[int(L)][node_name])
    children_list = data[int(L)][node_name]['children']
    children_list2 = []
    for d in children_list:
        children_list2.append({})
        for key in d:
            if key != 'children':
                children_list2[-1][key] = d[key]
    return children_list2