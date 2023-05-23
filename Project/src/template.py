import plotly.graph_objects as go
import plotly.io as pio
import assets.shared_styles.colors as colors

def create_template():
    pio.templates['viz1_template'] = go.layout.Template()
    
    pio.templates['viz1_template'].data.bar = [
        go.Bar(marker_color = colors.PRIMARY_COLORS[color]) for color in colors.PRIMARY_COLORS
    ]

    #VIZ 4
    template = go.layout.Template({
        'data': {
            'scatterpolar': [{
                'line': {'color': colors.PRIMARY_COLORS['gold'] },
                'marker': {'color': colors.SECONDARY_COLORS['lighter_gold']},
            }],
        },
        'layout': {
            'polar': {
                'radialaxis': {
                    'range': [0, 100],
                    'tickvals': [20, 40, 60, 80, 100],
                },
                'angularaxis': {
                    'tickfont': {'size': 12},
                    'direction':"clockwise",
                    'rotation': 30
                },
            },
            'font': {'size': 14},
            'showlegend': False,
            'dragmode': False,
            'width':600, 
            'height':600
        },
    })
    
    pio.templates['viz4_template'] = template