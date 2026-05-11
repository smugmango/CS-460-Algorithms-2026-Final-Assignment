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
  Since we want to find the path to all relics using the minimum amount of fuel,
  and there are multiple visitation orders to the necessary nodes, all with different fuel costs,
  we must search through these different orders to find that which is most fuel efficient.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection


| Source Node Type | Why it is a source |
|---|---|
| start_node (S) | we must start at the entrance (node S), and find all shortest paths to each relic, so (S) is our "base" starting node |
|---|---|
| relic_node | once we reach our first relic node traversing from S, that relic node now becomes our new source node to find the most efficient path to the next relic node - rinse and repeat until we reach the exit (T). |

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

- **Number of Dijkstra runs:** |M|+1
  - |M| runs to search from each relic node, and then an additional one for checking the spawn node
- **Cost per run:** $\mathcal{O}(m\log(n))$ 
  - Time complexity of one Dijkstra search per assignment instructions.
- **Total complexity:** $\mathcal{O}((k+1)m \log(n))$
  - (number of runs) $\times$ (cost per run) = $(k+1)\times \mathcal{O}(m \log (n))$, which gives us the above.
- **Justification (one line):** We must run a Dijkstra search on the spawn node and all relic nodes, and to do this, we will iterate through M (the set of relic nodes), and add on the one additional search on the spawn node, and since a single Dijkstra search has a time completexity of $\mathcal{O}(m \log(n))$, then we have a total complexity of $\mathcal{O}((k+1)m \log(n))$ for precomputing the distances of relevant nodes in the graph.

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  _Your answer here._

- **For nodes not yet finalized (not in S):**
  _Your answer here._

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  _Your answer here._

- **Maintenance : why finalizing the min-dist node is always correct:**
  _Your answer here._

- **Termination : what the invariant guarantees when the algorithm ends:**
  _Your answer here._

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

_Your answer here._

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** _Your answer here._
- **Counter-example setup:** _Your answer here._
- **What greedy picks:** _Your answer here._
- **What optimal picks:** _Your answer here._
- **Why greedy loses:** _Your answer here._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _Your answer here._

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

- _Your references here._
