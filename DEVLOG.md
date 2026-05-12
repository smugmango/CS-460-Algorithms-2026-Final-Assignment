# Development Log – The Torchbearer

**Student Name:** Monica Lester
**Student ID:** 132761938



---

## Entry 1 – [5/10/26, 4:19 PM]: Initial Plan



  - I plan to work through this assignment step-by-step in the order it’s laid out. I’ve already read through ASSIGNMENT.md and README.md, and skimmed the torchbearer.py file to get a sense of what I’ll be working with. I filled out Parts 1 and 2 of the README first, and now I’m moving into the .py file to start implementing the TODOs. I’ll start with the easier functions like explain_problem() and select_sources(), then move into Dijkstra and precomputing distances before getting into the search and pruning logic. I expect the hardest part will be the recursive search in _explore(), especially making sure I don’t accidentally prune the optimal solution. I also think keeping track of visited relics cleanly might take some thought. For testing, I’ll use the provided test cases in the file and also try a few small graphs that I can reason through by hand to make sure everything is working correctly.

  - [4:32] Completed Part 1, and code-wise completed explain_problem() and select_sources(). Began to look at run_dijkstra(g,s), but short day today. Bigger day tomorrow.

---

## Entry 2 – [5/11/26, 10:46 AM] Parts 2-3



 - [11:33 AM] Completed run_dijkstra(g,s) utilizing CS 460 Practice Quiz as a reference. Made sure to comment thoroughly, but we'll see how long that habit sticks for. Luckily, didn't run into any major issues or bugs. Next objective is Part 2c in README.md and precompute_distances(g,s,r,e).

 - [12:00 PM] Completed Part 2c in README.md. Have to run to class and plan to continue working later in the day. 

 - [3:35 PM] Completed precompute_distances(g,s,r,e). No big issues -- its a pretty simple function thanks to the defined before it. 

 - [4:20 PM] Written portion of Part 3 complete and "coding" component filled out. 

 
---

## Entry 3 – [5/11/26, 6:09 PM]: Part 4

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

- Written portion of Part 4 complete. I struggled a bit coming up with a good counter example graph, as I didn't want to make it too big or complex, but I think I was missing the mark on what was important to a greedy counter example, focusing more on the cost of individual edges rather than the bigger picture of forcing some inoptimal pathing due to picking the closest relic node. I also think that thinking like a person and not like a computer added some struggle to that, since I wasn't thinking about the amount of doubling back through previous explored paths resulting in a shorter overall path. I was able to figure something out in the end, and then spent 30 minutes fighting with the tikZ library in LaTeX to make it into a nice diagram. Overall, I am happy with it. Will be back again later -- hoping to be able to knock out the bulk of the project so then tomorrow is just final touches. 

---

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | |
| Part 2: Precomputation Design | |
| Part 3: Algorithm Correctness | |
| Part 4: Search Design | |
| Part 5: State and Search Space | |
| Part 6: Pruning | |
| Part 7: Implementation | |
| README and DEVLOG writing | |
| **Total** | |
