from django.db import models
import json

class Site(models.Model):
    name = models.CharField(max_length=100)
    timezone = models.CharField(max_length=50)
    average_cost_kwh = models.FloatField()
    unit_cost = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_sub_site = models.BooleanField()
    short_name = models.CharField(max_length=50, blank=True)
    efficiency_index = models.FloatField(null=True, blank=True)
    size_mq = models.IntegerField()
    size_mc = models.IntegerField()
    max_power_w = models.IntegerField()
    max_power_over_time = models.CharField(max_length=50, blank=True)
    max_daily_energy_wh = models.IntegerField()
    target_daily_generation_w = models.IntegerField()
    max_power_generation_w = models.IntegerField()
    contract_power_w = models.IntegerField(null=True, blank=True)
    target_daily_fedout_wh = models.IntegerField()
    max_daily_fedin_wh = models.IntegerField()
    max_daily_self_consumption_wh = models.IntegerField()
    target_power_fedout_w = models.IntegerField()
    max_power_fedin_w = models.IntegerField()
    max_power_self_consumption_w = models.IntegerField()
    stake_id = models.CharField(max_length=50, blank=True)
    etag = models.IntegerField()
    _id = models.CharField(max_length=50)
    lat = models.FloatField()
    lng = models.FloatField()

def create_sites_from_json(json_data):
    sites = []
    for site_data in json_data['sites']:
        site = Site(
            name=site_data['name'],
            timezone=site_data['timezone'],
            average_cost_kwh=site_data['averageCostKWh'],
            unit_cost=site_data['unitCost'],
            address=site_data['address'],
            description=site_data['description'],
            is_sub_site=site_data['isSubSite'],
            short_name=site_data['shortName'],
            efficiency_index=site_data['efficiencyIndex'],
            size_mq=site_data['sizeMq'],
            size_mc=site_data['sizeMc'],
            max_power_w=site_data['maxPowerW'],
            max_power_over_time=site_data['maxPowerOverTime'],
            max_daily_energy_wh=site_data['maxDailyEnergyWh'],
            target_daily_generation_w=site_data['targetDailyGenerationW'],
            max_power_generation_w=site_data['maxPowerGenerationW'],
            contract_power_w=site_data['contractPowerW'],
            target_daily_fedout_wh=site_data['targetDailyFedoutWh'],
            max_daily_fedin_wh=site_data['maxDailyFedinWh'],
            max_daily_self_consumption_wh=site_data['maxDailySelfConsumptionWh'],
            target_power_fedout_w=site_data['targetPowerFedoutW'],
            max_power_fedin_w=site_data['maxPowerFedinW'],
            max_power_self_consumption_w=site_data['maxPowerSelfConsumptionW'],
            stake_id=site_data['stakeId'],
            etag=site_data['etag'],
            _id=site_data['_id'],
            lat=site_data['lat'],
            lng=site_data['lng'],
        )
json_data = '{"sites": [{"name": "Keele University", "timezone": "Europe/London", "averageCostKWh": 0.15, "unitCost": "GBP", "address": "", "description": "", "isSubSite": false, "shortName": "", "efficiencyIndex": null, "sizeMq": 0, "sizeMc": 0, "maxPowerW": 305000, "maxPowerOverTime": null, "maxDailyEnergyWh": 7398000, "targetDailyGenerationW": 70200000, "maxPowerGenerationW": 300000, "contractPowerW": null, "targetDailyFedoutWh": 0, "maxDailyFedinWh": 0, "maxDailySelfConsumptionWh": 0, "targetPowerFedoutW": 0, "maxPowerFedinW": 0, "maxPowerSelfConsumptionW": 0, "stakeId": null, "etag": 1, "_id": "monet::"5c373d2ea23197005e5dd48f"}]}'

sites = create_sites_from_json(json_data)
import json
import rdflib

json_data = """
{
    "sites": [
        {
            "name": "Keele University",
            "timezone": "Europe/London",
            "averageCostKWh": 0.15,
            "unitCost": "GBP",
            "address": "",
            "description": "",
            "isSubSite": false,
            "shortName": "",
            "efficiencyIndex": null,
            "sizeMq": 0,
            "sizeMc": 0,
            "maxPowerW": 305000,
            "maxPowerOverTime": null,
            "maxDailyEnergyWh": 7398000,
            "targetDailyGenerationW": 70200000,
            "maxPowerGenerationW": 300000,
            "contractPowerW": null,
            "targetDailyFedoutWh": 0,
            "maxDailyFedinWh": 0,
            "maxDailySelfConsumptionWh": 0,
            "targetPowerFedoutW": 0,
            "maxPowerFedinW": 0,
            "maxPowerSelfConsumptionW": 0,
            "stakeId": null,
            "etag": 1,
            "_id": "monet::5c373d2ea23197005e5dd48f",
            "lat": 53.004352,
            "lng": -2.267431
        },
        {
            "name": "University of Manchester",
            "timezone": "Europe/London",
            "averageCostKWh": 0.12,
            "unitCost": "GBP",
            "address": "",
            "description": "",
            "isSubSite": false,
            "shortName": "",
            "efficiencyIndex": null,
            "sizeMq": 0,
            "sizeMc": 0,
            "maxPowerW": 600000,
            "maxPowerOverTime": null,
            "maxDailyEnergyWh": 14796000,
            "targetDailyGenerationW": 14040000,
            "maxPowerGenerationW": 600000,
            "contractPowerW": null,
            "targetDailyFedoutWh": 0,
            "maxDailyFedinWh": 0,
            "maxDailySelfConsumptionWh": 0,
            "targetPowerFedoutW": 0,
            "maxPowerFedinW": 0,
            "maxPowerSelfConsumptionW": 0,
            "stakeId": null,
            "etag": 1,
            "_id": "monet::5c373d2ea23197005e5dd490",
            "lat": 53.466734,
            "lng": -2.233875
        }
    ]
}

"""

# Parse the JSON data
data = json.loads(json_data)

# Create an RDF graph
g = rdflib.Graph()

# Iterate through the sites data
for site_data in data['sites']:
    # Create a blank node for the site
    site = rdflib.BNode()

    # Add triples to the graph for each property of the site
    g.add((site, rdflib.URIRef('http://schema.org/name'), rdflib.Literal(site_data['name'])))
    g.add((site, rdflib.URIRef('http://schema.org/timezone'), rdflib.Literal(site_data['timezone'])))
    g.add((site, rdflib.URIRef('http://schema.org/averageCostKWh'), rdflib.Literal(site_data['averageCostKWh'])))
    g.add((site, rdflib.URIRef('http://schema.org/unitCost'), rdflib.Literal(site_data['unitCost'])))
    g.add((site, rdflib.URIRef('http://schema.org/address'), rdflib.Literal(site_data['address'])))
    g.add((site, rdflib.URIRef('http://schema.org/description'), rdflib.Literal(site_data['description'])))

    g.add((site, rdflib.URIRef('http://schema.org/isSubSite'), rdflib.Literal(site_data['isSubSite'])))
    g.add((site, rdflib.URIRef('http://schema.org/shortName'), rdflib.Literal(site_data['shortName'])))
    g.add((site, rdflib.URIRef('http://schema.org/efficiencyIndex'), rdflib.Literal(site_data['efficiencyIndex'])))
    g.add((site, rdflib.URIRef('http://schema.org/_id'), rdflib.Literal(site_data['sizeMq'])))
    g.add((site, rdflib.URIRef('http://schema.org/lat'), rdflib.Literal(site_data['address'])))
    g.add((site, rdflib.URIRef('http://schema.org/lng'), rdflib.Literal(site_data['description'])))
# Perform a SPARQL query to get the description of all address in the graph
query = """
    PREFIX ex: <http://schema.org/>
    SELECT ?address
    WHERE {
        ?address a ex:address .
        ?address ex:description ?description .
    }
"""
results = g.query(query)
// Create a RDF graph
g = rdflib.Graph()
// Add triples to the graph
g.add((rdflib.URIRef('http://example.org/John'), rdflib.URIRef('http://example.org/age'), rdflib.Literal(42)))
g.add((rdflib.URIRef('http://example.org/John'), rdflib.URIRef('http://example.org/age'), rdflib.Literal(42)))
g.add((rdflib.URIRef('http://example.org/John'), rdflib.URIRef('http://example.org/age'), rdflib.Literal(42)))
