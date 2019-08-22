import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt
import matplotlib.dates as md
import matplotlib.dates as mdates
from matplotlib.animation import FuncAnimation
from database import Database


class Plotting:

    def __init__(self, database):

        self.items = Database(database)
        self.df = pd.DataFrame(self.items.view_table())

    def dataFrame(self):
        #takes database from Class, converts to DataFrame,
        #and converts datatime to readable format for plotting
        #also fills gabs in database (null) and retunrs all formated for plotting

        self.df[1] = pd.to_datetime(self.df[1], unit='s') # seconds since... UNIX EPOCH!
        filled = self.df.fillna(limit=7, method='ffill') #forward fill #filling all Null values
        return filled


    def temp_hum(self):
        #from pandas.plotting import register_matplotlib_converters
        #register_matplotlib_converters()

        #df_thresh = df[4].clip(lower=24, upper=None)
        #replace weird spikes, manual way but for now has to be OK

        #zamienić [1] pozycje w database na cos co moglbym zdefiniowac z zewnatrz ?

        rep = self.dataFrame()[4].replace([0.4, 12.4, 9.2, 11.4, 11.0], method='bfill')
        #print(rep.min())
        plt.style.use('bmh')
        plt.figure(figsize=(10,5))#
        plt.plot_date(self.dataFrame()[1],self.dataFrame()[2] , linestyle='solid', marker=None, label='temp_basement')
        plt.plot_date(self.dataFrame()[1],rep, linestyle='solid', marker=None, label='temp_inside')#
        plt.legend(loc='upper left')
        plt.tight_layout()
        plt.gcf().autofmt_xdate()#
        date_format = mdates.DateFormatter('%d-%b - %H:%M')
        plt.gca().xaxis.set_major_formatter(date_format)
        plt.show()


if __name__=='__main__':
    ploting = Plotting("oop.db")
    ploting.temp_hum()
