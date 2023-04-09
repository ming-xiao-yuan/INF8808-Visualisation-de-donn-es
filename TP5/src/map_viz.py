'''
    Contains the functions to set up the map visualization.

'''

import plotly.graph_objects as go
import plotly.express as px

import hover_template as hover


def add_choro_trace(fig, montreal_data, locations, z_vals, colorscale):
    '''
        Adds the choropleth trace, representing Montreal's neighborhoods.

        Note: The z values and colorscale provided ensure every neighborhood
        will be grey in color. Although the trace is defined using Plotly's
        choropleth features, we are simply defining our base map.

        The opacity of the map background color should be 0.2.

        Args:
            fig: The figure to add the choropleth trace to
            montreal_data: The data used for the trace
            locations: The locations (neighborhoods) to show on the trace
            z_vals: The table to use for the choropleth's z values
            colorscale: The table to use for the choropleth's color scale
        Returns:
            fig: The updated figure with the choropleth trace

    '''

    fig.add_trace(
        px.choropleth_mapbox(
            geojson=montreal_data, 
            locations=locations, 
            featureidkey="properties.NOM", 
            color_discrete_sequence=colorscale,
            opacity=0.2,
            custom_data=[locations],
        ).data[0])
    
    fig.update(data=[{'hovertemplate': hover.map_base_hover_template()}])
    
    fig.data[0].z = z_vals
    fig.data[0].showlegend= False


    return fig


def add_scatter_traces(fig, street_df):
    '''
        Adds the scatter trace, representing Montreal's pedestrian paths.

        The marker size should be 20.

        Args:
            fig: The figure to add the scatter trace to
            street_df: The dataframe containing the information on the
                pedestrian paths to display
        Returns:
            The figure now containing the scatter trace

    '''
    i = 0
    for name, site in street_df.groupby('properties.TYPE_SITE_INTERVENTION'): 
        fig.add_trace(
            go.Scattermapbox(
                lat=site['geometry.coordinates'].map(lambda x: x[1]),
                lon=site['geometry.coordinates'].map(lambda x: x[0]),
                name=name,
                customdata=[site['properties.NOM_PROJET'], site['properties.MODE_IMPLANTATION'], site['properties.OBJECTIF_THEMATIQUE']],
                hovertemplate= hover.map_marker_hover_template(name),
                mode='markers',
                marker= dict(size=20, color=px.colors.qualitative.Plotly[i])
            )
        )
        i += 1


    return fig
