from scipy import sparse
import pickle
basepath='/Users/manas/Downloads/'
X = sparse.load_npz(basepath+"data/yourmatrix.npz")
with open(basepath+'data/neigh.pkl','rb') as f:
    neigh=pickle.load(f)
def send_index(index):
	print(index)
	remm=neigh.kneighbors(X[index:index+1],n_neighbors=100,return_distance=False)
	print(list(remm[0]))
	return remm[0].tolist()