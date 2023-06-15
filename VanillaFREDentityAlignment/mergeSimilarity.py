from rdflib import Graph, Literal, RDF, URIRef
# rdflib knows about quite a few popular namespaces, like W3C ontologies, schema.org etc.
from rdflib.namespace import FOAF , XSD



def mergeSimilarity(file):
    # Create a Graph
    g = Graph()

    # Parse in an RDF file hosted on the Internet
    g.parse(file)

    # Loop through each triple in the graph (subj, pred, obj)
    for subj, pred, obj in g:
        # Check if there is at least one triple in the Graph
        if (subj, pred, obj) not in g:
           raise Exception("It better be!")
    g.serialize(format="turtle")
    # Print the number of "triples" in the Graph
    #print(f"Graph g has {len(g)} statements.")
    # Prints: Graph g has 86 statements.

    # Print out the entire Graph in the RDF Turtle format
    #print(g.serialize(format="turtle"))

    # Add triples using store's add() method.
    #g.add((donna, RDF.type, FOAF.Person))
    #g.add((donna, FOAF.nick, Literal("donna", lang="en")))
    #g.add((donna, FOAF.name, Literal("Donna Fales")))
    #g.add((donna, FOAF.mbox, URIRef("mailto:donna@example.org")))