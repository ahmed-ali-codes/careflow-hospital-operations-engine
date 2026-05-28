# CareFlow: Hospital Operations & Emergency Priority Engine

CareFlow is a modular, high-performance healthcare operations simulation engine built entirely in Python using custom-implemented data structures and algorithms from first principles. It models real-world clinical routing, patient registry management, emergency priority triage scheduling, and performance benchmarking without relying on any external packages or built-in complex collections.

This repository serves as a software engineering showcase of data structures and algorithms (DSA) applied to complex operational logistics.

For an in-depth breakdown of the custom design justifications, flowcharts, and technical mechanics, see the [Architecture & Design Specification](ARCHITECTURE.md).

---

## Technical Highlights & Features

The platform is designed around four decoupled, custom-built modules:

### 🌐 Module 1: Graph-Based Navigation (`graph.py`)
* Represents hospital departments and transit corridors as a **weighted, undirected graph**.
* **Adjacency List** implementation optimizes storage and traversal speeds.
* **Core Algorithms:**
  * **Breadth-First Search (BFS):** Performs level-wise hop traversals to map out reachable departments.
  * **Depth-First Search (DFS):** Detects cyclic corridor loops within the hospital graph to avoid navigation errors.
  * **Dijkstra's Algorithm:** Calculates the absolute shortest, time-weighted route between any two clinical departments.

### 🔑 Module 2: Hash-Based Patient Registry (`hash_table.py`)
* Implements a **custom hash table** for rapid patient lookup and record keeping.
* Resolves hash collisions using **Linear Probing**.
* **Dynamic Table Resizing:** Automatically scales the capacity and re-hashes active records when the load factor ($\alpha$) exceeds $0.70$ (maintaining high-efficiency performance).
* Offers average-case **$\mathcal{O}(1)$ operations** for registrations, lookups, and deletions.

### ⏳ Module 3: Emergency Triage Scheduler (`heap.py`)
* Implements a **Binary Max-Heap** priority queue to manage patient triage.
* **Triage Priority Scoring:** Evaluates patient urgency and treatment time to prioritize cases:
  $$\text{Score} = (6 - \text{urgency}) + \left(\frac{1000}{\text{treatment\_time}}\right)$$
* Handles real-time urgency updates via a custom extraction and heap-reconstruction sequence.
* Restores the Max-Heap invariant in $\mathcal{O}(\log n)$ time using percolation (`_up` and `_down`).

### 📊 Module 4: Sorting & Performance Benchmarking (`sorting.py`)
* Features custom implementations of **Merge Sort** (stable) and **Quick Sort** (in-place partitioning) supporting customizable key functions.
* **Empirical Analysis:** Runs multi-variable performance profiling comparing sorting algorithms across varying dataset sizes ($100$, $500$, $1000$ records) under **Random**, **Nearly Sorted**, and **Reversed** conditions.
* Compiles treated patient records into reports sorted by treatment duration.

---

## Core Complexity Profile

| Module | Core Algorithm | Time Complexity (Average) | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Graph** | BFS / DFS Traversals | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| **Graph** | Dijkstra (Shortest Path) | $\mathcal{O}(V^2)$ | $\mathcal{O}(V)$ |
| **Hash Table** | Insert / Search / Delete | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ |
| **Max-Heap** | Priority Insert / Extract | $\mathcal{O}(\log n)$ | $\mathcal{O}(n)$ |
| **Sorting** | Merge Sort | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n)$ |
| **Sorting** | Quick Sort | $\mathcal{O}(n \log n)$ | $\mathcal{O}(\log n)$ |

---

## File Structure

```
careflow-hospital-operations-engine/
├── ARCHITECTURE.md          # In-depth architectural & algorithm analysis
├── README.md                # Project landing page and execution guide
├── .gitignore               # Excludes OS and byte-compiled garbage files
├── main.py                  # Interactive CLI driver and workflow orchestrator
├── graph.py                 # Graph data structure & pathfinding logic
├── hash_table.py            # Hash Table with linear probing & resizing
├── heap.py                  # Binary Max-Heap priority queue triage
├── sorting.py               # Custom Merge Sort and Quick Sort algorithms
├── patient.py               # Patient entity definition & validation schema
└── Dept_&_Patients_details.txt  # Sample department layout and patient logs
```

---

## Setup & Running the Engine

### Prerequisites
* **Python 3.x** installed (no external dependencies are required!).

### Running the CLI Driver
Clone this repository to your local machine, navigate to the directory, and run the main entry point:

```bash
python main.py
```

The interactive Command-Line Interface allows you to manually run map navigations, manage patient registries, schedule emergencies, and trigger algorithmic benchmarks.

---

## Constraints & Assumptions
* **Department Registry:** Department nodes are case-sensitive and must be added to the graph before corridors can connect them.
* **Patient Operations:** Patients must be registered in the Hash Table before being admitted into the Emergency Triage priority queue.
* **Heap Urgency Updates:** Relies on a pop-and-rebuild strategy for updates rather than `decrease-key`.

---

## Author

* **Ahmed Ali** - *Software Engineer / Systems & Algorithms Designer*
* **LinkedIn:** [linkedin.com/in/ahmed-ali-jawad](https://www.linkedin.com/in/ahmed-ali-codes/)
* **GitHub:** [@ahmed-ali-codes](https://github.com/ahmed-ali-codes)

