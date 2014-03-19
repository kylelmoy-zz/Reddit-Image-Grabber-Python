'''
Created on Mar 13, 2014

@author: Kyle Moy
'''
import reddit, MySQLdb, getopt, sys

def main(argv):
    try:                                
        opts, args = getopt.getopt(argv, "h:u:p:d:l:", ["host=", "user=","pass=","db=","limit="])
    except getopt.GetoptError:
        print "Usage: redditCrawler.py -h <host> -u <user> -p <password> -d <db_name> -l <limit> <subreddit1> <subreddit2> <...>"
        sys.exit(2)  
    if (len(argv) < 9):
        print "Usage: redditCrawler.py -h <host> -u <user> -p <password> -d <db_name> -l <limit> <subreddit1> <subreddit2> <...>"
        sys.exit(2)
        
    for opt, arg in opts:
        if opt in ("-h", "--host"):
            host = arg
        elif opt in ("-u", "--user"):
            user = arg
        elif opt in ("-p", "--pass"):
            password = arg
        elif opt in ("-d", "--db"):
            db = arg
        elif opt in ("-l", "--limit"):
            limit = arg
    subNames = argv[10:]
    db = MySQLdb.connect(host=host, user=user, passwd=password, db=db,charset='utf8')
    cur = db.cursor() 
    for sub in subNames:
        result = reddit.parse(sub,limit)
        print "Found %s items in %s" % (len(result),sub)
        for item in result:
            print "[%s, %s]" % (item.sub,item.url)
            cur.execute("INSERT IGNORE INTO images (sub, title, author, permalink, link) VALUES (%s,%s,%s,%s,%s)",(item.sub,item.title,item.author,item.permalink,item.url))
    db.commit()
if __name__ == '__main__':
    main(sys.argv[1:])