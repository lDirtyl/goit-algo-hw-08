import heapq

def min_cost_to_connect_cables(cable_len):
    heapq.heapify(cable_len)
    
    total_cost = 0
    
    while len(cable_len) > 1:
        first = heapq.heappop(cable_len)
        second = heapq.heappop(cable_len)
        
        combined = first + second
        
        heapq.heappush(cable_len, combined)
        
        total_cost += combined
    
    return total_cost


cable_len = [30, 10, 40, 20]
print(min_cost_to_connect_cables(cable_len))
