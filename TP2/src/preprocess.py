'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd
from modes import MODE_TO_COLUMN


def summarize_lines(my_df):
    '''
        Sums each player's total of number of lines and  its
        corresponding percentage per act.

        The sum of lines per player per act is in a new
        column named 'LineCount'.

        The percentage of lines per player per act is
        in a new column named 'PlayerPercent'

        Args:
            my_df: The pandas dataframe containing the data from the .csv file
        Returns:
            The modified pandas dataframe containing the
            information described above.
    '''

    lines_per_act = my_df.groupby(['Act'], as_index=False)['Line'].count()
    my_df = my_df.groupby(['Act', 'Player'], as_index=False).size()
    my_df = my_df.merge(lines_per_act, on='Act', how='left')
    my_df['Line'] = my_df['size'] / my_df['Line'] * 100
    my_df.columns = ['Act', 'Player', 'LineCount', 'LinePercent']

    return my_df


def replace_others(my_df):
    '''
        For each act, keeps the 5 players with the most lines
        throughout the play and groups the other player
        together in a new line where :

        - The 'Act' column contains the act
        - The 'Player' column contains the value 'OTHER'
        - The 'LineCount' column contains the sum
            of the counts of lines in that act of
            all players who are not in the top
            5 players who have the most lines in
            the play
        - The 'PercentCount' column contains the sum
            of the percentages of lines in that
            act of all the players who are not in the
            top 5 players who have the most lines in
            the play

        Returns:
            The df with all players not in the top
            5 for the play grouped as 'OTHER'
    '''

    top_5 = my_df.groupby(['Player'])['LineCount'].sum().sort_values().tail(5)
    top_5 = top_5.index.values

    other = pd.DataFrame(columns = ['Act', 'Player', 'LineCount', 'LinePercent'])

    for act, list in my_df.groupby(['Act']):
        curr_other = list.loc[ list['Player'].isin(top_5) == False].sum()
        curr_other ['Act'] = act
        curr_other['Player'] = 'Other'
        curr_other.columns = ['Act', 'Player', 'LineCount', 'LinePercent']
        other = other.append(curr_other, ignore_index=True)

    
    my_df = my_df.loc[my_df['Player'].isin(top_5)]
    my_df = pd.concat([my_df, other], ignore_index=True)
    
    return my_df


def clean_names(my_df):
    '''
        In the dataframe, formats the players'
        names so each word start with a capital letter.

        Returns:
            The df with formatted names
    '''
    
    my_df['Player'] = my_df['Player'].str.capitalize()
    return my_df
