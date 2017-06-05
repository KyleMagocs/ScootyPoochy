from pygame import time

from inputs import get_mouse


def input_test_loop():
    prev_x = 0
    prev_y = 0
    distance_x = distance_y = 0
    for i in range(0, 15):
        events = get_mouse()
        print(len(events))
        for event in events:
            if event.code == 'ABS_X':
                distance_x = prev_x - event.state
                prev_x = event.state
            if event.code == 'ABS_Y':
                distance_y = prev_x - event.state
                prev_x = event.state
        print('x:  {0} '
              'y:  {1}'
              .format(distance_x, distance_y))

        time.wait(.03)
