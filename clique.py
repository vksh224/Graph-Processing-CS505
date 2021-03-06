import networkx as nx
import pickle

def get_constrained_undirected_graph(G, g):
    for u in G.nodes():
        for v in G. nodes():
            #add edge in the unidirected graph g only if both directed edges (u,v) and (v,u) are present in directed graph
            if u != v and G.has_edge(u, v) and G.has_edge(v,u):
                g.add_edge(u,v)
    return g

def print_largest_size_cliques(largest_clique_size):
    clique_list = nx.find_cliques_recursive(g)

    count = 0
    for n in clique_list:
        if len(n) == largest_clique_size:
            clique3.append([int(i) for i in n])
            count += 1
            for i in n:
                print(str(people_code[int(i)][1]), end=" ")
            print("")

    print("\nNumber of cliques of largest size: ", count)

    # print("\n================ END: List of cliques of maximum size ========== \n")

def print_butterfly():

    for c1 in range(len(clique3)):
        for c2 in range(c1, len(clique3)):

            if c1 != c2:
                butterfly = clique3[c1] + list(set(clique3[c2]) - set(clique3[c1]))
                # butterfly = list(set(clique3[c2]).union(set(clique3[c1])))
                sorted_butterfly = sorted(butterfly)

                H = G.subgraph([str(n) for n in sorted_butterfly])
                # print(len(H.edges()))

                #If butterfly exists
                if sorted(clique3[c1]) != sorted(clique3[c2]) and len(
                        sorted_butterfly) == 5 and sorted_butterfly not in butterfly_list and len(H.edges()) == 12:

                    butterfly_list.append(sorted_butterfly)
                    # print("Butterfly exists between these two cliques")

                    # print(sorted(clique3[c1]), end = " ")
                    # print(sorted(clique3[c2]), end = " ")
                    # print(" = ", end = " ")
                    # print(sorted_butterfly)

                    #Write name of the people involved in butterfly
                    for i in sorted_butterfly:
                        # print(people_code[int(i)][0], end =" ")
                        print(str(people_code[int(i)][1]), end =" ")
                    print(" ")

    print("\nNumber of butterfly: ", len(butterfly_list))



#main starts here
f = open("people_ID.txt", "r")
people_code = pickle.load(open("people_ID.txt", "rb"))


fh = open("dataset_coded.txt", "rb")
G = nx.read_adjlist(fh, create_using=nx.DiGraph())  #directed graph

g = nx.Graph()  #undirected graph

#reduced graph with only bidirected edges (or in other terms undirected graph)
g = get_constrained_undirected_graph(G, g)

# print("# nodes G and g: " + str(len(G.nodes())) + " " +  str(len(g.nodes())))
# print("# edges G and g: " + str(len(G.edges())) + " " +  str(len(g.edges())))

print(" Q2: ------------------------- ")
clique3 = []
largest_size_clique = max([len(n) for n in nx.find_cliques_recursive(g)])
print("Size of largest clique: ", largest_size_clique)
print("\nList of cliques of largest size: \n")
print_largest_size_cliques(largest_size_clique)

print("------------------------- \n")

###### Store it in a file
clique3_file = open("clique3.pkl", 'wb')
pickle.dump(clique3, clique3_file)
clique3_file.close()

print("Q3: ------------------------- ")

butterfly_list = []
print("List of butterfly: \n")
print_butterfly()
butterfly_file = open("butterfly.pkl", 'wb')
pickle.dump(butterfly_list, butterfly_file)

print("------------------------- ")

