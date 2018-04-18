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
    # print("1. Deg count ", [v for v in in_deg_count])
    return in_deg_count, out_deg_count


def plot_graph():
    plt.figure(num=None, figsize=(100, 100), dpi=100, facecolor='w', edgecolor='k')
    # plt.title('Graph')
    nx.draw(G, with_labels=True)
    plt.draw()
    plt.savefig('Plots/graph.png')
    plt.close()

def plot_degree_dist(in_degree_count, out_degree_count):
    plt.figure()
    plt.plot([i for i in range(len(G.nodes()))], in_degree_count, 'ro-')  # in-degree
    plt.plot([i for i in range(len(G.nodes()))], out_degree_count, 'bv-')  # in-degree
    plt.legend(['In-degree', 'Out-degree'])
    plt.xlabel('Degree')
    plt.ylabel('Number of nodes')
    plt.title('In/out degree distribution')
    plt.savefig('Plots/degree_distribution.png')
    plt.close()

def plot_inDegree_dist(in_degree_count):
    plt.figure()
    plt.plot([i for i in range(200)], in_degree_count[:200], 'ro-')  # in-degree
    plt.legend(['In-degree'])
    plt.xlabel('Degree')
    plt.ylabel('Number of nodes')
    plt.title('In degree distribution')
    plt.savefig('Plots/in_degree_dist.png')
    plt.close()

def plot_outDegree_dist(out_degree_count):
    plt.figure()
    plt.plot([i for i in range(200)], out_degree_count[:200], 'bv-')  # in-degree
    plt.legend(['Out-degree'])
    plt.xlabel('Degree')
    plt.ylabel('Number of nodes')
    plt.title('Out degree distribution')
    plt.savefig('Plots/out_degree_dist.png')
    plt.close()

def plot_leakers():
    leakers_ids = pickle.load(open("leakers_ids.pkl", "rb"))
    leakers_names = pickle.load(open("leakers_names.pkl", "rb"))
    print (leakers_ids)
    # str = ""
    # for i in range(len(leakers_ids)):
    #     str += leakers_ids[i] + ":" + leakers_names[i] +", "

    mapping = {127:'MORTON', 257:'WOODS', 355:'BRANCH', 420:'HUDSON', 492:'WEST', 561:'RICHARDSON', 565:'AYERS', 722:'BANKS', 896:'MCDANIEL', 963:'MORENO', 993:'HOWE'}
    # W = nx.relabel_nodes(G, mapping)

    H = G.subgraph(leakers_ids)
    plt.figure()
    plt.title('Subgraph consisting leakers (and WOODS)')
    nx.draw(H, with_labels=True)
    # plt.legend("Leakers")
    # plt.xlabel('Degree')
    # plt.ylabel('Number of nodes')
    plt.draw()
    plt.savefig('Plots/leakers.png')
    plt.close()

def plot_cliques():
    clique3 = pickle.load(open("clique3.pkl", "rb"))
    print("Cliques: ", len(clique3), " : ", clique3)
    clique3_nodes = set(clique3[0])
    for c in range(1, len(clique3)):
        clique3_nodes = clique3_nodes.union(set(clique3[c]))

    clique3_nodes = [str(n) for n in list(clique3_nodes)]
    print(clique3_nodes)

    # H = G.subgraph([str(n) for n in clique3[0]])
    H = G.subgraph(clique3_nodes)
    plt.figure(num=None, figsize=(80, 60), dpi=100, facecolor='w', edgecolor='k')
    # plt.title('Subgraph consisting largest sized cliques')
    nx.draw(H, with_labels=True)
    plt.draw()
    plt.savefig('Plots/all_cliques.png')
    plt.close()

def plot_one_clique():
    clique3 = pickle.load(open("clique3.pkl", "rb"))
    # print(clique3)
    clique3_nodes = set(clique3[0])
    for c in range(1, len(clique3)):
        clique3_nodes = clique3_nodes.union(set(clique3[c]))

    clique3_nodes = [str(n) for n in list(clique3_nodes)]
    print(clique3_nodes)

    H = G.subgraph([str(n) for n in clique3[0]])
    plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
    plt.title('One clique example (from network)')
    nx.draw(H, with_labels=True)
    plt.draw()
    plt.savefig('Plots/example_clique.png')
    plt.close()

def plot_butterfly():
    butterly = pickle.load(open("butterfly.pkl", "rb"))
    print("Butterfly: ", len(butterly), " : " , butterly)

    butterfly_nodes = set(butterly[0])
    for c in range(1, len(butterly)):
        butterfly_nodes = butterfly_nodes.union(set(butterly[c]))

    butterfly_nodes = [str(n) for n in list(butterfly_nodes)]
    # print(butterfly_nodes)

    H = G.subgraph(butterfly_nodes)
    plt.figure(num=None, figsize=(80, 60), dpi=100, facecolor='w', edgecolor='k')
    # plt.title('Butterfly')
    nx.draw(H, with_labels=True)
    plt.draw()
    plt.savefig('Plots/butterfly.png')
    plt.close()

def plot_one_butterfly():
    butterly = pickle.load(open("butterfly.pkl", "rb"))
    # print(butterly)

    butterfly_nodes = set(butterly[0])
    for c in range(1, len(butterly)):
        butterfly_nodes = butterfly_nodes.union(set(butterly[c]))

    butterfly_nodes = [str(n) for n in list(butterfly_nodes)]
    # print(butterfly_nodes)

    H = G.subgraph([str(n) for n in butterly[0]])
    plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
    # plt.title('Butterfly')
    nx.draw(H, with_labels=True)
    plt.draw()
    plt.savefig('Plots/example_butterfly.png')
    plt.close()



def plot_centrality():
    inDeg_cen = nx.in_degree_centrality(G)

fh= open("dataset_coded.txt", "rb")
G=nx.read_adjlist(fh, create_using=nx.DiGraph())

in_degree_count, out_degree_count = degree_count()
print(in_degree_count)
print(out_degree_count)
print(max(in_degree_count))
# plot_degree_dist(in_degree_count, out_degree_count)

# plot_graph()
# plot_inDegree_dist(in_degree_count)
# plot_outDegree_dist(out_degree_count)
# plot_leakers()
# plot_cliques()
# plot_one_clique()

plot_butterfly()
plot_one_butterfly()

# plot_centrality()
