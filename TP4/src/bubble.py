'''
    This file contains the code for the bubble plot.
'''

import plotly.express as px
import plotly.io as pio

import hover_template


def get_plot(my_df, gdp_range, co2_range):
    '''
        Generates the bubble plot.

        The x and y axes are log scaled, and there is
        an animation between the data for years 2000 and 2015.

        The discrete color scale (sequence) to use is Set1 (see : https://plotly.com/python/discrete-color/)

        The markers' maximum size is 30 and their minimum
        size is 6.

        Args:
            my_df: The dataframe to display
            gdp_range: The range for the x axis
            co2_range: The range for the y axis
        Returns:
            The generated figure
    '''

    fig = px.scatter(x=my_df['GDP'],
                     y=my_df['CO2'],
                     custom_data=[my_df['Country Name'], my_df['Population']],
                     log_x=True,
                     log_y=True,
                     range_x=gdp_range,
                     range_y=co2_range,
                     color=my_df['Continent'],
                     color_discrete_sequence=px.colors.qualitative.Set1,
                     animation_frame=my_df['Year'],
                     size=my_df['Population'],
                     size_max=30
                     )

    fig.update_traces({'marker': {'sizemin': 6}})

    return fig


def update_animation_hover_template(fig):
    '''
        Sets the hover template of the figure,
        as well as the hover template of each
        trace of each animation frame of the figure

        Args:
            fig: The figure to update
        Returns:
            The updated figure
    '''

    fig.update(
        data=[{'hovertemplate': hover_template.get_bubble_hover_template()}])

    for frame in fig.frames:
        for trace in frame.data:
            trace.hovertemplate = hover_template.get_bubble_hover_template()

    return fig


def update_animation_menu(fig):
    '''
        Updates the animation menu to show the current year, and to remove
        the unnecessary 'Stop' button.

        Args:
            fig: The figure containing the menu to update
        Returns
            The updated figure
    '''

    fig.update_layout(
        sliders=[dict(currentvalue={"prefix": "Data for year: "})])

    copied_btns = list(fig['layout'].updatemenus[0]['buttons'])
    copied_btns.pop(1)
    fig['layout'].updatemenus[0].buttons = copied_btns

    fig['layout'].updatemenus[0]['buttons'][0].label = 'Animate'

    return fig


def update_axes_labels(fig):
    '''
        Updates the axes labels with their corresponding titles.

        Args:
            fig: The figure to be updated
        Returns:
            The updated figure
    '''

    fig.update_layout(
        xaxis_title='GDP per capita ($ USD)',
        yaxis_title='CO2 emissions per capita (metric tonnes)'
    )

    return fig


def update_template(fig):
    '''
        Updates the layout of the figure, setting
        its template to 'simple_white'

        Args:
            fig: The figure to update
        Returns
            The updated figure
    '''

    fig.update_layout(template=pio.templates['simple_white'])

    return fig


def update_legend(fig):
    '''
        Updated the legend title

        Args:
            fig: The figure to be updated
        Returns:
            The updated figure
    '''

    fig.update_layout(legend=dict(title='Legend'))

    return fig
