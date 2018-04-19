import networkx as nx
import pickle
import matplotlib.pyplot as plt

def centrality_scatter(dict1,dict2):
    # Create figure and drawing axis
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    # Create items and extract centralities
    items1 = sorted(dict1.items())
    items2 = sorted(dict2.items())
    xdata=[b for a,b in items1]
    ydata=[b for a,b in items2]
    # Add each actor to the plot by ID
    for p in range(len(items1)):
        ax1.text(x=xdata[p], y=ydata[p], s=str(items1[p][0]), color="b")


    # use NumPy to calculate the best fit
    # slope, yint = plt.polyfit(xdata,ydata,1)
    # xline = plt.xticks()[0]
    # yline = map(lambda x: slope*x+yint,xline)
    # ax1.plot(xline,yline,ls='--',color='b')

    # Set new x- and y-axis limits
    plt.xlim((0.05,max(xdata)+(.15*max(xdata))))
    plt.ylim((0.05,max(ydata)+(.15*max(ydata))))
    # Add labels and save
    ax1.set_title("Centrality")
    ax1.set_xlabel("In-degree centrality")
    ax1.set_ylabel("Out-degree centrality")
    plt.savefig("Plots/deg_centrality.png")

def highest_K_centrality(cent_dict, K):
    cent_items = [(b, a) for (a, b) in cent_dict.items()]
    cent_items.sort()
    cent_items.reverse() #In decreasing order

    high_cent_items = []
    for i in range(1, len(cent_items)):
        if cent_items[i][0] == cent_items[0][0]:
            high_cent_items.append(cent_items[i])

    # print(" Other nodes with same centrality: ", high_cent_items)
    return tuple(reversed(cent_items[0:K]))


#Main starts here

fh= open("dataset_coded.txt", "rb")
G=nx.read_adjlist(fh, create_using=nx.DiGraph())

f = open("people_ID.txt", "r")
people_ID = pickle.load(open("people_ID.txt", "rb"))

largest_cc = max(nx.strongly_connected_components(G), key=len)
print("Size of largest strongly connected components ", len(largest_cc))

K = 10

#In degree centrality
in_deg_cen = nx.in_degree_centrality(G)
high_inDeg_cen = highest_K_centrality(in_deg_cen, K)

print("Q4---------------------------\n")
print("Top ", K , " influential people (in terms of highest in-degree centrality): \n")

print("\nPeople \t (In-degree, out-degree)")
print("-------------------------------------")
for n in high_inDeg_cen:
    print(people_ID[int(n[1])][1], "\t(", G.in_degree(n[1]), ", ", G.out_degree(n[1]), ")")

#Out degree centrality
out_deg_cen = nx.out_degree_centrality(G)
high_outDeg_cen = highest_K_centrality(out_deg_cen, K)


print("\nTop ", K , " influential people (in terms of highest out-degree centrality): \n")

print("\nPeople \t (In-degree, out-degree)")
print("-------------------------------------")
for n in high_outDeg_cen:
    print(people_ID[int(n[1])][1], "\t(", G.in_degree(n[1]), ", ", G.out_degree(n[1]), ")")

print("--------------------------------")




# print("Out-degree centrality:\t", high_outDeg_cen[0], "=>", high_outDeg_cen[1],  " # edges: ", G.out_degree(high_outDeg_cen[0]))


# centrality_scatter(in_deg_cen, out_deg_cen)

# Eigenvector centrality
# eig_cen = nx.eigenvector_centrality(G)
# high_eig_cen = highest_centrality(eig_cen)
# print("Eigen centrality:\t", high_eig_cen[0], "=>", high_eig_cen[1],  " # edges: ", G.in_degree(high_eig_cen[0]))
