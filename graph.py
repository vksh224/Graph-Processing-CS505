import networkx as nx
import matplotlib.pyplot as plt

#Get leakers list
def get_incoming_edges(node_id):
    leakers_ids = []
    leakers_names = []
    for u, v in G.in_edges(node_id):
        leakers_ids.append(u)

    with open("people_to_code.txt") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            lineArr = line.split(",")
            # print(lineArr[1])
            if(lineArr[1] in leakers_ids):
                leakers_names.append(lineArr[0])
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


#Question #1: Get list of leakers to woods
# Woods : 67
leakers_ids, leakers_names = get_incoming_edges('67')
print("Number of leakers: " + str(len(leakers_ids)))
print ("Leakers: ")
for name in leakers_names:
    print(name, end = " ")

# nx.draw(G, with_labels=True)
# plt.draw()
# plt.show()