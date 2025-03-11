from Network import *
import pygame as py


py.init()
screen_width = 800
screen_height = 800
num_boxes_hor = 7
num_boxes_ver = 7
box_width = screen_width / num_boxes_hor
box_height = screen_height / num_boxes_ver
screen = py.display.set_mode((screen_width, screen_height))
clock = py.time.Clock()


def unflatten_array(array):
    new_array = []
    dimension = []
    dimension_size = num_boxes_ver
    for i in range(len(array)):
        dimension.append(array[i])
        if (len(dimension) % dimension_size) == 0:
            new_array.append(dimension)
            dimension = []

    return new_array


def flatten_array(array):
    new_array = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            new_array.append(array[i][j])

    return new_array


def get_state_array(net):
    state_array = []
    for node in net.nodes:
        value = node.value
        state_array.append(node.value)

    return state_array


def display_array(array):
    disp_array = unflatten_array(array)
    box_x = 0
    box_y = 0
    for i in range(len(disp_array)):
        for j in range(len(disp_array[i])):
            if disp_array[i][j] == 1:
                rect = py.Rect(box_x, box_y, box_width, box_height)
                py.draw.rect(screen, "black", rect)
            box_x += box_width
        box_x = 0
        box_y += box_height


def create_net():
    initial_weight = 0
    num_boxes = num_boxes_hor * num_boxes_ver
    net = Network()

    for i in range(num_boxes):
        net.add_node()

    net.create_edges()

    return net


def main():
    net = create_net()
    in_state = [-1, -1, 1, 1, 1, -1, 1,
                     -1, -1, 1, -1, -1, -1, -1,
                     -1, -1, 1, -1, -1, -1, -1,
                     -1, 1, -1, -1, -1, -1, -1,
                     -1, 1, -1, -1, -1, -1, -1,
                     -1, -1, 1, -1, 1, -1, -1,
                     -1, -1, 1, 1, 1, 1, 1]


    learn_state_1 = [-1, -1, 1, 1, 1, 1, -1,
                     -1, -1, 1, -1, -1, -1, -1,
                     -1, -1, 1, -1, -1, -1, -1,
                     -1, -1, 1, -1, -1, -1, -1,
                     -1, -1, 1, -1, -1, -1, -1,
                     -1, -1, 1, -1, -1, -1, -1,
                     -1, -1, 1, 1, 1, 1, -1]

    learn_state_2 = [-1, -1, 1, 1, 1, 1, -1,
                     -1, -1, 1, -1, -1, 1, -1,
                     -1, -1, 1, -1, -1, 1, -1,
                     -1, -1, 1, 1, 1, 1, -1,
                     -1, -1, 1, -1, -1, -1, -1,
                     -1, -1, 1, -1, -1, -1, -1,
                     -1, -1, 1, -1, -1, -1, -1]

    net.learn(learn_state_1)

    running = True
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False

        screen.fill("white")
        display_array(in_state)
        net.inference(in_state)
        out_state = get_state_array(net)
        in_state = out_state

        py.display.flip()
        clock.tick(1)


if __name__ == "__main__":
    main()
    exit()
