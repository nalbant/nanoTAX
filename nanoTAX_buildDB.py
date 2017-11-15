import AMI_profile as ap
from subprocess import call
import sys

DatabaseType = sys.argv[1]
input_dir = sys.argv[2]
if len(sys.argv)>3:
	profile_len = sys.argv[3]

if DatabaseType == 'AMI':
	ap.build_AMI_database(input_dir,profile_len)
elif DatabaseType == 'RAI':
	call('raiphy - I '+input_dir+' -o '+input_dir+'/'+input_dir+'.db -m 2', shell=True )
else:
	print('Error: Unknown database method!')
	sys.exit()
	
