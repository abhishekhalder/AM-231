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

fig, ax = plt.subplots()

x = np.linspace(-3, 3, 100)

y1 = np.abs(x)

y2 = y1*np.abs(x**2 - 1)

plt.plot(x, y1, 'blue')

plt.plot(x, y2, 'red')

ax.set_ylabel(r"$|u|$",rotation="horizontal")
ax.set_xlabel(r"$x$")

ax.autoscale (enable=True, axis='both', tight=1)

plt.text(1.85, 13, r"$|u_{{\rm{FL}}}|$", fontsize=20, color='r')
plt.text(2.3, 3.1, r"$|u_{{\rm{L}}}|$", fontsize=20, color='b')

plt.savefig('HW5p1.png', dpi=300)


fig, ax1 = plt.subplots()

x = np.linspace(-2, 2, 5000)
ys = x**3 - x*np.sqrt(x**4 + 1)
yfl = x**3 - x
yl = -x
plt.plot(x, yl,'blue', x, yfl, 'red', x, ys, 'green')
ax1.axhline(linewidth=1.5, color='k')
ax1.set_ylabel(r"$u(x)$",rotation="horizontal")
ax1.set_xlabel(r"$x$")
plt.xticks((-2, -1, 0, 1, 2))
plt.yticks((-6, -3, 0, 3, 6))
ax1.autoscale (enable=True, axis='both', tight=1)

plt.text(-1.9, 0.45, r"$u_{{\rm{S}}}(x)$", fontsize=20, color='g')
plt.text(1.3, 4, r"$u_{{\rm{FL}}}(x)$", fontsize=20, color='r')
plt.text(-1.2, 1.3, r"$u_{{\rm{L}}}(x)$", fontsize=20, color='b')
plt.text(1.5, 0.2, r"$u_{0}(x)$", fontsize=20, color='k')


plt.savefig('HW5p11.png', dpi=300)












