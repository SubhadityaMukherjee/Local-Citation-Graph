#%%
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from pyvis.network import Network
import clipboard

# Write Graph to pyvis           
#%%
G = nx.DiGraph()

reader = pd.read_csv("gephi/Edges_titles.csv", delimiter = "\t")
reader.head(3)
for row in reader.itertuples():
    try:
        G.add_edge(row[1], row[2], weight=int(row[3]))
    except ValueError:
        pass

nx.write_graphml(G, "gephi/converted.graphml")

net = Network(
    directed = True,
    filter_menu = True, 
    bgcolor="#222222", font_color="white", select_menu=True,
    layout = True
)
net.show_buttons(filter_=['physics']) # Show part 3 in the plot (optional)
net.from_nx(G) # Create directly from nx graph
net.toggle_physics(True)
net.show('gephi/visualize_graph.html')
#%%
# Mermaid parser
"""```mermaid

graph TD;
E2[DeconvNet] --> E1
E3[Deep_Inside_Convolutional_Networks] --> E1
E1[Guided_BackProp]
"""
#%%
all_names = list(reader["Source"].unique())
all_names.extend(reader["Target"].unique())
# all_names = list(set(list(reader["Source"].values).extend(reader["Target"].values)))
unique_names= {name:f"Node_{i}" for i,name in enumerate(all_names)}
#%%
full_mermaid_string = """
```mermaid
graph TD;
"""
# Create graph entries
all_nodes = list(unique_names.values())
for name in unique_names.keys():
    full_mermaid_string += f"\n{unique_names[name]}[{name}]"

# Iterate over connections
for row in reader.itertuples():
    a,b = unique_names[row[1]] , unique_names[row[2]]
    full_mermaid_string += f"\n{a} --> {b}"

full_mermaid_string += "\n```"
print(full_mermaid_string)
# Copy to clipboard
clipboard.copy(full_mermaid_string)
