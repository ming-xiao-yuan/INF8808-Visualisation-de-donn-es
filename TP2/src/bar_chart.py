'''
    Contains some functions related to the creation of the bar chart.
    The bar chart displays the data either as counts or as percentages.
'''

import plotly.graph_objects as go
import plotly.io as pio

from hover_template import get_hover_template
from modes import MODES, MODE_TO_COLUMN


def init_figure():
    '''
        Initializes the Graph Object figure used to display the bar chart.
        Sets the template to be used to "simple_white" as a base with
        our custom template on top. Sets the title to 'Lines per act'

        Returns:
            fig: The figure which will display the bar chart
    '''
    fig = go.Figure()

    fig.update_layout(
        template=pio.templates['simple_white+new_theme'],
        dragmode=False,
        barmode='relative',
        title='Lines per act'
    )

    return fig


def draw(fig, data, mode):
    '''
        Draws the bar chart.

        Arg:
            fig: The figure comprising the bar chart
            data: The data to be displayed
            mode: Whether to display the count or percent data.
        Returns:
            fig: The figure comprising the drawn bar chart
    '''
    fig = go.Figure(fig)  # conversion back to Graph Object

    if len(fig.data) != 0:
        fig.data = []

    for name, data in data.groupby('Player'): 
        x_data = ['Act ' + str(prefix) for prefix in data['Act'] ]
        y_data = data['LineCount'] if mode == 'Count' else data['LinePercent']
        fig.add_trace(go.Bar(x= x_data, y=y_data, name=name, hovertemplate=get_hover_template(name, mode)))
   
    return fig


def update_y_axis(fig, mode):
    '''
        Updates the y axis to say 'Lines (%)' or 'Lines (Count) depending on
        the current display.

        Args:
            mode: Current display mode
        Returns: 
            The updated figure
    '''

    fig = go.Figure(fig)
    y_title = 'Lines (Count)' if mode == 'Count' else 'Lines (%)'
    fig.update_layout(yaxis_title=y_title)
    return fig
