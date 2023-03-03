import rdflib

# Define the namespace and prefix for the entities
ns = rdflib.Namespace("http://geoiot.org/energy#")
prefix = "energy"

# Create a list of entities
entities = ["Time", "Location", "Energy source", "Energy consumption", "Energy production", "Energy demand", "Efficiency", "Cost", "Carbon emissions", "Weather"]

# Create a graph
graph = rdflib.Graph()

# Define the namespace for the geo entities
geo_ns = rdflib.Namespace("http://schema.org/geo#")

# Add nodes for each entity using a for loop
for entity in entities:
    # Use the namespace and prefix to create a unique URI for the entity
    node_uri = ns[prefix + "_" + entity.replace(" ", "_")]
    # Add the node to the graph
    graph.add((node_uri, rdflib.RDF.type, rdflib.RDFS.Class))
    
    # Add properties for the Location entity
    if entity == "Location":
        graph.add((node_uri, rdflib.RDF.type, geo_ns.Point))
        graph.add((node_uri, rdflib.RDFS.label, rdflib.Literal(entity)))
        graph.add((node_uri, geo_ns.latitude, rdflib.Literal(0.0)))
        graph.add((node_uri, geo_ns.longitude, rdflib.Literal(0.0)))

# Serialize the RDF graph in Turtle (ttl) format
print(graph.serialize(format="ttl").decode())

# Serialize the RDF graph in JSON-LD format
context = {"@vocab": str(ns)}
print(graph.serialize(format="json-ld", context=context).decode())

# Retrieve all sites
print("\nRetrieve all sites:")
retrieveAllSiteIds = """
SELECT DISTINCT ?site
WHERE {
    ?site a  geo_ns.Point .
}"""
qres = graph.query(retrieveAllSiteIds, initNs={"geo_ns": geo_ns})
for row in qres:
    print(f"{row.site}")

# Retrieve details of a site
print("\nRetrieve details of a site:")
retrieveSiteDetails = """
SELECT DISTINCT ?p ?v
WHERE {
    ?site a geo_ns.Point ;
          ?p ?v.
}"""
qres = graph.query(retrieveSiteDetails, initNs={"geo_ns": geo_ns}, initBindings={"site": ns[prefix+"_Location"]})
for row in qres:
    print(f"Property: {row.p} - Value: {row.v}")
