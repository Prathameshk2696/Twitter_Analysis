
import pickle

def load_undirected_graph():
    global nx_u_graph
    f = open(r'F:\Fall 2020\Massive Data Storage and retrieval\TwitterAnalysis\MyApp'+'\\'+'nx_u_1M.pkl','rb')
    nx_u_graph = pickle.load(f)
    f.close()

def load_directed_graph():
    global nx_d_graph
    f = open(r'F:\Fall 2020\Massive Data Storage and retrieval\TwitterAnalysis\MyApp'+'\\'+'nx_d_1M.pkl','rb')
    nx_d_graph = pickle.load(f)
    f.close()

def load_dendrogram():
    global dendro_list
    f = open(r'F:\Fall 2020\Massive Data Storage and retrieval\Social_Network_Analysis\GeneratedData\dendro_1M_list.pkl','rb')
    dendro_list = pickle.load(f)
    f.close()

def load():
    load_undirected_graph()
    load_directed_graph()
    load_dendrogram()

def get_total_nodes():
    return len(nx_u_graph.nodes())

def get_total_edges():
    return len(nx_u_graph.edges())

def get_total_levels():
    return len(dendro_list)

def get_each_level():
    return [len(d) for d in dendro_list]

def get_graph_stats():
    return get_total_nodes(),get_total_edges(),get_total_levels()