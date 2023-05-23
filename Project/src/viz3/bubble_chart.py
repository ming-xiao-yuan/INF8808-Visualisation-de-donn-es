import plotly.express as px
import plotly.io as pio
import hover_template

def get_fig(data):
    fig = px.scatter(
            data_frame=data,
            x="Gls",
            y="GCA",
            custom_data=[data['KP'], data['Player']],
            range_x=[-2, 10],
            range_y=[-2, 10],
            color=data['Player'],
            size=data['KP'],
            size_max=60,
            hover_name=data['Player'],
            hover_data=['Player', 'KP']
        )

    fig.update_traces(
        {'marker': {'sizemin': 0}}
    )
    
    fig.update_layout(
        xaxis_title='Goals',
        template=pio.templates['simple_white'],
        dragmode=False,
        hoverlabel=dict(
            bgcolor="white",
        ),
        yaxis_title=None
    )

    fig.update_traces(
        hovertemplate=hover_template.get_hover_template_viz3()
    )

    return fig
