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


# =============================================================================
# PART 1
# =============================================================================

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


# =============================================================================
# PART 2
# =============================================================================

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

    TODO
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

    TODO
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

    TODO
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


# =============================================================================
# PART 3
# =============================================================================

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


# =============================================================================
# PART 4
# =============================================================================

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


# =============================================================================
# PARTS 5 + 6
# =============================================================================

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

    TODO
    """
    # Initialize a set to log the relics which have been collected
    collected_relics = {}
    curr_node = spawn
    fuel_burned = 0




def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
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

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    pass


# =============================================================================
# PIPELINE
# =============================================================================

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

    TODO
    """
    pass


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

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


if __name__ == "__main__":
    _run_tests()
