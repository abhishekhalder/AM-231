import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d

#====================================================
# Make plots beautiful
#====================================================

pts_per_inch = 72.27
# write "\the\textwidth" (or "\showthe\columnwidth" for a 2 collumn text)
text_width_in_pts = 300.0
# inside a figure environment in latex, the result will be on the
# dvi/pdf next to the figure. See url above.
text_width_in_inches = text_width_in_pts / pts_per_inch
# figure.png or figure.eps will be intentionally larger, because it is prettier
inverse_latex_scale = 2
fig_proportion = (3.0 / 3.0)
csize = inverse_latex_scale * fig_proportion * text_width_in_inches
# always 1.0 on the first argument
fig_size = (1.0 * csize, 0.85 * csize)
# find out the fontsize of your latex text, and put it here
text_size = inverse_latex_scale * 9
label_size = inverse_latex_scale * 10
tick_size = inverse_latex_scale * 8
# learn how to configure:
# http://matplotlib.sourceforge.net/users/customizing.html
params = {'backend': 'ps',
          'axes.labelsize': 16,
          'legend.fontsize': tick_size,
          'legend.handlelength': 2.5,
          'legend.borderaxespad': 0,
          'axes.labelsize': label_size,
          'xtick.labelsize': tick_size,
          'ytick.labelsize': tick_size,
          'font.family': 'serif',
          'font.size': text_size,
          'font.serif': ['Computer Modern Roman'],
          'ps.usedistiller': 'xpdf',
          'text.usetex': True,
          'figure.figsize': fig_size,
          # include here any neede package for latex
          'text.latex.preamble': [r'\usepackage{amsmath}'],
          }
plt.rcParams.update(params)
fig = plt.figure(1, figsize=fig_size)  # figsize accepts only inches.
fig.subplots_adjust(left=0.04, right=0.98, top=0.93, bottom=0.15,
                    hspace=0.05, wspace=0.02)


#====================================================
# Actual plot
#====================================================

utol = 500
ltol = -500

Lx1=-2
Lx2=2
Ly1=-2
Ly2=2

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
x, y = np.mgrid[Lx1:Lx2:50j, Ly1:Ly2:50j]

z = (1 + (1/x))*(1 + y)*(1 + 2*y)

# z[z > utol] = np.inf
# z[z < ltol] = -np.inf

ax.plot_surface(x, y, z, cmap="coolwarm", lw=0.5, rstride=1, cstride=1, alpha=0.8)

plt.xticks((-2, -1, 0, 1, 2))
plt.yticks((-2, -1, 0, 1, 2))

ax.set_ylabel(r"$y$",rotation="horizontal")
ax.set_xlabel(r"$x$")
ax.set_zlabel(r"$z$")

ax.autoscale (enable=True, axis='both', tight=1)

# plt.text(1.85, 13, r"$|u_{{\rm{FL}}}|$", fontsize=20, color='r')
# plt.text(2.3, 3.1, r"$|u_{{\rm{L}}}|$", fontsize=20, color='b')

plt.savefig('HW6p1.png', dpi=400)