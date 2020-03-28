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

#====================================================


a = 2
b = 3
p = 4
q = 5

t = np.linspace(0, 2 * np.pi, 100)

k = (a*q)/(b*p)

x1 = a*np.cos(t)
y1 = b*np.sin(t)

x2 = p*np.cos(t)
y2 = q*np.sin(t)

xsum = x1 + x2/(np.sqrt((k**2)*(np.sin(t))**2 + (np.cos(t))**2))

ysum = y1 + (k*y2)/(np.sqrt((k**2)*(np.sin(t))**2 + (np.cos(t))**2))

fig, ax = plt.subplots()
ax.fill(x1, y1, alpha=0.2, facecolor='blue')
plt.plot(x1, y1)
ax.fill(x2, y2, alpha=0.2, facecolor='darkorange')
plt.plot(x2, y2,'darkorange')
plt.plot(xsum, ysum, '--k')

ax.set_xlabel(r"$x_{1}$")
ax.set_ylabel(r"$x_{2}$", rotation="horizontal")


plt.savefig('MinkowskiSum2DEllipse.png', dpi=300)

