from scipy.cluster import hierarchy
import matplotlib.pyplot as plt
import numpy as np

translator = {
    'NA': -100
}


def getValuesReady(arr):
    core = []
    for line in arr:
        clearedLine = np.array(list(filter(lambda x: not (x in translator), line.split(",")))).astype(np.float)
        mean = clearedLine.mean()
        mappedLine = list(map(lambda x : mean if (x in translator) else float(x), line.split(",")))
        core.append(mappedLine)

    return np.array(core).astype(np.float)

f = open("votes.csv", "r")
answ = f.readlines()
f.close()
answ = answ[1:]
arr = getValuesReady(answ)


# ytdist = np.array([662., 877., 255., 412., 996., 295., 468., 268.,
#                    400., 754., 564., 138., 219., 869., 669.])
Z = hierarchy.linkage(arr, 'ward')
# plt.figure()
dn = hierarchy.dendrogram(Z)

hierarchy.set_link_color_palette(['m', 'c', 'y', 'k', 'a','b'])
# fig, axes = plt.subplots(1, 2, figsize=(8, 3))
# dn1 = hierarchy.dendrogram(Z, ax=axes[0], above_threshold_color='y',
#                            orientation='top')
# dn2 = hierarchy.dendrogram(Z, ax=axes[1],
#                            above_threshold_color='#bcbddc',
#                            orientation='right')
# hierarchy.set_link_color_palette(None)  # reset to default after use
plt.show()