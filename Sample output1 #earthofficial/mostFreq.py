import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
import csv



def main():
    
    plt.style.use('ggplot')
    x = []
    y = []
    z = []
    fig = plt.figure()
    with open('ht_sort_HASHTAG.csv') as csvfile:
        plots = csv.reader(csvfile, delimiter = ',')
        for row in plots:
            x.append(row[1])
            y.append(int(row[2]))
            z.append(float(row[3]))
    
   

    
    x = x[1:10]
    y = y[1:10]
    z = z[1:10]
   
    plt.barh(x, y, color='green')
    plt.xlabel("Hashtags")
    plt.ylabel("Frequency")
    plt.title("Frequency of most reccuring hashtags associated with earthofficial")

    
 
    for i, v in enumerate(y):
        plt.text(y[i] + 1, i + 0.01, str(v))
    plt.show()

   
if __name__ == "__main__":
  main()
