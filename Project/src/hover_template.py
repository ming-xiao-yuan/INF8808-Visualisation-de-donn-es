def get_hover_template_viz1(mode):
    return "<b>%{y} </b>" + f"<span>{mode}</span>"

def get_hover_template_viz2():
    return '<br>'.join([
        "%{y}",
        "<b>    Metric: </b><span>%{x}</span>",
        "<extra></extra>"
    ])

def get_hover_template_viz3():
    return '<br>'.join([
        "%{customdata[1]}",
        "<b>    %{y}</b> Goals",
        "<b>    %{y}</b> Goal-Creating Actions",
        "<b>    %{customdata[0]}</b> Key Passes"
        "<extra></extra>"
    ])

def get_hover_template_viz4():
    return '<br>'.join([
        "<b>%{r}</b>" + "<span style='text-transform:lowercase'> %{theta} score<span>",
        "<extra></extra>"
    ])

def get_hover_template_viz5():
    return "<b>%{x} </b>"
