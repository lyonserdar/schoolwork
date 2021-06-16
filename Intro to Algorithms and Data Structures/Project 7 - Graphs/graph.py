#!/usr/bin/env python

"""
Project: 7 - Graph
Author: Ali Serdar Aydogdu
Course: CS 2420-601
Date Created: 06/11/2021
Date Last Modified: 06/11/2021
"""

# Imports
import math


class Graph:
    """
    Graph
    """

    class Vertex:
        """
        Vertex
        """

        def __init__(self, label):
            """
            Initialize the vertex.
            Label is the identifier of the vertex.
            Neighbors dictionary will store the edges of the vertex.
            """
            self.label = label
            self.neighbors = {}

        def add_neighbor(self, neighbor, weight):
            """
            Adds the given vertex to neighbors list.
            This creates an edge for the graph.
            The key of the dictionary entry is the neighbor vertex reference and
            the value is the weight of the edge.
            """
            self.neighbors[neighbor] = weight

        def get_neighbors(self):
            """
            Returns all neighbors of the vertex.
            """
            return self.neighbors.keys()

        def get_label(self):
            """
            Returns the label of the vertex.
            """
            return self.label

        def get_weight(self, neighbor):
            """
            Returns the  weigh of the edge to the neighbor.
            """
            if neighbor in self.neighbors:
                return self.neighbors[neighbor]
            return None

    def __init__(self):
        """
        Initialize
        """
        self.vertices = {}

    def add_vertex(self, label):
        """
        Adds a vertex with the given label.
        Label must be a string, otherwise raises ValueError
        """
        if not isinstance(label, str):
            raise ValueError

        vertex = self.Vertex(label)
        self.vertices[label] = vertex
        return self

    def get_vertex(self, label):
        """
        Returns the vertex with given label.
        """
        if label in self.vertices:
            return self.vertices[label]
        raise ValueError

    def add_edge(self, src, dest, weight):
        """
        Adds an edge from vertex src to vertex dest with weight.
        Validates the src, dest, and weight.If not valid, raises ValueError
        """
        if src not in self.vertices:
            raise ValueError
        if dest not in self.vertices:
            raise ValueError
        if not isinstance(weight, (int, float)):
            raise ValueError

        self.vertices[src].add_neighbor(self.vertices[dest], weight)
        return self

    def get_vertices(self):
        """
        Returns all the vertices of the graph.
        """
        return self.vertices.keys()

    def get_weight(self, src, dest):
        """
        Returns the weight on edge src-dest.
        Raises ValueError if src or dest vertices does not exist.
        Returns math.inf if path does not exist.
        """
        if src not in self.vertices:
            raise ValueError
        if dest not in self.vertices:
            raise ValueError

        weight = self.vertices[src].get_weight(self.vertices[dest])
        return float(weight) if weight else math.inf

    def dfs(self, starting_vertex):
        """
        Returns a generator for traversing the graph in depth-first order
        starting from the given vertex.
        Raises a ValueError if the vertex does not exist.
        """
        # Uses stack: append and pop
        if starting_vertex not in self.vertices:
            raise ValueError

        visited = []
        stack = []
        index = 0
        vertex = self.vertices[starting_vertex]

        while True:
            if vertex not in visited:
                yield vertex.get_label()
                visited.append(vertex)

            neighbors = vertex.get_neighbors()
            found = False
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(vertex)
                    vertex = neighbor
                    found = True
                    break

            if len(stack) == 0:
                break

            if not found:
                vertex = stack.pop()

    def bfs(self, starting_vertex):
        """
        Returns a generator gor traversing the graph in breadth-first order
        staring from the given vertex.
        Raises a ValueError if the vertex does not exist.
        """
        # Uses queue: append and popleft
        if starting_vertex not in self.vertices:
            raise ValueError

        visited = [self.vertices[starting_vertex]]
        index = 0
        vertex = visited[index]
        yield vertex.get_label()

        while True:
            neighbors = vertex.get_neighbors()
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.append(neighbor)
                    yield neighbor.get_label()

            index += 1

            if index == len(visited):
                break

            vertex = visited[index]

    def dsp(self, src, dest):
        """
        Returns a tuple (path length, the list of vertices on the path from dest
        back to src).
        If no path exists, returns the tuple.(math.inf, empty list)
        TODO: Fix this to match dsp_all
        """
        if src not in self.vertices:
            raise ValueError
        if dest not in self.vertices:
            raise ValueError

        dist = {}
        prev = {}

        dist[src] = 0
        prev[src] = None

        unvisited_vertices = {}

        for vertex in self.vertices:
            if vertex != src:
                dist[vertex] = math.inf
                prev[vertex] = None
            unvisited_vertices[vertex] = math.inf

        while len(unvisited_vertices):
            selected_vertex = min(unvisited_vertices, key=unvisited_vertices.get)
            del unvisited_vertices[selected_vertex]

            if selected_vertex == dest:
                break

            for neighbor in self.vertices[selected_vertex].get_neighbors():
                alternative = dist[selected_vertex] + self.vertices[
                    selected_vertex
                ].get_weight(neighbor)
                if alternative < dist[neighbor.get_label()]:
                    dist[neighbor.get_label()] = alternative
                    prev[neighbor.get_label()] = selected_vertex

        if dist[dest] == math.inf:
            return (math.inf, [])

        path = [dest]
        selected_path_vertex = dest
        while selected_path_vertex != src:
            path.append(prev[selected_path_vertex])
            selected_path_vertex = prev[selected_path_vertex]

        return dist[dest], path[::-1]

    def dsp_all(self, src):
        """
        Returns a dictionary of the shortest weighted path between src and all other
        vertices using Dijkstra's Shortest Path algorithm.
        In the dictionary, the key is the dest vertex label, the value is a list of
        vertices on the path from srt to dest inclusive.
        """
        if src not in self.vertices:
            raise ValueError

        dist = {vertex: math.inf for vertex in self.vertices}
        prev = {vertex: None for vertex in self.vertices}
        dist[src] = 0

        unvisited_vertices = {src: dist[src]}

        while len(unvisited_vertices):
            current_vertex = min(unvisited_vertices, key=unvisited_vertices.get)
            current_distance = unvisited_vertices[current_vertex]
            del unvisited_vertices[current_vertex]

            if current_distance > dist[current_vertex]:
                continue

            for neighbor in self.vertices[current_vertex].get_neighbors():
                distance = current_distance + self.vertices[current_vertex].get_weight(
                    neighbor
                )
                neighbor = neighbor.get_label()

                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    unvisited_vertices[neighbor] = distance
                    prev[neighbor] = current_vertex

        dsp_dict = {}

        for vertex, distance in dist.items():
            if distance == math.inf:
                dsp_dict[vertex] = []
            else:
                dsp_dict[vertex] = self.__get_path_from_prev(prev, src, vertex)

        return dsp_dict

    def __get_path_from_prev(self, prev, src, dest):
        path = [dest]
        selected_path_vertex = dest
        while selected_path_vertex != src:
            path.append(prev[selected_path_vertex])
            selected_path_vertex = prev[selected_path_vertex]

        return path[::-1]

    def __str__(self):
        """
        Produces a string representation of the graph that can be used with print().
        The format of the graph is in GraphViz dot notation.
        """
        string = "digraph G {\n"
        for label in self.vertices:
            vertex = self.vertices[label]
            neighbors = vertex.get_neighbors()
            for neighbor in neighbors:
                string += f"   {vertex.get_label()} -> {neighbor.get_label()}"
                string += f' [label="{vertex.get_weight(neighbor)}"'
                string += f',weight="{vertex.get_weight(neighbor)}"];\n'
        string += "}\n"
        return string


def main():
    """
    Main
    1.Construct the graph shown in Figure 1 using your ADT.
    2.Print it to the console in GraphViz notation as shown in Figure 1.
    3.Print results of DFS starting with vertex “A” as shown in Figure 2.
    4.BFS starting with vertex “A” as shown in Figure 3.
    5.Print the path from vertex “A” to vertex “F” (not shown here) using Dijkstra's
       Shortest Path algorithm (DSP) as a string like #3 and #4.
    6.Print the shortest paths from “A” to each other vertex, one path per line using
       DSP.
    """
    g = Graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.add_vertex("E")
    g.add_vertex("F")

    g.add_edge("A", "B", 2)
    g.add_edge("A", "F", 9)
    g.add_edge("B", "F", 6)
    g.add_edge("B", "D", 15)
    g.add_edge("B", "C", 8)
    g.add_edge("C", "D", 1)
    g.add_edge("E", "C", 7)
    g.add_edge("E", "D", 3)
    g.add_edge("F", "B", 6)
    g.add_edge("F", "E", 3)

    print("Graph printed using GraphViz dot notation")
    print(g)

    print("DFS starting with vertex A")
    for vertex in g.dfs("A"):
        print(vertex, end="")
    print()

    print("BFS starting with vertex A")
    for vertex in g.bfs("A"):
        print(vertex, end="")
    print()

    print("Shortest path from vertex A to vertex F")
    print(g.dsp("A", "F"))

    print("All shortest paths from vertex A")
    print(g.dsp_all("A"))


if __name__ == "__main__":
    main()
