# 2018.01.01 G55T
# reference: https://github.com/jhlau/doc2vec
#

#python example to infer document vectors from trained doc2vec model
import gensim.models as g
import codecs
import math
import numpy as np
from scipy.cluster.vq import vq, kmeans, whiten


class ClassifySentences():
    # method: load Doc2Vec model
    def load_model(self):
        model="doc2vec/model/doc2vec.bin"

        d2v = g.Doc2Vec.load(model)
        return d2v

    # method: infer sentences
    def infer_sent(self,d2v,input_docs):
        #inference hyper-parameters
        START_ALPHA=0.01
        INFER_EPOCH=1000
        N_CLASS=4

        #infer test vectors
        vectors=[]
        for d in input_docs:
            vectors.append(d2v.infer_vector(d, alpha=START_ALPHA, steps=INFER_EPOCH))


#        output_vecs = np.array(vecs, dtype=float)
        output_vecs = np.array(vectors, dtype=float)

        # execute kmeans
        return calc_kmeans(output_vecs,N_CLASS)



def calc_kmeans(sim_matrix,n_class):
    # whiten matrix
    whiten(sim_matrix)
    # calculate kmeans
    centroid, destortion = kmeans(sim_matrix, n_class, iter=100, thresh=1e-05)
    labels, dist = vq(sim_matrix, centroid)
    return labels

