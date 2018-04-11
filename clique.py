import networkx as nx
import pickle
from k_clique import *
from max_clique import *

def get_constrained_undirected_graph(G, g):

    for u in G.nodes():
        for v in G. nodes():
            if u != v and G.has_edge(u, v) and G.has_edge(v,u):
                g.add_edge(u,v)
    return g

def print_largest_size_cliques():
    clique_list = nx.find_cliques_recursive(g)
    # clique_num = nx.graph_number_of_cliques(g, 3)
    # max_clique_size = max_clique(g)

    print("\n\n================ START: List of cliques of maximum size ========== ")
    count = 0
    for n in clique_list:
        if len(n) > 2:
            clique3.append([int(i) for i in n])
            count += 1
            for i in n:
                print(str(people_code[int(i)][1]), end=" ")
            print("")


    print("Number of cliques: ", count)

    print("\n================ END: List of cliques of maximum size ========== \n\n")

def print_butterfly():
    # k_clique_list = k_clique_communities(g, 3)

    print("\n============== START: Print butterfly ==== ")
    for c1 in range(len(clique3)):
        for c2 in range(c1, len(clique3)):

            if c1 != c2:
                butterfly = clique3[c1] + list(set(clique3[c2]) - set(clique3[c1]))
                # butterfly = set(clique3[c2]).union(set(clique3[c1]))
                #If butterfly exists
                if clique3[c1] != clique3[c2] and len(butterfly) == 5:
                    butterfly_list.append(butterfly)
                    # print("Butterfly exists between these two cliques")
                    for i in butterfly:
                        print(str(people_code[int(i)][1]), end =" ")
                    print(" ")

    print("Number of butterfly: ", len(butterfly_list))

    print("\n ============== END: Print butterfly ==== ")

    print_unique_butterfly()

def print_unique_butterfly():
    sorted_butterfly_list = sorted([sorted(b1) for b1 in butterfly_list])

    unique_butterfly_list = sorted_butterfly_list
    for ind1 in range(len(sorted_butterfly_list)):
        for ind2 in range(len(sorted_butterfly_list)):
            if ind1 != ind2 and sorted_butterfly_list[ind1] == sorted_butterfly_list[ind2]:
               print("Duplicate: " , sorted_butterfly_list[ind1])

    print("Count of unique butterfly ", sorted_butterfly_list)


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

clique3 = []
print_largest_size_cliques()

butterfly_list = []
unique_butterfly_list = []

print_butterfly()