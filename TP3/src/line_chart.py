'''
    Contains some functions related to the creation of the line chart.
'''
import plotly.express as px
import hover_template
import pandas as pd

from template import THEME


def get_empty_figure():
    '''
        Returns the figure to display when there is no data to show.

        The text to display is : 'No data to display. Select a cell
        in the heatmap for more information.

    '''

    fig = px.line()
    fig.add_annotation(
        text="No data to display. Select a cell in the heatmap for more information.",
        showarrow=False, 
        xanchor='center', 
        yanchor='middle',
    )
    
    fig.update_layout(
        dragmode=False,        
        xaxis=dict(visible=False),
        yaxis=dict(visible=False)
    )

    return fig


def add_rectangle_shape(fig):
    '''
        Adds a rectangle to the figure displayed
        behind the informational text. The color
        is the 'pale_color' in the THEME dictionary.

        The rectangle's width takes up the entire
        paper of the figure. The height goes from
        0.25% to 0.75% the height of the figure.
    '''

    fig.add_shape(
        type="rect", 
        xref="paper", yref="paper",
        fillcolor=THEME['pale_color'],
        x0=0,
        x1=1,
        y0=0.25,
        y1=0.75,
        line_width=0,
    )

    return fig


def get_figure(line_data, arrond, year):
    '''
        Generates the line chart using the given data.

        The ticks must show the zero-padded day and
        abbreviated month. The y-axis title should be 'Trees'
        and the title should indicated the displayed
        neighborhood and year.

        In the case that there is only one data point,
        the trace should be displayed as a single
        point instead of a line.

        Args:
            line_data: The data to display in the
            line chart
            arrond: The selected neighborhood
            year: The selected year
        Returns:
            The figure to be displayed
    '''

    if len(line_data) == 1 :
        fig = px.scatter(line_data)
    else:
        fig = px.line(line_data)

    fig.update_layout(
        showlegend=False,
        xaxis_title= "",
        yaxis_title= "Trees",
        title=f"Trees planted in {arrond} in {pd.to_datetime(year).year}",
        xaxis = dict(
            tickformat = '%d %b'
        )
    )    

    fig.update(data=[{'hovertemplate': hover_template.get_linechart_hover_template()}])
    
    return fig
