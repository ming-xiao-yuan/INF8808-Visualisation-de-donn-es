'''
    Provides the template for the tooltips.
'''


def get_bubble_hover_template():
    '''
        Sets the template for the hover tooltips.

        Contains four labels, followed by their corresponding
        value and units where appropriate, separated by a
        colon : country, population, GDP and CO2 emissions.

        The labels' font is bold and the values are normal weight

        returns:
            The content of the tooltip
    '''

    first_line = "<span style='font-weight:bold'>Country</span>: %{customdata[0]}"
    second_line = "<span style='font-weight:bold'>Population</span>: %{customdata[1]}"
    third_line = "<span style='font-weight:bold'>GDP</span>: %{x} $ (USD)"
    fourth_line = "<span style='font-weight:bold'>CO2 emissions</span>: %{y} metrics tonnes"
    fourth_line += "<extra></extra>"

    return "<br>".join([first_line, second_line, third_line, fourth_line])
