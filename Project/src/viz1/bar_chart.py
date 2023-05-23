import plotly.graph_objects as go
import plotly.io as pio

import template as template
import hover_template

def init_figure():
    fig = go.Figure()
    
    template.create_template()

    fig.update_layout(
        dragmode=False,
        xaxis_title="Opponent",
        yaxis_showgrid=False,
        template=pio.templates['simple_white+viz1_template'],
        legend_title_text='Type'
    )

    fig.update_yaxes(
        range=[0, 5]
    )

    return fig

def draw(fig, data, mode):
    fig = go.Figure(fig)

    if len(fig.data) != 0:
        fig.data = []

    fig.add_trace(
        go.Bar(
            x=data['Opponent'],
            y=data[mode], 
            name="Actual")
    )
    
    fig.add_trace(
        go.Bar(
            x=data['Opponent'],
            y=data["expected " + mode],
            name="Expected")
    )

    fig.update_layout(
        hovermode='x unified',
    )
    
    fig.update_traces(
        hovertemplate=hover_template.get_hover_template_viz1(mode)
    )
    
    return fig
