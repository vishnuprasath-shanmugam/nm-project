#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import datetime

get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


# Reading in the CSV file as a DataFrame 
games_df = pd.read_csv('games.csv')


# In[4]:


# Looking at the first five rows
games_df.head()


# In[5]:


# Viewing the shape of the DataFrame
games_df.shape


# In[6]:


# Converting to datetime.date values
games_df['gameDate'] = pd.to_datetime(games_df['gameDate']).dt.date

# Converting to datetime.time values
games_df['gameTimeEastern'] = pd.to_datetime(games_df['gameTimeEastern']).dt.time

# Looking at the first five rows
games_df.head()


# In[7]:


# Checking the frequency of games in relation to game dates
# games_df['gameDate'].value_counts().reset_index()

games_df['gameDate'].value_counts().reset_index()


# In[8]:


# Checking the frequency of games in relation to game dates
date_dist = games_df['gameDate'].value_counts().reset_index()

# Renaming the columns
date_dist.columns = ['date', 'frequency']

# Looking at the first five rows
date_dist.head()


# In[9]:


# Sorting the DataFrame based on the date values
sorted_date_dist = date_dist.sort_values('date').set_index('date')

# Looking at the first five rows
sorted_date_dist.head()


# In[10]:


# Plotting a bar plot
sorted_date_dist.plot(kind='bar', figsize=(20,4))


# In[11]:


def find_dist(df, col_name):
    
    # Checking the frequency of games in relation to the column values
    dist = df[col_name].value_counts().reset_index()
    
    # Renaming the columns
    dist.columns = [col_name, 'frequency']
        
    # Sorting the DataFrame based on the column values
    sorted_dist = dist.sort_values(col_name, ascending=True).set_index(col_name)

    # Plotting a bar plot
    sorted_dist.plot(kind='bar', figsize=(20,4))

    # Return a boolean indicating the function was successfully executed
    return True

# Visualizing the frequency distribution of games in relation to the date
find_dist(games_df, 'gameDate')


# In[12]:


# Looking at the first five rows
games_df.head()


# In[13]:


# Visualizing frequency distribution of games in relation to the time
find_dist(games_df, 'gameTimeEastern')


# In[14]:


# Visualizing frequency distribution of games in relation to the week
find_dist(games_df, 'week')


# In[15]:


# Looking at the first five rows
games_df.head()


# In[16]:


# Creating a column containing the day of the week information extracted from the date
games_df['gameDay'] = games_df['gameDate'].apply(lambda x: x.strftime('%A'))

# Looking at the first five rows
games_df.head()


# In[17]:


# Visualizing frequency distribution of games in relation to the day of the week
find_dist(games_df, 'gameDay')


# In[18]:


import seaborn as sns
import datetime


# In[19]:


# Reading in the CSV file as a DataFrame 
players_df = pd.read_csv('players.csv')


# In[20]:


# Looking at the first five rows
players_df.head()


# In[21]:


# Viewing the shape of the DataFrame
players_df.shape


# In[22]:


# Converting to datetime.date values
players_df['birthDate'] = pd.to_datetime(players_df['birthDate']).dt.date

# Extracting the year
players_df['birthYear'] = pd.to_datetime(players_df['birthDate']).dt.year

# Looking at the first five rows
players_df.head()


# In[23]:


# Finding the age of the players
players_df['age'] = 2018 - players_df['birthYear']

# Looking at the first five rows
players_df.head()


# In[24]:


def find_dist(df, col_name):
    
    # Checking the frequency of games in relation to the column values
    dist = df[col_name].value_counts().reset_index()
    
    # Renaming the columns
    dist.columns = [col_name, 'frequency']
        
    # Sorting the DataFrame based on the column values
    sorted_dist = dist.sort_values(col_name, ascending=True).set_index(col_name)

    # Plotting a bar plot
    sorted_dist.plot(kind='bar', figsize=(20,4))

    # Return a boolean indicating the function was successfully executed
    return True


# In[25]:


# Visualizing frequency distribution of players in relation to their age
find_dist(players_df, 'age')


# In[26]:


# Looking at the first five rows
players_df.head()


# In[27]:


# Visualizing frequency distribution of players in relation to their positions
find_dist(players_df, 'position')


# In[28]:


# Selecting position = CB
players_df.query('position == "CB"')


# In[29]:


# Visualizing frequency distribution of players in relation to the CB position
find_dist(players_df.query('position == "CB"'), 'age')


# In[30]:


# Visualizing frequency distribution of players in relation to the WR position
find_dist(players_df.query('position == "WR"'), 'age')


# In[31]:


# Looking at the first twenty rows
players_df.head(20)


# In[32]:


# Fixing the inconsistency by converting all data to inches
players_df['height'] = players_df['height'].apply(lambda x: int(x[0])*12 + int(x[2]) if '-' in x else int(x))

# Looking at the first twenty rows
players_df.head(20)


# In[33]:


# Extracting the height values
players_df['height'].values


# In[34]:


# Assigning the height and weight values
height = players_df['height'].values
weight = players_df['weight'].values


# In[37]:


# Plotting a joint plot
sns.jointplot(weight)


# In[38]:


# Plotting a joint plot
sns.jointplot(height)


# In[39]:


# Reading in the CSV file as a DataFrame 
plays_df = pd.read_csv('plays.csv')


# In[40]:


# Looking at the first five rows
plays_df.head()


# In[41]:


plays_df.shape


# In[42]:


import matplotlib.patches as patches


# In[43]:


# Create a rectangle defined via an anchor point *xy* and its *width* and *height*
rect = patches.Rectangle((0, 0), 120, 53.3, facecolor='darkgreen', zorder=0)

# Creating a subplot to plot our field on
fig, ax = plt.subplots(1, figsize=(12, 6.33))

# Adding the rectangle to the plot
ax.add_patch(rect)


# In[44]:


# Create a rectangle defined via an anchor point *xy* and its *width* and *height*
rect = patches.Rectangle((0, 0), 120, 53.3, facecolor='darkgreen', zorder=0)

# Creating a subplot to plot our field on
fig, ax = plt.subplots(1, figsize=(12, 6.33))

# Adding the rectangle to the plot
ax.add_patch(rect)

# Plotting a line plot for marking the field lines
plt.plot([10, 10, 20, 20],
         [0, 53.3, 53.3, 0],
         color='white', zorder=0)


# In[45]:


# Create a rectangle defined via an anchor point *xy* and its *width* and *height*
rect = patches.Rectangle((0, 0), 120, 53.3, facecolor='darkgreen', zorder=0)

# Creating a subplot to plot our field on
fig, ax = plt.subplots(1, figsize=(12, 6.33))

# Adding the rectangle to the plot
ax.add_patch(rect)

# Plotting a line plot for marking the field lines
plt.plot([10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60, 70, 70, 80,
          80, 90, 90, 100, 100, 110, 110, 120, 0, 0, 120, 120],
         [0, 53.3, 53.3, 0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 
          0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 53.3, 0, 0, 53.3],
         color='white', zorder = 0)


# In[46]:


# Create a rectangle defined via an anchor point *xy* and its *width* and *height*
rect = patches.Rectangle((0, 0), 120, 53.3, facecolor='darkgreen', zorder=0)

# Creating a subplot to plot our field on
fig, ax = plt.subplots(1, figsize=(12, 6.33))

# Adding the rectangle to the plot
ax.add_patch(rect)

# Plotting a line plot for marking the field lines
plt.plot([10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60, 70, 70, 80,
          80, 90, 90, 100, 100, 110, 110, 120, 0, 0, 120, 120],
         [0, 53.3, 53.3, 0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 
          0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 53.3, 0, 0, 53.3],
         color='white', zorder = 0)

# Creating the left end-zone
left_end_zone = patches.Rectangle((0, 0), 10, 53.3, facecolor='blue', alpha=0.2, zorder=0)

# Creating the right end-zone
right_end_zone = patches.Rectangle((110, 0), 120, 53.3, facecolor='blue', alpha=0.2, zorder=0)

# Adding the patches to the subplot
ax.add_patch(left_end_zone)
ax.add_patch(right_end_zone)

# Setting the limits of x-axis from 0 to 120
plt.xlim(0, 120)

# Setting the limits of y-axis from -5 to 58.3
plt.ylim(-5, 58.3)

# Removing the axis values from the plot
plt.axis('off')


# In[47]:


# Create a rectangle defined via an anchor point *xy* and its *width* and *height*
rect = patches.Rectangle((0, 0), 120, 53.3, facecolor='darkgreen', zorder=0)

# Creating a subplot to plot our field on
fig, ax = plt.subplots(1, figsize=(12, 6.33))

# Adding the rectangle to the plot
ax.add_patch(rect)

# Plotting a line plot for marking the field lines
plt.plot([10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60, 70, 70, 80,
          80, 90, 90, 100, 100, 110, 110, 120, 0, 0, 120, 120],
         [0, 53.3, 53.3, 0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 
          0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 53.3, 0, 0, 53.3],
         color='white', zorder = 0)

# Creating the left end-zone
left_end_zone = patches.Rectangle((0, 0), 10, 53.3, facecolor='blue', alpha=0.2, zorder=0)

# Creating the right end-zone
right_end_zone = patches.Rectangle((110, 0), 120, 53.3, facecolor='blue', alpha=0.2, zorder=0)

# Adding the patches to the subplot
ax.add_patch(left_end_zone)
ax.add_patch(right_end_zone)

# Setting the limits of x-axis from 0 to 120
plt.xlim(0, 120)

# Setting the limits of y-axis from -5 to 58.3
plt.ylim(-5, 58.3)

# Removing the axis values from the plot
# plt.axis('off')

# Plotting the numbers starting from x = 20 and ending at x = 110
# with a step of 10
for x in range(20, 110, 10):

    # Intializing another variable named 'number'
    number = x

    # If x exceeds 50, subtract it from 120
    if x > 50:
        number = 120 - x

    # Plotting the text at the bottom
    plt.text(x, 5, str(number - 10),
             horizontalalignment='center',
             fontsize=20,
             color='white')

    # Plotting the text at the top
    plt.text(x - 0.95, 53.3 - 5, str(number - 10),
             horizontalalignment='center',
             fontsize=20,
             color='white',
             rotation=180)


# In[48]:


# Create a rectangle defined via an anchor point *xy* and its *width* and *height*
rect = patches.Rectangle((0, 0), 120, 53.3, facecolor='darkgreen', zorder=0)

# Creating a subplot to plot our field on
fig, ax = plt.subplots(1, figsize=(12, 6.33))

# Adding the rectangle to the plot
ax.add_patch(rect)

# Plotting a line plot for marking the field lines
plt.plot([10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60, 70, 70, 80,
          80, 90, 90, 100, 100, 110, 110, 120, 0, 0, 120, 120],
         [0, 53.3, 53.3, 0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 
          0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 53.3, 0, 0, 53.3],
         color='white', zorder = 0)

# Creating the left end-zone
left_end_zone = patches.Rectangle((0, 0), 10, 53.3, facecolor='blue', alpha=0.2, zorder=0)

# Creating the right end-zone
right_end_zone = patches.Rectangle((110, 0), 120, 53.3, facecolor='blue', alpha=0.2, zorder=0)

# Adding the patches to the subplot
ax.add_patch(left_end_zone)
ax.add_patch(right_end_zone)

# Setting the limits of x-axis from 0 to 120
plt.xlim(0, 120)

# Setting the limits of y-axis from -5 to 58.3
plt.ylim(-5, 58.3)

# Removing the axis values from the plot
plt.axis('off')

# Plotting the numbers starting from x = 20 and ending at x = 110
# with a step of 10
for x in range(20, 110, 10):

    # Intializing another variable named 'number'
    number = x

    # If x exceeds 50, subtract it from 120
    if x > 50:
        number = 120 - x

    # Plotting the text at the bottom
    plt.text(x, 5, str(number - 10),
             horizontalalignment='center',
             fontsize=20,
             color='white')

    # Plotting the text at the top
    plt.text(x - 0.95, 53.3 - 5, str(number - 10),
             horizontalalignment='center',
             fontsize=20,
             color='white',
             rotation=180)

# Making ground markings
for x in range(11, 110):
        ax.plot([x, x], [0.4, 0.7], color='white', zorder = 0)
        ax.plot([x, x], [53.0, 52.5], color='white', zorder = 0)
        ax.plot([x, x], [22.91, 23.57], color='white', zorder = 0)
        ax.plot([x, x], [29.73, 30.39], color='white', zorder = 0)


# In[49]:


def create_football_field():
    
    # Create a rectangle defined via an anchor point *xy* and its *width* and *height*
    rect = patches.Rectangle((0, 0), 120, 53.3, facecolor='darkgreen', zorder=0)

    # Creating a subplot to plot our field on
    fig, ax = plt.subplots(1, figsize=(12, 6.33))

    # Adding the rectangle to the plot
    ax.add_patch(rect)

    # Plotting a line plot for marking the field lines
    plt.plot([10, 10, 20, 20, 30, 30, 40, 40, 50, 50, 60, 60, 70, 70, 80,
              80, 90, 90, 100, 100, 110, 110, 120, 0, 0, 120, 120],
             [0, 53.3, 53.3, 0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 
              0, 0, 53.3, 53.3, 0, 0, 53.3, 53.3, 53.3, 0, 0, 53.3],
             color='white', zorder = 0)

    # Creating the left end-zone
    left_end_zone = patches.Rectangle((0, 0), 10, 53.3, facecolor='blue', alpha=0.2, zorder=0)

    # Creating the right end-zone
    right_end_zone = patches.Rectangle((110, 0), 120, 53.3, facecolor='blue', alpha=0.2, zorder=0)

    # Adding the patches to the subplot
    ax.add_patch(left_end_zone)
    ax.add_patch(right_end_zone)

    # Setting the limits of x-axis from 0 to 120
    plt.xlim(0, 120)

    # Setting the limits of y-axis from -5 to 58.3
    plt.ylim(-5, 58.3)

    # Removing the axis values from the plot
    plt.axis('off')

    # Plotting the numbers starting from x = 20 and ending at x = 110
    # with a step of 10
    for x in range(20, 110, 10):

        # Intializing another variable named 'number'
        number = x

        # If x exceeds 50, subtract it from 120
        if x > 50:
            number = 120 - x

        # Plotting the text at the bottom
        plt.text(x, 5, str(number - 10),
                 horizontalalignment='center',
                 fontsize=20,
                 color='white')

        # Plotting the text at the top
        plt.text(x - 0.95, 53.3 - 5, str(number - 10),
                 horizontalalignment='center',
                 fontsize=20,
                 color='white',
                 rotation=180)

    # Making ground markings
    for x in range(11, 110):
            ax.plot([x, x], [0.4, 0.7], color='white', zorder = 0)
            ax.plot([x, x], [53.0, 52.5], color='white', zorder = 0)
            ax.plot([x, x], [22.91, 23.57], color='white', zorder = 0)
            ax.plot([x, x], [29.73, 30.39], color='white', zorder = 0)
    
    # Returning the figure and axis
    return fig, ax


# In[50]:


# Calling the plotting function
fig, ax = create_football_field()

# Plotting the figure
plt.show()


# In[51]:


# Reading the data as a Pandas DataFrame
df = pd.read_csv('week_data.csv')


# In[52]:


# Looking at the first five rows of the DataFrame 
df.head()


# In[53]:


# Looking at the shape of the DataFrame
df.shape


# In[54]:


# Converting to Time values
df['time'] = pd.to_datetime(df['time']).dt.time

# Looking at the first five rows of the DataFrame 
df.head()


# In[55]:


# Sorting the values of the DataFrame by time in an ascending order
df = df.sort_values(by='time', ascending=True).reset_index(drop=True)

# Looking at the first five rows of the DataFrame 
df.head()


# In[56]:


# Selecting the data for the given game and play based on their Id
sel_df = df.query('gameId == 2018111900 and playId == 5577')

# Looking at the shape of the DataFrame
print(f'The shape of the DataFrame is: {sel_df.shape}')

# Looking at the DataFrame
sel_df


# In[57]:


# Selecting the home and away team
home_team = sel_df.query('team == "home"')
away_team = sel_df.query('team == "away"')

# Selecting the football
football = sel_df.query('team == "football"')


# In[58]:


# Creating the football field
fig, ax = create_football_field()

# Plotitng the home team
home_team.plot(x='x', y='y', kind='scatter', ax=ax, color='blue', s=20, zorder=2)

# Plotting the away team
away_team.plot(x='x', y='y', kind='scatter', ax=ax, color='orange', s=20, zorder=2)

# Plotting the football
football.plot(x='x', y='y', kind='scatter', ax=ax, color='brown', s=20, zorder=2)

# Displaying the plot
plt.show()


# In[59]:


sel_df['event'].unique()


# In[60]:


# Creating the football field
fig, ax = create_football_field()

# Plotitng the home team
home_team.query('event == "ball_snap"').plot(x='x', y='y', kind='scatter', ax=ax, color='blue', s=20, zorder=2)

# Plotting the away team
away_team.query('event == "ball_snap"').plot(x='x', y='y', kind='scatter', ax=ax, color='orange', s=20, zorder=2)

# Plotting the football
football.query('event == "ball_snap"').plot(x='x', y='y', kind='scatter', ax=ax, color='brown', s=20, zorder=2)

# Displaying the plot
plt.show()


# In[ ]:




