import sys

ARGS   = ['[query]', '[number_of_links - nofl]']
ERRORS = ['\x1b[1;;31mERROR\x1b[0m : ',
		  'Argument \x1b[2;41;30m %s \x1b[0m was not provided.',
		  'Arguments \x1b[2;41;30m %s - %s \x1b[0m were not provided.',
		  '\x1b[2;41;30mNetworking issue.\x1b[0m',
		  '\x1b[2;;31mKeyboard Interruption\x1b[0m'
		 ]
HELP   = ['\x1b[1;;33m%s\x1b[0m : Means the sequence you search for.'%ARGS[0],
		  '\x1b[1;;33m%s\x1b[0m : Means a certain number of urls to return.'%ARGS[1]
		 ]

def notify(err_index, *args):
	print(ERRORS[0] + ERRORS[err_index] % args)

def pages(links_number):
	if len(str(links_number)) == 1 or links_number == 10:
		return [0]
	else:
		pages = int(str(links_number)[0] + '0'*(len(str(links_number))-1))
		x = []
		for i in range(pages+1):
			if i%10 == 0:
				x.append(i)
			else:
				continue
		return x

def satisfy_arguments():
	try:
		number_of_links, query = sys.argv[1], ' '.join(sys.argv[2:]) 

		try:
			number_of_links = int(number_of_links)
		except ValueError:
			if number_of_links == '-h' or number_of_links == '--help':
				if query.lower() == 'query':
					print(HELP[0])
					exit(0)
				elif query.lower() == 'number_of_links' or query.lower() == 'nofl':
					print(HELP[1])
					exit(0)
				else:
					print(HELP[0]+'\n'+HELP[1])
					exit(0)
			notify(1, "number_of_links")
			exit(0)

		if query == '':
			notify(1, "query")
			exit(0)

	except IndexError:
		notify(2, 'number_of_links', 'query')
		exit(0)
		
	return number_of_links, pages(number_of_links), query
