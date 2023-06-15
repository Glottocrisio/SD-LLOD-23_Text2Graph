import rdflib
from rdflib.extras.external_graph_libs import rdflib_to_networkx_multidigraph
import networkx as nx
import matplotlib.pyplot as plt
from rdflib import Graph
import io
import pydotplus
from IPython.display import display, Image
from rdflib.tools.rdf2dot import rdf2dot
import graphviz


def graphviz(file = "tbl.ttl"):
	#url = 'https://github.com/Glottocrisio/IKG4CH/blob/main/turtleBerlusconiManual.ttl'

	g = rdflib.Graph()
	result = g.parse(file, format='turtle')

	G = rdflib_to_networkx_multidigraph(result)

	# Plot Networkx instance of RDF Graph
	pos = nx.spring_layout(G, scale=2)
	edge_labels = nx.get_edge_attributes(G, 'r')
	nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
	nx.draw(G, with_labels=True)

	#if not in interactive mode for 
	plt.show()


def visualize(g):
	
    stream = io.StringIO()
    rdf2dot(g, stream, opts = {display})
    dg = pydotplus.graph_from_dot_data(stream.getvalue())
    png = dg.create_png()
    display(Image(png))

