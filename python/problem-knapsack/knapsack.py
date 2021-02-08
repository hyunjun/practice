#   problem; http://philosophical.one/post/roadtrip-in-australia-financial-settlement/
from math import pow

def maximize_price(price_weight_list, limit_weight):

    def _maximize_price(checked_list, unchecked_list):
        sum_of_price = sum([t[0] for i, t in enumerate(price_weight_list) if i in checked_list])
        sum_of_weight = sum([t[1] for i, t in enumerate(price_weight_list) if i in checked_list])
        # print(checked_list, '->', sum_of_price)

        if sum_of_weight < limit_weight:
            prices = []
            for i in unchecked_list:
                tmp_checked_list = checked_list[:]
                tmp_checked_list.append(i)
                tmp_unchecked_list = unchecked_list[:]
                del tmp_unchecked_list[tmp_unchecked_list.index(i)]
                # print(tmp_checked_list, tmp_unchecked_list)
                prices.append(_maximize_price(tmp_checked_list, tmp_unchecked_list))
            return max(prices)

        elif sum_of_weight == limit_weight:
            return sum_of_price

        return 0

    return _maximize_price([], list(range(len(price_weight_list))))


def combination(n):
    result_set = []
    for i in range(1, int(pow(2, n))):
        j = i
        ind = 0
        tmp_list = []
        while 0 < j:
            if j & 0x1:
                tmp_list.append(ind)
            ind += 1
            j >>= 1
        result_set.append(tmp_list)
    return result_set


def maximize_price2(price_weight_list, limit_weight):
    combinations = combination(len(price_weight_list))
    prices = []
    for combi in combinations:
        sum_of_price = sum([t[0] for i, t in enumerate(price_weight_list) if i in combi])
        sum_of_weight = sum([t[1] for i, t in enumerate(price_weight_list) if i in combi])
        if sum_of_weight <= limit_weight:
            prices.append(sum_of_price)
    return max(prices)


if __name__ == '__main__':
    print(maximize_price([(4, 12), (2, 2), (2, 1), (1, 1), (10, 4)], 5))
    print(maximize_price2([(4, 12), (2, 2), (2, 1), (1, 1), (10, 4)], 5))
