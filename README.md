# dsba_5122_final_project


# Streamlit App Link
https://liammaxwell24-dsba-5122-final-project-final-e75xy1.streamlit.app/

# Introduction:
The problem I am looking to solve is to provide advanced visibility into NBA player statistics in order to provide an app that can allow NBA decision makers, both teams and agents, to make better data-driven decisions regarding:
-Free Agent agreements
-Extension agreements
-Opt in/opt out of final year of contract 

This analysis can also be used as a fun and interactive way for NBA fans to efficiently compare players based on chosen attributes and view the league leaders in those same attributes.

# Data/Operation Abstraction Design:
 I have aggregated all NBA player statistics from the 2022 NBA season, excluding those players still on a rookie contract as that isn't indicative of market value. All counting stats were accrued from NBA.com (Points, Assists) while advanced statistics were pulled from 538.com (RAPTOR, WAR, On/Off). Contract data was pulled from Spotrac.com while other values such as Age, Offseason of New Contract and Team were pulled from ESPN.com. Data was manually pulled from each site and combined using player name as the table key.

# Future Work:
In the future, I would like to incorporate more data from previous seasons in order to gain a broader picture/trend of each player's performance. I would also like to incorporate the success of the team each player was on to see which players tend to attribute to successful seasons. I think there is also an opportunity to have a constantly refreshed dataset from current season to give the most up-to-date statistics.
