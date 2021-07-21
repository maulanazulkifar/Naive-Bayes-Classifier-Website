import numpy as np
import pandas as pd
import io
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import csv


class Model:
    def __init__(self):
        self.df = None
        self.hasil = None

    # Get DataTrain

    def getdf(self, value):
        self.df = pd.read_csv("data.csv")

    # Get Data from user
    def getHasil(self, value):
        self.hasil = [('1', '0', '1')]
        self.f = open('test.csv', 'w')
        self.w = csv.writer(self.f)
        self.w.writerow(('IPK', 'Psikologi', 'Wawancara'))
        for self.h in self.hasil:
            self.w.writerow(self.h)
        self.f.close()

    # pra proses data test
    def preProcessing(self, value):
        # Variabel independen
        self.x = self.df.drop(['Pelamar', 'Diterima'], axis=1)
        # Variabel dependen
        self.y = self.df['Diterima']
        # Set datatrain dan dataset
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(
            self.x, self.y, test_size=0.4, random_state=12)

    # Train Data
    def trainData(self):
        self.modelnb = GaussianNB()
        self.nbtrain = self.modelnb.fit(self.x_train, self.y_train)
        self.nbtrain.class_count_

    # test hasil klasifikasi
    def testData(self):
        self.y_pred = self.nbtrain.predict(self.hasil)

    def processData(self, data):
        self.getdf(self)
