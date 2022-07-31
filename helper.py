from scipy import sparse
import pickle
basepath='./'
X = sparse.load_npz(basepath+"data/yourmatrix.npz")
with open(basepath+'data/neigh.pkl','rb') as f:
    neigh=pickle.load(f)
def send_index(index):
	remm=neigh.kneighbors(X[index:index+1],n_neighbors=100,return_distance=False)
	return remm[0].tolist()