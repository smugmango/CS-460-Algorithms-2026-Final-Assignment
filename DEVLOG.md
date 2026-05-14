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

- Written portion of Part 4 complete. I struggled a bit coming up with a good counter example graph, as I didn't want to make it too big or complex, but I think I was missing the mark on what was important to a greedy counter example, focusing more on the cost of individual edges rather than the bigger picture of forcing some inoptimal pathing due to picking the closest relic node. I also think that thinking like a person and not like a computer added some struggle to that, since I wasn't thinking about the amount of doubling back through previous explored paths resulting in a shorter overall path. I was able to figure something out in the end, and then spent 30 minutes fighting with the tikZ library in LaTeX to make it into a nice diagram. Overall, I am happy with it. Will be back again later -- hoping to be able to knock out the bulk of the project so then tomorrow is just final touches. 

---

## Entry 4 – [5/13/26, 6:38 PM]: Part 4 Coding Implementation Wrap Up & Part 5

- Whelp, yesterday did not go as planned, so today has become crunch day. Plan to crush Part 5 (and 6 with fingers crossed). Already had a bit of the Part 5 README section completed, so polishing that and then hopping into torchbearer.py.

- [7:02 PM] In reviewing the written section of Part 5a I noticed a descrepancy between the `README.md` file template and the code in `torchbearer.py`. The component which the row is asking me to name is the variable which notes the relics *already* collected, so the variable which would drive decision making for pathing to the next relic, but the only parameter in `_explore(d_t,c_l,r_r,r_v_o,c_s_ff,e_n,b)` which would do that is `relics_remaining`, which is a collection of the relics which have *not yet* been visited -- not those which have already been collected. I will be keeping the parameter name as is, as we were instructed to have the variable names match *exactly* as what is used in `torchbearer.py`, and implementing it with the interpretation of relics which have *not* been collected yet, as I anticipate that will work better functionally for how I am planning to code the function, but I wanted to make note of this since my response contradicts what the component I was asked to describe is. I have also included this note in my response to Part 5a in `README.MD`. 

- [7:28 PM] Written portion of Part 5 completed. Moving onto the written portion of Part 6 so I can be fully prepared before I switch over to `torchbearer.py`.

- [8:10 PM] Completed writted portion of 6a, took care of some quick chores, and now wrapping up Part 6 written portion.

---
## Entry 5 – [5/13/26, 9:16 PM]: Wrong Assumption Because I am a Fool Who Can't Read


- I finished filling out the entirety of the `README.MD` file, so on my final major check to ensure everything looked proper (correct logic, proper grammar, no spelling mistakes, etc.), upon checking it against the `ASSIGNMENT.md` file, I realized I had been operating under the assumption that this problem works with a weighted, **undirected** graph, which anyone who can read and follow directions properly knows that the graph representing the dungeon is a *directed* graph, meaning there are some edges which onces traversed, you can't simply turn around to backtrack, but if you wanted to go back to the previous node, you would need to find some alternate (possibly fuel-draining) path to make it. Luckily, this shameful bafoonery didn't cost me much overall. The one major issue it caused is that my greedy counter example, which I so painstakingly made in TikZ, is not as adequate an example as I had previously thought. It still works, and still disproves a greedy approach to this problem, but the pathing required for that, since the example is an undirected graph, can be a little confusing since backtracking is made cheaper than it could be were I to apply an orientation to the graph, which could result in a more explicit counterexample to a greedy approach to picking the relic visitation order. Since it is late, and I still have the coding segments of Parts 5 & 6 left to complete, I am making the executive decision to leave the graph and counterexample as is, adding a note that all edges are bidirectional, since it is still sufficient in disproving the greedy approach. Should I complete the remaining parts of the assignment more promptly than I anticipate, I might revisit that decision, but this where we stand as of now. 

---


## Entry 6 – [Date]: Post-Implementation Reflection

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
