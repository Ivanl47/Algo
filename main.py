from collections import deque

def has_cycle_bfs(graph, start, visited):
    queue = deque([(start, -1)])
    visited[start] = True

    while queue:
        vertex, parent = queue.popleft()

        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, vertex))
            elif parent != neighbor:
                return True

    return False

def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()
    n = int(lines[0])
    graph = [[] for _ in range(n)]

    for line in lines[1:]:
        u, v = map(int, line.split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    visited = [False] * n

    cycle_present = False
    for i in range(n):
        if not visited[i]:
            if has_cycle_bfs(graph, i, visited):
                cycle_present = True
                break

    with open("output.txt", "w") as output_file:
        output_file.write(str(cycle_present))

if __name__ == "__main__":
    main()
