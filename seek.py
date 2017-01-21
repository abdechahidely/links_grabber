"""
Author  : Abdechahid Ihya
Email   : abdechahide.ihya@hotmail.fr
Version : 0.1

Note : Contribution are appreciated
	   The results are generated from google web pages
	   You can find this software on Github in this link:
	   	https://github.com/abdechahidely/links_grabber/
"""

from errors_handler import satisfy_arguments
from worker         import *

def main():
	n_links, n_pages, query = satisfy_arguments()
	Web_Worker(n_links, n_pages, query).start()

if __name__ == '__main__':
	main()
