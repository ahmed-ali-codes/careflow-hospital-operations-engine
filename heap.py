class EmergencyHeap:
    def __init__(self):
        # Initialize an empty list to represent the heap
        # Each element is a dictionary storing patient details and priority score
        self.heap = []

    def insert(self, pid, urgency, time):
        # Validate that treatment time is positive
        if time <= 0:
            print(" ERROR: Treatment time must be positive.")
            return
        
        # Calculate priority score using given formula:
        # Higher score = higher priority
        # Lower urgency number (more critical) and lower treatment time increase priority
        score = (6 - urgency) + (1000 / time)
        
        # Create a dictionary entry for the patient
        entry = {"id": pid, "score": score, "u": urgency, "t": time}
        
        # Add entry to the end of the heap
        self.heap.append(entry)
        
        # Restore heap property by moving element up
        self._up(len(self.heap) - 1)
        
        # REQUIRED TRACING for the assignment (shows insertion and heap state)
        print(f" TRACE: Inserted Patient {pid} with Priority Score: {score:.2f}")
        print(f" Heap State (Scores): {[round(x['score'], 1) for x in self.heap]}")

    def peek(self):
        """Returns the highest priority element without removing it."""
        # If heap is empty, return None
        if not self.heap:
            return None
        
        # Root of max-heap contains highest priority patient
        return self.heap[0]

    def extract_priority(self):
        """Removes and returns the highest priority patient."""
        # Check if heap is empty
        if not self.heap:
            print(" INFO: Scheduling Queue is empty.")
            return None
        
        # Store root (highest priority patient)
        root = self.heap[0]
        
        # Remove last element from heap
        last = self.heap.pop()
        
        # If heap still has elements, move last to root and restore heap
        if self.heap:
            self.heap[0] = last
            self._down(0)
        
        # REQUIRED TRACING for extraction process
        print(f" TRACE: Extracted Patient {root['id']} for treatment.")
        print(f" Heap State (Scores): {[round(x['score'], 1) for x in self.heap]}")
        
        return root

    def _up(self, i):
        """Standard Max-Heap Percolate Up logic."""
        # Move element up until heap property is satisfied
        while i > 0:
            p = (i - 1) // 2  # Parent index
            
            # If current node has higher score than parent, swap
            if self.heap[i]["score"] > self.heap[p]["score"]:
                self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                i = p  # Continue checking from parent position
            else:
                break  # Heap property satisfied

    def _down(self, i):
        """Standard Max-Heap Percolate Down logic."""
        # Move element down until heap property is restored
        while True:
            max_idx = i
            l, r = 2 * i + 1, 2 * i + 2  # Left and right child indices
            
            # Check if left child exists and has higher score
            if l < len(self.heap) and self.heap[l]["score"] > self.heap[max_idx]["score"]:
                max_idx = l
            
            # Check if right child exists and has higher score
            if r < len(self.heap) and self.heap[r]["score"] > self.heap[max_idx]["score"]:
                max_idx = r
                
            # If a child has higher priority, swap and continue
            if max_idx != i:
                self.heap[i], self.heap[max_idx] = self.heap[max_idx], self.heap[i]
                i = max_idx
            else:
                break  # Heap property restored