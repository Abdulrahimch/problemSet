# def countServers(grid):
#     all_com_servers = 0
#     for i in grid:
#         temp = sum(i)
#         if temp > 1:
#             all_com_servers += temp
#     temp = 0
#     for j in range(len(grid)):
#         for i in range(len(grid)):
#             temp += grid[i][j]
#
#         if temp > 1:
#             all_com_servers += temp
#
#         temp = 0
#
#     return all_com_servers
#
# print(countServers([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
#
def countServers(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Check the input: size of the grid. If it is 0 then exit
    if not (cols and rows):
        return 0

    connected = 0  # store number of connected computers
    points = []  # store coordinates of all the computers
    comps_per_row = [0] * rows  # store number of computers in given row
    comps_per_col = [0] * cols  # store number of computers in given column

    for row_i in range(rows):
        for col_i in range(cols):
            if grid[row_i][col_i]:  # checking if given cell is not 0
                points.append((row_i, col_i))  # add coordinated to the set
                comps_per_row[row_i] += 1  # increase nimber of computers in a given row
                comps_per_col[col_i] += 1  # increase nimber of computers in a given column

    # iterate through all computers
    print(comps_per_row)
    print(comps_per_col)
    for row_i, col_i in points:
        # is there more than 1 computer in given row or column
        if comps_per_row[row_i] > 1 or comps_per_col[col_i] > 1:
            # if yes, then computer is connected, count him
            connected += 1

    return connected
print(countServers([[1, 0], [1, 1]]))