#from email.mime import base
from scipy import sparse
import pickle
#import pandas as pd
basepath='/Users/manas/Downloads/'
X = sparse.load_npz(basepath+"data/yourmatrix.npz")
with open(basepath+'data/neigh.pkl','rb') as f:
    neigh=pickle.load(f)
#df=pd.read_csv(basepath+'/data/data.csv')
#df.fillna('')
# def top(start=0,end=20):
# 	collect=[]
# 	for i,row in df.iloc[start:end,[0,1,3,5,21,4,19,7]].iterrows():
# 		collect.append(dict(row))
# 	return collect		
	
# def rem(index=0):
# 	remm=neigh.kneighbors(X[index:index+1],n_neighbors=100,return_distance=False)
# 	data=df.iloc[remm[0],[0,1,3,5,21,4,19,7]].dropna()
# 	# ['title', 'author', 'description', 'coverImg', 'rating', 'likedPercent','isbn']
# 	'''
# 	{1: 'title',
#  3: 'author',
#  4: 'rating',
#  5: 'description',
#  19: 'likedPercent',
#  21: 'coverImg'
# 	7:'isbn'
# 	}
# 	'''
# 	collect=[]
# 	for index,row in data.iterrows():
# 		collect.append(dict(row))
# 	return collect
def send_index(index):
	print(index)
	remm=neigh.kneighbors(X[index:index+1],n_neighbors=100,return_distance=False)
	print(list(remm[0]))
	return remm[0].tolist()