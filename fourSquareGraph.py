import networkx as nx
import foursquare
import math

#distance between two points: sqrt((y1 - y0)^2 + (x1 - x0)^2)
def venues_distance(v1,v2):
    y1 = v1["pos"][0]
    x1 = v1["pos"][1]
    y2 = v2["pos"][0]
    x2 = v2["pos"][1]
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


def generate_graph():
    CLIENT_ID = "..."
    CLIENT_SECRET = "..."
    client = foursquare.Foursquare(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

    G = nx.Graph()
    search = client.venues.explore(params={'near':'Rome,Italy'})
    for group in search['groups']:
        #creates all the nodes
        for venue in group['items']:
            G.add_node(venue["venue"]["id"],
                       id=venue["venue"]["id"],
                       name=venue["venue"]["name"],
                       pos=(venue["venue"]["location"]["lat"],venue["venue"]["location"]["lng"]),
                       country=venue["venue"]["location"]["country"],
                       size=10)

        #creates the edges between next venues
        for venue in group['items']:
            nextVenues = client.venues.nextvenues(venue["venue"]["id"])
            for nextvenue in nextVenues["nextVenues"]["items"]:
                v1 = G.node[venue["venue"]["id"]]
                if(nextvenue["id"] in G):
                    v2 = G.node[nextvenue["id"]]
                    G.add_edge(v1["id"], v2["id"], distance=venues_distance(v1, v2))
    return G
