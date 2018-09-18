Tennis_Analysis
==============================

## Repo Information
A repo for analyzing tennis ATP tournament data 


#### Currently I'm checking ATP finals data (2008-2017) with Pandas dataframe
--> /notebooks/

<p align="center">
  <img width="500" src="https://raw.githubusercontent.com/Linn39/Tennis_Analysis/master/reports/figures/ATP_finals_2008-2017/winner_age_year.png"/>
</p>
Distribution of ages of tournament winners from 2008 to 2017. Linear regression shows that there's a trend for players to get older over the years, which is consistent with the fact that top players in the game of tennis has always been the same people over the years. 

<br>
<br>
<p align="center">
  <img width="600" src="https://raw.githubusercontent.com/Linn39/Tennis_Analysis/master/reports/figures/ATP_finals_2008-2017/winner_tournament_count.png"/>
</p>
I counted the number of tournaments won by each player from 2008-2017, and plotted the top 10. Novak Djokovic has been very active in recent years and is beating the records set by his predecessors. But further analysis on Grand Slams could tell a different sotry. 

<br>

#### To try out SQLite commdands in Python, I converted csv to sqlite database and tried basic queries 
<br>--> /src/data/

<br>
---
## Datasets
#### “atp_matches_*.csv”: by Jeff Sackmann / Tennis Abstract, 
<br> https://github.com/JeffSackmann/tennis_atp

The player file columns are player_id, first_name, last_name, hand, birth_date, country_code.
The columns for the ranking files are ranking_date, ranking, player_id, ranking_points.

<br>
---
## Folder Structure
<br>The folder structure is based on the "Data Science" project template, created by the command line tool "Cookiecutter":
<br>Ducumentation: http://drivendata.github.io/cookiecutter-data-science/
<br>I highly recommend Cookiecutter. I find it very helpful for organizing projects, even when I am just starting a project with very little contents, I already have an idea of the overall structure. And it's easy for others to understand/ reproduce what I've done =)
