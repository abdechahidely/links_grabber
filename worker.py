from bs4            import BeautifulSoup
from re             import findall
from requests       import get
from time           import time
from errors_handler import notify
import os

class Web_Worker:

	def __init__(self, n_of_links, n_of_pages, query):
		self.n_of_pages = n_of_pages
		self.n_of_links = n_of_links
		self.query      = query
		self.tracker    = []

	def links(self, page):
		data    = {'q':self.query, 'start': page}
		headers = {'User-agent': 'Mozilla/11.0'}
		try:
			source_code = get('https://google.com/search', data, headers=headers).text
		except KeyboardInterrupt:
			notify(4)
			exit(0)
		except:
			notify(3)
			exit(0)
		soup    = BeautifulSoup(source_code, 'html.parser')
		h3tags  = soup.findAll('h3', class_='r')
		total_l = []
		for tag in h3tags:
			try:
				total_l.append(findall(r'/?q=(.+?)&amp', str(tag))[0])
			except:
				continue
		return total_l

	def loop(self):
		path      = os.path.expanduser('~')
		file_name = '%s/Documents/Seek_logs/log_%s.txt'%(path, '_'.join(self.query.split(' ')))
		print('\n-> Searching in [%d] pages...'%len(self.n_of_pages))
		print('-> Results will be stored in :\n   \x1b[1;;34m%s\x1b[0m\n'%file_name)
		while True:
			if os.path.exists('%s/Documents/Seek_logs'%path):
				with open(file_name, 'w') as log_file:
					start = time()
					for n in self.n_of_pages:
						for link in self.links(n):
							self.tracker.append(link)
					self.tracker = self.tracker[:self.n_of_links]
					end = time() - start
					i = 1
					for link in self.tracker:
						log_file.write(link+'\n')
						print(str(i), '-', link)
						i +=1
				break
			else:
				os.chdir('%s/Documents'%path)
				os.system('mkdir Seek_logs')
	
		print('\nDone in : %ds\n'%end)

	def start(self):
		self.loop()
