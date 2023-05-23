import pandas as pd

def viz1_get_results(scores_and_fixtures_df):
    scores_and_fixtures_df['Opponent'] = scores_and_fixtures_df['Opponent'].str.split(
        ' ', n=1).str[1]

    df = pd.DataFrame(
        scores_and_fixtures_df[['Opponent', 'Gls', 'xG', 'npxG']])
    df['npG'] = scores_and_fixtures_df['Gls'] - scores_and_fixtures_df['PK']

    df = df.rename(columns={
        "Gls": "Goals",
        'xG': "expected Goals",
        'npG': "Non Penalty Goals",
        'npxG': "expected Non Penalty Goals"
    })

    return df

def viz2_hm1(possession_data, passing_data, s_n_f_data, gk_per_game_data):
    poss = possession_data[['Opponent','Poss']]
    poss['Opponent'] = poss['Opponent'].str.split(' ', n=1).str[1]
    passing = passing_data['Cmp%']
    sot_perc = s_n_f_data['SoT%']
    gcr = s_n_f_data['G/Sh'] * 100
    save_perc = gk_per_game_data['Save%']
    df = pd.concat([poss, passing, sot_perc, gcr, save_perc], axis=1)
    df = df.dropna(subset=['Opponent'])
    df = df.set_index('Opponent')
    df = df.rename(columns={'Poss': 'Possession (%)', 'Cmp%': 'Pass Completion Rate (%)', 'SoT%': 'Shots on Target (%)', 'G/Sh': 'Goal Conversion Rate (%)', 'Save%': 'Saves (%)'})

    return df

def viz3_get_offensive_stats(shooting_df, passing_df, gca_df):
    df = pd.concat([shooting_df, passing_df, gca_df], axis=1)
    df = df.loc[:, ~df.columns.duplicated()]
    df = df[['Player', 'Pos', 'Gls', 'KP', 'GCA']]
    df = df.iloc[:-2]
    df = df[df['Pos'].isin(['FW', 'MFFW', 'MF'])]
    df = df[df['KP'] != 0]
    return df


def viz4_get_stats(shooting_df, passing_df, def_act_df, goalkeeping_df, possession_df, s_n_f_df):
    sot = shooting_df.loc[shooting_df['Player'] == 'Squad Total', ['SoT%']]
    
    cmp = passing_df.loc[passing_df['Player'] == 'Squad Total', ['Cmp%']]
    
    tkl_tklw = def_act_df.loc[def_act_df['Player'] == 'Squad Total', ['Tkl', 'TklW']]
    tkl_tklw['TklW/Tkl'] = round(tkl_tklw['TklW'] / tkl_tklw['Tkl'] * 100, 1)
    tkl_tklw = tkl_tklw.drop(['Tkl', 'TklW'], axis=1)
    
    save = goalkeeping_df.loc[goalkeeping_df['Player'] == 'Squad Total', ['Save%']]
    save = save.reset_index(drop=True)
    
    poss = possession_df['Poss']
    poss = possession_df['Poss'].iloc[11]
    
    g_p_sh = s_n_f_df['G/Sh']
    g_p_sh = s_n_f_df['G/Sh'].iloc[11] * 100
    
    df = pd.concat([sot, cmp, tkl_tklw], axis=1).reset_index(drop=True)
    df = pd.concat([df,save], axis=1)
    df['Poss'] = poss
    df['G/Sh'] = g_p_sh
    
    return df


def viz5_get_stats(shooting_df):
    df = pd.DataFrame(shooting_df[['Player','Sh', 'Gls']])
    df['nGls'] = shooting_df['Sh'] - shooting_df['Gls']

    df = df.drop(df[df['Gls'] == 0].index)
    df = df.drop(df.tail(2).index)
    
    df = df.sort_values(['nGls', 'Gls'])

    return df