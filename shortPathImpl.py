# Arquivo test.py
import osmnx as ox
from dijkstra import dijkstra
from geopy.geocoders import Nominatim
import time

def main():
    
    origin = input("Digite o local de origem em Aracaju: ")
    destination = input("Digite o local de destino em Aracaju: ")

    try:
        coord_origin = ox.geocode(origin + ", Aracaju, Brasil")
        coord_destination = ox.geocode(destination + ", Aracaju, Brasil")
    except Exception as e:
        print(f"Erro ao geocodificar: {str(e)}")
        return
    
    G = ox.graph_from_place("Aracaju, Sergipe, Brasil", network_type="drive", simplify=True)
    G = ox.add_edge_bearings(G)

    node_origin = ox.distance.nearest_nodes(G, X=coord_origin[1], Y=coord_origin[0])
    node_destination = ox.distance.nearest_nodes(G, X=coord_destination[1], Y=coord_destination[0])

    nodes = list(G.nodes())
    node_index = {node: int(idx) for idx, node in enumerate(nodes)}
    adj_list = []

    for node in nodes:
        neighbors = []
        for _, neighbor, data in G.edges(node, data=True):
            neighbors.append((node_index[neighbor], data['length']))
        adj_list.append(neighbors)

    start = node_index[node_origin]
    end = node_index[node_destination]
    total_distance, route_idx = dijkstra(adj_list, start=start, end=end)
    nodes_route = [nodes[int(idx)] for idx in route_idx]

    addresses = []
    last_address = None
    geolocator = Nominatim(user_agent="route_details", timeout=10)

    for node_id in nodes_route:
        node_data = G.nodes[node_id]
        lat, lon = node_data['y'], node_data['x']

        try:
            location = geolocator.reverse((lat, lon), exactly_one=True, language='pt')
            address = location.raw.get('address', {})
            current_address = {
                'rua': address.get('road', ''),
                'bairro': address.get('suburb', address.get('neighbourhood', '')),
                'CEP': address.get('postcode', ''),
                'cidade': address.get('city', 'Aracaju')
            }

            if current_address != last_address:
                addresses.append(current_address)
                last_address = current_address
            time.sleep(1)
            
        except Exception as e:
            addresses.append({'rua': 'Endereço não encontrado!'})


    print(f"\nOrigem: {origin} ({coord_origin})")
    print(f"Destino: {destination} ({coord_destination})")
    print(f"Distância total: {total_distance/1000:.2f} km")
    print("\nEndereços completos na rota:")
    
    for idx, endereco in enumerate(addresses, 1):
        print(f"{idx}. {endereco['rua']}, {endereco['bairro']} - CEP {endereco['CEP']}")
    """
    street_names = []

    street_names.append(origin.split(',')[0])
    
    for i in range(len(nodes_route) - 1):
        u, v = nodes_route[i], nodes_route[i+1]
        if G.has_edge(u, v):
            edge_data = G.get_edge_data(u, v)
            for key in edge_data:
                if 'name' in edge_data[key]:
                    name = edge_data[key]['name']
                    if isinstance(name, list):
                        name = name[0]  
                    if name != street_names[-1]:
                        street_names.append(name)
                    break
                    

    street_names.append(destination.split(',')[0])
    
    print(f"Origem: {origin} ({coord_origin})")
    print(f"Destino: {destination} ({coord_destination})")
    print(f"Distância total: {total_distance/1000:.2f} km")
    print("\nRuas percorridas:")
    for name in street_names:
        if name:
            print(f"- {name}")
    """
    


if __name__ == "__main__":
    main()
