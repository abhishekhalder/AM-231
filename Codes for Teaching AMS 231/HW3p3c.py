import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
import matplotlib.pyplot as plt

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

Lx1=-2
Lx2=2
Ly1=-2
Ly2=2

z0 = 5

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
X, Y = np.mgrid[Lx1:Lx2:30j, Ly1:Ly2:30j]
Z_manifold = (0.5*(X**2 + Y**2) - 0.25*X**4 + 5)
ax.plot_surface(X, Y, Z_manifold, cmap="summer", lw=0.5, rstride=1, cstride=1, alpha=0.7,label=r'$\sin (x)$')
cp = ax.contour(X, Y, Z_manifold, 25, linewidths=(1,), cmap="gray", linestyles="solid", offset=z0)
plt.clabel(cp, inline=True, 
          fontsize=10)
plt.xlim((Lx1, Lx2))
plt.ylim(Ly1, Ly2)
a1 = Arrow3D([-0.06, 4.5], [-0.06, -0.04], 
                [4.9, 4.9], mutation_scale=20, 
                lw=1, arrowstyle="-|>", color="r")
ax.add_artist(a1)
a2 = Arrow3D([-0.08, -0.08], [-0.08, 4.5], 
                [4.9, 4.9], mutation_scale=20, 
                lw=1, arrowstyle="-|>", color="r")
ax.add_artist(a2)
ax.axis('tight')
ax.set_aspect('equal')
plt.axis('off')
plt.savefig("HW3p3cContour.png", dpi=300)