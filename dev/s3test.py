import botocore
import boto3
import boto
import smart_open

access_id = "AKIAIZ6QOMS2HHTSLFZA"
secret_id = "E0Y4CzpF/eYMUYJRQLsp+PivV5Zsfp1In+14JwRX"
conn = boto.connect_s3(access_id,secret_id)

# stream lines from an S3 object
for i in range(1,2):
	for line in smart_open.smart_open('s3://moyang28/Location.tsv'):
		print line
