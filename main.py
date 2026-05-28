import random
import time
from graph import HospitalGraph
from hash_table import HashTable
from heap import EmergencyHeap
from sorting import merge_sort, quick_sort
from patient import Patient

def get_int(msg):
    """To ensure valid integer input and handle non-numeric errors."""
    while True:
        try:
            val = int(input(msg))  # Try converting user input to integer
            return val
        except ValueError:
            # If conversion fails, show error and ask again
            print(" INVALID INPUT: Please enter a number (integer).")

def main():
    # Initialize the four core modules of the system
    g = HospitalGraph()   # Graph for hospital navigation
    h = HashTable()       # Hash table for patient records
    heap = EmergencyHeap()  # Heap for emergency scheduling

    while True:
        # Main menu display
        print("\n" + "="*40)
        print("   HOSPITAL RESOURCE MANAGEMENT SYSTEM")
        print("="*40)
        print("1. Module 1: Hospital Navigation (Graph)")
        print("2. Module 2: Patient Records (Hash Table)")
        print("3. Module 3: Emergency Scheduling (Heap)")
        print("4. Module 4: Sorting & Performance Analysis")
        print("0. Exit")
        ch = input("Select Module: ")

        # --- MODULE 1: GRAPH ---
        if ch == "1":
            print("\n-- [Module 1: Navigation Menu] --")
            print("1. Add Dept | 2. Add Corridor | 3. BFS (Levels) | 4. DFS (Cycle Check) | 5. Dijkstra | 6. View Map")
            c = input("Choice: ")
            
            if c == "1":
                # Add a new department node
                names = input("Enter Department Names (comma-separated): ").strip()

                # Split input by comma
                dept_list = names.split(",")

                added = []

                for dept in dept_list:
                    dept = dept.strip()  # remove extra spaces
                    if dept:
                        g.add_department(dept)
                        added.append(dept)

                print("\n" f" SUCCESS: Added Departments: {', '.join(added)}")
            
            elif c == "2":
                print("Enter corridors in format: Dept1-Dept2-Time")

                data = input("Enter corridors: ").strip()
                corridors = data.split(",")

                added = []

                for item in corridors:
                    try:
                        u, v, w = item.strip().split("-")
                        u, v = u.strip(), v.strip()
                        w = int(w.strip())

                        if u not in g.adj_list or v not in g.adj_list:
                            print(f" ERROR: '{u}' or '{v}' not found.")
                            continue

                        if w <= 0:
                            print(f" ERROR: Invalid weight for {u}-{v}. Must be positive.")
                            continue

                        g.add_corridor(u, v, w)
                        added.append(f"{u}<->{v} ({w})")

                    except ValueError:
                        print(f" ERROR: Invalid format → {item}")

                if added:
                    print(" SUCCESS: Added Corridors:")
                    for c in added:
                        print("  -", c)
            
            elif c == "3":
                # Perform BFS traversal and show levels
                start = input("Start Point for BFS: ").strip()
                levels = g.bfs_levels(start)
                if isinstance(levels, dict):
                    print("\n--- Reachable Departments by Hops ---")
                    for lvl, depts in levels.items():
                        print(f"Level {lvl}: {', '.join(depts)}")
                else:
                    print(f" {levels}")
            
            elif c == "4":
                # Detect cycles using DFS
                found, nodes = g.detect_cycle_dfs()
                if found:
                    print(f" ALERT: Cycle detected! Path: {nodes}")
                else:
                    print(" No cycles (loops) found in the current map.")
            
            elif c == "5":
                # Find shortest path using Dijkstra's algorithm
                start, end = input("From: ").strip(), input("To: ").strip()
                path, cost = g.dijkstra(start, end)
                if path:
                    print(f" OPTIMAL PATH: {' -> '.join(path)} ({cost} mins)")
                else:
                    print(f" ERROR: No path exists between '{start}' and '{end}'.")
            
            elif c == "6":
                # Display full hospital map (adjacency list)
                print("\n--- Current Hospital Map ---")
                if not g.adj_list: 
                    print("Map is empty.")
                for dept, neighbors in g.adj_list.items():
                    print(f"{dept:15} connects to: {neighbors}")
            else:
                print(f" INVALID CHOICE: '{c}' is not an option in Module 1.")

        # --- MODULE 2: HASH TABLE ---
        elif ch == "2":
            print("\n-- [Module 2: Patient Records] --")
            print("1. Register | 2. Search | 3. Delete | 4. Table Status")
            c = input("Choice: ")
            
            if c == "1":
                print("Enter multiple patients (comma-separated)")
                print("Format: ID-Name-Age-Dept-Urgency")

                data = input("Enter patients: ").strip()

                entries = data.split(",")

                for entry in entries:
                    try:
                        pid, name, age, dept, urg = entry.strip().split("-")

                        pid = int(pid)
                        age = int(age)
                        urg = int(urg)

                        if dept not in g.adj_list:
                            print(f" ERROR: Department '{dept}' does not exist.")
                            continue

                        p = Patient(pid, name, age, dept, urg)

                        if h.insert(p):
                            print(f" SUCCESS: Patient {pid} ('{name}') registered.")

                    except Exception:
                        print(f" ERROR: Invalid format -> {entry}")
            
            elif c == "2":
                # Search for a patient by ID
                pid = get_int("Search ID: ")
                res = h.search(pid)
                print(f" RESULT: {res}" if res else f" ERROR: ID {pid} not found.")
            
            elif c == "3":
                # Delete a patient record
                pid = get_int("Delete ID: ")
                if h.delete(pid):
                    print(f" SUCCESS: ID {pid} removed.")
                else:
                    print(f" ERROR: Could not find ID {pid} to delete.")
            
            elif c == "4":
                # Display hash table statistics
                load = h.count / h.size
                print(f"\n--- Table Stats ---")
                print(f"Patients: {h.count} / {h.size} | Load: {load:.2%}")
            else:
                print(f" INVALID CHOICE: '{c}' is not an option in Module 2.")

        # --- MODULE 3: HEAP ---
        elif ch == "3":
            print("\n-- [Module 3: Emergency Scheduling] --")
            print("1. Add to Queue | 2. Peek Next | 3. Extract Next | 4. View Heap State | 5. Update Urgency")
            c = input("Choice: ")
            
            if c == "1":
                # Add a patient to emergency queue
                pid = get_int("Enter Patient ID: ")
                p = h.search(pid)
                if p:
                    t = get_int("Est. Treatment Time (mins): ")
                    heap.insert(pid, p.urgency, t)
                    print(f" SUCCESS: Patient {pid} moved to priority queue.")
                else:
                    print(" ERROR: Patient must be registered in Module 2 first.")
            
            elif c == "2":
                # View highest priority patient without removing
                nxt = heap.peek()
                if nxt:
                    print(f" NEXT UP: ID {nxt['id']} | Priority Score: {nxt['score']:.2f}")
                else:
                    print(" INFO: Emergency queue is empty.")
            
            elif c == "3":
                # Remove highest priority patient
                heap.extract_priority()
            
            elif c == "4":
                # Display current heap state
                scores = [round(x['score'], 2) for x in heap.heap]
                print(f" Current Heap Scores: {scores}")
            
            elif c == "5":
                pid = get_int("Enter Patient ID to update: ")
                p = h.search(pid)

                if not p:
                    print(" ERROR: Patient not found.")
                    continue

                new_urg = get_int("Enter NEW urgency (1-Highest to 5-Lowest): ")
                t = get_int("Enter updated treatment time (mins): ")

                # Update in hash table
                p.urgency = new_urg  

                # STEP 1: Remove old entry from heap
                heap.heap = [item for item in heap.heap if item["id"] != pid]

                # STEP 2: Rebuild heap using own logic
                for i in range(len(heap.heap)//2, -1, -1):
                    heap._down(i)

                # STEP 3: Insert updated entry
                heap.insert(pid, new_urg, t)

                print(f" SUCCESS: Patient {pid} urgency updated and reinserted into queue.")
            else:
                print(f" INVALID CHOICE: '{c}' is not an option in Module 3.")
                        

        # --- MODULE 4: SORTING & PERFORMANCE ---
        elif ch == "4":
            print("\n-- [Module 4: Sorting & Performance Analysis] --")
            print("1. Run Benchmarks (Efficiency Analysis)")
            print("2. Generate Treatment Report (Sorted by Duration)")
            sub_ch = input("Choice: ")

            if sub_ch == "1":
                # Run performance benchmarks for sorting algorithms
                print("\n" + "-"*65)
                print(f"{'Size':<6} | {'Condition':<15} | {'Merge Sort':<12} | {'Quick Sort':<12}")
                print("-"*65)
                
                for n in [100, 500, 1000]:
                    # Generate random dataset
                    data_r = [random.randint(1, 10000) for _ in range(n)]
                    
                    # Create nearly sorted dataset
                    data_s = merge_sort(data_r[:]) 
                    for _ in range(n // 10): 
                        i1, i2 = random.randint(0, n-1), random.randint(0, n-1)
                        data_s[i1], data_s[i2] = data_s[i2], data_s[i1]
                    
                    # Create reversed dataset
                    data_rev = []
                    for i in range(n, 0, -1):
                        data_rev.append(i)

                    datasets = [("Random", data_r), ("Nearly Sorted", data_s), ("Reversed", data_rev)]

                    for label, dataset in datasets:
                        # Measure Merge Sort time
                        m_arr = list(dataset)
                        start = time.time()
                        merge_sort(m_arr)
                        tm = time.time() - start

                        # Measure Quick Sort time
                        q_arr = list(dataset)
                        start = time.time()
                        quick_sort(q_arr)
                        tq = time.time() - start
                        
                        print(f"{n:<6} | {label:<15} | {tm:.5f}s     | {tq:.5f}s")
                
                print("\n-> ANALYSIS: Quick Sort is generally faster for random data,")
                print("   but Merge Sort provides O(n log n) stability for all cases.")

            elif sub_ch == "2":
                # Generate report sorted by treatment duration
                if not heap.heap:
                    print(" ERROR: No patients in the scheduling queue to sort.")
                else:
                    # Copy heap data
                    raw_records = list(heap.heap) 
                    
                    # Sort by treatment time (t)
                    sorted_records = merge_sort(raw_records, key=lambda p: p['t'])
                    
                    print("\n--- FINAL TREATMENT REPORT (Sorted by Duration) ---")
                    print(f"{'Patient ID':<12} | {'Urgency':<8} | {'Duration (T)':<12} | {'Priority Score'}")
                    print("-" * 60)
                    for p in sorted_records:
                        print(f"{p['id']:<12} | {p['u']:<8} | {p['t']:<12} | {p['score']:.2f}")
                    print("-" * 60)
                    
        elif ch == "0":
            # Exit program
            print("Exiting... All records cleared from memory.")
            break
        else:
            print(f" INVALID MODULE: '{ch}' is not 1, 2, 3, 4, or 0.")

# Entry point of the program
if __name__ == "__main__":
    main()