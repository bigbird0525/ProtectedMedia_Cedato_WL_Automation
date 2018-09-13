'''
Written by Andrew Ravn
Last Updated: Sept132018
'''
import pandas as pd

class Filter(object):

    def __int__(self):
        super().__init__()

    def manipulateProtectedData(self, data, sensitive_ids):

        df = pd.DataFrame(data).iloc[:,[5,6,12,13]]
        df = df.loc[df['l3'].isin(sensitive_ids)]
        df['ivt_perc'] = df['af_fraud'].astype(float)/df['total'].astype(float)*100
        df = df[df['ivt_perc'] >= 2.5].sort_values(by=['l3'], ascending=True).reset_index(drop=True)
        return df.to_dict('records')
