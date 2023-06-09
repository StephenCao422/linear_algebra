import numpy as np
import numpy.linalg as la


friend_groups = nullspace(friends)
num_friend_groups = friend_groups.shape[1]
friend_groups_sum = np.sum(friend_groups, axis = 0)
group_idx = np.where(friend_groups[12] == 1)[0][0]
num_meme_spread = friend_groups_sum[group_idx]