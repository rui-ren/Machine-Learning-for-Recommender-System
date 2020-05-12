# _*_ coding = utf-8 -*-
'''
Calculate the user similarity matrix

Create time 2020-5-11

'''

import collections
import numpy as np 
import pandas as pd 

def user_similarity(trainingset, user_iif_similarity):
    '''
    @ param
    : trainingset: JSON file.
    : user_iif_similarity. inverse item frequency
    @ return 
        similarity matrix
    '''
    movie_to_user = collections.defaultdict(set)
    movie_view_count = collections.defaultdict(int)
    # build the move to user table
    for user, movies in trainingset:
        for movie in movies:
            # hashset
            movie_to_user[movie].add(user)
            movie_view_count[movie] += 1
    num_movie = len(movie_to_user)

    user_similarity_matrices = {}

    for movie, users in movie_to_user.items():
        for user1 in users:
            usersim_mat.setdefault(user, {})
            for user2 in users:
                if user1 == user2:
                    continue
                if user_iif_similarity:
                    user_similarity_matrices[user1][user2] += 1 / math.log(1 + len(users))
                else:
                    user_similarity_matrices[user1][user2] += 1
    
    for user1, corr_users in user_similarity_matrices.items():
        len_user1 = len(trainset[user1])
        for user2, count in corr_users.items():
            len_user2 = len(trainingset[user2])
            user_similarity_matrices[user1][user2] = count / math.sqrt(len_user1 * len_user2)
    
    return user_similarity_matrices, movie_view_count, num_movie



