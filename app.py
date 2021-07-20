from multiapp import MultiApp
from apps import charts, map


app = MultiApp()


#Adding all the applications here

app.add_app("Charts/Graphs", charts.app)
app.add_app("Map", map.app)


#The main app
app.run()