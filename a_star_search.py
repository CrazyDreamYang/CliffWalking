from implementation import *

def from_id_width1(id, width):
    return (id % width, id // width)

# 悬崖
cliffHoles = [from_id_width1(id, width=12) for id in
                  [37,38,39,40,41,42,43,44,45,46]]

if __name__ == '__main__':
    #创建地图
    diagram = GridWithWeights(12, 4)
    diagram.walls = cliffHoles
    start = (0, 3)
    goal = (11, 3)

    # 开始搜索
    came_from, cost_so_far = a_star_search(diagram, start, goal)
    draw_grid(diagram, point_to=came_from, start=start, goal=goal)
    print()
    draw_grid(diagram, path=reconstruct_path(came_from, start=start, goal=goal))