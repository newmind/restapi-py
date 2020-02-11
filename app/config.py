import os

mysql_config = {
	'host': os.environ.get('MYSQL_HOST', 'localhost:32000'),
	'user': os.environ.get('MYSQL_USER', 'root'),
	'pass': os.environ.get('MYSQL_PASS', ''),
	'db':   os.environ.get('MYSQL_DB', 'esport'),
}

def alchemy_uri():
	return 'mysql://%s:%s@%s/%s?charset=utf8mb4' % (
		mysql_config['user'], mysql_config['pass'], mysql_config['host'], mysql_config['db']
	)