## Добавляем необходимые библиотеки


```python
import pandas as pd
import seaborn as sns
```

## Чтение датасета


```python
videogames = pd.read_csv("vgsales.csv")
videogames
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Platform</th>
      <th>Year</th>
      <th>Genre</th>
      <th>Publisher</th>
      <th>NA_Sales</th>
      <th>EU_Sales</th>
      <th>JP_Sales</th>
      <th>Other_Sales</th>
      <th>Global_Sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kaboom!</td>
      <td>2600</td>
      <td>1980.0</td>
      <td>Misc</td>
      <td>Activision</td>
      <td>1.07</td>
      <td>0.07</td>
      <td>0.0</td>
      <td>0.01</td>
      <td>1.15</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Boxing</td>
      <td>2600</td>
      <td>1980.0</td>
      <td>Fighting</td>
      <td>Activision</td>
      <td>0.72</td>
      <td>0.04</td>
      <td>0.0</td>
      <td>0.01</td>
      <td>0.77</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Ice Hockey</td>
      <td>2600</td>
      <td>1980.0</td>
      <td>Sports</td>
      <td>Activision</td>
      <td>0.46</td>
      <td>0.03</td>
      <td>0.0</td>
      <td>0.01</td>
      <td>0.49</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Freeway</td>
      <td>2600</td>
      <td>1980.0</td>
      <td>Action</td>
      <td>Activision</td>
      <td>0.32</td>
      <td>0.02</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.34</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Bridge</td>
      <td>2600</td>
      <td>1980.0</td>
      <td>Misc</td>
      <td>Activision</td>
      <td>0.25</td>
      <td>0.02</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.27</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>16534</th>
      <td>LEGO Harry Potter: Years 5-7</td>
      <td>PC</td>
      <td>NaN</td>
      <td>Action</td>
      <td>Warner Bros. Interactive Entertainment</td>
      <td>0.05</td>
      <td>0.14</td>
      <td>0.0</td>
      <td>0.03</td>
      <td>0.22</td>
    </tr>
    <tr>
      <th>16535</th>
      <td>Happy Feet Two</td>
      <td>DS</td>
      <td>NaN</td>
      <td>Action</td>
      <td>Warner Bros. Interactive Entertainment</td>
      <td>0.09</td>
      <td>0.02</td>
      <td>0.0</td>
      <td>0.01</td>
      <td>0.12</td>
    </tr>
    <tr>
      <th>16536</th>
      <td>Happy Feet Two</td>
      <td>PS3</td>
      <td>NaN</td>
      <td>Action</td>
      <td>Warner Bros. Interactive Entertainment</td>
      <td>0.09</td>
      <td>0.01</td>
      <td>0.0</td>
      <td>0.01</td>
      <td>0.10</td>
    </tr>
    <tr>
      <th>16537</th>
      <td>Happy Feet Two</td>
      <td>X360</td>
      <td>NaN</td>
      <td>Action</td>
      <td>Warner Bros. Interactive Entertainment</td>
      <td>0.08</td>
      <td>0.01</td>
      <td>0.0</td>
      <td>0.01</td>
      <td>0.10</td>
    </tr>
    <tr>
      <th>16538</th>
      <td>Happy Feet Two</td>
      <td>Wii</td>
      <td>NaN</td>
      <td>Action</td>
      <td>Warner Bros. Interactive Entertainment</td>
      <td>0.07</td>
      <td>0.01</td>
      <td>0.0</td>
      <td>0.01</td>
      <td>0.09</td>
    </tr>
  </tbody>
</table>
<p>16539 rows × 10 columns</p>
</div>



## Вытягивание из датасета столбца Genre и Global_Sales


```python
GenceAndGlobal_Sales = pd.crosstab(videogames["Genre"], videogames["Global_Sales"], margins=True)
```

## Установка размера графика


```python
sns.set(rc={"figure.figsize":(15, 4)})
```

## Формирование графика по стобцам


```python
chart = sns.barplot(x=GenceAndGlobal_Sales["All"][:12].index, y=GenceAndGlobal_Sales["All"][:12])
chart.set(xlabel='Genre', ylabel='Sales(in millions)')
```








    
![png](GamesSales_files/GamesSales_9_1.png)
    



```python

```
