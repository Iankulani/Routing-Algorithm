# -*- coding: utf-8 -*-
"""
Created on Tue Feb 4 08:27:25 2025

@author: IAN CARTER KULANI

"""

import time

# Simulating a basic ad hoc network
class Node:
    def __init__(self, mac_address):
        self.mac_address = mac_address
        self.routing_table = {}  # Will hold the routes to other nodes
    
    def add_route(self, destination_mac, next_hop_mac):
        self.routing_table[destination_mac] = next_hop_mac
    
    def send_packet(self, destination_mac, packet_data):
        if destination_mac in self.routing_table:
            next_hop = self.routing_table[destination_mac]
            print(f"Sending packet to {destination_mac} via next hop {next_hop}")
            # Simulate packet transfer delay
            time.sleep(1)
            print(f"Packet delivered to {destination_mac}: {packet_data}")
        else:
            print(f"Route not found for {destination_mac}. Broadcasting for route discovery.")
            self.route_discovery(destination_mac, packet_data)
    
    def route_discovery(self, destination_mac, packet_data):
        print(f"Node {self.mac_address} initiating route discovery for {destination_mac}...")
        # Simulate route discovery process
        time.sleep(2)
        print(f"Route discovered! Adding route to routing table.")
        self.add_route(destination_mac, destination_mac)  # Direct route for simplicity
        print(f"Route to {destination_mac} is {destination_mac}")
        self.send_packet(destination_mac, packet_data)

def get_mac_address_input():
    mac_address = input("Enter MAC Address of the node:")
    return mac_address

def main():
    # Example ad hoc network setup
    print("Welcome to the Ad Hoc Network Routing Simulation!")
    
    # Get MAC addresses for nodes
    source_mac = get_mac_address_input()
    destination_mac = get_mac_address_input()

    # Create nodes
    source_node = Node(source_mac)
    destination_node = Node(destination_mac)

    # Simulate basic routing between nodes
    source_node.add_route(destination_mac, destination_mac)  # Direct route for simplicity
    
    # Send packet from source node to destination node
    packet_data = "Hello, this is a test packet!"
    source_node.send_packet(destination_mac, packet_data)

if __name__ == "__main__":
    main()
