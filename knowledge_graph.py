import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node("Student")
G.add_node("CSE")
G.add_node("AI")
G.add_node("Python")

G.add_edge("Student", "CSE")
G.add_edge("Student", "AI")
G.add_edge("AI", "Python")

print("Nodes:")
print(G.nodes())

print("\nEdges:")
print(G.edges())

nx.draw(G, with_labels=True)
plt.show()