import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


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

delta = 0.025
x = np.arange(-2.0, 2.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z = 0.5*(X**2 + Y**2) - 0.25*X**4

fig, ax = plt.subplots()
N = 20
CS = plt.contour(X, Y, Z, N, colors='black')
plt.clabel(CS, inline=1, fontsize=10)
levels = [0.05, 0.1, 0.2]
CS1 = plt.contour(X, Y, Z, levels,colors='black')
plt.clabel(CS1, inline=1, fontsize=10)

plt.imshow(Z, extent=[-2, 2, -2, 2], origin='lower',
           cmap='RdBu', alpha=0.5)
plt.colorbar();


Y, X = np.mgrid[-2:2:100j, -2:2:100j]

U = Y
V = -X - Y + X**3

speed = np.sqrt(U*U + V*V)
ax.streamplot(X, Y, U, V, density=1.4,color='gray', linewidth=1)







plt.title('{} levels'.format(N+3))

plt.xlim(-2, 2)
plt.ylim(-2, 2)

ori = plt.Circle((0, 0), radius=0.04, facecolor='green')
ax.add_artist(ori)

lfp = plt.Circle((-1, 0), radius=0.04, facecolor='red')
ax.add_artist(lfp)
rfp = plt.Circle((1, 0), radius=0.04, facecolor='red')
ax.add_artist(rfp)

# plot lines x_1 = \pm 1
plt.plot([-1, -1], [-2, 2], 'g--', lw=1)
plt.plot([1, 1], [-2, 2], 'g--', lw=1)


ax.set_xlabel(r"$x_{1}$")
ax.set_ylabel(r"$x_{2}$", rotation="horizontal")

plt.xticks((-2, -1, 0, 1, 2))
plt.yticks((-2, -1, 0, 1, 2))

plt.savefig('HW3p3cLevelSets.png', dpi=300)