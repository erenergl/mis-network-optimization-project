# Field Service Network Optimization

## 1. Real-World Problem Context
Field support teams of a large company are constantly on the move to respond to network, hardware, or operational failures. In the event of a failure (downtime), every minute the systems are down means financial loss and wasted workforce for the company. Therefore, minimizing the travel time for field technicians to reach their destinations is a critical Management Information Systems (MIS) and logistics problem.

## 2. Problem Definition
A critical infrastructure failure has occurred at the company's "Production Facility" location. The fully equipped support team located at the "Headquarters" needs to find the shortest and fastest route to reach the "Production Facility", taking city traffic and distance factors into consideration.

## 3. Network Model
The network model established in this problem is a transportation network.
* **Nodes:** Represent the company's operational locations, including the Headquarters, branch offices, data center, and production facility (7 nodes in total).
* **Edges:** Represent the existing road connections between these locations.
* **Weights:** The weights of the edges between nodes are determined as the "estimated travel time (minutes)" depending on the distance and traffic conditions.

## 4. Nodes and Edges
**Nodes (7 Total):** Headquarters, Branch Office A, Branch Office B, Branch Office C, Branch Office D, Data Center, Production Facility.

**Edges (9 Total) and Weights (Minutes):**
- Headquarters <-> Branch Office A: 15
- Headquarters <-> Branch Office B: 20
- Branch Office A <-> Branch Office C: 10
- Branch Office B <-> Branch Office C: 12
- Branch Office B <-> Branch Office D: 25
- Branch Office C <-> Data Center: 30
- Branch Office C <-> Branch Office D: 18
- Branch Office D <-> Production Facility: 15
- Data Center <-> Production Facility: 20

## 5. Selected Algorithm
The **Shortest Path** optimization model and the **Dijkstra Algorithm** running in the background have been selected for this problem. Our goal is to minimize the total weight (time) between the starting point (Headquarters) and the endpoint (Production Facility).

## 6. Python Implementation
The project was developed using Python and the `NetworkX` library for network optimization. 
1. An undirected graph was created using `nx.Graph()`.
2. Nodes and edges were added to the graph along with their estimated travel times.
3. The algorithm was executed using the `nx.shortest_path()` function.
4. The entire network and the shortest path found were visualized using `matplotlib`.

## 7. Results
The following results were obtained when the algorithm was executed:
* **Selected Optimum Route:** Headquarters -> Branch Office A -> Branch Office C -> Branch Office D -> Production Facility
* **Total Travel Time:** 58 Minutes

The algorithm successfully found the fastest path by selecting the time-efficient alternative route (58 minutes) rather than the route that seemingly has fewer stops (Headquarters -> Branch Office B -> Branch Office D -> Production Facility = 60 minutes).

## 8. Managerial Interpretation
From the perspective of an MIS Manager or a Business Development specialist, the implications of these results are as follows:
* **Service Level Agreement (SLA) Compliance:** By reducing the incident response time to under 60 minutes (1 hour), the company's quality standards and operational commitments have been maintained.
* **Time and Workforce Savings:** When route planning is done manually, employees might rely on habit and choose sub-optimal routes. Thanks to Data-Driven Decision Making, travel times have been optimized by 3-5%, increasing the overall efficiency of field teams and allowing for better human resource allocation.
* **Cost Reduction:** Shortening the travel time directly reduces fuel consumption and logistical costs.

## 9. How to Run the Code
To run the code on your local machine:
1. Ensure Python is installed on your system.
2. Open your terminal and install the required libraries: `pip install networkx matplotlib`
3. Navigate to the project directory and run the file: `python src/solution.py`
4. The outputs will be printed to the terminal, and the network visualization will be saved in the `results` folder.

## 10. References
* NetworkX Documentation: https://networkx.org/documentation/stable/
* Management Information Systems Concepts, Routing Operations.
