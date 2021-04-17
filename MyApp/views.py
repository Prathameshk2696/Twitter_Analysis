
from django.shortcuts import render, HttpResponse
from MyApp import dendrogram as dg
import json
from MyApp import GraphMain as gm
from MyApp import Triangles as tri
from MyApp import PageRank as pr
from MyApp import ShortestPath as sp

# Create your views here.

def home(request):
    return render(request,'home.html')

def main(request):
    gm.load()
    return render(request,'main.html')

def index(request):
    return render(request,'index.html')

def city(request):
    return render(request,'city.html')

def get_root(request):
    context = {
        'data' : [dg.get_root()]
    }
    return HttpResponse(json.dumps(context))

def get_children(request):
    node_name = request.POST['node_name']
    context = {
        'children_list':dg.get_children(node_name)
    }
    return HttpResponse(json.dumps(context))

def get_graph_stats(request):
    total_nodes,total_edges,total_levels = gm.get_graph_stats()
    context = {
        'total_nodes':total_nodes,
        'total_edges':total_edges,
        'total_levels':total_levels
    }
    return HttpResponse(json.dumps(context))

def get_triangles_data(request):
    community_name = request.POST['community_name']
    triangles_vis = tri.get_triangles(community_name)
    context = {
        'triangles_vis':triangles_vis
    }
    return HttpResponse(json.dumps(context))

def get_page_rank_data(request):
    community_name = request.POST['community_name']
    page_ranks_vis = pr.get_page_ranks(community_name)
    context = {
        'page_ranks_vis':page_ranks_vis
    }
    return HttpResponse(json.dumps(context))

def get_shortest_path(request):
    n1 = int(request.POST['node_1'])
    n2 = int(request.POST['node_2'])
    print(type(n1))
    path_vis = sp.get_shortest_path_graph_vis(n1,n2)
    context = {
        'path_vis':path_vis
    }
    return HttpResponse(json.dumps(context))