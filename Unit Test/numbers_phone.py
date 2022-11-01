def number_phone_br(num):
	num = str(num)
	number = ''

	for char in num:
		if char in '0123456789':
			number += char

	if number[-9] == '9':
		number = number[-1:-10:-1][::-1]

	else:
		number = number[-1:-9:-1][::-1]

	number = int(str('21' + number))

	return number