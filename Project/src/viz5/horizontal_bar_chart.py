import plotly.graph_objects as go
import plotly.io as pio
import assets.shared_styles.colors as colors
import hover_template

def get_horizontal_bar_chart(df):
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            y= df['Player'],
            x= df['nGls'],
            name='Missed Shots',
            orientation='h',
            hovertemplate= hover_template.get_hover_template_viz5(),
            marker=dict(
                color=colors.PRIMARY_COLORS['gold'],
            )
        )
    )
    
    fig.add_trace(
        go.Bar(
            y= df['Player'],
            x= df['Gls'],
            name='Goals',
            orientation='h',
            hovertemplate= hover_template.get_hover_template_viz5(),
            marker=dict(
                color=colors.PRIMARY_COLORS['navy_blue'],
            )
        )
    )

    fig.update_layout(
        barmode='stack',
        template=pio.templates['simple_white'],
        hovermode='y unified',
        dragmode=False,
        legend_title_text='Shots'
    )
    
    fig.update_xaxes(
        title_text='Number of shots'
    )
    
    return fig

    
    