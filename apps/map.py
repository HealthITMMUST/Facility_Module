import streamlit as st
import pandas as pd
import plotly.express as px


@st.cache(persist=True, suppress_st_warning=True)
def get_data(filename):
    data = pd.read_csv(filename)

    return data


def app():

    data = get_data('data/kmfl_test.csv')

    #Set zoom slider
    size = st.slider('Set zoom level', 0, 10)

    #map type drop-down
    map_opt = ['carto-positron', 'open-street-map', 'white-bg',
                'carto-darkmatter']
    mp = st.selectbox('Choose type of map', map_opt)

    #Map filter
    map_filter = ['Keph level', 'Facility type']
    mp1 = st.selectbox('Filter map by...', map_filter)
    #Define function to plot map
    def animate_map(time_col):
        fig = px.scatter_mapbox(data,
                lat="Latitude" ,
                lon="Longitude",
                hover_name="Keph level",
                color=mp1,
                animation_frame=time_col,
                mapbox_style=mp,
                zoom=size
                )
        st.write(fig)
    animate_map(time_col='Owner type')
