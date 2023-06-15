import turtleParser
import graphvisu
import fredlib
import rdflib

#file = "turtleBerlusconi.ttl"
#turtleParser.turtleParser(file)

#graphviz.graphviz("tbl.ttl")
g = rdflib.Graph()
g.parse("tbl.ttl")
graphvisu.visualize(g)
