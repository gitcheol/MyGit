#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 00:35:34 2019

@author: kkim
"""
# Sources from https://github.com/cbrownley/foundations-for-analytics-with-python/tree/master/plots

##1 Bar plots represent numerical values, such as counts, for a set of categories. Common bar plots include vertical and horizontal plots, stacked plots, and grouped plots.
#
#import matplotlib.pyplot as plt
#plt.style.use('ggplot')

#customers = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO']
#customers_index = range(len(customers))
#sale_amounts = [127, 90, 201, 111, 232]
#
#fig = plt.figure()
#ax1 = fig.add_subplot(1,1,1)
#ax1.bar(customers_index, sale_amounts, align='center', color='darkblue')
#ax1.xaxis.set_ticks_position('bottom')
#ax1.yaxis.set_ticks_position('left')
#plt.xticks(customers_index, customers, rotation=0, fontsize='small')
#
#plt.xlabel('Customer Name')
#plt.ylabel('Sale Amount')
#plt.title('Sale Amount per Customer')
#
#plt.savefig('bar_plot.png', dpi=400, bbox_inches='tight')
#plt.show()

##2 Histograms represent distributions of numerical values. Common histograms include frequency distributions, frequency density distributions, probability distributions, and probability density distributions
#
#import numpy as np
#import matplotlib.pyplot as plt
#plt.style.use('ggplot')
#
#mu1, mu2, sigma = 100, 130, 15
#x1 = mu1 + sigma*np.random.randn(10000)
#x2 = mu2 + sigma*np.random.randn(10000)
#
#fig = plt.figure()
#ax1 = fig.add_subplot(1,1,1)
#n, bins, patches = ax1.hist(x1, bins=50, normed=False, color='darkgreen')
#n, bins, patches = ax1.hist(x2, bins=50, normed=False, color='orange', alpha=0.5)
#ax1.xaxis.set_ticks_position('bottom')
#ax1.yaxis.set_ticks_position('left')
#
#plt.xlabel('Bins')
#plt.ylabel('Number of Values in Bin')
#fig.suptitle('Histograms', fontsize=14, fontweight='bold')
#ax1.set_title('Two Frequency Distributions')
#
#plt.savefig('histogram.png', dpi=400, bbox_inches='tight')
#plt.show()


##3 Line plots represent numerical values along a number line. It’s common to use line plots to show data over time.
#from numpy.random import randn
#import matplotlib.pyplot as plt
#plt.style.use('ggplot')
#
#plot_data1 = randn(50).cumsum()
#plot_data2 = randn(50).cumsum()
#plot_data3 = randn(50).cumsum()
#plot_data4 = randn(50).cumsum()
#
#fig = plt.figure()
#ax1 = fig.add_subplot(1,1,1)
#ax1.plot(plot_data1, marker=r'o', color=u'blue', linestyle='-', label='Blue Solid')
#ax1.plot(plot_data2, marker=r'+', color=u'red', linestyle='--', label='Red Dashed')
#ax1.plot(plot_data3, marker=r'*', color=u'green', linestyle='-.', label='Green Dash Dot')
#ax1.plot(plot_data4, marker=r's', color=u'orange', linestyle=':', label='Orange Dotted')
#ax1.xaxis.set_ticks_position('bottom')
#ax1.yaxis.set_ticks_position('left')
#
#ax1.set_title('Line Plots: Markers, Colors, and Linestyles')
#plt.xlabel('Draw')
#plt.ylabel('Random Number')
#plt.legend(loc='best')
#
#plt.savefig('line_plot.png', dpi=400, bbox_inches='tight')
#plt.show()


##4 Scatter plots represent the values of two numerical variables along two axes—for example, height versus weight or supply versus demand. Scatter plots provide some indication of whether the variables are positively correlated (i.e., the points are con‐ centrated in a specific configuration) or negatively correlated (i.e., the points are spread out like a diffuse cloud). You can also draw a regression line, the line that min‐ imizes the squared error, through the points to make predictions for one variable based on values of the other variable.
#
#import numpy as np
#import matplotlib.pyplot as plt
#plt.style.use('ggplot')
#
#x = np.arange(start=1., stop=15., step=1.)
#y_linear = x + 5. * np.random.randn(14)
#y_quadratic = x**2 + 10. * np.random.randn(14)
#
#fn_linear = np.poly1d(np.polyfit(x, y_linear, deg=1))
#fn_quadratic = np.poly1d(np.polyfit(x, y_quadratic, deg=2))
#
#fig = plt.figure()
#ax1 = fig.add_subplot(1,1,1)
#ax1.plot(x, y_linear, 'bo', x, y_quadratic, 'go', \
#			x, fn_linear(x), 'b-', x, fn_quadratic(x), 'g-', linewidth=2.)
#ax1.xaxis.set_ticks_position('bottom')
#ax1.yaxis.set_ticks_position('left')
#
#ax1.set_title('Scatter Plots with Best Fit Lines')
#plt.xlabel('x')
#plt.ylabel('f(x)')
#plt.xlim((min(x)-1., max(x)+1.))
#plt.ylim((min(y_quadratic)-10., max(y_quadratic)+10.))
#
#plt.savefig('scatter_plot.png', dpi=400, bbox_inches='tight')
#plt.show()

##5 Box plots represent data based on its minimum, first quartile, median, third quartile, and maximum values. The bottom and top of the box show the first and third quar‐ tile values, and the line through the middle of the box shows the median value. The lines, called whiskers, that extend from the ends of the box show the smallest and largest non-outlier values, and the points beyond the whiskers represent outliers.
#
#import numpy as np
#import matplotlib.pyplot as plt
#plt.style.use('ggplot')
#
#N = 500
#normal = np.random.normal(loc=0.0, scale=1.0, size=N)
#lognormal = np.random.lognormal(mean=0.0, sigma=1.0, size=N)
#index_value = np.random.random_integers(low=0, high=N-1, size=N)
#normal_sample = normal[index_value]
#lognormal_sample = lognormal[index_value]
#box_plot_data = [normal,normal_sample,lognormal,lognormal_sample]
#
#fig = plt.figure()
#ax1 = fig.add_subplot(1,1,1)
#
#box_labels = ['normal','normal_sample','lognormal','lognormal_sample']
#ax1.boxplot(box_plot_data, notch=False, sym='.', vert=True, whis=1.5, \
#				showmeans=True, labels=box_labels)
#ax1.xaxis.set_ticks_position('bottom')
#ax1.yaxis.set_ticks_position('left')
#ax1.set_title('Box Plots: Resampling of Two Distributions')
#ax1.set_xlabel('Distribution')
#ax1.set_ylabel('Value')
#
#plt.savefig('box_plot.png', dpi=400, bbox_inches='tight')
#plt.show()


##6 pandas simplifies the process of creating figures and plots based on data in Series and DataFrames by providing a plot function that operates on Series and DataFrames. By default, the plot function creates line plots, but you can use the kind argument to create different types of plots.
#
#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#plt.style.use('ggplot')
#
#fig, axes = plt.subplots(nrows=1, ncols=2)
#ax1, ax2 = axes.ravel()
#
#data_frame = pd.DataFrame(np.random.rand(5, 3),
#						index=['Customer 1', 'Customer 2', 'Customer 3', 'Customer 4', 'Customer 5'],
#						columns=pd.Index(['Metric 1', 'Metric 2', 'Metric 3'], name='Metrics'))
#
#data_frame.plot(kind='bar', ax=ax1, alpha=0.75, title='Bar Plot')
#plt.setp(ax1.get_xticklabels(), rotation=45, fontsize=10)
#plt.setp(ax1.get_yticklabels(), rotation=0, fontsize=10)
#ax1.set_xlabel('Customer')
#ax1.set_ylabel('Value')
#ax1.xaxis.set_ticks_position('bottom')
#ax1.yaxis.set_ticks_position('left')
#
#colors = dict(boxes='DarkBlue', whiskers='Gray', medians='Red', caps='Black')
#data_frame.plot(kind='box', color=colors, sym='r.', ax=ax2, title='Box Plot')
#plt.setp(ax2.get_xticklabels(), rotation=45, fontsize=10)
#plt.setp(ax2.get_yticklabels(), rotation=0, fontsize=10)
#ax2.set_xlabel('Metric')
#ax2.set_ylabel('Value')
#ax2.xaxis.set_ticks_position('bottom')
#ax2.yaxis.set_ticks_position('left')
#
#plt.savefig('pandas_plots.png', dpi=400, bbox_inches='tight')
#plt.show()
#
##7 seaborn simplifies the process of creating informative statistical graphs and plots in Python. It is built on top of matplotlib, supports numpy and pandas data structures, and incorporates scipy and statsmodels statistical routines.
#
#
#import seaborn as sns
#import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
#
#sns.set(color_codes=True)
#
#
## Simple plot of linear, quadratic, and cubic curves
#x = np.linspace(0, 2, 100)
#plt.plot(x, x, label='linear')
#plt.plot(x, x**2, label='quadratic')
#plt.plot(x, x**3, label='cubic')
#plt.xlabel('x label')
#plt.ylabel('y label')
#plt.title("Simple Plot")
#plt.legend(loc="best")
#plt.show()
#
#
## Histogram
#x = np.random.normal(size=1000)
#sns.distplot(x, bins=20, kde=True, rug=False, label="Histogram w/o Density")
#sns.utils.axlabel("Value", "Frequency")
#plt.title("Histogram of a Random Sample from a Normal Distribution")
#plt.legend()
#plt.show()
#
#
## Scatter plot
#mean, cov = [5, 10], [(1, .5), (.5, 1)]
#data = np.random.multivariate_normal(mean, cov, 200)
#data_frame = pd.DataFrame(data, columns=["x", "y"])
#sns.jointplot(x="x", y="y", data=data_frame, kind="reg").set_axis_labels("x", "y")
#plt.suptitle("Joint Plot of Two Variables with Bivariate and Univariate Graphs")
#plt.show()
#
#
## Pairwise bivariate
##iris = sns.load_dataset("iris")
##sns.pairplot(iris)
##plt.show()
#
#
## Linear regression model
#tips = sns.load_dataset("tips")
##sns.lmplot(x="total_bill", y="tip", data=tips)
#sns.lmplot(x="size", y="tip", data=tips, x_jitter=.15, ci=None)
##sns.lmplot(x="size", y="tip", data=tips, x_estimator=np.mean, ci=None)
#plt.show()
#
#
## Box plots
#sns.boxplot(x="day", y="total_bill", hue="time", data=tips)
##sns.factorplot(x="time", y="total_bill", hue="smoker",
##               col="day", data=tips, kind="box", size=4, aspect=.5)
#plt.show()
#
#
## Bar plots
#titanic = sns.load_dataset("titanic")
##sns.barplot(x="sex", y="survived", hue="class", data=titanic)
##sns.countplot(y="deck", hue="class", data=titanic, palette="Greens_d")
##plt.show()
#
#
## Non-linear regression model
#anscombe = sns.load_dataset("anscombe")
## polynomial
##sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'II'"),
##           order=2, ci=False, scatter_kws={"s": 80})
##plt.show()
#
#
## robust to outliers
##sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'III'"),
##           robust=True, ci=False, scatter_kws={"s": 80})
##plt.show()
#
#
## logistic
##tips["big_tip"] = (tips.tip / tips.total_bill) > .15
##sns.lmplot(x="total_bill", y="big_tip", data=tips, logistic=True, y_jitter=.03).set_axis_labels("Total Bill", "Big Tip")
##plt.title("Logistic Regression of Big Tip vs. Total Bill")
##plt.show()
#
#
## lowess smoother
##sns.lmplot(x="total_bill", y="tip", data=tips, lowess=True)
##plt.show()
#
#
## Condition on other variables
##sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips,
##           markers=["o", "x"], palette="Set1")
##sns.lmplot(x="total_bill", y="tip", hue="smoker",
##           col="time", row="sex", data=tips)
##plt.show()
#
#
## Control shape and size of plot
##sns.lmplot(x="total_bill", y="tip", col="day", data=tips, col_wrap=2, size=3)
##sns.lmplot(x="total_bill", y="tip", col="day", data=tips, aspect=.5)
##plt.show()
#
#
## Plotting regression in other contexts
##sns.jointplot(x="total_bill", y="tip", data=tips, kind="reg")
##sns.pairplot(tips, x_vars=["total_bill", "size"], y_vars=["tip"],
##             size=5, aspect=.8, kind="reg")
##sns.pairplot(tips, x_vars=["total_bill", "size"], y_vars=["tip"],
##             hue="smoker", size=5, aspect=.8, kind="reg")
##plt.show()



#8 ggplot provides a few basic elements: geometries, aesthetics, and scales. It also provides some additional elements for more advanced plots: statistical transfor‐ mations, coordinate systems, facets, and visual themes.
# $ pip install ggplot 해야 함
#
#from ggplot import *
#"""
#print(mtcars.head())
#plt1 = ggplot(aes(x='mpg'), data=mtcars) +\
# 		geom_histogram(fill='darkblue', binwidth=2) +\
#		xlim(10, 35) + ylim(0, 10) +\
#		xlab("MPG") + ylab("Frequency") +\
#		ggtitle("Histogram of MPG") +\
#		theme_matplotlib()
#print(plt1)
#print(meat.head())
#plt2 = ggplot(aes(x='date', y='beef'), data=meat) +\
#		geom_ne(color='purple', size=1.5, alpha=0.75) +\
#		stat_smooth(colour='blue', size=2.0, span=0.15) +\
#		xlab("Year") + ylab("Head of Cattle Slaughtered") +\
#		ggtitle("Beef Consumption Over Time") +\
#		theme_seaborn()
#print(plt2)
#"""
#print(diamonds.head())
#plt3 = ggplot(diamonds, aes(x='carat', y='price', colour='cut')) +\
#		geom_point(alpha=0.5) +\
#		scale_color_gradient(low='#05D9F6', high='#5011D1') +\
#		xlim(0, 6) + ylim(0, 20000) +\
#		xlab("Carat") + ylab("Price") +\
#		ggtitle("Diamond Price by Carat and Cut") +\
#		theme_gray()
#print(plt3)
#
##ggsave(plt3, "ggplot_plots.png")