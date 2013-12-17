
def minimalCoins(sum, coins):
	if sum in coins:
		return	1
	l = []
	for coin in coins:
		if coin <= sum:
			l.append(1 + minimalCoins(sum - coin, coins))
	return	min(l)

if __name__ == '__main__':
	print minimalCoins(15, [1, 3, 9, 10])
