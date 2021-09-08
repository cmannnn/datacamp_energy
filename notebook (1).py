#!/usr/bin/env python
# coding: utf-8

# ## Energy saved from recycling
# <p>Did you know that recycling saves energy by reducing or eliminating the need to make materials from scratch? For example, aluminum can manufacturers can skip the energy-costly process of producing aluminum from ore by cleaning and melting recycled cans. Aluminum is classified as a non-ferrous metal.</p>
# <p>Singapore has an ambitious goal of becoming a zero-waste nation. The amount of waste disposed of in Singapore has increased seven-fold over the last 40 years. At this rate, Semakau Landfill, Singapore’s only landfill, will run out of space by 2035. Making matters worse, Singapore has limited land for building new incineration plants or landfills.</p>
# <p>The government would like to motivate citizens by sharing the total energy that the combined recycling efforts have saved every year. They have asked you to help them.</p>
# <p>You have been provided with three datasets. The data come from different teams, so the names of waste types may differ.</p>
# <div style="background-color: #efebe4; color: #05192d; text-align:left; vertical-align: middle; padding: 15px 25px 15px 25px; line-height: 1.6;">
#     <div style="font-size:16px"><b>datasets/wastestats.csv - Recycling statistics per waste type for the period 2003 to 2017</b>
#     </div>
#     <div>Source: <a href="https://www.nea.gov.sg/our-services/waste-management/waste-statistics-and-overall-recycling">Singapore National Environment Agency</a></div>
# <ul>
#     <li><b>waste_type: </b>The type of waste recycled.</li>
#     <li><b>waste_disposed_of_tonne: </b>The amount of waste that could not be recycled (in metric tonnes).</li>
#     <li><b>total_waste_recycle_tonne: </b>The amount of waste that could be recycled (in metric tonnes).</li>
#     <li><b>total_waste_generated: </b>The total amount of waste collected before recycling (in metric tonnes).</li>
#     <li><b>recycling_rate: </b>The amount of waste recycled per tonne of waste generated.</li>
#     <li><b>year: </b>The recycling year.</li>
# </ul>
#     </div>
# <div style="background-color: #efebe4; color: #05192d; text-align:left; vertical-align: middle; padding: 15px 25px 15px 25px; line-height: 1.6; margin-top: 17px;">
#     <div style="font-size:16px"><b>datasets/2018_2019_waste.csv - Recycling statistics per waste type for the period 2018 to 2019</b>
#     </div>
#     <div> Source: <a href="https://www.nea.gov.sg/our-services/waste-management/waste-statistics-and-overall-recycling">Singapore National Environment Agency</a></div>
# <ul>
#     <li><b>Waste Type: </b>The type of waste recycled.</li>
#     <li><b>Total Generated: </b>The total amount of waste collected before recycling (in thousands of metric tonnes).</li> 
#     <li><b>Total Recycled: </b>The amount of waste that could be recycled. (in thousands of metric tonnes).</li>
#     <li><b>Year: </b>The recycling year.</li>
# </ul>
#     </div>
# <div style="background-color: #efebe4; color: #05192d; text-align:left; vertical-align: middle; padding: 15px 25px 15px 25px; line-height: 1.6; margin-top: 17px;">
#     <div style="font-size:16px"><b>datasets/energy_saved.csv -  Estimations of the amount of energy saved per waste type in kWh</b>
#     </div>
# <ul>
#     <li><b>material: </b>The type of waste recycled.</li>
#     <li><b>energy_saved: </b>An estimate of the energy saved (in kiloWatt hour) by recycling a metric tonne of waste.</li> 
#     <li><b>crude_oil_saved: </b>An estimate of the number of barrels of oil saved by recycling a metric tonne of waste.</li>
# </ul>
# 
# </div>
# <pre><code>
# </code></pre>

# 

# # How much energy in kiloWatt hour (kWh) has Singapore saved per year by recycling glass, plastic, ferrous, and non-ferrous metals between 2015 and 2019?

# In[2]:


import pandas as pd
import numpy as np


# ## Recycling statistics per waste type for the period 2003 to 2017

# -waste_type: The type of waste recycled.
# -waste_disposed_of_tonne: The amount of waste that could not be recycled (in metric tonnes).
# -total_waste_recycle_tonne: The amount of waste that could be recycled (in metric tonnes).
# -total_waste_generated: The total amount of waste collected before recycling (in metric -tonnes).
# -recycling_rate: The amount of waste recycled per tonne of waste generated.
# -year: The recycling year.
# 

# In[3]:


wastestats = pd.read_csv('datasets/wastestats.csv', usecols=['waste_type', 'waste_disposed_of_tonne', 'total_waste_recycled_tonne',  'year'])


# In[4]:


# total_waste_generated - total_waste_recycle_ton = total_recycled


# In[5]:


wastestats.info()


# In[6]:


wastestats['waste_type'].value_counts()


# In[7]:


#wastestats.head()


# In[8]:


# filtering by waste_type 
wastestats_filtered = wastestats.loc[wastestats['waste_type'].isin(['Glass', 'Plastics', 'Plastic', 'Ferrous metal', 'Ferrous Metals', 'Ferrous Metal', 'Non-ferrous metal', 'Non-ferrous Metals', 'Non-ferrous metals', 'Ferrous Metals'])]


# In[9]:


# filtering by year 2015-2019
wastestats_filtered = wastestats_filtered[wastestats_filtered['year'] > 2014]


# In[10]:


wastestats_filtered.reset_index(drop=True, inplace=True)


# In[11]:


wastestats_filtered.head()


# In[12]:


# total_waste_generated - total_waste_recycle_ton = total_recycled


# In[13]:


# total waste after filtering by waste type
# total_waste_recycled = int(wastestats['total_waste_recycled_tonne'].sum())
# print(f'The total waste that was recycled 2015-2017: {total_waste_recycled}')


# ## Recycling statistics per waste type for the period 2018 to 2019

# In[14]:


eighteen_stats = pd.read_csv('datasets/2018_2019_waste.csv')


# Waste Type: The type of waste recycled.
# Total Generated: The total amount of waste collected before recycling (in thousands of metric tonnes).
# Total Recycled: The amount of waste that could be recycled. (in thousands of metric tonnes).
# Year: The recycling year.

# In[15]:


eighteen_stats.info()


# In[16]:


#eighteen_stats['year'].value_counts()


# In[17]:


#multiply total trash value by 1,000
eighteen_stats['Total Generated (\'000 tonnes)'] = eighteen_stats['Total Generated (\'000 tonnes)'].map(lambda x: x * 1000)


# In[18]:


#multiply total recycling by 1,000
eighteen_stats['Total Recycled (\'000 tonnes)'] = eighteen_stats['Total Recycled (\'000 tonnes)'].map(lambda x: x * 1000)


# In[19]:


eighteen_stats = eighteen_stats.rename(columns={'Year':'year', 'Waste Type': 'waste_type', 'Total Recycled (\'000 tonnes)': 'total_waste_recycled_tonne', 'Total Generated (\'000 tonnes)': 'total_waste_generated_tonne'})


# In[20]:


eighteen_stats.head()


# In[21]:


#total_waste_recycled_later = eighteen_stats['Total Generated in Tonnes'].sum()


# In[22]:


#total_waste_recycled_later


# In[23]:


#total_waste_generated_later = eighteen_stats['Total Recycled in Tonnes'].sum()


# In[24]:


#total_waste_generated_later


# ## Estimations of the amount of energy saved per waste type in kWh

# material: The type of waste recycled.
# energy_saved: An estimate of the energy saved (in kiloWatt hour) by recycling a metric tonne of waste.
# crude_oil_saved: An estimate of the number of barrels of oil saved by recycling a metric tonne of waste.

# In[25]:


energy_saved = pd.read_csv('datasets/energy_saved.csv')


# In[26]:


energy_saved.columns = energy_saved.iloc[2]


# In[27]:


energy_saved_data = energy_saved.iloc[3:4, 1:5].copy()


# In[28]:


energy_saved_data = energy_saved_data.apply(lambda x: x.str.replace('Kwh', ''))


# In[29]:


energy_saved_data = energy_saved_data.apply(pd.to_numeric)


# In[30]:


energy_saved_data


# In[31]:


energy_saved_data.rename(columns={'Plastic':'Plastics', 'Ferrous Metal': 'Ferrous metal', 'Non-Ferrous Metal':'Non-ferrous metal'}, inplace=True)


# In[32]:


energy_saved_data_new = energy_saved_data.T.reset_index()


# In[33]:


energy_saved_data_new


# In[34]:


energy_saved_data_new.rename(columns={2:'waste_type', 3:'energy_saved'}, inplace=True)


# In[35]:


energy_saved_data_new.set_index('waste_type', inplace=True)


# In[36]:


energy_saved_data_new


# In[37]:


#energy_saved.set_index('waste_type', inplace=True)


# In[38]:


# only care about glass, plastic, ferrous, and non-ferrous metals


# In[39]:


wastestats_filtered[wastestats_filtered['year'] == 2017]


# In[43]:


wastestats_filtered.groupby(['year'])['total_waste_recycled_tonne'].sum()


# In[44]:


eighteen_stats.head()


# In[45]:


eighteen_stats.groupby(['year'])['total_waste_recycled_tonne'].sum()


# In[40]:


wastest = pd.merge(wastestats_filtered, eighteen_stats, how='outer')


# In[41]:


wastest.head()


# In[42]:


wastest = pd.merge(wastest, energy_saved_data_new, left_on='waste_type', how='outer', right_index=True)


# In[43]:


wastest.head()


# In[44]:


wastest = wastest.sort_values('year').reset_index(drop=True)


# In[45]:


wastest.set_index('year', inplace=True)


# In[46]:


wastest.head()


# In[47]:


wastest['total_energy_saved'] = wastest['total_waste_recycled_tonne'] * wastest['energy_saved']


# In[48]:


annual_energy_savings = wastest.groupby(['year'])['total_energy_saved'].sum().reset_index()


# In[49]:


annual_energy_savings.set_index('year', inplace=True)


# In[50]:


annual_energy_savings


# In[ ]:


get_ipython().run_cell_magic('nose', '', '\nimport pandas as pd\nimport re\nimport numpy as np\n\nconvert_index = lambda x: [re.match(\'(\\d{4})\', date).group(0) for date in x.index.values.astype(str)]\n\ntest_solution = pd.DataFrame({\'year\': [2015, 2016, 2017, 2018, 2019],\\\n                             \'total_energy_saved\': [3.435929e+09, 2554433400, 2.470596e+09, 2.698130e+09,\n       2.765440e+09]}).set_index(\'year\')\n\ndef test_project():\n    \n    # Check whether the answer has been saved and is a DataFrame\n    assert \'annual_energy_savings\' in globals() and type(annual_energy_savings) == pd.core.frame.DataFrame, \\\n    "Have you assigned your answer to a DataFrame named `annual_energy_savings`?"\n    \n    # Check whether they have the right column in their DataFrame\n    assert annual_energy_savings.columns.isin([\'total_energy_saved\']).any(), \\\n    "Your DataFrame is missing the required column!"\n    \n    # Check whether they have included the correct index\n    assert annual_energy_savings.index.name == \'year\', \\\n    "Your DataFrame is missing the required index!"\n    \n    # Check whether the values (converted to an integer) contain in the only column are correct\n    # and check whether the index is identical\n    assert (test_solution.total_energy_saved.astype(\'int64\').values == \\\n    annual_energy_savings.total_energy_saved.astype(\'int64\').values).all()\\\n    and convert_index(test_solution) == convert_index(annual_energy_savings), \\\n    "Your submitted DataFrame does not contain the correct values!"')

