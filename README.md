# The Torchbearer

**Student Name:** Monica Lester

**Student ID:** 132761938

**Course:** CS 460 – Algorithms | Spring 2026


---

## Part 1: Problem Analysis



- **Why a single shortest-path run from S is not enough:**
  
  We cannot determine the most fuel-efficient path to grabbing all the relics in the dungeon with a single
  shortest-path run.
  
  A single shortest-path run would tell us the most fuel-efficient path to each node, but cannot decide the 
  best order in which to visit them, with our main goal in mind.
  
- **What decision remains after all inter-location costs are known:**
  
  Once we know all inter-location costs, we must decide the order in which to traverse the nodes to collect 
  all relics using the least fuel.

- **Why this requires a search over orders:**
  
  Since we want to find the path to all relics using the minimum amount of fuel, and there are multiple visitation orders to the necessary nodes, all with different fuel costs/distances, we must search through these different orders to find that which is most efficient.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection


| Source Node Type | Why it is a source |
|---|---|
| start_node (S) | We must start at the entrance (node S), and find all shortest paths to each relic, so (S) is our "base" starting node. |
| relic_node | Once we reach our first relic node traversing from S, that relic node now becomes our new source node to find the most efficient path to the next relic node - rinse and repeat until we reach the exit (T). |

### Part 2b: Distance Storage



| **Property** | **Your answer** |
|---|---|
| *Data structure name* | (Nested) Dictionary/Hash map |
| *What the keys represent* | key_i (outer key)= source node, key_j (inner) = terminal node |
| *What the values represent* | shortest path distance between key_i -> key_j|
| *Lookup time complexity* | $\mathcal{O}(1)$|
| *Why $\mathcal{O}(1)$ lookup is possible* | The lovely average time-complexity of hash maps - constant time - what a wonderful thing it is. |

### Part 2c: Precomputation Complexity


Note the variables $n=|V|,m=|E|$, and $k=|M|$.

- **Number of Dijkstra runs:** $k+1$
  - $k$ runs to search from each relic node, and then an additional one for checking the spawn node.
- **Cost per run:** $\mathcal{O}(m\log(n))$ 
  - Time complexity of one Dijkstra search per assignment instructions.
- **Total complexity:** $\mathcal{O}((k+1)m \log(n))$
  - (number of runs) $\times$ (cost per run) = $(k+1)\times \mathcal{O}(m \log (n))$, which gives us the above.
- **Justification:** We must run a Dijkstra search on the spawn node and all relic nodes, and to do this, we will iterate through M (the set of relic nodes), and add on the one additional search on the spawn node, and since a single Dijkstra search has a time completexity of $\mathcal{O}(m \log(n))$, then we have a total complexity of $\mathcal{O}((k+1)m \log(n))$ for precomputing the distances of relevant nodes in the graph.

---

## Part 3: Algorithm Correctness

### Part 3a: What the Invariant Means


- **For nodes already finalized (in S):**
  For some node $n\in S$, `min_node_dist[n]` is the *shortest possible path* to take from the source node to $n$. This distance will not change again.

- **For nodes not yet finalized (not in S):**
  For some node $n \notin S$, `min_node_dist[n]` is the shortest path *we have encountered* from the source node to $n$. If a new shorter path is encountered, the `min_node_dist[n]` will be updated with that new path.

### Part 3b: Why Each Phase Holds


- **Initialization: why the invariant holds before iteration 1:**
  - 'dist[source]' = 0, and for all $n \in V$, `min_node_dist[n]` $\geq 0$.
  - We have not visited any nodes (other than the source which we established we know the final distance of will always be 0), so the shortest path between them and the source could be some unknown, infinitely large value, and we have no other data to invalidate a distance of `min_node_dist[n]` = $\infty$.

- **Maintenance: why finalizing the min-dist node is always correct:**
  - We always pick the node with the smallest current `min_node_dist[n]` via the min heap/priority queue.
  - Since all edge weights are nonnegative, any other path to this node would have to go through nodes with equal or larger distances, so it can’t end up being shorter.

- **Termination: what the invariant guarantees when the algorithm ends:**
  - The invariant guarantees that `min_node_dist[n]` will hold the finalized shortest possible paths between the source node and all other (reachable) nodes in the graph. 

### Part 3c: Why This Matters for the Route Planner


We must be able to trust that our list of shortest paths is correct when comparing relic orders so that we avoid accidentatlly taking an longer path when traversing the graph from spawn to exit, picking up all the relics as we go.

---

## Part 4: Search Design

### Why Greedy Fails
![Greedy Counter Example](Figures/GreedyCounterExampleGraph.png)
> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** 
  - A locally cheap choice (i.e. next closest relic) can domino and force far more expensive choices in the future.
- **Counter-example setup:** 
  - Consider the graph above. We spawn at node $S$, nodes $A$ and $B$ contain relics, and the exit is at node $T$. 
  
- **What greedy picks:** 
  - Since $S \to A < S \to B$, greedy will choose to go to node $A$ first.
- **What optimal picks:** 
  - Optimal will pick the path starting from $B$: $S \to B \to S \to A \to T$
- **Why greedy loses:** While $A$ is closer to $S$ than $B$, the total path from $S \to B \to S \to A \to T = 6$ is much cheaper than any option where we traverse to $A$ before $B$. For example:
  - Greedy Path $(i)$: $S \to A \to S \to B \to \to S \to A \to T = 8$.
  - Greedy Path $(ii)$: $S \to A \to B \to T = 111$
  - Greedy Path $(iii)$: $S \to A \to B \to A \to T = 22$.
  - etc.
So greedy loses because choosing the closest relic $A$ first results in a more expensive order overall.
### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- It should explore different **orders** of visiting relic nodes, starting from the spawn node and finishing at the exit node, to determine which relic visit order produces the most optimal path. 

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- CS 460 Graphs Practice Quiz
