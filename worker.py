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
		total_l = []
		for tag in BeautifulSoup(source_code, 'html.parser').findAll('h3', class_='r'):
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
					for n in self.n_of_pages:
						for link in self.links(n):
							self.tracker.append(link)
					self.tracker = self.tracker[:self.n_of_links]
					i = 1
					for link in self.tracker:
						log_file.write(link+'\n')
						print(str(i), '-', link)
						i +=1
				break
			else:
				os.system('mkdir %s/Documents/Seek_logs'%path)

	def start(self):
		self.loop()
