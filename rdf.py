from rdflib import Graph as RDFGraph, Dataset
from rdflib.extras.external_graph_libs import rdflib_to_networkx_multidigraph
import networkx as nx
import time, glob


files = glob.glob("f_jsonld/*.jsonld")


