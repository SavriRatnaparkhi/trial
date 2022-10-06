import streamlit as st
import pandas as pd
from matplotlib.pyplot import figure
import seaborn as sns

col1, col2, col3 = st.columns(3)
with col2:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/F1.svg/420px-F1.svg.png", width=200)

data = pd.read_csv("C:/Users/Savri/Downloads/F1/f1_2010-2021/f1_2010-2021.csv")
driver = pd.read_csv("C:/Users/Savri/Downloads/F1/f1_2010-2021/driver_standings_2010-2021.csv")
team = pd.read_csv("C:/Users/Savri/Downloads/F1/f1_2010-2021/constructor_standings_2010-2021.csv")
circuits = pd.read_csv("C:/Users/Savri/Downloads/circuits.csv")

tab1, tab2, tab3 = st.tabs(['Home', 'Team Wins-comparison', 'Driver Points-comparison'])
with tab1:
    st.write("Formula One (also known as Formula 1 or F1) is the highest class of international racing for open-wheel"
             " single-seater formula racing cars sanctioned by the Fédération Internationale de l'Automobile (FIA). "
             "The World Drivers' Championship, which became the FIA Formula One World Championship in 1981, has been "
             "one of the premier forms of racing around the world since its inaugural season in 1950. "
             "The word formula in the name refers to the set of rules to which all participants' cars must conform. "
             "A Formula One season consists of a series of races, known as Grands Prix, which take place worldwide "
             "on both purpose-built circuits and closed public roads.")
    st.header("Locations of Grand Prix")
    st.map(circuits)

with tab2:
    st.header("How would you like to see the data?")
    way1 = st.checkbox("According to Year")
    way2 = st.checkbox("According to Grand Prix")
    if way1:
        selectbox = st.selectbox(
            "Select any one of the following years",
            (data['year'].unique())
        )
        st.write("Total wins of a team in the respective year:")
        data1 = data[data['year'] == selectbox]
        st.bar_chart(data1['team'].value_counts())

        st.write("Cumulative wins of team till the respective year:")
        for i in range(0, data.shape[0]):
            if selectbox == data['year'][i]:
                newdata = data[:i]
        st.bar_chart(newdata['team'].value_counts())

    if way2:
        selectbox2 = st.selectbox(
            "Select any one of the following countries",
            (data['grand_prix'].unique())
        )
        data2 = data[data['grand_prix'] == selectbox2]
        st.bar_chart(data2['team'].value_counts())

with tab3:
    st.header("Choose 2 drivers to compare")
    col6, col7 = st.columns(2)
    with col6:
        participant1 = st.selectbox("Select Driver 1", driver['fullname'].unique())
        data3 = driver[driver['fullname'] == participant1]
        st.write(participant1, "'s points over the years")
        fig = figure(figsize=(20, 10))
        sns.lineplot(x=data3['year'], y=data3['points'])
        st.pyplot(fig)
    with col7:
        participant2 = st.selectbox("Select Driver 2", driver['fullname'].unique())
        data4 = driver[driver['fullname'] == participant2]
        st.write(participant2, "'s points over the years")
        fig1 = figure(figsize=(20, 10))
        sns.lineplot(x=data4['year'], y=data4['points'])
        st.pyplot(fig1)

    st.header("Driver and Constructor Standings in a particular year")
    selectbox3 = st.selectbox("Select a year to see driver and constructor standings", driver['year'].unique())
    col4, col5 = st.columns(2)
    with col4:
        for i in range(0, driver.shape[0]):
            if selectbox3 == driver['year'][i]:
                st.write(driver.iloc[i, 3]  + "'s  Points:", driver.iloc[i, 5])
    with col5:
        for i in range(0, team.shape[0]):
            if selectbox3 == team['year'][i]:
                st.write(team.iloc[i, 1] + "'s Points:", team.iloc[i, 2])