from rdflib import Graph, Dataset
from rdflib.extras.external_graph_libs import rdflib_to_networkx_multidigraph
from rdflib.util import guess_format
import networkx as nx
import glob

files = glob.glob("files/*.*")

for f in files:
   print(guess_format(f))

rg = Graph()
rg.parse("http://www.w3.org/People/Berners-Lee/card")

G = rdflib_to_networkx_multidigraph(rg)
print(len(G))

