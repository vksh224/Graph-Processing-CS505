import networkx as nx
import matplotlib.pyplot as plt
import pickle

#In or Out-degree distribution
def degree_count():
    in_deg_count = [0 for i in range(len(G.nodes()))]
    out_deg_count = [0 for i in range(len(G.nodes()))]

    for n in G.nodes():
        in_deg_count [G.in_degree(n)] += 1
        out_deg_count[G.out_degree(n)] += 1
    print("1. Deg count ", [v for v in in_deg_count])
    return in_deg_count, out_deg_count


def plot_degree_dist(in_degree_count, out_degree_count):
    plt.figure()
    plt.plot([i for i in range(len(G.nodes()))], in_degree_count, 'ro-')  # in-degree
    plt.plot([i for i in range(len(G.nodes()))], out_degree_count, 'bv-')  # in-degree
    plt.legend(['In-degree', 'Out-degree'])
    plt.xlabel('Degree')
    plt.ylabel('Number of nodes')
    plt.title('In/out degree distribution')
    plt.savefig('degree_distribution.png')
    plt.close()

def plot_leakers():
    leakers_ids = pickle.load(open("leakers_ids.pkl", "rb"))
    leakers_names = pickle.load(open("leakers_names.pkl", "rb"))

    str = ""
    for i in range(len(leakers_ids)):
        str += leakers_ids[i] + ":" + leakers_names[i] +", "

    mapping = {127:'MORTON', 257:'WOODS', 355:'BRANCH', 420:'HUDSON', 492:'WEST', 561:'RICHARDSON', 565:'AYERS', 722:'BANKS', 896:'MCDANIEL', 963:'MORENO', 993:'HOWE'}
    # W = nx.relabel_nodes(G, mapping)

    H = G.subgraph(leakers_ids)
    plt.figure()
    nx.draw(H, with_labels=True)
    plt.draw()
    plt.savefig('leakers.png')
    plt.close()

def plot_cliques():
    clique3 = pickle.load(open("clique3.pkl", "rb"))
    

fh= open("dataset_coded.txt", "rb")
G=nx.read_adjlist(fh, create_using=nx.DiGraph())

# in_degree_count, out_degree_count = degree_count()
# plot_degree_dist(in_degree_count, out_degree_count)
plot_leakers()
plot_cliques()
