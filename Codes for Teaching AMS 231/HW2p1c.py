import numpy as np
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


#====================================================
# Actual plot
#====================================================

minlim = -3.0
maxlim = 3.0

a = 0.8
b = 1
k = 3

Y, X = np.mgrid[minlim:maxlim:100j, minlim:maxlim:100j]

U = Y
V = -(2*b - k*(np.abs(X)<=1))*a*Y - a**2*X

speed = np.sqrt(U*U + V*V)

fig, ax = plt.subplots()
ax.streamplot(X, Y, U, V, density=1.45,color='gray', linewidth=1)

# plot lines x_1 = \pm 1
plt.plot([-1, -1], [minlim, maxlim], 'xkcd:sienna', lw=1)
plt.plot([1, 1], [minlim, maxlim], 'xkcd:sienna', lw=1)
# add text for lines x_1 = \pm 1
ax.text(0.6, 3.05, r"$x_{1} = +1$", color = 'xkcd:sienna')
ax.text(-1.4, 3.05, r"$x_{1} = -1$", color = 'xkcd:sienna')

# plot axes
yaxs = plt.plot([0, 0], [minlim, maxlim], 'k--', lw=1)
xaxs = plt.plot([minlim, maxlim], [0, 0], 'k--', lw=1)

plt.xticks((-2, -1, 0, 1, 2))
plt.yticks((-2, -1, 0, 1, 2))
ax.axis('tight')
ax.set_aspect('equal')

p =2.1

start1 = [[0,p]]
strm1 = ax.streamplot(X, Y, U*(X>=0), V*(X>=0), start_points=start1, color="xkcd:azure", linewidth=2)
start2 = [[0,-p]]
strm2 = ax.streamplot(X, Y, U*(X<=0), V*(X<=0), start_points=start2, color="xkcd:azure", linewidth=2)
# mark the points
ax.text(-0.15, 2.08, r"\textbf{A}", color = 'xkcd:azure', size="11")
ax.text(1.06, 2.87, r"\textbf{B}", color = 'xkcd:azure', size="11")
ax.text(2.15, 0.01, r"\textbf{C}", color = 'xkcd:azure', size="11")
ax.text(1.06, -0.71, r"\textbf{D}", color = 'xkcd:azure', size="11")
ax.text(0.02, -1.83, r"\textbf{E}", color = 'xkcd:azure', size="11")

ax.text(0.01, -2.24, r"\textbf{A}$^{\!\!\prime}$", color = 'xkcd:azure', size="11")
ax.text(-0.96, -2.97, r"\textbf{B}$^{\!\prime}$", color = 'xkcd:azure', size="11")
ax.text(-2.32, 0.01, r"\textbf{C}$^{\prime}$", color = 'xkcd:azure', size="11")
ax.text(-1.18, 0.61, r"\textbf{D}$^{\!\prime}$", color = 'xkcd:azure', size="11")
ax.text(-0.16, 1.73, r"\textbf{E}$^{\!\prime}$", color = 'xkcd:azure', size="11")


# c = plt.Circle((0, 0), radius=1, color='b', lw=1.5, fill=False)
# ax.add_patch(c)

# draw origin (red=unstable)
ori = plt.Circle((0, 0), radius=0.06, facecolor='red')
ax.add_artist(ori)




ax.set_xlabel(r"$x_{1}$")
ax.set_ylabel(r"$x_{2}$", rotation="horizontal")

plt.savefig('HW2p1phaseplane.png', dpi=300)