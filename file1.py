#import class
import pandas as pd
import matplotlib.pyplot as plt
countries = pd.read_excel('IMVA.xlsx')

#Getting our Country from Excel
trumpNfriends = countries.iloc[360: 479, 30: 35]

print(trumpNfriends) #Print the Countrys

print(trumpNfriends.sum())

trumpNofriends = trumpNfriends.sum()

#Our PlotGraph
trumpNofriends.plot(kind="bar", title= "Total Travellers from Others 08-17")
plt.show()



########################Unit Testing for Print###############################################
import unittest

class TestFile1(unittest.TestCase):

    def test(self):
      print(trumpNfriends)

if __name__ == '__main__':
    unittest.main()