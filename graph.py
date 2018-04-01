import networkx as nx

fh= open("sample_dataset.txt", "rb")
G=nx.read_adjlist(fh)

print (G.node())