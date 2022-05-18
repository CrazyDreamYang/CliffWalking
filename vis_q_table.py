import matplotlib.patches as mpatches
import numpy as np
import matplotlib.pyplot as plt

ACTION_COLORS = {
    0: (142, 207, 201),
    1: (255, 190, 122),
    2: (250, 127, 111),
    3: (130, 176, 210),
}
ACTION_LABELS = ["UP", "Right", "Down","Left"]
ACTION_SPACE = [key for key in ACTION_COLORS]

def convert2matplotlib_cmap(colors = ACTION_COLORS):
    cmap_colors = []
    for color in colors:
        r = colors[color][0] / 255.0
        g = colors[color][1] / 255.0
        b = colors[color][2] / 255.0
        alpha = 1.0
        cmap_colors.append((r, g, b, alpha))
    return cmap_colors

def get_action_idx(q_table, colunm, x, y):
    state_idx = colunm * x + y
    action_idx = np.argmax(q_table[state_idx])
    return action_idx

def get_state_value(q_table, colunm, x, y):
    state_idx = colunm * x + y
    # V = max(Q(s,a))
    state_value = np.max(q_table[state_idx])
    return state_value

def get_patches(colors, labels = ACTION_LABELS):
    patches = []
    for i in range(len(colors)):
        patches.append(mpatches.Patch(color=colors[i], label=labels[i]))
    return patches

def get_q_map(map, q_table):
    render_map = np.zeros((map.shape[1],map.shape[0]))
    for i in range(map.shape[1]):
        for j in range(map.shape[0]):
            action_idx = get_action_idx(q_table, map.shape[0], i, j)
            render_map[i][j] = action_idx
    return render_map

def get_v_map(map, q_table):
    render_map = np.zeros((map.shape[1],map.shape[0]))
    for i in range(map.shape[1]):
        for j in range(map.shape[0]):
            state_value = get_state_value(q_table, map.shape[0], i, j)
            render_map[i][j] = state_value
    return render_map

def vis_q_map(q_map, action_space=ACTION_SPACE):
    # visualize the q_map with the ACTION_COLORS
    # (h, w) -> (h, w, 3)
    canvas = np.zeros(q_map.shape + (3,), dtype=np.uint8)
    for action in action_space:
        canvas[q_map == action] = ACTION_COLORS[action]
    return canvas

