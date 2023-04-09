'''
    This file contains the functions to call when
    a click is detected on the map, depending on the context
'''
import dash_html_components as html
import plotly.graph_objects as go


def no_clicks(style):
    '''
        Deals with the case where the map was not clicked

        Args:
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''

    return None, None, None, style


def map_base_clicked(title, mode, theme, style):
    '''
        Deals with the case where the map base is
        clicked (but not a marker)

        Args:
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''

    return title, mode, theme, style


def map_marker_clicked(figure, curve, point, title, mode, theme, style): # noqa : E501 pylint: disable=unused-argument too-many-arguments line-too-long
    '''
        Deals with the case where a marker is clicked

        Args:
            figure: The current figure
            curve: The index of the curve containing the clicked marker
            point: The index of the clicked marker
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''

    fig = go.Figure(figure)
    color = fig['data'][curve]['marker']['color']
    title = html.Span(children=fig.data[curve]['customdata'][0][point], style={'color': color })
    mode = fig.data[curve]['customdata'][1][point]
    tmp_theme = fig.data[curve]['customdata'][2][point]
    style['visibility'] = 'visible'
  
    if tmp_theme is None :
        return title, mode, None, style 
    
    theme = html.Div(children=[html.P(children='Thématique:')])
    ul = html.Ul(children=[])
    
    for curr_theme in tmp_theme.split('\n'):
        ul.children.append(html.Li(children=curr_theme))

    theme.children.append(ul)

    return title, mode, theme, style
