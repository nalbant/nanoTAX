import numpy as np
from os import listdir
from Bio import SeqIO

def s2ix():
	return {'A':0,'C':1,'G':2,'T':3}


def dimer_freq(s,AMI,ix):
	for i in range(1,AMI.shape[0]+1):
		for j in range(len(s)-i):
			AMI[i-1,ix[s[j]],ix[s[j+i]]]+=1.0
	return AMI

def dimer2entropy(AMI):
	h = np.zeros((AMI.shape[0]))
	for i in range(AMI.shape[0]):
		p1 = AMI[i,:,:].sum(axis=0)
		p1 = p1/p1.sum()
		p2 = AMI[i,:,:].sum(axis=1)
		p2 = p2/p2.sum()
		pp = AMI[i,:,:]/AMI[i,:,:].sum()
		for j in range(4):
			for k in range(4):
				if pp[j,k]>0.0:
					h[i]+=pp[j,k]*np.log2(pp[j,k]/(p1[j]*p2[k]))
	return h

def build_AMI_database(directory,profile_len):
	from Bio import SeqIO
	fo = open(directory+'/'+directory+'.csv','w')	

	inputtype = ['fasta','fna','fa']
	fin = listdir(directory)
	ix = s2ix()
	for fi in fin:
		if fi.split('.')[-1] in inputtype:
			AMI = np.zeros((profile_len,4,4))
			for rec in SeqIO.parse(directory+'/'+fi, "fasta"):
				AMI = dimer_freq(str(rec.seq),AMI,ix)
			h = dimer2entropy(AMI)
		fo.write(''.join(fi.split('.')[:-1])+',')
		for ent in h[:-1]:
			fo.write(str(ent)+',')
		fo.write(str(h[-1])+'\n')
	fo.close()

def AMI_score(DB,DB_dot,h,metric):
	if metric=='corr':
		return DB.dot(h).argmax()
	elif metric == 'Euclidian':
		return (DB_dot +h.T.dot(h)-2*DB.dot(h)).argmin()
	else:
		return np.absolute(DB-np.tile(h.T,(DB.shape[0],1))).sum(axis=1).argmin()





