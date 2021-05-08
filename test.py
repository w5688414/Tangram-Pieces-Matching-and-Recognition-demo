from game_class import Solver

pieces_num = [2, 1, 1, 1, 2]
path='img/tangram1.png'
solver = Solver(path, pieces_num = pieces_num)
# dfs
# for i in range(3):
#     solver.solve_dfs(i)
# print(solver.graph.current_graph)


# solver.solve_dfs(0)
# solver.solve_bfs()

# greedy search
solver.greedy()