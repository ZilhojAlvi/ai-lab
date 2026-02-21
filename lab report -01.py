def iddfs_maze(grid, start, target, label):
    if not grid or not grid[0]:
        print(f"{label}Output:\nEmpty grid\n")
        return

    rows = len(grid)
    cols = len(grid[0])

    # This line gives depth 6 for 3×3 and depth 8 for 4×4
    max_depth = rows + cols

    if grid[start[0]][start[1]] == 1 or grid[target[0]][target[1]] == 1:
        print(f"{label}Output:")
        print(f"Path not found at max depth {max_depth} using IDDFS\n")
        return

    def dls(path, current, depth_left, visited):
        if current == target:
            return path

        if depth_left == 0:
            return None

        r, c = current

        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and (nr,nc) not in visited:
                visited.add((nr,nc))
                res = dls(path + [(nr,nc)], (nr,nc), depth_left-1, visited)
                if res is not None:
                    return res
                visited.remove((nr,nc))

        return None

    print(f"{label}Output:")

    for depth in range(1, max_depth + 1):
        visited = {start}               # fresh visited every depth!!
        result = dls([start], start, depth, visited)

        if result is not None:
            print(f"Path found at depth {depth} using IDDFS")
            print("Traversal Order:", result)
            print()  # empty line
            return

    print(f"Path not found at max depth {max_depth} using IDDFS\n")




grid1 = [
    [0, 1, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 0, 0],
    [1, 1, 1, 1]
]

iddfs_maze(grid1, (0,0), (2,3), "Case#1")



grid2 = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
]

iddfs_maze(grid2, (0,0), (2,2), "Case#2")