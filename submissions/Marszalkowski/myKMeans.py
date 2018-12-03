from sklearn import preprocessing
import matplotlib.pyplot as plt
import numpy as np

nbaPGData = [
[	15.8, 8.2, 8.1, 1.7	],
[	25.4, 10.3, 10.1, 1.8	],
[	22.1, 5.6, 3.1, 1.1	],
[	16.7, 3.4, 3.7, 1.0	],
[	16.2, 6.9, 5.6, 1.1	],
[	13.1, 5.3, 4.6, 1.6	],
[	17.3, 4.8, 4.1, 0.8	],
[	17.7, 5.0, 3.8, 2.0	],
[	26.9, 6.6, 4.5, 1.1	],
[	14.2, 7.0, 3.0, 1.5	],
[	15.2, 5.2, 3.8, 1.0	],
[	19.4, 6.2, 3.1, 1.1	],
[	12.4, 5.3, 2.6, 1.3	],
[	12.7, 6.2, 4.3, 1.3	],
[	8.3, 8.2, 4.0, 1.1	],
[	24.4, 5.1, 3.8, 1.1	],
[	11.6, 4.4, 2.8, 1.0	],
[	10.0, 2.8, 2.7, 0.9	],
[	18.6, 7.9, 5.4, 1.7	],
[	12.6, 6.6, 3.2, 0.9	],
[	7.5, 5.6, 3.1, 0.6	],
[	26.4, 6.1, 5.1, 1.6	],
[	10.2, 7.2, 6.9, 1.7	],
[	8.1, 2.9, 5.7, 1.2	],
[	9.5, 3.2, 2.3, 0.7	],
[	14.6, 5.3, 2.8, 0.6	],
[	13.4, 6.0, 4.3, 2.0	],
[	7.8, 4.4, 1.8, 1.0	],
[	19.4, 9.6, 3.7, 1.4	],
[	15.3, 7.8, 4.0, 1.2	],
[	29.1, 11.2, 8.1, 1.5	],
[	31.6, 10.4, 10.7, 1.6	],
[	25.3, 6.6, 4.5, 1.8	],
[	23.2, 5.5, 3.9, 1.1	],
[	17.9, 6.3, 3.1, 0.9	],
[	23.1, 10.7, 4.2, 2.0	],
[	28.9, 5.9, 2.7, 0.9	],
[	27.0, 5.9, 4.9, 0.9	],
[	11.1, 9.1, 4.1, 1.7	],
[	20.3, 5.8, 3.8, 1.2	],
[	25.2, 5.8, 3.2, 1.2	],
[	20.5, 6.3, 3.5, 1.3	],
[	21.1, 6.3, 4.8, 1.4	],
[	13.2, 4.6, 2.2, 1.0	],
[	18.0, 4.4, 3.8, 0.7	],
[	10.1, 4.5, 1.8, 0.5	],
[	15.4, 7.3, 3.9, 1.5	],
[	18.1, 9.2, 5.0, 2.0	],
[	22.4, 7.0, 4.8, 1.5	],
[	15.6, 4.8, 3.5, 1.4	],
[	12.8, 6.5, 4.7, 1.1	],
[	7.6, 4.7, 1.9, 0.7	],
[	6.9, 6.6, 3.1, 1.7	],
[	14.5, 5.2, 2.2, 0.7	],
[	16.9, 4.2, 3.4, 1.0	],
[	11.0, 5.6, 2.3, 0.5	],
[	12.8, 2.7, 2.6, 1.1	],
[	7.8, 6.7, 5.1, 1.4	],
[	11.0, 3.9, 3.2, 0.7	],
[	20.9, 5.2, 4.4, 1.6	],
[	23.5, 10.4, 7.8, 2.0	],
[	16.9, 4.3, 7.7, 1.2	],
[	30.1, 6.7, 5.4, 2.1	],
[	18.8, 6.2, 3.0, 1.1	],
[	22.2, 6.2, 3.0, 1.1	],
[	15.7, 5.9, 2.7, 1.2	],
[	21.2, 6.4, 4.7, 2.1	],
[	19.9, 10.2, 4.9, 1.9	],
[	10.1, 8.7, 4.3, 2.1	],
[	25.1, 6.8, 4.0, 0.9	],
[	19.5, 10.0, 4.2, 2.1	],
[	12.1, 3.5, 4.0, 1.1	],
[	19.0, 4.6, 4.1, 1.1	],
[	7.6, 4.1, 3.2, 0.9	],
[	14.1, 5.8, 3.8, 1.0	],
[	11.9, 5.3, 2.4, 0.8	],
[	11.9, 11.7, 6.0, 2.0	],
[	10.7, 6.4, 3.6, 1.2	],
[	12.8, 5.5, 3.4, 1.0	],
[	16.4, 4.7, 3.4, 0.7	],
[	9.9, 3.4, 3.5, 1.3	],
[	14.1, 5.8, 2.9, 0.9	],
[	15.3, 6.1, 2.9, 1.2	],
[	19.6, 4.7, 3.0, 1.1	],
[	12.6, 6.5, 4.0, 3.4	],
[	13.2, 3.3, 3.4, 1.2	],
[	10.3, 5.4, 2.2, 0.5	],
[	15.6, 10.2, 4.3, 1.3	],
[	12.2, 6.4, 3.4, 1.5	],
[	17.6, 5.6, 4.0, 1.2	],
[	15.5, 7.9, 8.7, 1.4	],
[	15.9, 7.6, 3.0, 0.7	],
[	15.0, 6.0, 4.5, 1.3	],
[	9.0, 4.8, 2.3, 1.5	],
[	12.6, 2.3, 1.8, 0.7	],
[	27.1, 6.0, 5.3, 0.8	],
[	27.4, 6.3, 4.3, 1.3	],
[	21.5, 8.1, 3.6, 1.7	],
[	20.3, 6.6, 3.4, 1.2	],
[	17.5, 7.5, 4.0, 1.2	],
[	22.0, 6.4, 4.9, 1.9	],
[	17.5, 4.5, 4.3, 0.9	],
[	8.2, 4.5, 5.6, 1.0	],
[	16.0, 4.2, 2.7, 0.7	],
[	13.9, 3.9, 2.8, 1.2	],
[	6.7, 4.0, 4.0, 0.7	],
[	12.6, 7.6, 2.3, 1.3	],
[	7.5, 3.3, 2.6, 0.6	],
]



normalized_data = preprocessing.normalize(nbaPGData)


Examples = {
    'pgNotNormalized': {
        'data': nbaPGData,
        'k': [3, 2, 4],
    },
    'pgNormalized': {
        'data': normalized_data,
        'k': [2, 4, 3],
    },
}