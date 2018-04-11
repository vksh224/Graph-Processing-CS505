import networkx as nx
import pickle
from k_clique import *
def get_constrained_undirected_graph(G, g):

    for u in G.nodes():
        for v in G. nodes():
            if u != v and G.has_edge(u, v) and G.has_edge(v,u):
                g.add_edge(u,v)
    return g

def print_largest_size_cliques():
    clique_list = nx.find_cliques_recursive(g)

    print("\n\n================ START: List of cliques of maximum size ========== ")
    for n in clique_list:
        if len(n) > 2:
            for i in n:
                print(str(people_code[int(i)][1]), end=" ")
            print("")

    print("\n================ END: List of cliques of maximum size ========== \n\n")
    # MILES ALEXANDER GARRETT VELASQUEZ
    # PERRY JENSEN NICHOLSON HUNT

def print_butterfly():
    k_clique_list = k_clique_communities(g, 3)

    print("\n============== START: Print butterfly ==== ")
    for c1 in k_clique_list:
        for c2 in k_clique_list:
            #If butterfly exists
            if len(c1.union(c2)) <= 5:
                print("Butterfly exists between these two cliques")
                butterflySet = c1.union(c2)
                # print(butterflySet)
                for i in butterflySet:
                    print(str(people_code[int(i)][1]), end = " ")

    print("\n ============== END: Print butterfly ==== ")

    #MCGEE COBB ROBINSON WYATT ELLIOTT

#main starts here

f = open("people_ID.txt", "r")
people_code = pickle.load(open("people_ID.txt", "rb"))


fh = open("dataset_coded.txt", "rb")
G = nx.read_adjlist(fh, create_using=nx.DiGraph())

g = nx.Graph()

#reduced graph with only bidirected edges (or in other terms undirected graph)
g = get_constrained_undirected_graph(G, g)

print("# nodes G and g: " + str(len(G.nodes())) + " " +  str(len(g.nodes())))
print("# edges G and g: " + str(len(G.edges())) + " " +  str(len(g.edges())))

print_largest_size_cliques()
print_butterfly()