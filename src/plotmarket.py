from alphavantage import AlphaVantage
import numpy as np
import matplotlib.pyplot as plt


dataQuerier = AlphaVantage("WGTCZMVQIT2F0E69")
mkData = dataQuerier.query("MSFT")


color = 'cornflowerblue'
text_style = dict(horizontalalignment='right', verticalalignment='center',
                  fontsize=12, fontdict={'family': 'monospace'})


def format_axes(ax):
    ax.margins(0.2)
    ax.set_axis_off()


def nice_repr(text):
    return repr(text).lstrip('u')


x = [x.timestamp for x in mkData]
y = [x.open for x in mkData]
fig, ax = plt.subplots()
ax.scatter(x, y)
ax.grid(True, zorder=5)

plt.show()
