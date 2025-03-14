class Utils:
    def extract_prices(self, list_prices):
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
