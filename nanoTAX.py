from Bio import SeqIO
from os import listdir
import numpy as np
import sys
import AMI_profile as ap
from subprocess import call



input_dir = sys.argv[1]
batch_mode_on = sys.argv[2]
Algorithm = sys.argv[3]
database = sys.argv[4]

if len(sys.argv)>5:
	profile_len = sys.argv[5]
	metric = sys.argv[6]
else:
	profile_len = 11 

inputtype = ['fasta','fna','fa']

fin = listdir(input_dir)


if int(batch_mode_on) == 1 and Algorithm == 'AMI' :
	ix = ap.s2ix()
	DB = np.genfromtxt(database,delimiter=',')[:,1:]
	targetnames = [l.split(',')[0]  for l in open(database)]
	DB_dot = DB.dot(DB.T).diagonal()
	outfilename = input_dir.strip('/').split('/')[-1]
	if outfilename =='.' or outfilename =='..':
		outfilename = 'stdout'
	fo = open(input_dir+'/'+outfilename+'.ami','w')
	for fi in fin:
		if fi.split('.')[-1] in inputtype:
			AMI = np.zeros((int(profile_len),4,4))
			for rec in SeqIO.parse(input_dir+'/'+fi, "fasta"):
				s = str(rec.seq)
				AMI = ap.dimer_freq(s,AMI,ix)
			h = ap.dimer2entropy(AMI)
			picked_ix = ap.AMI_score(DB,DB_dot,h,metric)
			fo.write('>'+fi+'\n'+ targetnames[picked_ix]+'\n')
	fo.close()
elif Algorithm == 'AMI':
	ix = ap.s2ix()
	DB = np.genfromtxt(database,delimiter=',')[:,1:]
	targetnames = [l.split(',')[0]  for l in open(database)]
	DB_dot = DB.dot(DB.T).diagonal()
	for fi in fin:
		if fi.split('.')[-1] in inputtype:
			fo = open(input_dir+'/'+fi+'.ami','w')
			for rec in SeqIO.parse(input_dir+'/'+fi, "fasta"):
				AMI = np.zeros((int(profile_len),4,4))
				s = str(rec.seq)
				AMI = ap.dimer_freq(s,AMI,ix)
				h = ap.dimer2entropy(AMI)
				picked_ix = ap.AMI_score(DB,DB_dot,h,metric)
				fo.write('>'+rec.id+'\n'+ targetnames[picked_ix]+'\n')
			fo.close()
elif Algorithm == 'RAI' and int(batch_mode_on) != 1:
	for fi in fin:
		if fi.split('.')[-1] in inputtype:
			call('raiphy -i '+input_dir+'/'+fi+ ' -o '+input_dir+'/'+fi+'.rai', shell=True )
else:
	print("Error: RAI classificatio in batch mode is not available in this version!")
	sys.exit()








