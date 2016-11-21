import foursquare
import fourSquareGraph as lib
import matplotlib.pyplot as plt
import networkx as nx

def main():
    CLIENT_ID = "..."
    CLIENT_SECRET = "..."
    client = foursquare.Foursquare(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    #
    # res = client.venues("4c31a1e26f1fef3b440dec3d")
    # print(res["venue"]["name"])
    # print(res["venue"]["hours"])
    # print(res["venue"]["popular"])
    # print(res["venue"]["location"]["lat"])
    # print(res["venue"]["location"]["lng"])
    #
    # #'ll search by latitude and longitude
    # search = client.venues.explore(params={'ll':'41.89,12.50'})
    # for group in search['groups']:
    #     print(group["name"])
    #     for nv in group['items']:
    #         print(nv["venue"]["name"])
    # print("---------END---------")
    #
    # search = client.venues.explore(params={'near':'Rome,Italy'})
    # for group in search['groups']:
    #     print(group["name"])
    #     for nv in group['items']:
    #         print(nv["venue"]["name"])
    # print("---------END---------")
    #
    # search = client.venues.explore(params={'near':'Rome,Italy','query':'transtevere'})
    # for group in search['groups']:
    #     print(group["name"])
    #     for nv in group['items']:
    #         print(nv["venue"]["name"])
    # print("---------END---------")
    #
    # next_venues = client.venues.nextvenues("4c31a1e26f1fef3b440dec3d")
    # for nv in next_venues['nextVenues']['items']:
    #     print(nv["name"])
    # print("---------END---------")

    G = lib.generate_graph()
    for edge in G.edges():
        print(client.venues(edge[0])["venue"]["name"]," <- is near -> ", client.venues(edge[1])["venue"]["name"])

    plt.clf()
    nx.draw_networkx_nodes(G, nx.get_node_attributes(G, 'pos'),
                           node_size=[s for s in nx.get_node_attributes(G,"size").values()])
    nx.draw_networkx_edges(G, nx.get_node_attributes(G, 'pos'), width=0.2, alpha=0.5)
    plt.show()


if __name__ == "__main__":
    main()
