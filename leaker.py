import networkx as nx
import matplotlib.pyplot as plt
import pickle


def get_leaker_id(name):
    person_id = -1

    for ind in range(len(people_code)):
        if people_code[ind][1] == name:
            #print ("ID is" , people_code[ind][0])
            person_id = people_code[ind][0]

    return person_id

#Get leakers list
def get_leakers(node_id):
    leakers_ids = []
    leakers_names = []

    # for u, v in G.in_edges(node_id):
    #     leakers_ids.append(u)

    for n in G.nodes():
        if n != node_id and G.has_edge(n, node_id) and G.has_edge(node_id, n):
            leakers_ids.append(n)
            leakers_names.append(people_code[int(n)][1])

    return leakers_ids, leakers_names


#In or Out-degree distribution
def plot_degree_distribution():
    degs = {}
    for n in G.nodes():
        deg = G.out_degree(n)
        if deg not in degs:
            degs[deg] = 0
        degs [deg] += 1
    items = sorted(degs.items())
    plt.plot([k for (k, v) in items], [v for (k, v) in items])
    plt.show()


fh= open("dataset_coded.txt", "rb")
G=nx.read_adjlist(fh, create_using=nx.DiGraph())
#plot_degree_distribution()

f = open("people_ID.txt", "r")
people_code = pickle.load(open("people_ID.txt", "rb"))

#Question #1: Get list of leakers to woods
# Woods : 301
person_id = get_leaker_id("WOODS")

print("Number of nodes and edges: " + str(len(G.nodes())) + " " + str(len(G.edges())))
leakers_ids, leakers_names = get_leakers(str(person_id))
print("Number of leakers: " + str(len(leakers_ids)))
print ("Leakers: ")
for name in leakers_names:
    print(name, end = " ")

# nx.draw(G, with_labels=True)
# plt.draw()
# plt.show()