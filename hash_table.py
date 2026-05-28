class HashTable:
    """
    Hash Table with Linear Probing for patient record storage.
    Supports ~20+ records with resizing logic.
    """
    def __init__(self, size=31): # Prime size for better distribution.
        # Initialize hash table size, storage array, and element count
        self.size = size
        self.table = [None] * size  # Array to store patient records
        self.count = 0              # Number of stored records
        self.deleted = object()     # Special marker for deleted slots

    def _hash(self, key):
        # Simple hash function using modulo operation
        return key % self.size

    def _resize(self):
        """Resizes table when load factor > 0.7 """
        # Save old table
        old_table = self.table
        
        # Increase table size (approximate next prime)
        self.size = self.size * 2 + 1
        
        # Create new empty table and reset count
        self.table = [None] * self.size
        self.count = 0
        
        # Reinsert all existing (non-deleted) records into new table
        for item in old_table:
            if item and item != self.deleted:
                self.insert(item)

    def insert(self, patient):
        # Resize if load factor exceeds 0.7
        if self.count / self.size > 0.7:
            self._resize()
        
        # Compute initial index using hash
        index = self._hash(patient.patientID)
        start = index  # Store starting index to detect full cycle
        probe_sequence = [index]  # Track indices visited during probing

        # Linear probing: move to next slot if collision occurs
        while self.table[index] not in (None, self.deleted):
            # If same patient ID exists, update record
            if self.table[index].patientID == patient.patientID:
                self.table[index] = patient  # Replace existing record
                print(f"Updated existing record at index {index}")
                return True
            
            # Collision occurred, move to next index
            print(f"Collision at {index}, trying {(index + 1) % self.size}...")
            index = (index + 1) % self.size
            
            # If we return to start, table is full
            if index == start:
                print("Table is full. Insert failed.")
                return False
            
            probe_sequence.append(index)

        # Insert patient into found empty/deleted slot
        if len(probe_sequence) > 1:
            print(f"Probe sequence: {probe_sequence}")
            print(f"Inserted at index {index}")
        
        self.table[index] = patient
        self.count += 1  # Increase stored record count
        return True

    def search(self, pid):
        # Find patient record by patient ID
        index = self._hash(pid)
        start = index
        
        # Traverse table using linear probing
        while self.table[index] is not None:
            # Check if matching and not deleted
            if self.table[index] != self.deleted and self.table[index].patientID == pid:
                return self.table[index]
            
            # Move to next index
            index = (index + 1) % self.size
            
            # Stop if full loop completed
            if index == start: break
        return None  # Not found

    def delete(self, pid):
        # Remove patient record by marking slot as deleted
        index = self._hash(pid)
        start = index
        
        # Traverse table using linear probing
        while self.table[index] is not None:
            # If matching record found
            if self.table[index] != self.deleted and self.table[index].patientID == pid:
                self.table[index] = self.deleted  # Mark as deleted
                self.count -= 1  # Decrease count
                return True
            
            # Move to next index
            index = (index + 1) % self.size
            
            # Stop if full loop completed
            if index == start: break
        return False  # Record not found