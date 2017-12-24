import heapq

class Star:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    @property
    def distance(self):
        return self.x**2 + self.y**2 + self.z**2
        
    def __lt__(self, rhs):
        return self.distance < rhs.distance
        
def find_k_nearest_start(stars, k):
    
    # Init
    reader = csv.reader(stars)
    max_heap = []
    
    # Iterate through the file line by line
    for line in reader:
        star = Star(*map(float, line))
        heapq.heappush(max_heap, (-star.distance, star))
        if len(max_heap) > k:
            heapq.heappop(max_heap)
            
    return [s[1] for s in heapq.nlargest(k, max_heap)]