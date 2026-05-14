"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Monica Lester
Student ID:   132761938

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# ---=================
# PART 1
# ---=================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.
    """
    ans_1 = (
        "We cannot determine the most fuel-efficient path to grabbing "
        "all the relics in the dungeon with a single shortest-path run. "
        "A single shortest-path run tells us the most fuel-efficient path "
        "to each node, but cannot decide the best order in which to visit them.\n"
    )

    ans_2 = (
        "Once we know all inter-location costs, we must decide the order "
        "in which to traverse the nodes to collect all relics using the least fuel.\n"
    )

    ans_3 = (
        "Since there are multiple visitation orders to the necessary nodes "
        "with different fuel costs, we must search through these orders to "
        "find the most fuel-efficient one.\n"
    )

    return ans_1 + ans_2 + ans_3


# ---=================
# PART 2
# ---=================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.
    """
    # inialize list with the starting (spawn) node
    source_nodes = [spawn]
    # iterate through the list of relic nodes and add them all to source_nodes
    for node in relics:
        # we check to avoid duplicates
        if node not in source_nodes:
            source_nodes.append(node)
    # we dont add exit_node since it will never be a starting node,
    # only a terminal node and we assume it cannot contain a relic
    return source_nodes


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    """
    # Utilizied CS 460 Practice Quiz as a reference for implementation.

    # initialize a list of tuples to keep track of distances between nodes
    # then turn it into a priority queue, so that the node with
    # the smallest distance to traverse to it is at the top of the queue
    # initialze with source
    node_check_list = [(0, source)]
    heapq.heapify(node_check_list)
    # Initialize return disctionary
    min_node_dist = {}
    # and then iterate through graph, adding all other nodes such that (node, inf).
    # We will update the min distance from source node (source or relic)
    # and all other nodes when a shorter path is found.
    for node in graph:
        min_node_dist[node] = float('inf')
    # Then correct distance to source node with (source, 0),
    # (since the distance between source and itself is 0).
    min_node_dist[source] = float(0)

    # We iterate until node_check_list is empty (i.e. no nodes in
    # the graph left to check):
    while node_check_list:
        # pop top (prioritized) node from heap and store in curr_node
        (curr_dist, curr_node) = node_check_list.pop()
        # check to see if min distance to curr_node which has been logged
        # in min_node_dist is less than curr_dist. If not, then skip
        # and move to next iteration of loop
        if curr_dist > min_node_dist[curr_node]:
            continue

        # Iterate through all adjacent nodes to curr_node and check if
        # the distance between curr_node and adj_node is smaller than
        # the current min traveral path to adj_node logged in min_node_dist
        # If smaller, then update min_node_dist of adj_node as a shorter path
        # to it has been found, and then add it to check list to check
        # adjacent nodes of adj_node in a future iteration of loop.
        #
        # This process allows us to follow through every shortest traversal
        # path within the graph and continue updating min_node_dist until
        # we have found the shortest path from the source to every node in
        # the graph.
        for (adj_node, adj_dist) in graph[curr_node]:
            if min_node_dist[curr_node] + adj_dist < min_node_dist[adj_node]:
                min_node_dist[adj_node] = min_node_dist[curr_node] + adj_dist
                heapq.heappush(node_check_list,
                               (min_node_dist[adj_node], adj_node))
    # Once we exit the while loop, min_node_dist has been finalized with all shortest paths
    # from source to every node in graph, and we return min_node_dist
    return min_node_dist


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    """
    # Initialize return dictionary that will hold the dijkstra results (i.e. shortest path) between every
    # source node and all other nodes in the graph
    node_distances = {}
    # Use select_sources(s,r,e) to find all relevant source nodes in graph
    source_nodes = select_sources(spawn, relics, exit_node)
    # Iterate though source_nodes and add each node
    # to node_distances, computing the shortest paths with run_dijkstra(graph, source).
    for node in source_nodes:
        node_distances[node] = run_dijkstra(graph, node)
    # Return node_distances once all relevant nodes have been added to it.
    return node_distances


# ---=================
# PART 3
# ---=================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.
    """
    # 3a
    ans_1 = (
        "What the Invariant Means: \n"
        r"For some node $n\in S$, 'dist[n]' is the shortest "
        "possible path to take from the source node to $n$."
        " This distance will not change again.\n"
        r"For some node $n \notin S$, 'dist[n]' is the "
        r"shortest path we have encountered from the source node"
        " to $n$. If a new shorter path is encountered, the 'dist[n]' "
        "will be updated with that new path.\n"
    )

    # 3b
    ans_2 = (
        "Intitialization: \n"
        r"\t - 'dist[source]' = 0, and for all $n \in V$, 'dist[n]' $\geq 0$. \n"
        r"\t - We have not visited any nodes (other than the source which we established we know the final distance of will always be 0), so the shortest path between them and the source could be some unknown, infinitely large value, and we have no other data to invalidate a distance of 'dist[n]' = $\infty$. \n\n"
        "Maintenance: \n"
        "\t - We always pick the node with the smallest current `dist[n]` via the min heap.\n"
        "\t - Since all edge weights are nonnegative, any other path to this node would have to go through nodes with equal or larger distances, so it can’t end up being shorter. \n\n"
        "Termination:\n"
        "\t - The invariant guarantees that 'dist[n]' will hold the finalized shortest possible paths between the source node and all other (reachable) nodes in the graph. \n "
    )

    # 3c
    ans_3 = (
        "Why this is Important for the Route Planner: \n"
        "We must be able to trust that our list of shortest paths is correct when comparing relic orders so that we avoid accidentatlly taking an longer path when traversing the graph from spawn to exit, picking up all the relics as we go.\n"
    )

    return ans_1 + ans_2 + ans_3


# ---=================
# PART 4
# ---=================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.
    """
    # 4
    ans_1 = (
        "Why Greedy Fails: \n"
        "The failure mode: \n"
        "\t - A locally cheap choice (i.e. next closest relic) can domino and force far more expensive choices in the future.\n"
        "Counter-example setup: \n"
        r"\t - Consider the graph above. We spawn at node $S$, nodes $A$ and $B$ contain relics, and the exit is at node $T$. " "\n"
        "What greedy picks: \n"
        r"\t - Since $S \to A < S \to B$, greedy will choose to go to node $A$ first." "\n"
        "What optimal picks: \n"
        r"\t - Optimal will pick the path starting from $B$: $S \to B \to S \to A \to T$" "\n"
        r"Why greedy loses: While $A$ is closer to $S$ than $B$, the total path from $S \to B \to S \to A \to T = 6$ is much cheaper than any option where we traverse to $A$ before $B$. For example:" "\n"
        r"\t - Greedy Path $(i)$: $S \to A \to S \to B \to \to S \to A \to T = 8$." "\n"
        r"\t - Greedy Path $(ii)$: $S \to A \to B \to T = 111$" "\n"
        r"\t - Greedy Path $(iii)$: $S \to A \to B \to A \to T = 22$." "\n"
        "\t - etc.\n"
        "So greedy loses because choosing the closest relic $A$ first results in a more expensive order overall.\n"
    )

    return ans_1


# ---=================
# PARTS 5 + 6
# ---=================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.
    """
    # Initialize a set to log the relics which have not been collected yet (see devnotes entry 4)
    relics_remaining = set(relics)
    cost_so_far = 0
    # Create an empty, ordered list which will store the order in which we visit the relic nodes
    relics_visited_order = []
    # And initialize return variable for holding the most optimal route we've encountered so far
    # i.e. best=[best cost, best route]
    best = [float('inf'), []]
    # By the time we reach the return call, this variable should contain the most optimal visitation
    # order and the minimum cost of traversing from spawn, visiting relics in said order, and
    # ending traversal at exit_node

    # We use _explore() helper function in order to find best
    # _explore() is a recursive function which updates in place
    # and will recurse through all cost effective permutations of relics to
    # find the most optimal ordering, and once the recursion rolls back up
    # best will contain said optimal ordering and its cost of traversal
    # which we will return its elements as a tuple
    _explore(
        dist_table,
        spawn,
        relics_remaining,
        relics_visited_order,
        cost_so_far,
        exit_node,
        best
    )

    # Return the best cost and route found by _explore()
    return (best[0], best[1])


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : set
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list -> best[0] = (float) minimum fuel cost found so far (initialized at 'inf'),
                   best[1] = [] ordered list of corresponding best visiting order (so far)
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    """

    # Base case: If there are no relics left to collect, immediately find
    # the cheapest path to the exit and update cost so far
    if not relics_remaining:
        exit_cost = dist_table[current_loc][exit_node]

        # if the exit is unreachable from current_loc, then this ordering is invalid
        # so we exit this recursive line
        if exit_cost == float('inf'):
            return

        total_cost = cost_so_far + exit_cost

        # then we check if the current cost of the visited order is < best
        # if it is, then update best, and if not, exit recursion
        if total_cost < best[0]:
            best[0] = total_cost
            best[1] = relics_visited_order.copy()
        return

    # Pruning: define a lower bound (minimum possible cost from this state)
    # start with the cost we've already accumulated
    lower_bound = cost_so_far

    # find all possible next move costs from current_loc to any remaining relic
    # and ignore any relics which are unreachable from current_loc
    possible_next_costs = [
        dist_table[current_loc][relic]
        for relic in relics_remaining
        if dist_table[current_loc][relic] != float('inf')
    ]

    # if there are no possible next moves, i.e. all remaining relic nodes are unreachable,
    #  then this ordering cannot be completed so we exit this recursive line
    if not possible_next_costs:
        return

    # find the cheapest possible next move from current_loc to any remaining relic
    # this represents the minimum cost we MUST pay next no matter what
    cheapest_next = min(possible_next_costs)

    # add that minimum cost to our lower bound estimate
    lower_bound += cheapest_next

    # actual pruning condition:
    # if even our BEST CASE (lower_bound) is worse than the best solution found so far,
    # then this path cannot possibly lead to an optimal solution, so we stop exploring it
    #
    # Pruning is safe here because our lower_bound represents the minimum possible cost
    # to complete this traversal; if it is already >= best[0], then no continuation of
    # this path can produce a better (lower-cost) solution, so we can safely abandon it.
    if lower_bound >= best[0]:
        return

    # Recursive case: We now explore all possible next steps by choosing each
    # remaining relic as the next node to visit in the traversal
    # this effectively branches our search into all possible visiting orders
    for relic_node in list(relics_remaining):

        # get the cost to travel from the current location to this relic node
        travel_cost = dist_table[current_loc][relic_node]

        # if this relic is unreachable from current_loc, then this path is invalid
        # so we skip this relic and move on to the next possible option
        if travel_cost == float('inf'):
            continue

        # choose: we now commit to visiting this relic next
        # so we remove it from the set of remaining relics and add it to our visited order
        relics_remaining.remove(relic_node)
        relics_visited_order.append(relic_node)

        # recursively explore the rest of the traversal starting from this relic node
        # we also update cost_so_far to include the fuel cost required to reach this node
        _explore(dist_table, relic_node, relics_remaining, relics_visited_order,
                 cost_so_far + travel_cost, exit_node, best)

        # backtrack: after exploring this branch, we must undo our choice so that
        # other possible visiting orders can be explored correctly
        # this restores the state of relics_remaining and relics_visited_order
        relics_visited_order.pop()
        relics_remaining.add(relic_node)


# ---=================
# PIPELINE
# ---=================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.
    """
    # First initialise the shortest distances from the nodes we care about using
    # precompute_distances() which we defined earlier. Then, the search can use O(1) distance
    # lookups instead of rerunning Dijkstra in every recursive call
    dist_table = precompute_distances(graph, spawn, relics, exit_node)

    # Then use the dist_table to search for the best relic visiting order via find_optimal_route()
    return find_optimal_route(dist_table, spawn, relics, exit_node)

    ### Yayyyy -- All done :)) ###


# ---=================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# ---=================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


def run_extra_tests():
    print("\nRunning extra tests...")

    # ---
    # Extra 1: No relics case
    # We should just take the shortest path from S -> T
    # Tests that we don’t break when relic list is empty
    # ---
    graph = {
        'S': [('A', 2), ('T', 10)],
        'A': [('T', 3)],
        'T': []
    }

    cost, order = solve(graph, 'S', [], 'T')

    # Expected: S -> A -> T = 2 + 3 = 5
    assert cost == 5, f"Extra 1 FAILED: expected 5, got {cost}"
    assert order == [], f"Extra 1 FAILED: expected [], got {order}"
    print("  Extra 1 passed")


    # ---
    # Extra 2: Directed graph where greedy order fails
    # Tests that algorithm actually explores different orders
    # instead of just picking closest next relic
    # ---
    graph = {
        'S': [('A', 1), ('B', 2)],
        'A': [('B', 100), ('T', 100)],
        'B': [('A', 1), ('T', 1)],
        'T': []
    }

    cost, order = solve(graph, 'S', ['A', 'B'], 'T')

    # Best route: S -> A -> B -> T
    # cost = 1 (S->A) + 100 (A->B) + 1 (B->T) = 102
    # Note: visiting B first looks tempting (short edge),
    # but leads to a worse total cost overall (i.e. a greedy 
    # approach ends up unoptimal for this problem as shown in 
    # README.md Part 4).
    assert cost == 102, f"Extra 2 FAILED: expected 102, got {cost}"
    assert order == ['A', 'B'], f"Extra 2 FAILED: expected ['A', 'B'], got {order}"
    print("  Extra 2 passed")

    # ---
    # Extra 3: Unreachable relic
    # Tests that we correctly return (inf, [])
    # when a required relic cannot be reached
    # ---
    graph = {
        'S': [('A', 1)],
        'A': [('T', 1)],
        'R': [('T', 1)],
        'T': []
    }

    cost, order = solve(graph, 'S', ['R'], 'T')

    # R is not reachable from S, so no valid route exists
    assert cost == float('inf'), f"Extra 3 FAILED: expected inf, got {cost}"
    assert order == [], f"Extra 3 FAILED: expected [], got {order}"
    print("  Extra 3 passed")

    # ---
    # Extra 4: Shortest path uses intermediate node
    # Tests that precomputed distances (Dijkstra) are working
    # and not just direct edges
    # ---
    graph = {
        'S': [('R1', 2)],
        'R1': [('X', 1), ('R2', 10)],
        'X': [('R2', 1)],
        'R2': [('T', 2)],
        'T': []
    }

    cost, order = solve(graph, 'S', ['R1', 'R2'], 'T')

    # Best route: S -> R1 -> X -> R2 -> T
    # cost = 2 + 1 + 1 + 2 = 6
    assert cost == 6, f"Extra 4 FAILED: expected 6, got {cost}"
    assert order == [
        'R1', 'R2'], f"Extra 4 FAILED: expected ['R1', 'R2'], got {order}"
    print("  Extra 4 passed")

    print("All extra tests passed.")

if __name__ == "__main__":
    _run_tests()
    run_extra_tests()
