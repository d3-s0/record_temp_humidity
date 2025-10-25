import panel as pn
import pandas as pd
import plotly.express as px
pn.extension('plotly')

col_names = ['datetime','ignore','humidity','temperature','hic']
df = pd.read_csv('data/temp_humid_data.csv', header=None, names=col_names)
df['datetime'] = pd.to_datetime(df['datetime']) 

def plot_data(metric):
    fig = px.scatter(df, x='datetime', y=metric, title=f"{metric} over Time")
    return fig

# Metric filter
selected_columns = ['temperature', 'humidity']
metric_selector = pn.widgets.Select(name='Metric', options=selected_columns)

# Wraps the function to rerun anytime the metric dependency changes and 
# passing the updated value as a parameter.
@pn.depends(metric=metric_selector)
def interactive_plot(metric):
    fig = plot_data(metric)
    return pn.pane.Plotly(fig, sizing_mode='stretch_width', height=400)

# Arranges the 3 given components vertically in a single column in order
dashboard = pn.Column(
    pn.pane.Markdown("Temperature and Humidity"),
    metric_selector,
    interactive_plot
)

dashboard.save('plots/temp_humidity.html', embed=True)