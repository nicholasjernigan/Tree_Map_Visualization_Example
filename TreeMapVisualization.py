# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 19:08:05 2022

Example code creating a Tree Map and Bar Chart.

Data was cleaned, cleaning process was removed due to sensitivity of original data.
Data was also randomized.


I left in some of the first iterations of the Tree Map so you can see different options there are. The last one that is saved
turned out the best by far.




@author: nicho
"""
import pandas as pd
import sqlalchemy


#Load (cleaned previously) data that was originally in SQL

df = pd.read_csv('July_Spend_by_Category.csv')


df['tag_id'] = df['Category']
#Turn categories that are < 1% into 'other'
#Change names of other categories so they fit better in a visualization
other_list = ''
for x in range(0,len(df)):
    if df['Total Spend'][x] < (df['Total Spend'].sum()/100):
        other_list = other_list + df['tag_id'][x] +', '
        df['tag_id'][x] = 'other'
    elif df['tag_id'][x] == 'beauty_fashion':
        df['tag_id'][x] = 'beauty fash'
    elif df['tag_id'][x] == 'business_finance_nft':
        df['tag_id'][x] = 'bussiness finance NFT'
    elif df['tag_id'][x] == 'business_finance_personal':
        df['tag_id'][x] = 'bussiness finance personal'
    elif df['tag_id'][x] == 'hobbies_interests':
        df['tag_id'][x] = 'hobbies'
    elif df['tag_id'][x] == 'politics_campaigns':
        df['tag_id'][x] = 'poli camp'
    elif df['tag_id'][x] == 'technology_computing':
        df['tag_id'][x] = 'tech computing'
    elif df['tag_id'][x] == 'religion_spirituality':
        df['tag_id'][x] = 'religion'
    elif df['tag_id'][x] == 'food_drink':
        df['tag_id'][x] = 'food drink'
    elif df['tag_id'][x] == 'business_help':
        df['tag_id'][x] = 'business help'
    elif df['tag_id'][x] == 'entertainment_music':
        df['tag_id'][x] = 'entertainment music'
    elif df['tag_id'][x] == 'entertainment_rappers':
        df['tag_id'][x] = 'entertainment rappers'
    elif df['tag_id'][x] == 'healthy_living':
        df['tag_id'][x] = 'healthy living'
    elif df['tag_id'][x] == 'home_garden':
        df['tag_id'][x] = 'home garden'
    elif df['tag_id'][x] == 'medical_health':
        df['tag_id'][x] = 'medical health'
    elif df['tag_id'][x] == 'personalads':
        df['tag_id'][x] = 'personal ads'
    elif df['tag_id'][x] == 'real_estate':
        df['tag_id'][x] = 'real estate'
    elif df['tag_id'][x] == 'style_fashion':
        df['tag_id'][x] = 'style fashion'
d = df.groupby(by=["tag_id"]).sum()
df = d.reset_index()





#Create cool visualization


#TREEMAP ATTEMPT 1

#For each item add the percentage to the name
for x in range(0,len(df)):
    df['tag_id'][x] = df['tag_id'][x] + ' ' + str((round(100*df['Total Spend'][x]/df['Total Spend'].sum(),1))) + '%'


import matplotlib.pyplot as plt
import squarify    # pip install squarify (algorithm for treemap)


#Requires extra package installed from Github
#pip install git+https://github.com/chenyulue/matplotlib-extra.git
import mpl_extra.treemap as tr

# plot it
squarify.plot(sizes=df['Total Spend'], label=df['tag_id'], alpha=.8, pad=2, 
              norm_x=100)
plt.axis('off')
plt.show()





#TREEMAP ATTEMPT 2

fig, ax = plt.subplots(figsize=(14,14), dpi=300, subplot_kw=dict(aspect=1.156))

tr.treemap(ax, df, area='Total Spend', labels='tag_id', 
           cmap='Set2', fill='tag_id',
           rectprops=dict(ec='w'),
           textprops=dict(c='w'))

ax.axis('off')

#fig.savefig("spend_tree_map.png", bbox_inches='tight', dpi=300)



#FINAL TREEMAP (BEST ONE)

fig, ax = plt.subplots(figsize=(7,7), dpi=100, subplot_kw=dict(aspect=1.156))

trc = tr.treemap(
    ax, df, area='Total Spend', fill='Total Spend', labels='tag_id',
    rectprops={'ec':'w', 'lw':2},
    textprops={'c':'w', 'fontstyle':'italic','reflow':True},
               cmap='RdBu_r')
ax.axis('off')

cb = fig.colorbar(trc.mappable, ax=ax, shrink=0.5)

cb.ax.set_title('           Total Spend')
cb.outline.set_edgecolor('w')

fig.savefig('Spend_Percent_by_Category.png', dpi='figure', bbox_inches='tight')

plt.show()





#Bar graph of the spenders
df['Category'] = df['tag_id']
df = df.sort_values(by=['Total Spend'])


### Seaborn Bar Plot

import seaborn as sns
import matplotlib.pyplot as plt

sns.set(font_scale = 2)
sns.set_theme(style="whitegrid")
df1 = df[['Category','Total Spend']]
df1 = df1.sort_values(by='Total Spend', ascending=False)

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(10, 15), dpi=300)

# Plot the total crashes
sns.set_color_codes("pastel")
sns.barplot(x="Total Spend", y="Category", data=df1,
            label="Category", color="b")


f.savefig('Total_Spend.png', dpi=300, bbox_inches='tight')

plt.show()





