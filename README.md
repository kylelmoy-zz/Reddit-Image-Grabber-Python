RedditCrawler-Python
====================
Module Dependencies:
MySQLdb
requests

Usage:
redditCrawler.py -h <host> -u <user> -p <password> -d <db_name> -l <limit> <subreddit1> <subreddit2> <...>

Example:
-h localhost -u root -p MyPassword -d images -l 50 awwnime kemonomimi nekomimi

Currently known issues:
	No option for table name, currently hard-coded as "images"