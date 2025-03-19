import random


def extract_prices(list_prices):
    results = []

    for data in list_prices:
        if '$' in data:
            last_part = data.rsplit('$', 1)[-1]
            last_price_value = last_part.replace('USD', '').strip()
            last_price_value = last_price_value.replace('.', '')
            try:
                last_price_number = int(last_price_value)
                results.append(last_price_number)
            except ValueError:
                results.append(0)
    return results


def get_random_slider_value(min_value, max_value, step):
    num_steps = int((max_value - min_value) / step) - 1
    random_step = random.randint(1, num_steps)
    random_value = min_value + (random_step * step)
    return random_value
