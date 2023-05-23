import plotly.graph_objects as go
import plotly.io as pio
import hover_template


def get_fig(data):
    fig = go.Figure(
        data=go.Scatterpolar(
            r=[data['SoT%'][0],
            data['Cmp%'][0],
            data['TklW/Tkl'][0],
            data['G/Sh'][0],
            data['Save%'][0],
            data['Poss'][0]],
            theta=['Shots on Target Percentage','Pass Completion Percentage','Successful Tackle Percentage','Goal Conversion Rate', 'Save Percentage', 'Possession'],
            fill='toself',
            name="Argentina's strengths and weaknesses"
        )
    )

    fig.update_layout(
        template=pio.templates['ggplot2+viz4_template'],
        hoverlabel=dict(
            bgcolor="white",
        )
    )

    fig.update_traces(
        hovertemplate=hover_template.get_hover_template_viz4()
    )

    return fig