import random


def get_random_slider_value(min_value, max_value, step):
    num_steps = int((max_value - min_value) / step) - 1
    random_step = random.randint(1, num_steps)
    random_value = min_value + (random_step * step)
    return random_value
