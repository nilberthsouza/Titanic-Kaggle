import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')
fig = plt.figure(figsize=(18,6))

female_color = '#FA0000'

plt.subplot2grid((3,4),(0,0))
df.Sex.value_counts(normalize=True).plot(kind='bar')
plt.title('Sex')


plt.subplot2grid((3,4),(0,1))
df.Survived[df.Sex=='male'].value_counts(normalize=True).plot(kind='bar')
plt.title('Men Survived')


plt.subplot2grid((3,4),(0,2))
df.Survived[df.Sex=='female'].value_counts(normalize=True).plot(kind='bar',color=female_color)
plt.title('Women Survived')


plt.subplot2grid((3,4),(0,3))
df.Sex[df.Survived==1].value_counts(normalize=True).plot(kind='bar',color=[female_color,'b'])

plt.title('Sex of Survived')




plt.show()
