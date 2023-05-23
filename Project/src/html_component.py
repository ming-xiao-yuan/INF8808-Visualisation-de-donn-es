from dash import html, dcc
from viz1.modes import MODES

image_path = "assets/header.jpg"

def welcome_page():
    return html.Div(className='welcome-page-container', children=[
        html.Img(className='header-img', src=image_path),
        html.Div(className='content', children=[
            html.Div(className='welcome-title', children=[
                'Examining Argentina\'s Performance in the 2022 World Cup: A Statistical Analysis'
            ])
        ]),
    ])

def viz1_html(fig):
    markdown_title="""
    ## How Did Argentina Perform Compared to Expectation?
    """
    return html.Div(className='page-container', children=[
        dcc.Markdown(className='markdown-title', children=markdown_title),
        html.Div(className='radio-group', children=[
            html.Div(className='radio-group-text', id='info', children=[
                html.Span(MODES['goals'], className='metric-text')
            ]),
            html.Div(className='radio-container', children=[
                html.Div(className='radio-items', children=[                            
                    html.Span(
                        'Metric :',
                        style={ 'margin-right': 10, 'text-decoration' : 'underline' }),
                    dcc.RadioItems(
                        id='radio-items',
                        options=[
                            dict(
                                label=[
                                    MODES[mode],
                                    html.Span(style={
                                        'margin-right': 10
                                        })
                                    ],
                                value=MODES[mode]) for mode in MODES
                        ],
                        value=MODES['goals'],
                        inline=True
                    )
                ])
            ])
        ]),
        html.Div(className='app-container', children=[
            html.Div(className='y-axis-title', id='mode'),
            html.Div(className='graph-container', children=[
                dcc.Graph(
                    figure=fig,
                    config=dict(
                        scrollZoom=False,
                        showTips=False,
                        showAxisDragHandles=False,
                        doubleClick=False,
                        displayModeBar=False
                    ),
                    id='bar-chart'
                )
            ]),
        ])
    ])
    
def viz2_html(fig):
    markdown_title="""
    ## How Did Argentina Perform In Each Game?
    """
    markdown_text = """
    The Albiceleste started off on the wrong foot in the World Cup 2022, losing their first match as one of the tournament favorites against Saudi Arabia. However, they 
    soon picked up the pace and took the crown from reigning champions France. Argentina had an overall strong performance throughout the tournament.

    *It should be noted that the save percentage against Poland is unavailable as Robert Lewandowski's side failed to take any shots on target, meaning no saves were necessary.*
    """
    return html.Div(className='page-container', children=[
        dcc.Markdown(className='markdown-title', children=markdown_title),
        dcc.Markdown(children=markdown_text),
        html.Div(className='app-container', children=[
            html.Div(className='y-axis-title', children=['Opponent']),
            html.Div(className='graph-container', children=[
                dcc.Graph(
                    id='Heatmap',
                    figure=fig,
                    config=dict(
                        scrollZoom=False,
                        showTips=False,
                        showAxisDragHandles=False,
                        doubleClick=False,
                        displayModeBar=False
                    ),
                )
            ])
        ])
    ])
    
def viz3_html(fig):
    markdown_title="""
    ## Which Offensive Player Contributed the most to Argentina's Success?
    """

    markdown_text = """
    Argentina is known for its offensive prowess with world-class players such as Lionel Messi and Angel Di Maria dominating any pitch they compete on. 
    In such manner, we have chosen 3 key metrics that best represent a well-rounded attacking player.
    
    
    *Goal-creating actions: The last two offensive actions directly leading to a goal. These can be passes, take-ons and drawing fouls.*

    *Key passes: Passes that lead directly to a shot*
    
    *Goals: Number of goals scored by the player (penalty and non-penalties included)*
    """
    
    return html.Div(className='page-container', children=[
        dcc.Markdown(className='markdown-title', children=markdown_title),
        dcc.Markdown(children=markdown_text),
        html.Div(className='app-container', children=[
            html.Div(className='y-axis-title', children=['Goal-Creating Actions']),
            html.Div(className='graph-container', children=[
                dcc.Graph(
                    id='bubble-chart',
                    figure=fig,
                    config=dict(
                        scrollZoom=False,
                        showTips=False,
                        showAxisDragHandles=False,
                        doubleClick=False,
                        displayModeBar=False
                    ),
                )
            ])
        ])
    ])
    
def viz4_html(fig):
    markdown_text = """
    ## What Were Argentina's Strengths and Weaknesses?
    """
    return html.Div(className='page-container', children=[
        dcc.Markdown(className='markdown-title', children=markdown_text),
        html.Div(className='app-container', children=[
            html.Div(className='graph-container', children=[
                dcc.Graph(
                    id='radar-chart',
                    figure=fig,
                    config=dict(
                        scrollZoom=False,
                        showTips=False,
                        showAxisDragHandles=False,
                        doubleClick=False,
                        displayModeBar=False
                    ),
                ),
            ])
        ])
    ])
    
def viz5_html(fig):
    markdown_title = """
    ## Who Are the Most Efficient Scorers?
    """

    markdown_text = """
        An efficient scorer is a player who manages to score goals while making fewer shots.
    """

    return html.Div(className='page-container', children=[
        html.Div(className='app-container', children=[
            html.Div(className='graph-container', children=[
                dcc.Markdown(className='markdown-title', children=markdown_title),
                dcc.Markdown(className='markdown-title', children=markdown_text),
                dcc.Graph(
                    id='horizontal-bar-chart',
                    figure=fig,
                    config=dict(
                        scrollZoom=False,
                        showTips=False,
                        showAxisDragHandles=False,
                        doubleClick=False,
                        displayModeBar=False
                    ),
                ),
            ])
        ])
    ])