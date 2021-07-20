import streamlit as st
import pandas as pd
import plotly.express as px


@st.cache(persist=True, suppress_st_warning=True)
def get_data(filename):
    data = pd.read_csv(filename)

    return data


def app():

    data = get_data('data/kmfl.csv')

    #Drop columns with missing values as they are not so relevant
    #Also drop other irrelevant/redundant columns
    df1 = data.drop(['Code', 'Officialname', 'Registration_number', 'Facility_type_category',
               'Owner', 'Constituency', 'Sub county', 'Ward', 'Service_names',
               'Public visible'], axis=1)

    #Create a dropdown for charts
    choice = ['histogram', 'pie chart']
    opt = st.selectbox('Choose to view', choice)

    if opt == 'histogram':
        col1, col2 = st.beta_columns([3,1])

        with col2:
            #Create drop down for drilling-through
            options = ['County', 'Facility type']
            drop = st.selectbox('Filter by...', options)

        with col1:
            #Plot histogram
            fig = px.histogram(df1, x='Keph level', color=drop,
            animation_frame='Owner type', title="Number of Facilities")
            st.write(fig)

    else:
        #Create a dataframe with total counts for Keph Levels
        df2 = pd.DataFrame(df1["Keph level"].value_counts()).reset_index()
        df2.columns = ['keph level', 'count']

        #Plot a pie chart
        fig = px.pie(df2, values='count', color='keph level',
             title='Total Number of Facility Levels in the country')
        st.write(fig)