from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDFS, XSD, RDF
from rdflib.plugins.sparql import prepareQuery

GEOIOT=Namespace("http://geoiot.org/")
SCHEMA=Namespace("https://schema.org/")
SEND=Namespace("http://energykit.deop.siemens.com/send/")

g = Graph()
g.bind("geoiot", GEOIOT)
g.bind("schema", SCHEMA)
g.bind("send", SEND)

g.add((GEOIOT.site, RDFS.subClassOf, SCHEMA.Place))

crb = URIRef("http://energykit.deop.siemens/send/crb")
g.add((crb, RDF.type, GEOIOT.Site))
g.add((crb, RDFS.label, Literal("Colin Reeves Building")))
g.add((crb, GEOIOT.averageCost, Literal(4)))
g.add((crb, GEOIOT.averageCostUnit, GEOIOT.kwh))
g.add((crb, SCHEMA.latitude, Literal(1)))
g.add((crb, SCHEMA.longitude, Literal(3)))

su = URIRef("http://energykit.deop.siemens.com/send/su")
g.add((su, RDF.type, GEOIOT.Site))
g.add((su, RDFS.label, Literal("Student Union")))
g.add((su, GEOIOT.averageCost, Literal(4)))
g.add((su, GEOIOT.averageCostUnit, GEOIOT.kwh))
g.add((su, SCHEMA.latitude, Literal(2)))
g.add((su, SCHEMA.longitude, Literal(4)))

library = URIRef("http://energykit.deop.siemens.com/send/Library")
g.add((library, RDF.type, GEOIOT.Site))
g.add((library, RDFS.label, Literal("Library")))
g.add((library, GEOIOT.timezone, Literal("Europe/London")))
g.add((library, GEOIOT.averageCost, Literal(0.15)))
g.add((library, GEOIOT.averageCostUnit, GEOIOT.kwh))
g.add((library, GEOIOT.unitCost, GEOIOT.GBP))
g.add((library, RDFS.comment, Literal("--")))
g.add((library, GEOIOT.isSubSite, Literal("false")))
#g.add((library, GEOIOT.areaSize, Literal("0")))
#g.add((library, GEOIOT.areaSizeUnit, Literal("Mq")))
g.add((library, GEOIOT.maxPower, Literal("305000")))
g.add((library, GEOIOT.maxPowerUnit, GEOIOT.W))
#g.add((library, GEOIOT.maxPowerOverTime, GEOIOT.W))
g.add((library, GEOIOT.maxDailyEnergy, Literal("4000000")))
g.add((library, GEOIOT.maxDailyEnergyUnit, GEOIOT.Wh))
g.add((library, GEOIOT.targetDailyGeneration, Literal("0")))
g.add((library, GEOIOT.targetDailyGenerationUnit, GEOIOT.W))
#g.add((library, GEOIOT.contractPower, Literal("0")))
#g.add((library, GEOIOT.contractPowerUnit, GEOIOT.W))

print(g.serialize(format="ttl").decode())

context = {"@vocab": GEOIOT, "@language": "en"}
print(g.serialize(format="json-ld", context=context).decode())
#print(g.serialize(format="json-ld", context=dict(g.namespaces())))

print ("\r\nRetrieve all sites:")

retrieveAllSiteIds = """
SELECT ?building
WHERE {
    ?building a geoiot:Site .
}
"""


