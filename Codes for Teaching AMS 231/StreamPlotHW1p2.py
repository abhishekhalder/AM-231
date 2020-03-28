import numpy as np
import matplotlib.pyplot as plt

minlim = -3.0
maxlim = 3.0

Y, X = np.mgrid[minlim:maxlim:100j, minlim:maxlim:100j]

U = -X - Y/np.log(np.sqrt(X**2  + Y**2))
V = -Y + X/np.log(np.sqrt(X**2  + Y**2))

speed = np.sqrt(U*U + V*V)

fig, ax = plt.subplots()
ax.streamplot(X, Y, U, V, density=0.9,color='gray', linewidth=1)
plt.xticks((minlim, 0, maxlim))
plt.yticks((minlim, 0, maxlim))
plt.xlim((minlim, maxlim))
plt.ylim(minlim, maxlim)
ax.axis('tight')
ax.set_aspect('equal')

c = plt.Circle((0, 0), radius=1, color='b', lw=1.5, fill=False)
ax.add_patch(c)

ori = plt.Circle((0, 0), radius=0.05, facecolor='green')
ax.add_artist(ori)

plt.savefig('HW1p2Streamplot.png', dpi=300)