import pandas as pd
import pickle
from scipy.stats import poisson

df = pickle.load(open("dict_table","rb"))
df2 = pd.read_csv("clean_american_cup_historical_data.csv")
df3 = pd.read_csv("clean_american_cup_fixture.csv")

df2['HomeTeam'].unique()
df2['AwayTeam'].unique()
df2['HomeTeam']= df2['HomeTeam'].replace({"Chile\xa0Chile": "Chile", "Colombia\xa0Colombia": "Colombia"})
df2['AwayTeam']= df2['AwayTeam'].replace({"México\xa0México": "México", "Colombia\xa0Colombia": "Colombia"})

# Calculate Team Strength

df_home = df2[['HomeTeam', 'HomeGoals', 'AwayGoals']]
df_away = df2[['AwayTeam', 'HomeGoals', 'AwayGoals']]

df_home = df_home.rename(columns={'HomeTeam':'Team', 'HomeGoals': 'GoalsScored', 'AwayGoals': 'GoalsConceded'})
df_away = df_away.rename(columns={'AwayTeam':'Team', 'HomeGoals': 'GoalsConceded', 'AwayGoals': 'GoalsScored'})

df_team_strength = pd.concat([df_home, df_away], ignore_index=True).groupby(['Team']).mean()
df_team_strength

#Function predict_points

def predict_points(home, away):
    if home in df_team_strength.index and away in df_team_strength.index:
        # goals_scored * goals_conceded
        lamb_home = df_team_strength.at[home,'GoalsScored'] * df_team_strength.at[away,'GoalsConceded']
        lamb_away = df_team_strength.at[away,'GoalsScored'] * df_team_strength.at[home,'GoalsConceded']
        prob_home, prob_away, prob_draw = 0, 0, 0
        for x in range(0,11): #number of goals home team
            for y in range(0, 11): #number of goals away team
                p = poisson.pmf(x, lamb_home) * poisson.pmf(y, lamb_away)
                if x == y:
                    prob_draw += p
                elif x > y:
                    prob_home += p
                else:
                    prob_away += p
        
        points_home = 3 * prob_home + prob_draw
        points_away = 3 * prob_away + prob_draw
        return (points_home, points_away)
    else:
        return (0, 0)
