import networkx as nx
import pickle
import matplotlib.pyplot as plt


def highest_in_out_deg_centrality(cent_dict):
    cent_items = [(b, a) for (a, b) in cent_dict.items()]
    cent_items.sort()
    cent_items.reverse()

    return tuple(reversed(cent_items[0]))

fh= open("dataset_coded.txt", "rb")
G=nx.read_adjlist(fh, create_using=nx.DiGraph())


in_deg_cent_dict = nx.in_degree_centrality(G)
out_deg_cent_dict = nx.out_degree_centrality(G)

f = open("people_ID.txt", "r")
people_ID = pickle.load(open("people_ID.txt", "rb"))

highest_in_degree_node = highest_in_out_deg_centrality(in_deg_cent_dict)
highest_out_degree_node = highest_in_out_deg_centrality(out_deg_cent_dict)

print("In-degree: " +  str(people_ID[int(highest_in_degree_node[0])][1]) + " " + str(highest_in_degree_node[1]))
print("Out-degree: " +  str(people_ID[int(highest_out_degree_node[0])][1]) + " " + str(highest_out_degree_node[1]))


