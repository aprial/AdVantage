import psycopg2
import numpy as np
import prettyplotlib as ppl
from matplotlib import pyplot
from pprint import pprint as pp

conn = psycopg2.connect(database='zipfian', host='localhost')

def execute_sql(sql_command):
    cur = conn.cursor()
    cur.execute(sql_command)
    rows = cur.fetchall()
    return rows


title = "Distribution of CPCs"
r = execute_sql("""SELECT cpc, COUNT(*) FROM ejam GROUP BY cpc ORDER BY cpc DESC;""")
pp(r)
pyplot.plot(zip(*r)[0], zip(*r)[1], 'o')
pyplot.xlabel('CPC')
pyplot.ylabel('Frequency of occurrence')
pyplot.title(title)
pyplot.show()


title = "Distribution of CPMs"
r = execute_sql("""SELECT cpm, COUNT(*) FROM ejam GROUP BY cpm ORDER BY cpm DESC;""")
pp(r)
pyplot.plot(zip(*r)[0], zip(*r)[1], 'o')
pyplot.xlabel('CPM')
pyplot.ylabel('Frequency of occurrence')
pyplot.title(title)
pyplot.show()


title = "Distribution of adIds: Avgerage CPC"
r = execute_sql("""SELECT adId, AVG(cpc), SUM(cpc), COUNT(cpc) FROM ejam GROUP BY adId HAVING count(cpc) > 0 ORDER BY count(cpc) DESC;""")
pp(r)
pyplot.plot(zip(*r)[1], 'o')
pyplot.xlabel('adId (ordered by frequency)')
pyplot.ylabel('Average CPC (blue dots)')
pyplot.twinx().plot(zip(*r)[3], '-r')
pyplot.ylabel('Frequency of occurrence (red line)')
pyplot.title(title)
pyplot.show()


title = "Distribution of apps: Avgerage CPC"
r = execute_sql("""SELECT app_id, AVG(cpc), SUM(cpc), COUNT(*) FROM ejam GROUP BY app_id ORDER BY count(*) DESC;""")
pp(r)
pyplot.plot(zip(*r)[1], 'o')
pyplot.xlabel('App (ordered by frequency)')
pyplot.ylabel('Average CPC (blue dots)')
pyplot.twinx().plot(zip(*r)[3], '-r')
pyplot.ylabel('Frequency of occurrence (red line)')
pyplot.title(title)
pyplot.show()


title = "Distribution of apps: Avgerage CPM"
r = execute_sql("""SELECT app_id, AVG(cpm), SUM(cpm), COUNT(*) FROM ejam GROUP BY app_id ORDER BY count(*) DESC;""")
pp(r)
pyplot.plot(zip(*r)[1], 'o')
pyplot.xlabel('App (ordered by frequency)')
pyplot.ylabel('Average CPM (blue dots)')
pyplot.twinx().plot(zip(*r)[3], '-r')
pyplot.ylabel('Frequency of occurrence (red line)')
pyplot.title(title)
pyplot.show()


title = "24-hour traffic pattern"
r = execute_sql("""SELECT dayofweek*24+hour, AVG(cpc), SUM(cpc), COUNT(*) FROM ejam GROUP BY dayofweek*24+hour ORDER BY dayofweek*24+hour;""")
pp(r)
pyplot.plot(zip(*r)[1], '-b')
pyplot.xlabel('Time (broken down by hour)')
pyplot.ylabel('Average CPC (blue line)')
pyplot.twinx().plot(zip(*r)[3], '-r')
pyplot.ylabel('Number of ads shown (red line)')
pyplot.title(title)
pyplot.show()


title = "Scatter-plot of adIds"
r = execute_sql("""SELECT AVG(cpc), COUNT(*) FROM ejam GROUP BY adId;""")
pp(r)
pyplot.plot(zip(*r)[0], zip(*r)[1], 'o')
pyplot.xlabel('Average CPC')
pyplot.ylabel('Frequency of occurrence')
pyplot.title(title)
pyplot.show()


title = "Scatter-plot of apps"
r = execute_sql("""SELECT AVG(cpc), COUNT(*) FROM ejam GROUP BY app_id;""")
pp(r)
pyplot.plot(zip(*r)[0], zip(*r)[1], 'o')
pyplot.xlabel('Average CPC')
pyplot.ylabel('Frequency of occurrence')
pyplot.title(title)
pyplot.show()


title = "Scatter-plot of users"
r = execute_sql("""SELECT AVG(cpc), COUNT(*) FROM ejam GROUP BY udid;""")
pp(r)
pyplot.plot(zip(*r)[0], zip(*r)[1], 'o')
pyplot.xlabel('Average CPC')
pyplot.ylabel('Frequency of occurrence')
pyplot.title(title)
pyplot.show()


title = "Summed revenue for each app"
r = execute_sql("""SELECT app_id, SUM(cpc) FROM ejam GROUP BY app_id HAVING SUM(cpc) > 0 ORDER BY SUM(cpc) DESC;""")
pp(r)
# pyplot.plot(zip(*r)[1], '-')
pyplot.vlines(range(len(r)), [0] * len(r), zip(*r)[1])
pyplot.xlabel('App (ordered by summed revenue)')
pyplot.ylabel('Sum of revenue')
pyplot.title(title)
pyplot.show()


title = "Summed revenue for each user"
r = execute_sql("""SELECT udid, SUM(cpc) FROM ejam GROUP BY udid HAVING SUM(cpc) > 0 ORDER BY SUM(cpc) DESC;""")
pp(r)
# pyplot.plot(zip(*r)[1], '-')
pyplot.vlines(range(len(r)), [0] * len(r), zip(*r)[1])
pyplot.xlabel('User (ordered by summed revenue)')
pyplot.ylabel('Sum of revenue')
pyplot.title(title)
pyplot.show()


title = "Summed revenue for each zone"
r = execute_sql("""SELECT zone, SUM(cpc) FROM ejam GROUP BY zone HAVING SUM(cpc) > 0 ORDER BY SUM(cpc) DESC;""")
pp(r)
# pyplot.plot(zip(*r)[1], '-')
pyplot.vlines(range(len(r)), [0] * len(r), zip(*r)[1])
pyplot.xlabel('Geographical Zone (ordered by summed revenue)')
pyplot.ylabel('Sum of revenue')
pyplot.title(title)
pyplot.show()




def device_model_bar_chart(data_dict):
    # data_dict is like this:
    #   {
    #    'Linux': 50.7577,
    #    'iPhone': 83.7963,
    #    'iPad': 34.564,
    #    'iPod': 27.1098
    #   }
    pyplot.bar([1.4, 2.0, 2.2, 2.4], # Left
               [data_dict['Linux'], data_dict['iPhone'], data_dict['iPad'], data_dict['iPod']], # Height
               [0.2, 0.2, 0.2, 0.2], # Width
               [0, 0, 0, 0], # Bottom
              )
    pyplot.xticks( (1.5, 2.1, 2.3, 2.5),
                   ('Android', 'iPhone', 'iPad', 'iPod') )


title = "Summed revenue for each device model"
r = execute_sql("""SELECT device_model, SUM(cpc) FROM ejam GROUP BY device_model HAVING SUM(cpc) > 0 ORDER BY SUM(cpc) DESC;""")
pp(r)
d = dict(r)
device_model_bar_chart(d)
pyplot.ylabel('Sum of revenue (CPC)')
pyplot.title(title)
pyplot.show()


title = "Summed revenue for each device model"
r = execute_sql("""SELECT device_model, SUM(cpm) FROM ejam GROUP BY device_model HAVING SUM(cpm) > 0 ORDER BY SUM(cpm) DESC;""")
pp(r)
d = dict(r)
device_model_bar_chart(d)
pyplot.ylabel('Sum of revenue (CPM)')
pyplot.title(title)
pyplot.show()


title = "Average CPC for each device model"
r = execute_sql("""SELECT device_model, AVG(cpc) FROM ejam GROUP BY device_model HAVING AVG(cpc) > 0 ORDER BY AVG(cpc) DESC;""")
pp(r)
d = dict(r)
device_model_bar_chart(d)
pyplot.ylabel('Average CPC')
pyplot.title(title)
pyplot.show()


title = "Average CPM for each device model"
r = execute_sql("""SELECT device_model, AVG(cpm) FROM ejam GROUP BY device_model HAVING AVG(cpm) > 0 ORDER BY AVG(cpm) DESC;""")
pp(r)
d = dict(r)
device_model_bar_chart(d)
pyplot.ylabel('Average CPM')
pyplot.title(title)
pyplot.show()




# --------------------------------------------------
# Create a heatmap.
# Feature ideas: App, zone, country, adId
# Color could represent: count(*), avg(cpc), sum(cpc)

title = "Heatmap of average CPC for each (adId, app)"
adId_indices = execute_sql("""SELECT adId FROM ejam GROUP BY adId HAVING AVG(cpc) > 0 ORDER BY COUNT(*) DESC;""")
app_indices = execute_sql("""SELECT app_id FROM ejam GROUP BY app_id ORDER BY COUNT(*) DESC;""")
adId_indices = dict((k[0],v) for v,k in enumerate(adId_indices))
app_indices = dict((k[0],v) for v,k in enumerate(app_indices))
pp(adId_indices)
pp(app_indices)
r = execute_sql("""SELECT adId, app_id, AVG(cpc) FROM ejam GROUP BY adId, app_id HAVING AVG(cpc) > 0;""")
pp(r)
matrix = np.zeros((len(adId_indices), len(app_indices)))
for adId, app, value in r:
  if adId in adId_indices and app in app_indices:
    adId = adId_indices[adId]
    app = app_indices[app]
    matrix[adId][app] = value
matrix = matrix.clip(0, 0.15)
pp(matrix)
fig, ax = ppl.subplots(1)
ppl.pcolormesh(fig, ax, matrix)
pyplot.xlabel('App (ordered by frequency)')
pyplot.ylabel('adId (ordered by frequency)')
pyplot.title(title)
pyplot.show()







