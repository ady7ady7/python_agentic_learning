#I will be putting the CD Python course for Data Anylsis tasks here
#Please note that the .csv dataframes (as mini-df.csv) are loaded in a webapp environment and I don't have them here, so I'm not able to load them.
#I'm running them in that environment and actually testing here only the ones that can be launched (as in T203 below)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from scipy.stats import ttest_ind #added on 17.06.26

#CD Python T200 (#estimated task number, as I've stored previous tasks in pcap_archive/practice.py)
'''
Zadanie
Za pomocą metody plot() stwórz histogram pokazujący rozkład powierzchni mieszkań. Dodaj tytuł do wykresu. Przypisz wykres do zmiennej fg.

Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()
'''

# df = pd.read_csv("mini-df.csv")
# df.head()

# fg = df['area'].plot(kind = 'hist', title = 'rozklad powierzchni')
# plt.show()


#CD Python T201
'''
Zadanie
Narysuj wykres liniowy pokazujący jak zmienia się średnia cena mieszkania za metr w czasie (kolumna date). Przypisz wykres do zmiennej fg.

Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:
plt.show()
'''

# import pandas as pd
# import matplotlib.pyplot as plt


# df = pd.read_csv("mini-df.csv")
# fg = df["price_per_m"].groupby(df["date"]).mean().plot()
# plt.show()


#CD Python T202

'''
Narysuj wykres pokazujący gdzie w Krakowie są rozmieszczone oferty mieszkań. Na podstawie wykresu oceń czy więcej ofert pojawia się na północ (w górnej części wykresu), czy południe (dolna część wykresu) od punktu środkowego. Przypisz odpowiedź polnoc lub poludnie do zmiennej flats.

Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()
'''


# df = pd.read_csv("mini-df.csv")
# df.head()


# fg = plt.scatter(df['longitude'], df['latitude']) #scatterplot obviously
# plt.show()

# flats = 'polnoc'


#CD Python T203
'''
Zadanie
Stwórz scatterplot, w którym widzimy zależność między wiekiem a sumą wydanej kwoty. Nadaj odrębne kolory punktom reprezentującym kobiety (jeżeli imię kończy się na a) i mężczyzn. Przypisz wykres do zmiennej fg.

Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()

'''

# users = pd.DataFrame({
#     "user_id":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25],
#     "name":["Anna","Jan","Kasia","Piotr","Ola","Marek","Ewa","Tomek","Magda","Paweł","Natalia","Bartek","Zosia","Adam","Karolina","Michał","Alicja","Filip","Monika","Kamil","Julia","Mateusz","Weronika","Łukasz","Dominika"],
#     "age":[19,22,25,28,31,None,37,40,43,46,39,52,55,58,49,41,21,27,33,22,45,51,57,63,38],
#     "city":["Warszawa","Kraków","Gdańsk","Wrocław","Poznań","Łódź","Katowice","Lublin","Szczecin","Bydgoszcz","Rzeszów","Białystok","Gdynia","Opole","Toruń","Kielce","Olsztyn","Radom","Zielona Góra","Koszalin","Płock","Elbląg","Legnica","Słupsk","Tarnów"]
# })

# orders = pd.DataFrame({
#     "order_id":[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240],
#     "user_id":[1,2,3,1,4,5,2,6,7,8,9,10,11,12,13,14,15,3,5,7,2,1,16,17,18,19,20,21,22,23,24,25,16,18,20,22,24,17,19,21],
#     "order_date":[
#         "2024-01-05","2024-01-07","2024-01-10","2024-01-12","2024-01-15","2024-01-18","2024-01-20","2024-01-22","2024-01-25","2024-01-27",
#         "2024-02-01","2024-02-03","2024-02-05","2024-02-07","2024-02-10","2024-02-12","2024-02-15","2024-02-18","2024-02-20","2024-02-22",
#         "2024-02-25","2024-02-28","2024-03-02","2024-03-04","2024-03-06","2024-03-08","2024-03-10","2024-03-12","2024-03-14","2024-03-16",
#         "2024-03-18","2024-03-20","2024-03-22","2024-03-24","2024-03-26","2024-03-28","2024-03-30","2024-04-01","2024-04-03","2024-04-05"
#     ],
#     "amount":[120,200,150,80,300,220,50,400,90,180,250,130,75,310,160,300,95,140,275,60,210,330,180,95,260,310,120,150,40,220,130,170,280,200,90,350,410,160,240,30]
# })


# users_orders = users.merge(orders, on = 'user_id')

# def check_gender(name):
#     if str(name).endswith('a'):
#         return 'female'
#     else:
#         return 'male'

# users_orders['gender'] = users_orders['name'].apply(check_gender)
# age_gender_df = users_orders.groupby(['gender', 'age'])['amount'].agg('sum').reset_index()

# fg = plt.scatter(x=age_gender_df[age_gender_df["gender"] == 'male']["age"], y=age_gender_df[age_gender_df["gender"] == 'male']["amount"], c="pink", label="mężczyźni")
# plt.scatter(x=age_gender_df[age_gender_df["gender"] == 'female']["age"], y=age_gender_df[age_gender_df["gender"] == 'female']["amount"], c="blue", label="kobiety")
# plt.xlabel("Wiek")
# plt.ylabel("Wydana kwota")
# plt.legend()
# plt.show()


#CD Python T204
'''
Zadanie
Stwórz wykres słupkowy, który pokazuje średnią cenę za metr dla poszczególnych typów ogrzewania. Przypisz wykres do zmiennej fg.

Wykres powinien:

być narysowany na obrazie (Figure) o rozmiarze (15 ,7)
mieć posortowane słupki od największych do najmniejszych
mieć tytuł
mieć nazwaną oś x i y
Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()
'''

# df = pd.read_csv("mini-df.csv")
# df.head()


# heating_prices_per_m_df = df.groupby('heating')['price_per_m'].agg('mean').reset_index()
# heating_prices_per_m_df = heating_prices_per_m_df.sort_values('price_per_m', ascending = False)
# heating_prices_per_m_df.head()

# fg = plt.figure(figsize = (15, 7))
# fg = plt.bar(x = heating_prices_per_m_df['heating'], height = heating_prices_per_m_df['price_per_m'])
# fg = plt.title('Średnie ceny za metr według rodzaju ogrzewania')
# fg = plt.xlabel('Rodzaj ogrzewania')
# fg = plt.ylabel('Średnia cena za m2')
# plt.show()


#CD Python T205
'''
Zadanie
Czy rozkład wartości ceny mieszkania za metr ma rozkład normalny, lewo- czy prawoskośny? Przypisz odpowiedź do zmiennej rozklad: norm, lewo, lub prawo.

Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()
'''

# df = pd.read_csv("mini-df.csv")
# df.head()

# df['price_per_m'].hist()
# plt.show()

# rozklad = 'prawo'


#CD Python T206
'''
Zadanie
Stwórz wykres kołowy pokazujący udział mieszkań z rynku pierwotnego oraz wtórnego. Dodaj etykiety (labels) na podstawie oryginalnych wartości z kolumny. Przypisz wykres do zmiennej fig.

Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()
'''

# df = pd.read_csv("mini-df.csv")
# df.head()

# market_type_split = df.groupby('market_type')['url'].agg('count').reset_index()
# market_type_split.head()

# fig = plt.pie(market_type_split['url'], labels = market_type_split['market_type'])
# plt.show()


#CD Python T207

'''
Dla wszystkich kolumn numerycznych, które mają więcej niż 2 unikalne wartości (nie tylko 0/1) narysuj histogramy pokazujące wartości w tych kolumnach.

Histogramy narysuj w formie subplots, każda zmienna powinna być w innym wierszu. Użyj kodu poniżej podkładając pod X liczbę zmiennych:

fig, ax = plt.subplots(X, 1)
plt.show()
'''

# df = pd.read_csv("mini-df.csv")
# df.head()
# columns = ['area', 'price', 'price_per_m', 'rooms_no', 'floor_no', 'build_year', 'build_floor_num', 'latitude', 'longitude',]

# fig, ax = plt.subplots(9, 1)
# for i in range(9):
#     ax[i].hist(df[columns[i]])
# plt.show()


#CD Python T208
'''
Minusem wykresu słupkowego jest to, że pokazuje różnice między grupami tylko dla jednej miary, np. dla średniej.

Stwórz dwa wykresy słupkowe, na jednej pokaż średnią cenę mieszkania (price) na typ budynku (build_type), na drugim medianę ceny dla typu budynku. Dodaj tytuły do wykresów. Przypisz wykres do zmiennych: fig_mean oraz fig_median.

Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()

'''


# df = pd.read_csv("mini-df.csv")
# df.head()

# build_type_avgs = df['price'].groupby(df['build_type']).agg(['mean', 'median']).reset_index()
# build_type_avgs.head()

# fig_mean = build_type_avgs['mean'].plot(kind = 'bar')
# fig_mean = plt.title('Średnia')
# fig_mean = plt.xlabel(build_type_avgs['build_type'])
# plt.show()

# fig_median = build_type_avgs['median'].plot(kind = 'bar')
# fig_median = plt.title('Mediana')
# fig_mean = plt.xlabel(build_type_avgs['build_type'])
# plt.show()


#CD Python T209
'''
Alternatywą dla wykresu słupkowego jest wykres pudełkowy (boxplot), który zamiast jednej miary pokazuje rozkład wartości.

Stwórz wykres pudełkowy w którym pokażesz rozkład ceny (price) dla rynku (market_type) pierwotnego i wtórnego. Aby zestawić koło siebie dwa pudełka możesz użyć składni plt.boxplot([df1, df2]). Przypisz wykres do zmiennej fig.

Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()
'''


# df = pd.read_csv("mini-df.csv")
# df.head()

# df1 = df['price'].groupby(df['market_type'])
# fig = plt.boxplot(
#     [
#     df['price'][df['market_type'] == 'primary'],
#     df['price'][df['market_type'] == 'secondary']
#     ],
#     labels = ['Primary', 'Secondary']
# )
# plt.show()

#CD Python T210

'''
Stwórz wykres punktowy (scatterplot), w którym pokazujesz metraż (area) na osi x vs. cenę (price) na osi y. Przypisz go do zmiennej fig.

Sformatuj wykres:

nadaj mu tytuł
nadaj nazwy osi x i y
uwzględnij zakres osi x od 40 do 55 metrów
uwzględnij zakres osi y od 250,000 do 800,000
narysuj siatkę (grid)
Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()
'''

# df = pd.read_csv("mini-df.csv")
# df.head()


# fig = plt.scatter(x = df['area'], y = df['price'])
# fig = plt.title('Wielkosc vs cena mieszkania')
# fig = plt.xlabel('Wielkosc mieszkania w m2')
# fig = plt.ylabel('Cena mieszkania')
# fig = plt.xlim(40, 55)
# fig = plt.ylim(250000, 800000)
# fig = plt.grid(True)
# plt.show()



#CD Python T211
'''
Zadanie
Im bardziej agregujemy dane do dłuższych okresów czasu, tym bardziej wygładzamy informacje. Agregacja dzienna pokazuje dużo krótkoterminowych zmian i wahań, natomiast agregacja tygodniowa lub miesięczna pozwala łatwiej zauważyć ogólne trendy.

Stwórz wykresy liniowe liczące średnią wartość amount dla każdego:

dnia - przypisz do zmiennej fig_d
tygodnia - przypisz do zmiennej fig_w
miesiąca - przypisz do zmiennej fig_m
Tygodnie oraz miesiące możesz wyciągnąć na kolumnie typu datetime za pomocą metody: df["col"].dt.to_period("W").dt.start_time

Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()
'''

# df = pd.read_csv("orders.csv")
# df.head()

# df['order_date'] = pd.to_datetime(df['order_date'])
# df['day'] = df['order_date'].dt.to_period('D').dt.start_time
# df['week'] = df['order_date'].dt.to_period('W').dt.start_time
# df['month'] = df['order_date'].dt.to_period('M').dt.start_time

# fig_d = df.groupby('day')['amount'].agg('mean').plot()
# plt.show()
# fig_w = df.groupby('week')['amount'].agg('mean').plot()
# plt.show()
# fig_m = df.groupby('month')['amount'].agg('mean').plot()
# plt.show()



#CD Python T212
'''Na podstawie dokumentacji metody plot() zmodyfikuj wykres tak, aby punkty były oznaczone czerwonymi diamentami.
Przypisz nowy wykres do zmiennej fg.

Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()'''

# df = pd.read_csv("mini-df.csv")
# fg = df["price_per_m"].groupby(df["date"]).mean().plot(marker = 'D', color = 'r')
# plt.show()


#CD Python T213
'''Stwórz wykres słupkowy poziomy (horizontal), który pokazuje średnią cenę mieszkania za metr na typ ogrzewania. 
Dodaj pionową linię (zobacz funkcję axvline), która zaznacza średnią cenę za metr mieszkania z wszystkich ofert df.
Przypisz wykres do zmiennej fig.

Zmień kolory:

słupki w kolorze lightblue
linia w kolorze red
Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()'''


# df = pd.read_csv("mini-df.csv")
# df.head()

# fig = df['price_per_m'].groupby(df['heating']).mean().sort_values().plot(kind = 'barh', color = 'lightblue')
# fig = plt.axvline(df['price_per_m'].mean(), color = 'red')
# plt.show()



#CD Python T214
'''Zadanie
Stwórz wykres typu scatterplot za pomocą biblioteki Seaborn, wybierz jakiekolwiek kolumny z df.

Przypisz go do zmiennej fig.

Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()'''

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# df = pd.read_csv("mini-df.csv")
# df.head()

# fig = sns.scatterplot(df, x = 'area', y = 'price')
# plt.show()


#CD Python T215
'''Zadanie
Za pomocą metody plot() stwórz histogram pokazujący rozkład powierzchni mieszkań. Dodaj tytuł do wykresu. Przypisz wykres do zmiennej fg.

Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()'''

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("mini-df.csv")
# df.head()

# fg = df['area'].plot(kind = 'hist', title = 'rozklad powierzchni')
# plt.show()



#CD Python T216
'''Zadanie
Narysuj wykres liniowy pokazujący jak zmienia się średnia cena mieszkania za metr w czasie (kolumna date). Przypisz wykres do zmiennej fg.

Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()'''


# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("mini-df.csv")
# fg = df["price_per_m"].groupby(df["date"]).mean().plot()
# plt.show()


#CD Python T217
'''Zadanie
Porównaj zrobienie wykresu słupkowego za pomocą biblioteki Matplotlib i Seaborn. Na wykresach pokaż średnią powierzchnię na typ budynku.

Przypisz wykresy do zmiennych: fig_plt oraz fig_sns.

Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()'''

# df = pd.read_csv("mini-df.csv")
# df.head()

# fig_plt = df["area"].groupby(df["build_type"]).mean().plot(kind = 'bar')
# plt.show()

# fig_sns = sns.barplot(
#     df,
#     y = 'area',
#     x = 'build_type',
#     estimator = 'mean'
#     )
# plt.show()


#CD Python T218
'''Zadanie
Stwórz wykres słupkowy, który pokazuje wysokość słupka na podstawie mediany powierzchni na typ budynku, a słupki błędu reprezentują błąd standardowy.

Przypisz wykres do zmiennej: fig.

Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()'''

# df = pd.read_csv("mini-df.csv")
# df.head()

# fig = sns.barplot(
#     df,
#     x = 'build_type',
#     y = 'area',
#     estimator = 'median',
#     errorbar = 'se'
# )

# plt.show()

#CD Python T219
'''Zadanie
Narysuj wykres liniowy w bibliotece Seaborn pokazujący jak zmienia się mediana powierzchni (area) mieszkań w czasie ( date). Przypisz wykres do zmiennej fg.

Czy widzisz trend spadkowy, porównując poszczególne tygodnie? Przypisz odpowiedź True / False do zmiennej is_area_decreasing.

Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()'''


# df.head()

# fg = sns.lineplot(
#     df,
#     x = 'date',
#     y = 'area',
# )
# fg = plt.xticks(rotation=45)
# plt.show()

# is_area_decreasing = False


#CD Python T220

'''
Zadanie
Narysuj wykres liniowy w bibliotece Seaborn pokazujący jak zmienia się średnia cena za metr w czasie ( date) dla mieszkań z i bez garażu. Usuń słupki błędu (errorbar). Przypisz wykres do zmiennej fg.

Które mieszkania miały wyższą średnią cenę dnia 2020-12-16? Przypisz True, jeżeli mieszkania z garażem do zmiennej garage_higher i False w innym przypadku.

Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()
'''

# df = pd.read_csv("mini-df.csv")
# df.head()

# fg = sns.lineplot(
#     df,
#     x = 'date',
#     y = 'price_per_m',
#     estimator = 'mean',
#     hue = 'garage',
#     errorbar = None
# )
# fg = plt.xticks(rotation = 45)

# plt.show()

# garage_higher = False


#CD Python T221
'''
Zadanie
Narysuj wykres pudełkowy (boxplot) w bibliotece Seaborn pokazujący rozkład powierzchni dla różnych typów ogrzewania. Przypisz go do zmiennej fg.

Który typ ogrzewania ma najwyższą medianę? Przypisz odpowiedź do zmiennej higher_median.

Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()
'''

# df = pd.read_csv("mini-df.csv")
# df.head()


# fg = sns.boxplot(
#     df,
#     x = 'heating',
#     y = 'area'
# )
# plt.show()

# higher_median = 'gas'


#CD Python T222
'''Zadanie
Stwórz histogram pokazujący rozkład cen (price) mieszkania. Dodaj do niego wykres KDE. Przypisz wykres do zmiennej fig.

Czy rozkład jest normalny? Przypisz wartość True / False do zmiennej normal_distribution.

Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()'''

# df = pd.read_csv("mini-df.csv")
# df.head()

# fig = sns.histplot(
#     df['price'], kde = True
# )
# plt.show()

# normal_distribution = False

#CD Python T223
'''Stwórz wykres KDE pokazujący rozkład cen (price) mieszkania dla rynku pierwotnego i wtórnego. Przypisz wykres do zmiennej fig.

Na jakim rynku częściej pojawiają się bardzo drogie mieszkania? Przypisz odpowiedź primary lub secondary do very_expensive_flats

Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()'''

# fig = sns.kdeplot(
#     df,
#     x = 'price',
#     hue = 'market_type'
# )

# plt.show()

# very_expensive_flats = 'secondary'

#CD Python T224
'''
Zadanie
Zobaczmy jak się różnią dane dla małych i większych mieszkań.

Stwórz wykres typu pairplot, w którym porównasz price_per_m, area i floor_no.

Narysuj różnymi kolorami:

mieszkania na wschodzie: longitude > 19.943
mieszkania na zachodzie longitude <= 19.943
Na podstawie wykresu określ które mieszkania mają wyższą medianę ceny za metr. Przypisz odpowiedź east lub west do zmiennej higher_price

Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()
'''
# df = pd.read_csv("mini-df.csv")
# df.head()

# df['east'] = df['longitude'] > 19.943
# fig = sns.pairplot(data = df[['price_per_m', 'area', 'floor_no', 'east']], hue = 'east')
# plt.show()

# higher_price = 'west'

#CD Python T225
'''Porównaj jak wygląda histogram z i bez outlierów.

Narysuj na początku rozkład wartości df["price"]. Następnie stwórz drugi histogram, w którym oś x kończy się na wartości odpowiadającej 99. percentylowi tej kolumny, przypisz go do zmiennej fig.

Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()'''


# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# np.random.seed(42)
# normal_values = np.random.lognormal(mean=10, sigma=0.4, size=300)
# outliers = [180000, 250000]
# df = pd.DataFrame({"price": np.concatenate([normal_values, outliers])})

# df.head()
# hist = sns.histplot(df['price'])
# plt.show()

# perc_99 = df['price'].quantile(0.99)
# fig = sns.histplot(
#     df['price']
#     )
# fig.set_xlim(0, perc_99)
# plt.show()



#CD Python T226
'''Centralne Twierdzenie Graniczne (ang. Central Limit Theorem, CLT) mówi,
że średnie z wielu próbek zaczynają przypominać rozkład normalny, nawet jeśli oryginalne dane mają inny rozkład.

Stwórz histogram dla kolumny amount i sprawdź rozkład transakcji.

Następnie pogrupuj dane licząc średnią wartość transakcji dla każdego użytkownika.
Dla otrzymanych średnich ponownie narysuj histogram, przypisz go do zmiennej fig.

Porównaj jak zmienia się rozkład danych po uśrednieniu wartości dla użytkowników.

Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()'''


# np.random.seed(42)
# transactions_per_user = np.random.randint(1, 11, size=1000)

# rows = []
# for user_id, n_transactions in enumerate(transactions_per_user, start=1):
#     amounts = np.random.exponential(scale=120, size=n_transactions)
#     for amount in amounts:
#         rows.append([user_id, round(amount, 2)])

# df = pd.DataFrame(rows, columns=["user_id", "amount"])

# df.head()

# hist = sns.histplot(
#     df['amount'],
#     kde = True
#     )
# plt.show()

# grouped_means = df['amount'].groupby(df['user_id']).mean().reset_index()
# print(grouped_means)
# fig = sns.histplot(grouped_means['amount'], kde = True)
# plt.show()


#CD Python T227
'''Zadanie
Wykres KDE ma przewagę nad histogramem przy porównywaniu rozkładów różnych zbiorów danych o kompletnie innej liczebności.

Stwórz wykres KDE dla rozkładu kolumny amount dla df i df_mini. Porównaj wyniki z histogramem.

Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()'''

# np.random.seed(42)
# transactions_per_user = np.random.randint(1, 11, size=1000)

# rows = []
# for user_id, n_transactions in enumerate(transactions_per_user, start=1):
#     amounts = np.random.exponential(scale=120, size=n_transactions)
#     for amount in amounts:
#         rows.append([user_id, round(amount, 2)])

# df = pd.DataFrame(rows, columns=["user_id", "amount"])
# df_mini = pd.read_csv("orders.csv")

# fg = sns.histplot(data=df, x="amount", label="more data")
# fg = sns.histplot(data=df_mini, x="amount", label="less data")
# fg = plt.legend()
# plt.show()


# fg = sns.kdeplot(
#     df,
#     x = 'amount',
#     label = 'more_data'
# )
# fg = sns.kdeplot(
#     df_mini,
#     x = 'amount',
#     label = 'less_data'
# )
# fg = plt.legend()
# plt.show()


#CD Python T228

'''Zadanie
Wykres countplot przedstawia liczebność dla danych kategorialnych.

Stwórz wykres typu countplot pokazując liczebność na miasto, dla 5 miast z największą liczbą ofert pracy. Posortuj słupki malejąco.

Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()'''

# df = pd.read_csv("offers.csv")

# city_counts = df.groupby('MIASTO').agg(
#     offer_count = ('LINK', 'count')
# ).reset_index()
# city_counts = city_counts.sort_values(by = 'offer_count', ascending = False)
# cities_list = city_counts['MIASTO'][0:5].values.tolist()

# filtered_df = df[df['MIASTO'].isin(cities_list)]

# plot = sns.countplot(
#     filtered_df,
#     x = 'MIASTO'
# )
# plt.show()

#być może trochę na okrętkę, ale ogarnąłem elegancko :))

#wariant Kasi

# df = pd.read_csv("offers.csv")
# top_cities = df["MIASTO"].value_counts().head(5).index.tolist()
# sns.countplot(data=df[df.MIASTO.isin(top_cities)], x="MIASTO", order=top_cities)
# plt.show()


#CD Python T229
'''Zadanie
Stwórz wykres typu heatmap, w którym pokażesz wartości korelacji między poniższymi cechami. Zmień kolory na palete kolorystyczną Blues.

"area", "price_per_m", "rooms_no", "floor_no", "build_year"
Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()'''


# df = pd.read_csv("mini-df.csv")
# df.head()

# mapa = sns.heatmap(
#     df[['area', 'price_per_m', 'rooms_no', 'floor_no', 'build_year']].corr(),
#     cmap = 'Blues'
# )
# plt.show()


#CD Python T230
'''Zadanie
Stwórz wykres skrzypcowy violinplot. Wybierz ze zbioru danych zmienne, dla których ten wykres ma sens.

Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()'''


# df = pd.read_csv("mini-df.csv")
# df.head()

# wykres = sns.violinplot(
#     df,
#     x = 'market_type',
#     y = 'price_per_m'
# )
# plt.show()


#CD Python T231
'''Zadanie
Stwórz wykres catplot pokazujący zależność ceny za metr dla rynku wtórnego i pierwotnego,
ze zróżnicowaniem na fakt, czy jest to małe mieszkanie, czy nie (poniżej 50 m2)
'''

# df = pd.read_csv("mini-df.csv")
# df["is_small_flat"] = df["area"] < 50
# sns.catplot(
#     data=df, x="market_type", y="price_per_m", hue="is_small_flat",
#     kind="boxen"
# )
# plt.show()



#Weekend Python review #1 T1

'''Using comprehensions (no loops), produce:

1a. A list of gross values (`qty * price`) for buy trades only.

1b. A dict mapping each symbol to its total qty traded (both sides combined).
    Expected: `{'AAPL': 180, 'TSLA': 170, 'NVDA': 200, 'MSFT': 30}`

1c. A set of symbols where at least one trade has gross value above 50,000.'''

# trades = [
#     {'symbol': 'AAPL', 'side': 'buy', 'qty': 100, 'price': 182.5},
#     {'symbol': 'TSLA', 'side': 'sell', 'qty': 50, 'price': 245.0},
#     {'symbol': 'NVDA', 'side': 'buy', 'qty': 200, 'price': 610.0},
#     {'symbol': 'AAPL', 'side': 'sell', 'qty': 80, 'price': 190.0},
#     {'symbol': 'MSFT', 'side': 'buy', 'qty': 30, 'price': 415.0},
#     {'symbol': 'TSLA', 'side': 'buy', 'qty': 120, 'price': 238.0},
# ]


# gross_values =  [trade['qty'] * trade['price'] for trade in trades]
# print(gross_values)


# symbol_qty = {trade['symbol'] : (trade['qty'] * trade['price']) for trade in trades}
# print(symbol_qty)

# high_value_symbols = list(set([trade['symbol'] for trade in trades if trade['qty'] * trade['price'] >= 50000]))
# print(high_value_symbols)



#Weekend Python review #1 T2

'''Write a function `weighted_avg_price(trades, symbol)` that:
- Takes the trades list above and a symbol string
- Returns the weighted average price for that symbol across all trades (weighted by qty)
- Raises a `ValueError` with a descriptive message if the symbol doesn't exist in the list
- Returns a float rounded to 2 decimal places

Example: `weighted_avg_price(trades, 'AAPL')` → `(100*182.5 + 80*190.0) / (100+80)` → `185.83`

Then write a second function `top_n_by_value(trades, n)`
that returns the top n trades by gross value as a list of dicts, sorted descending.
Handle the case where n exceeds the number of trades gracefully.'''

# from typing import List

# def weighted_avg_price(trades: List[dict], symbol: str) -> float:
#     filtered_trades = [trade for trade in trades if trade['symbol'] == symbol]
    
    
#     vwap_sums = [(trade['price'] * trade['qty']) for trade in filtered_trades]
#     vwap_qties = sum([(trade['qty']) for trade in filtered_trades])
    
#     vwap = round(sum(vwap_sums) / vwap_qties, 2)
#     return vwap
    
    
# trades = [
#     {'symbol': 'AAPL', 'side': 'buy', 'qty': 100, 'price': 182.5},
#     {'symbol': 'TSLA', 'side': 'sell', 'qty': 50, 'price': 245.0},
#     {'symbol': 'NVDA', 'side': 'buy', 'qty': 200, 'price': 610.0},
#     {'symbol': 'AAPL', 'side': 'sell', 'qty': 80, 'price': 190.0},
#     {'symbol': 'MSFT', 'side': 'buy', 'qty': 30, 'price': 415.0},
#     {'symbol': 'TSLA', 'side': 'buy', 'qty': 120, 'price': 238.0},
# ]

# print(weighted_avg_price(trades, 'TSLA'))




# def top_n_by_value(trades: List[dict], n: int):
#     try:
    
#         sorted_trades = sorted(trades, 
#                                key = lambda trade: trade['qty'] * trade['price'],
#                                reverse = True)
#         return sorted_trades[:n]
#     except IndexError:
#         print(f'Please make sure your desired n trades is shorter than {len(trades)}')


# print(top_n_by_value(trades, 15))



#Weekend Python review #1 T3

'''
Write a `Portfolio` class that:

- `__init__` takes an owner name (string) and initialises an empty list of positions
- `add_position(symbol, qty, avg_price)` adds a position dict to the list
- `remove_position(symbol)` removes the position by symbol — raises `KeyError` if not found
- `total_value(current_prices: dict)` takes a dict of `{symbol: current_price}` and returns the total portfolio value as a float
- `__repr__` returns something like `Portfolio(owner='Adrian', positions=3)`
- `__len__` returns the number of positions

Bonus: add a `most_valuable(current_prices)` method that returns the symbol with the highest current value.
'''


# class Portfolio():
    
#     def __init__(self, owner_name: str):
#         self.owner_name = owner_name,
#         self.positions_list = []
        
#     def __repr__(self):
#         return f'Portfolio(owner = {self.owner_name}, positions = {len(self.positions_list)})'
    
#     def __len__(self):
#         return len(self.positions_list)
        
#     def add_position(self, symbol, qty, avg_price):
#         '''A method used to add positions'''
#         self.positions_list.append({'symbol': symbol, 'qty': qty, 'avg_price': avg_price})
    
#     def remove_position(self, symbol):
#         '''A method used to remove positions'''
#         list_of_positions_to_remove = [position for position in self.positions_list if position['symbol'] == symbol]
        
#         try:
#             self.positions_list.remove(list_of_positions_to_remove)
#         except KeyError as e:
#             print(f'There are no positions for {symbol}')
    
#     def total_value(self, current_prices: dict):
#         '''A method used to calculate the total value of our portfolio, we need a dict of symbol + current_price for that e.g.
        
#         {symbol: current_price}
#         '''
#         total_porfolio_value = sum([position['qty'] * current_prices['current_price'] for position in self.positions_list if position['symbol'] == current_prices['symbol']])
#         return total_porfolio_value
        
        
        
        
#Weekend Python review #1 T4

'''Write a generator function `drawdown_periods(prices)` that:
- Takes a list of prices (floats)
- Yields the percentage drawdown at each point from the running peak
- Drawdown = `(current - peak) / peak * 100` — will be 0 or negative

Example input: `[100, 105, 102, 98, 110, 107]`
Expected yields: `0.0, 0.0, -2.86, -6.67, 0.0, -2.73`

Then write a regular function `max_drawdown(prices)` that uses the generator to find the worst (most negative) drawdown value.
'''
# from typing import List

# def drawdown_periods(prices: List[float]):
#     peak = 0
#     for price in prices:
#         if price > peak:
#             peak = price
#         yield (price - peak) / peak * 100


# xd = [100, 105, 102, 98, 110, 107]

# print(list(drawdown_periods(xd)))


# def max_drawdown(prices):
#     dd_list = list(drawdown_periods(prices))
#     return min(dd_list)

# print(max_drawdown(xd))



#Weekend Python review #1 T5
'''
Write a decorator `validate_positive` that:
- Wraps any function
- Before the function runs, checks all numeric arguments (positional and keyword)
- Raises a `ValueError` if any numeric argument is zero or negative
- Lets non-numeric arguments pass through unchecked

Apply it to a simple function `calc_position_size(capital, risk_pct, stop_distance)` that returns `(capital * risk_pct / 100) / stop_distance`.

Test that:
- Normal call works: `calc_position_size(10000, 1.5, 2.0)` → `75.0`
- `calc_position_size(10000, 1.5, -2.0)` raises `ValueError`
- `calc_position_size(10000, 0, 2.0)` raises `ValueError`'''


# from functools import wraps


# def validate_positive(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         for arg in args:
#             if isinstance(arg, (int, float)) and arg <= 0:
#                 raise ValueError(f'All numeric values must be positive, got {arg} instead')
#         for key, val in kwargs.items():
#             if isinstance(val, (int, float)) and val <= 0:
#                 raise ValueError(f'Argument {key} should have only positive arguments, got {val}')
#         return func(*args, **kwargs)
#     return wrapper


# @validate_positive
# def calc_position_size(capital: float, risk_pct: float, stop_distance: float):
#     return (capital * risk_pct / 100 / stop_distance)

# print(calc_position_size(10000, 1.5, 2.0))
# # print(calc_position_size(10000, 1.5, -2.0))
# print(calc_position_size(10000, 0, 2.0))


#CD Python - stats - T232

'''
Zadanie
Ile kolumn z danymi numerycznymi ma średnią wartość większą od mediany?

Przypisz liczbę kolumn do zmiennej mean_wins.
'''


# import pandas as pd
# import numpy as np
# df = pd.read_csv("mini-df.csv")
# df.head()

# check_dict = dict()
# filtered_columns = []
# for column in df.columns:
#     if df[column].dtypes == 'int64' or df[column].dtypes == 'int64' == 'float64':
#         filtered_columns.append(column)

# filtered_df = df[filtered_columns]
# filtered_df.head()

# for column in filtered_df.columns:
#     mean = filtered_df[column].mean()
#     median = filtered_df[column].median()
    
#     print(mean, median)

#     if mean > median:
#         check_dict[column] = 1
#     else:
#         continue


# print(check_dict)
# mean_wins = len(check_dict)
# print(mean_wins)



#Moje rozwiazanie średnio pythoniczne, poniżej rozwiązanie Kasi

# import pandas as pd
# df = pd.read_csv("mini-df.csv")

# num_cols = df.select_dtypes(include="number").columns.tolist()

# mean_wins = 0
# for col in num_cols:
#     if df[col].mean() > df[col].median():
#         mean_wins += 1

# print(mean_wins)



#CD Python - 233

'''Aby obliczyć wariancję oraz odchylenie standardowe liczymy kwadrat różnicy, czyli dla każdego wiersza liczymy różnicę między wartością tego wiersza a średnią tej kolumny, podniesioną do kwadratu.

Stwórz dwie nowe kolumny w DataFrame df:

diff - liczącą różnicę między wartością w kolumnie price_per_m a średnią w tej kolumnie
diff_2 - liczącą kwadrat powyższej różnicy
Ile wynosi wartość największego kwadratu różnicy? Przypisz odpowiedź do zmiennej top_diff_2'''

# import pandas as pd
# pd.set_option("display.float_format", "{:.2f}".format)
# df = pd.read_csv("mini-df.csv")
# df.head()

# df['diff'] = df['price_per_m'] - df['price_per_m'].mean()
# df['diff_2'] = (df['price_per_m'] - df['price_per_m'].mean())**2

# top_diff_2 = max(df['diff_2'])
# print(top_diff_2)



#CD Python - 234

'''Zadanie
Kwadrat różnicy, który liczył(a)ś w poprzednim zadaniu tworzy wartość w dziwnej jednostce, którą ciężko interpretować. Żeby wrócić do pierwotnej jednostki kolumny używamy pierwiastkowania na końcu.

Stwórz dwie nowe kolumny w DataFrame df:

diff - liczącą różnicę między wartością w kolumnie price_per_m a średnią w tej kolumnie
diff_2 - liczącą kwadrat powyższej różnicy
Następnie oblicz:

średnią z wartości bezwzględnych kolumny diff
pierwiastek ze średniej z kolumny diff_2
Jaka jest różnica między tymi średnimi? Przypisz ją do zmiennej mad_vs_std.
'''


# import pandas as pd
# import numpy as np
# pd.set_option("display.float_format", "{:.2f}".format)
# df = pd.read_csv("mini-df.csv")
# df.head()

# df['diff'] = df['price_per_m'] - df['price_per_m'].mean()
# df['diff_2'] = (df['price_per_m'] - df['price_per_m'].mean())**2


# mad = df['diff'].abs().mean()
# std = np.sqrt(df['diff_2'].mean())

# mad_vs_std = mad - std
# print(mad_vs_std)




#CD Python - 235
'''Zadanie
Rozstęp międzykwartylowy (IQR) jest wykorzystywany do określania outlierów, czyli wartości odstających, na podstawie wzoru:

outlier < Q1 - 1.5 * IQR
outlier > Q3 + 1.5 * IQR
Narysuj boxplot na podstawie kolumny df["build_year"] i zobacz jakie wartości przyjmują outliery (narysowane na wykresie pudełkowym jako kółeczka). Następnie policz liczbę outlierów na podstawie powyższych wzorów i przypisz tę liczbę do zmiennej cnt_outliers.

Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()'''



# import matplotlib.pyplot as plt 
# import seaborn as sns

# df = pd.read_csv("mini-df.csv")
# df.head()


# boxplot_1 = sns.boxplot(
#     data = df['build_year']
# )

# plt.show()

# q1 = df['build_year'].quantile(0.25)
# q3 = df['build_year'].quantile(0.75)
# iqr = q3 - q1

# cnt_outliers = len(df[(df['build_year'] > q1 - 1.5 * iqr) & (df['build_year'] < q3 + 1.5 * iqr)])
# print(cnt_outliers)


#CD Python - 236
'''
Zadanie
Która kolumna zawiera wartości najbliższe rozkładu normalnemu?

Odpowiedź (nazwę kolumny) przypisz do zmiennej col_like_normal.

'''


# import pandas as pd
# import numpy as np
# np.random.seed(42)
# df = pd.DataFrame({"age": np.random.normal(35, 10, 1000), "salary": np.random.lognormal(10, 0.5, 1000), "transactions": np.random.poisson(8, 1000), "session_time": np.random.exponential(15, 1000), "rating": np.random.randint(1, 6, 1000), "city_population": np.random.lognormal(12, 1, 1000), "products_bought": np.random.poisson(3, 1000), "discount_pct": np.random.uniform(0, 50, 1000), "website_visits": np.random.poisson(20, 1000), "account_balance": np.random.exponential(5000, 1000)})

# fig, ax = plt.subplots(2, 5, figsize = (14, 8))
# sns.histplot(data = df, x = 'age',kde = True, ax = ax[0, 0])
# sns.histplot(data = df, x = 'salary',kde = True, ax = ax[0, 1])
# sns.histplot(data = df, x = 'transactions',kde = True, ax = ax[0, 2])
# sns.histplot(data = df, x = 'session_time',kde = True, ax = ax[0, 3])
# sns.histplot(data = df, x = 'rating',kde = True, ax = ax[0, 4])
# sns.histplot(data = df, x = 'city_population',kde = True, ax = ax[1, 0])
# sns.histplot(data = df, x = 'products_bought',kde = True, ax = ax[1, 1])
# sns.histplot(data = df, x = 'discount_pct',kde = True, ax = ax[1, 2])
# sns.histplot(data = df, x = 'website_visits',kde = True, ax = ax[1, 3])
# sns.histplot(data = df, x = 'account_balance', kde = True, ax = ax[1, 4])

# plt.show()

# col_like_normal = 'age'
# #Ja to sobie zwizualizowałem, ale w zasadzie rozwiązaniem Kasi było sprawdzenie wartości skew i kurtosis i posrotowanie


# df_stats = pd.DataFrame(columns=["col", "skew", "kurtosis"])
# for col in df.columns:
#     new_row = {
#         "col": col,
#         "skew": abs(df[col].skew()),
#         "kurtosis": abs(df[col].kurtosis())
#         }

#     df_stats.loc[len(df_stats)] = new_row

# df_stats["skew_kurtosis"] = df_stats["skew"] + df_stats["kurtosis"]
# col_like_normal = df_stats.sort_values(by = "skew_kurtosis")["col"].head(1).item()
# print(col_like_normal)


#CD Python - 237

'''Zadanie
Która kolumna zawiera rozkład najbardziej prawoskośny?

Odpowiedź (nazwę kolumny) przypisz do zmiennej top_skewed_col.'''

# import pandas as pd
# import numpy as np
# np.random.seed(42)
# df = pd.DataFrame({"age": np.random.normal(35, 10, 1000), "salary": np.random.lognormal(10, 0.5, 1000), "transactions": np.random.poisson(8, 1000), "session_time": np.random.exponential(15, 1000), "rating": np.random.randint(1, 6, 1000), "city_population": np.random.lognormal(12, 1, 1000), "products_bought": np.random.poisson(3, 1000), "discount_pct": np.random.uniform(0, 50, 1000), "website_visits": np.random.poisson(20, 1000), "account_balance": np.random.exponential(5000, 1000)})



# df_stats = pd.DataFrame(columns = ['col', 'skew'])
# for col in df.columns:
#     new_row = {
#         'col': col,
#         'skew': abs(df[col].skew())
#     }
#     df_stats.loc[len(df_stats)] = new_row

# df_stats = df_stats.sort_values(by = 'skew', ascending = False)
# print(df_stats)
# top_skewed_col = df_stats['col'].head(1).item()



#CD Python - 238
'''
Zadanie
Wspominałam podczas lekcji, że rzadko możemy spotkać rozkład normalny w danych niebiologicznych.

Czy są jakieś zmienne w dataframe df, które mają rozkład normalny?

Przypisz odpowiedź True / False do zmiennej is_anything_normal
'''

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("mini-df.csv")
# df.head()

# numeric_cols = [col for col in df.select_dtypes(include='number')]

# normals = []
# for col in numeric_cols:
#     skew = abs(df[col].skew())
#     kurtosis = abs(df[col].kurtosis())
#     both_sum = skew + kurtosis
#     normals.append({col: both_sum})

# print(normals)

# is_anything_normal = False



#CD Python - 239
'''
Jak nazywa się rozkład, który opisuje zmienną df["separate_kitchen"]?

Wybierz pośród poniższych wartości i przypisz nazwę rozkładu do zmiennej distribution:

normalny
jednostajny
wykladniczy
log-normalny
bernoulliego
dwumianowy
poisson
'''


# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# df = pd.read_csv("mini-df.csv")
# df.head()

# plot = sns.histplot(data = df, x = 'separate_kitchen', kde = True)
# plt.show()

# distribution = 'bernoulliego'



#CD Python - 240

'''Która z poniższych zmiennych charakteryzuje się największym rozproszeniem?
Przypisz nazwę kolumny do zmiennej top_dispersion.
'''

'''
Aby porównywać rozproszenie między RÓŻNYMI zmiennymi, musimy wybrać metrykę rozproszenia,
która nie jest zależna od jednostki badanych zmiennych - sięgamy zatem po współczynnik zmienności.

Nie chcemy np. porównywać rozkładu międzykwartylowego, który dla kolumny price przyjmuje wartości w złotówkach,
a area w metrach kwadratowych.

Ponieważ badane zmienne nie mają rozkładu normalnego, sięgamy po pozycyjny współczynnik zmienności.'''

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("mini-df.csv")
# df.head()

# filtered_df = df[["area", "price", "floor_no", "latitude", "longitude"]]
# col_disp = {col:0 for col in filtered_df.columns}

# for col in filtered_df.columns:
#     q1 = df[col].quantile(0.25)
#     q3 = df[col].quantile(0.75)
#     col_disp[col] = (q3 - q1) / (q3 + q1)

# top_dispersion = sorted(col_disp.items(), key = lambda x: x[1], reverse = True)[0][0]
# print(top_dispersion)


#CD Python - 241

'''
Chociaż nie jestem fanką wynajdowania koła na nowo i uważam, 
że w normalnych warunkach zawsze powinniśmy korzystać z gotowych funkcji, 
to dla celów edukacyjnych czasami warto przejść przez obliczenia "ręcznie", krok po kroku,
żeby dokładnie zrozumieć jak coś działa.

Policz krok po kroku odchylenie standardowe dla kolumny df["price"] nie korzystając z metody lub funkcji std.
Wynik zaokrąglony do dwóch cyfr po przecinku przypisz do zmiennej price_std.
'''

# import pandas as pd
# import numpy as np

# df = pd.read_csv("mini-df.csv")
# df.head()

# df['diff_squared'] = (df['price'] - df['price'].mean())**2 #najpierw liczymy odchylenie od sredniej podniesione do kwadratu dla kazdej wartosci
# wariancja = sum(df['diff_squared'])/(len(df)-1) #wariancja to suma kwadratow odchylen podzielona przez dlugosc zbioru-1
# price_std = np.sqrt(wariancja) #odchylenie standardowe to pierwiastek z wariancji
# print(price_std)


#CD Python - 242

'''
Zadanie
Rozkład normalny opisują dwa parametry.

Przypisz te parametry (zaokrąglone do 2 cyfr po przecinku) na podstawie wartości s do zmiennej par_1 i par_2.
'''

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# s = pd.Series([42]*2 + [43]*4 + [44]*8 + [45]*12 + [46]*18 + [47]*24 + [48]*30 + [49]*35 + [50]*35 + [51]*30 + [52]*30 + [53]*24 + [54]*18 + [55]*12 + [56]*8 + [57]*4 + [58]*2 + [59])
# sns.histplot(s, bins=17, kde=True)
# plt.show()


# #WAŻNE, BO TU SIĘ POMYLIŁEM
# #ROZKŁADU NORMALNEGO NIE OPISUJĄ SKEW() I KURTOSIS() - oczywistym jest, że będą bliskie 0
# #Rozkład normalny opisują średnia i ochylenie standardowe
# #Średnia określa, gdzie jest środek rozkładu na osi X
# #Std określa jak bardzo rozproszony jest rozkład

# par_1 = round(s.mean(), 2)
# par_2 = round(s.std(), 2)
# print(par_1, par_2)


#CD Python - 243

'''
Zadanie
Przekształć dane zapisane w zmiennej s tak, aby ich rozkład był bardziej zbliżony do rozkładu normalnego. 
Użyj jednej operacji matematycznej i przypisz wynik do zmiennej s_transformed.
'''

#w przypadku rozkładu lognormal, zmienia się on w rozkład normalny po zamianie wartości w logarytmy


# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# np.random.seed(42)

# s = pd.Series(
#     np.random.lognormal(mean=2, sigma=0.6, size=1000)
# )
# fg = sns.histplot(s)
# plt.show()


# s_transformed = np.log(s)
# fg = sns.histplot(s_transformed)
# plt.show()



#CD Python - 244
'''
Zadanie
Zobacz czy wartości w zmiennej s mają rozkład normalny na zasadzie reguły 68-95-99.7.
Jeżeli odchylenie jest +- 1.5 punkta procentowego, traktuj to jako rozkład normalny.

Przypisz odpowiedź True / False do zmiennej is_normal.
'''

# import pandas as pd
# import numpy as np

# s = pd.Series([42, 45, 48, 50, 52, 55, 58, 60, 62, 64, 66, 68, 70, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 90, 91, 91, 92, 92, 93, 93, 94, 94, 95, 95, 96, 96, 97, 97, 98, 98, 99, 99, 100, 100, 100, 100, 101, 101, 102, 102, 103, 103, 104, 104, 105, 105, 106, 106, 107, 107, 108, 108, 109, 109, 110, 110, 111, 111, 112, 112, 113, 113, 114, 114, 115, 115, 116, 116, 117, 117, 118, 118, 119, 120, 121, 122, 123, 124, 125, 126, 128, 130, 132, 134, 136, 138, 140, 142, 145, 148, 150, 152, 155, 158, 162])

# min_s = s.mean() - s.std() #średnia wartość od której odejmujemy 1std
# max_s = s.mean() + s.std() #i dodajemy 1std

# #następnie sprawdzamy jaką długość całego zbioru stanowią wartości,
# #które zawierają się w zakresie między średnią a 1 std
# print(len(s[(s > min_s) & (s < max_s)]) / len(s)) #0.71


# min_s = s.mean() - 2*s.std() #a tutaj 2std
# max_s = s.mean() + 2*s.std() 
# print(len(s[(s > min_s) & (s < max_s)]) / len(s)) #0.93


# min_s = s.mean() - 3*s.std() #i 3std
# max_s = s.mean() + 3*s.std()
# print(len(s[(s > min_s) & (s < max_s)]) / len(s)) #1.0

# #Nie do końca odpowiada to regule 68-95-99,7 i nie mieścimy się w przyjętej granicy tolerancji 1.5pp)
# is_normal = False


#CD Python - 245

'''
Porównaj która grupa (df["group"]) ma największe rozproszenie danych.
Wszystkie grupy mają wartości z rozkładu normalnego, ale są opisane w różnych jednostkach.

Przypisz nazwę grupy z największym rozproszeniem do zmiennej top_dispersion_group.
'''

# import pandas as pd
# import numpy as np
# np.random.seed(42)
# df = pd.DataFrame({"group": ["A"]*100 + ["B"]*100 + ["C"]*100 + ["D"]*100, "value": np.r_[np.random.normal(5, 1, 100), np.random.normal(50, 10, 100), np.random.normal(1500, 200, 100), np.random.normal(600000, 80000, 100)]})

# dispersion_df = pd.DataFrame(columns = ('group', 'dispersion'))
# groups = df['group'].unique().tolist()

# for group in groups:
#     filtered_df = df[df['group'] == group]
#     q1 = filtered_df['value'].quantile(0.25)
#     q3 = filtered_df['value'].quantile(0.75)
#     cv = (q3 - q1) / (q3 + q1)
#     print(cv)
    
#     new_row = {
#         'group': group,
#         'dispersion': cv
#     }

#     dispersion_df.loc[len(dispersion_df)] = new_row

# top_dispersion_group = dispersion_df.sort_values(by = 'dispersion', ascending = False).head(1).values.tolist()[0][0]
# print(top_dispersion_group)


#CD Python - 246


'''
Jak nazywa się rozkład, który opisuje zmienną s?

Wybierz pośród poniższych wartości i przypisz nazwę rozkładu do zmiennej distribution:

normalny
jednostajny
wykladniczy
log-normalny
bernoulliego
dwumianowy
poisson
'''


# import pandas as pd
# import matplotlib.pyplot as plt

# s = pd.Series([0.1, 0.2, 0.2, 0.3, 0.3, 0.4, 0.4, 0.5, 0.5, 0.6, 0.6, 0.7, 0.8, 0.8, 0.9, 1.0, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.3, 3.7, 4.1, 4.6, 5.2, 5.9, 6.7, 7.6, 8.7, 10.0, 12.0])

# plt.hist(s)
# plt.show()

# distribution = 'wykladniczy'


#CD Python - 247

'''
Dataframe df zawiera informacje o zgłoszeniach do działu obsługi klienta.

Twoim zadaniem jest:

stworzyć histogram, który pokazuje rozkład liczby zgłoszeń na każdą godzinę
przypisać nazwę powstałego rozkładu do zmiennej distribution
przypisać do zmiennej cnt_params ile parametrów opisuje powyższy rozkład
Nazwę rozkładu wybierz pośród poniższych wartości:

normalny
jednostajny
wykladniczy
log-normalny
bernoulliego
dwumianowy
poisson1600
'''

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# np.random.seed(42)

# hours = pd.date_range("2025-01-01", periods=24*30, freq="h")
# rows = []
# ticket_id = 1
# for dt, cnt in zip(hours, [7, 9, 8, 6, 10, 11, 5, 8, 9, 7, 6, 12, 8, 7, 9, 10, 6, 8, 7, 9, 11, 5, 8, 7] * 30):
#     for _ in range(cnt):
#         rows.append([
#             ticket_id,
#             dt + pd.Timedelta(minutes=np.random.randint(0, 60)),
#             np.random.choice([
#                 "Login issue",
#                 "Payment failed",
#                 "Bug report",
#                 "Feature request",
#                 "Password reset"
#             ])
#         ])
#         ticket_id += 1
# df = pd.DataFrame(rows, columns=["ticket_id", "created_at", "description"])
# df['hour'] = df['created_at'].dt.hour

# hist_plot = sns.histplot(
#     data = df,
#     x = 'hour'
# )
# plt.show()

# distribution = 'poisson'
# cnt_params = 1


#CD Python - 248

'''
Czy średnie w grupach A i B różnią się istotnie statystycznie według testu t-Studenta?
Przyjmijmy poziom istotności 0.05.

Przypisz odpowiedź True / False do zmiennej is_different.
'''
# from scipy.stats import ttest_ind
# group_a = [48, 52, 55, 57, 58, 59, 60, 61, 62, 64, 65, 67, 69, 71, 74]
# group_b = [53, 56, 58, 60, 61, 63, 65, 66, 67, 69, 70, 72, 74, 76, 79]

# test_results = ttest_ind(group_a, group_b)
# print(test_results)
'''TtestResult(statistic=np.float64(-1.667572025484055),
pvalue=np.float64(0.10654853467007974), df=np.float64(28.0))'''
#We adapt the 0.05 as the significance level

# is_different = False


#CD Python - 249
'''Wynik testu t-Studenta zależy od wielkości próby: im większa próba, 
tym łatwiej wykryć nawet niewielkie różnice między grupami. 
Porównaj statystycznie dwie grupy, z których każda zawiera po 150 obserwacji.

Czy średnie w grupach A i B różnią się istotnie statystycznie według testu t-Studenta? 
Przyjmijmy poziom istotności 0.05.

Przypisz odpowiedź True / False do zmiennej is_different.'''

# import numpy as np
# np.random.seed(42)
# group_a = np.round(np.random.normal(60, 8, 150)).astype(int)
# group_b = np.round(np.random.normal(65, 8, 150)).astype(int)

# print(ttest_ind(group_a, group_b))
'''TtestResult(statistic=-6.768457931422672, pvalue=6.911415201784208e-11, df=298.0)'''
#We adapt the 0.05 as the significance level

# is_different = True #this time the p-value is very low, so we have to reject the zero hypothesis
#Zero hypothesis is obvious here: there's no difference between the groups.


#CD Python - 250
'''
Czy istnieje istotna statystycznie różnica między grupami A i B?
Grupy nie mają rozkładu normalnego, użyj nieparametrycznego odpowiednika testu t-Studenta.
Przyjmijmy poziom istotności 0.05.

Przypisz odpowiedź True / False do zmiennej is_different.
'''

# from scipy.stats import mannwhitneyu

# group_a = [2, 3, 4, 4, 5, 5, 6, 7, 8, 10, 12, 15, 20, 28, 45]
# group_b = [3, 4, 5, 6, 7, 8, 10, 12, 14, 18, 22, 30, 40, 55, 80]

# print(mannwhitneyu(group_a, group_b)) 
# #We adapt the 0.05 as the significance level
# '''MannwhitneyuResult(statistic=np.float64(79.0), pvalue=np.float64(0.1704021390871755))'''
# #We interpret it in the same way as t-test, the p-value is above the significance level,
# #which means we cannot negate the zero hypothesis = there's no difference

# is_different = False


#CD Python - 251
'''Czy rozkład zmiennej df["x"] jest rozkładem normalnym? 
Przyjmij poziom istotności 0.05.

Przypisz True / False do zmiennej is_normal.
'''

# import pandas as pd
# import numpy as np
# np.random.seed(42)

# df = pd.DataFrame({"x": np.concatenate([np.random.normal(100, 15, 950),np.random.normal(180, 10, 50)])})

# #zero hypothesis: data comes from normal distribution

# from scipy.stats import normaltest
# _, pvalue = normaltest(df["x"])
# print(_, pvalue) #372.47783624941746, 1.310586055533558e-81

# #the value is way below the 0.05 significance level
# #it's obvious that data does not come from the normal distribution, we reject the zero hypothesis

# is_normal = False


#CD Python - 252
'''
Czy różnica w cenie za metr dla rynku pierwotnego i wtórnego jest istotna statystycznie?
Przyjmijmy poziom istotności 0.05.

Przypisz odpowiedź True / False do zmiennej is_different.
'''

# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# df.head()

# from scipy.stats import normaltest
# pri = df["price_per_m"][df["market_type"]=="primary"]
# sec = df["price_per_m"][df["market_type"]=="secondary"]

# _, p_value = normaltest(pri) #normal?
# print(_, p_value)
# _, p_value = normaltest(sec) #not normal
# print(_, p_value)

# '''
# 1.9309194820569853 0.38080808638773117 - normal?
# 7.0602866163771125 0.02930071653353869 - not normal
# '''

# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.histplot(pri)
# plt.show()

# sns.histplot(sec)
# plt.show()


# from scipy.stats import mannwhitneyu
# alpha = 0.05
# _, pvalue = mannwhitneyu(pri, sec)
# is_different = pvalue < alpha
# '''963.0 0.20858352442836026'''

# print(is_different) #False


#CD Python - 253
'''
Sprawdź, czy średnia cena za metr kwadratowy różni się istotnie statystycznie
pomiędzy poszczególnymi typami budynków (build_type).
Przyjmij poziom istotności równy 0.05.

Następnie przypisz do listy different_pairs wszystkie pary typów budynków,
dla których różnica jest istotna statystycznie. Wybierz wartości z poniższej listy:

apartment-tenement
apartment-block
tenement-block
'''

# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# df.head()

# block = df["price_per_m"][df["build_type"]=="block"]
# apartment = df["price_per_m"][df["build_type"]=="apartment"]
# tenement = df["price_per_m"][df["build_type"]=="tenement"]

# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.histplot(block)
# plt.show()

# sns.histplot(apartment)
# plt.show()

# sns.histplot(tenement)
# plt.show()

# #rozkłady nie są normalne

# from scipy.stats import kruskal
# kruskal_test = kruskal(block, apartment, tenement)
# print(kruskal_test)

# '''KruskalResult(statistic=28.595066180957456, pvalue=6.175331470333519e-07)'''
# #We can clearly see that there is at least one different group, so it's time to check the differences

# from scikit_posthocs import posthoc_dunn
# x = posthoc_dunn(
#     df[df['build_type'].isin(['block', 'apartment', 'tenement'])],
#     val_col = 'price_per_m',
#     group_col = 'build_type'
# )

# print(x)
# '''
#            apartment     block  tenement
# apartment   1.000000  0.000003  0.908663
# block       0.000003  1.000000  0.000128
# tenement    0.908663  0.000128  1.000000
# '''

# different_pairs = ['apartment-block', 'tenement-block']




#CD Python - 254
'''
Zobacz, jaki wpływ na wynik testu statystycznego ma odchylenie standardowe,
czyli to, jak bardzo rozkłady nachodzą na siebie.

Mamy dwie grupy po 20 obserwacji każda. Obie pochodzą z rozkładu normalnego:

grupa A ma średnią 60
grupa B ma średnią 63
Sprawdź, jak zmienia się wartość p wraz ze zmniejszaniem odchylenia standardowego.

Zmniejszaj odchylenie standardowe o 1, zaczynając od wartości 10, i znajdź pierwszą wartość,
dla której różnica między grupami stanie się istotna statystycznie przy poziomie istotności 0.05.

Przypisz tę wartość do zmiennej std_stats.
'''


# import numpy as np
# from scipy.stats import ttest_ind

# std = 10

# # przy zmianie std zawsze uruchamiaj w każdej iteracji poniższy fragment kodu:
# rng = np.random.default_rng(42)
# base_a = rng.normal(0, 1, 20)
# base_b = rng.normal(0, 1, 20)
# group_a = 60 + base_a * std
# group_b = 63 + base_b * std
# # koniec fragmentu

# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.kdeplot(group_a)
# sns.kdeplot(group_b)
# plt.show()

# std_stats = 0
# for i in range(10, 1, -1):
#     std = i

#     rng = np.random.default_rng(42)
#     base_a = rng.normal(0, 1, 20)
#     base_b = rng.normal(0, 1, 20)
#     group_a = 60 + base_a * std
#     group_b = 63 + base_b * std

#     p_value = ttest_ind(group_a, group_b)[1]
#     if p_value < 0.05:
#         std_stats = i
#         break
 
# print(std_stats) #7
# sns.kdeplot(group_a) 
# sns.kdeplot(group_b)
# plt.show()



# import pandas as pd

# df = pd.read_csv('project1_phones_sales_analytics/data/price_history_full.csv')
# launch_ref = pd.read_csv('project1_phones_sales_analytics/data/official_launch_prices.csv')
# # small sample: 500 rows per brand
# df = df.groupby('brand').sample(n=500, random_state=42).reset_index(drop=True)
# df = df.merge(launch_ref, on = 'submodel_name')

# print(df.shape)
# print(df['brand'].value_counts())
# print(df.head())

#W7 D3 - Pandas practice T4
'''
Given a DataFrame with columns `['brand', 'submodel_name', 'price_pct_of_launch']`, find:
- The submodel with the highest average `price_pct_of_launch` per brand
- The submodel with the lowest average per brand

One line per brand, value is the tier name.
'''

# df = df[df['new_price'].notna()]
# df['new_price'] = df['new_price'] * 100
# df['price_pct_of_launch'] = round(df['new_price'] / df['official_launch_price'] * 100, 2)

# df_submodels_avg_prices = df.groupby(['brand', 'submodel_name'])['price_pct_of_launch'].mean().reset_index()

# df_submodels_top_model = df.groupby(['brand', 'submodel_name'])['price_pct_of_launch'].mean().idxmax()
# df_submodels_worst_model = df.groupby(['brand', 'submodel_name'])['price_pct_of_launch'].mean().idxmin()


#T5 
'''
Given the same data:
- What is the average `price_pct_of_launch` for Samsung's Ultra tier specifically?
- Extract it as a single float, not a DataFrame or Series
'''

# filtered_df = df[(df['brand'] == 'Samsung') & (df['submodel_name'].str.contains('Ultra'))]
# print(filtered_df.head())
# avg_price = filtered_df['price_pct_of_launch'].mean()
# print(avg_price)

# acg_price = filtered_df


#T6
'''
Task 6 — rank() within groups

Add a new column `retention_rank` that ranks each tier within its brand by average `price_pct_of_launch`, 
from highest (rank 1) to lowest. 

The result stays in a DataFrame — one row per brand+tier combination.
'''



# df['retention_rank'] = df.groupby(['brand', 'generation_name'])['price_pct_of_launch'].transform('rank', ascending = False)
# df = df.sort_values(by = 'retention_rank', ascending = True)
# print(df.head())




#CD Python - 255 

'''
Zadanie
Zobacz, jaki wpływ na wynik testu statystycznego ma liczebność.

Mamy dwie grupy, obie pochodzą z rozkładu normalnego i mają odchylenie standardowe 10:

grupa A ma średnią 60
grupa B ma średnią 63
Sprawdź, jak zmienia się wartość p wraz ze zwiększaniem liczebności (n).

Zwiększaj liczebność każdej grupy o 10, zaczynając od wartości 10, i znajdź pierwszą wartość n,
dla której różnica między grupami stanie się istotna statystycznie przy poziomie istotności 0.05.

Przypisz tę wartość do zmiennej n_stats.
'''

# import numpy as np
# from scipy.stats import ttest_ind

# n = 10

# # przy zmianie liczebności zawsze uruchamiaj w każdej iteracji poniższy fragment kodu:
# rng = np.random.default_rng(42)
# base_a = rng.normal(0, 1, 100)
# base_b = rng.normal(0, 1, 100)
# group_a = 60 + base_a[:n] * 10
# group_b = 63 + base_b[:n] * 10
# # koniec fragmentu

# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.kdeplot(group_a)
# sns.kdeplot(group_b)
# plt.show()

# n_stats = 0

# for i in range(10, 500, 10):
#     n = i

#     rng = np.random.default_rng(42)
#     base_a = rng.normal(0, 1, 100)
#     base_b = rng.normal(0, 1, 100)
#     group_a = 60 + base_a[:n] * 10
#     group_b = 63 + base_b[:n] * 10

#     p_value = ttest_ind(group_a, group_b)[1]
#     print(p_value)

#     if p_value < 0.05:
#         print(f'p_value {p_value} is statistically significant with n = {n}')
#         n_stats = n
#         break


#CD Python - 256 
'''
Zadanie
Centralne Twierdzenie Graniczne (ang. Central Limit Theorem, CLT) mówi, 
że średnie z wielu próbek zaczynają przypominać rozkład normalny, nawet jeśli oryginalne dane mają inny rozkład.

W df mamy ocenę rating czatów prowadzonych przez agentów działu obsługi klienta.

Zobacz jaki rozkład ma ta cecha, a następnie policz średnią ocenę dla każdego agenta
i zobacz jak zmienia się rozkład.

Przeprowadź normaltest dla średnich ocen agentów
i na jego podstawie przypisz wartość True/False do zmiennej is_normal.
Jeżeli rozkład jest normalny na poziomie istotności 0.05, przypisz wartość True.
'''

# import pandas as pd
# import numpy as np
# from scipy.stats import normaltest
# import seaborn as sns
# import matplotlib.pyplot as plt
# np.random.seed(42)

# df = pd.DataFrame({"ticket_id": range(1, 301), "agent": np.random.choice([f"agent_{i}" for i in range(1, 16)], size=300), "rating": np.random.choice([1, 2, 3, 4, 5], size=300, p=[0.02, 0.03, 0.05, 0.20, 0.70])})
# df.head()

# global_avg_rating = df['rating'].mean()
# print(global_avg_rating)
# rating_distribution = sns.histplot(
#     df['rating']
# )
# plt.show()


# agent_df = df["rating"].groupby(df["agent"]).mean() 
'''
there was a trap of using transform to add mean to each agent to the origianl df here, which I've done at the begininning
It altered the results as each mean value was then recalculated and aggregated, which changed the mean
'''

# sns.histplot(agent_df)
# plt.show()

# is_normal = normaltest(agent_df)[1] > 0.05
# print(is_normal)


#CD Python - 257

'''
Studenci podchodzili do testu z języka hiszpańskiego przed i po kursie. 
Użyj odpowiedniego testu statystycznego i zobacz czy ich wynik po kursie się zmienił. 
Przypisz wartość p z tego testu do zmiennej p_value.

'''


# import pandas as pd
# from scipy.stats import normaltest, ttest_rel

# df = pd.DataFrame({"student_id":[7,2,10,4,1,8,3,6,9,5,2,7,1,10,4,9,8,5,3,6],"score":[44,55,47,61,42,52,38,57,60,49,68,57,58,60,74,73,65,61,52,70],"created_at":pd.to_datetime(["2025-01-10","2025-01-10","2025-01-10","2025-01-10","2025-01-10","2025-01-10","2025-01-10","2025-01-10","2025-01-10","2025-01-10","2025-03-20","2025-03-20","2025-03-20","2025-03-20","2025-03-20","2025-03-20","2025-03-20","2025-03-20","2025-03-20","2025-03-20"])})
# df.head(15)

# before_test = df[df['created_at'] < '2025-03-20'].sort_values('student_id')['score'] #VERY IMPORTANT - for this t-test we must sort data
# after_test = df[df['created_at'] >= '2025-03-20'].sort_values('student_id')['score']

# normal_test1 = normaltest(before_test['score']) #0.6 - normal distribution
# normal_test2 = normaltest(after_test['score']) #0.63 - nromal distribution
# print(normal_test1, normal_test2)

# _, p_value = ttest_rel(before_test['score'], after_test['score'])
# print(_, p_value) #p_value bliskie zeru, czyli chyba się nie zmienił, nie można odrzucić hipotezy zerowej
# #-39.701983889378575 2.029761902012733e-11


#CD Python - 258

'''
Głównym problemem testów statystycznych jest to, że zawsze zwrócą jakiś wynik,
nawet jeśli ich założenia nie są spełnione.

To od osoby przeprowadzającej testy zależy, czy przed ich wykonaniem sprawdzi poprawność zastosowania.

Zobacz, jak wyglądają rozkłady w grupach A i B. Następnie wykonaj test parametryczny oraz test nieparametryczny i porównaj ich wyniki.

Przypisz do zmiennych odpowiedź True, jeżeli mamy dowody, by odrzucić hipotezę zerową:

dla testu parametrycznego: param_stats
dla testu nieparametrycznego: non_param_stats
W innym przypadku przypisz False.

Przyjmij poziom istotności 0.05.
'''

# import numpy as np
# from scipy.stats import normaltest, ttest_ind, mannwhitneyu
# import seaborn as sns
# import matplotlib.pyplot as plt

# group_a = np.array([10] * 30 + [1000] * 3)
# group_b = np.array([20] * 33)

# # x = normaltest(group_a) #tu się udaje, przy drugiej grupie nie

# # plot1 = sns.kdeplot(group_a)
# # plt.show()
# # plot2 = sns.kdeplot(group_b)
# # plt.show()

# t_test = ttest_ind(group_a, group_b)
# print(t_test)
# param_stats = ttest_ind(group_a, group_b)[1] < 0.05

# mann_w = mannwhitneyu(group_a, group_b)
# non_param_stats =  mannwhitneyu(group_a, group_b)[1] < 0.05

# print(param_stats, non_param_stats)
#p-value = jak prawdopodobne byłoby zaobserwaoanie takich (lub bardziej ekstremalnych) danych
#gdyby hipoteza zerowa była prawdziwa

#jeśli wartość p jest mała to znaczy, że dane byłyby bardzo nietypwoe
#oznacza to, że obserwowana różnica między grupami prawdopoddobnie nie jest dziełem przypadku
#oznacza to, że możemy odzrzucić hipotezę zerową

#Hipoteza zerowa: Nie ma rzeczywistej różnicy/efektu, nic się nie dzieje.


#CD Python - 259

'''
Istotność statystyczna nie mówi, czy różnica między grupami jest duża lub ważna z biznesowego punktu widzenia.
Świadczy jedynie o tym, że zaobserwowana różnica prawdopodobnie nie wynika z losowego przypadku.

W tym zadaniu:

narysuj jeden wykres KDE plot z dwoma grupami
oblicz statystykę testu t Studenta i przypisz wartość p do zmiennej p_value
przypisz do zmiennej mean_diff bezwzględną różnicę między średnimi w obu grupach, zaokrągloną do 2 cyfr po przecinku

'''

# import numpy as np
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# from scipy.stats import ttest_ind

# np.random.seed(42)

# group_a = np.random.normal(100, 10, 5000)
# group_b = np.random.normal(101, 10, 5000)

# df = pd.DataFrame({
#     "group": ["A"] * 5000 + ["B"] * 5000,
#     "score": np.concatenate([group_a, group_b])
# })
# df.head()

# kde_plot = sns.kdeplot(
#     df,
#     x = 'score',
#     hue = 'group'
# )

# ttest = ttest_ind(group_a, group_b)
# print(ttest) #TtestResult(statistic=-4.211541023064685, pvalue=2.5585752137847796e-05, df=9998.0)
# mean_diff = round(abs(np.mean(group_a) - np.mean(group_b)), 2)
# print(mean_diff) #0.85 



#CD Python - 260
'''
Aby określić istotność biznesową możemy użyć miary wielkości efektu,
np. miara d Cohena pozwala określić siłę efektu dla porównywania średnich.
Sprawdza ona o ile odchyleń standardowych różnią się średnie dwóch grup - im mniejsza miara, tym rozkłady są bliżej.

Najczęstsza interpretacja d Cohena:

d = 0.2  → mały efekt
d = 0.5  → średni efekt
d = 0.8  → duży efekt
Oblicz wartość d Cohena dla grup używanych w poprzednim zadaniu na podstawie wzoru:

d = abs(średnia 1. grupy - średnia 2. grupy) / std
Przyjmij wartość std = 10.

Przypisz wartość d Cohena do zmiennej d. Zaokrąglij do 2 cyfr po przecinku.
'''

# import numpy as np
# import pandas as pd
# np.random.seed(42)

# group_a = np.random.normal(100, 10, 5000)
# group_b = np.random.normal(101, 10, 5000)

# d = round(abs(group_a.mean() - group_b.mean()) / 10, 2) #tutaj przyjmujemy STD jako 10
# print(d)


#W7 D4 - T1 + T2
'''
Yesterday you used `submodel_name` instead of `tier` because you forgot the lambda. Fix it.

Goal: one row per brand, showing which tier has the highest average price_pct_of_launch and which has the lowest.
'''


import pandas as pd

df = pd.read_csv('project1_phones_sales_analytics/data/price_history_full.csv')
launch_ref = pd.read_csv('project1_phones_sales_analytics/data/official_launch_prices.csv')
# small sample: 500 rows per brand
df = df.groupby('brand').sample(n=500, random_state=42).reset_index(drop=True)
df = df.merge(launch_ref, on = 'submodel_name')

df['tier'] = df.apply(lambda row: row['submodel_name'].replace(row['generation_name'], '').strip(), axis = 1)
df['tier'] = df['tier'].replace('', 'Base')


df = df[df['new_price'].notna()]
df['new_price'] = df['new_price'] * 100
df['price_pct_of_launch'] = round(df['new_price'] / df['official_launch_price'] * 100, 2)


best_prices_by_tier = df.groupby(['brand', 'tier'])['price_pct_of_launch'].mean().groupby('brand').idxmax().str[1]
worst_prices_by_tier = df.groupby(['brand', 'tier'])['price_pct_of_launch'].mean().groupby('brand').idxmin().str[1]
print(best_prices_by_tier)
print(worst_prices_by_tier)
check_prices_by_tier = df.groupby(['brand', 'tier'])['price_pct_of_launch'].mean()
print(check_prices_by_tier)

# #W7 D4 - T3
'''`transform('rank')` ranks individual rows within a group, not per-tier averages. 
Your output had one rank per row, not one per tier. The correct approach: aggregate first, then rank.
'''

tier_avg = df.groupby(['brand', 'tier'])['price_pct_of_launch'].mean().reset_index()
tier_avg['retention_rank'] = tier_avg.groupby('brand')['price_pct_of_launch'].rank(ascending=False)

df = df.merge(tier_avg, on = ['brand', 'tier'])


#CD Python - 261

'''
Sprawdź, czy średnia wartość w grupie group różni się istotnie statystycznie od 35. 
Przyjmij poziom istotności 0.05. 

Przypisz wartość True lub False do zmiennej is_different.
'''


# from scipy.stats import ttest_1samp

# group = [29, 31, 32, 33, 34, 35, 36, 37, 38, 41]

# p_value = ttest_1samp(group, 35)[1] #tutaj ttest 1samp (porównanie średniej grupy z próbką albo oczekiwaną wartością średniej)
# is_different = p_value < 0.05 #False
# print(p_value) #0.73
# print(is_different) #False


#CD Python - 262

'''
W teście jednostronnym łatwiej uzyskać istotność statystyczną, 
ponieważ od początku zakładamy konkretny kierunek efektu i szukamy dowodów tylko na jego potwierdzenie. 

Jeżeli chcemy sprawdzić, czy grupa B osiąga wyższe wyniki niż grupa A, nie interesuje nas sytuacja odwrotna.
Dzięki temu cały „budżet błędu” (poziom istotności α) jest przeznaczony na wykrycie różnicy w jednym kierunku.

W teście dwustronnym musimy natomiast uwzględnić dwa możliwe scenariusze: 
że grupa B ma wyniki wyższe lub niższe od grupy A. 

Kryterium odrzucenia hipotezy zerowej jest więc bardziej rygorystyczne,
ponieważ dowody muszą być wystarczająco silne niezależnie od kierunku różnicy.

Przeprowadź jednostronny test t-Studenta sprawdzający, czy grupa B ma większą średnią niż grupa A.
Odpowiedź jako True / False przypisz do zmiennej b_is_greater. Przyjmij poziom istotności 0.05.
'''


# from scipy.stats import ttest_ind

# group_a = [50, 51, 52, 50, 52, 47, 50, 51, 49, 52]
# group_b = [52, 53, 50, 51, 54, 49, 52, 53, 51, 52]

# _, p_value = ttest_ind(group_a, group_b, alternative = 'less') #chcemy sprawdzić, cz B ma większą średnią
# #używamy tu argumentu 'less' sprawdzając, czy srednia a jest mniejsza od b, bo tak są w kolejności
# print(p_value) #0.0373 - hipotezę zerową można odrzucić

# b_is_greater = True


#CD Python - 263

'''
Aby obliczyć moc testu t-Studenta możemy użyć funkcji TTestIndPower.

Równanie na moc testu możemy także wykorzystać przy obliczeniu jakich liczebności
potrzebujemy przy założonej wielkości efektu, poziomie istotności i mocy.

Zobacz jak zmieni się sample_size, gdy zmienisz wielkość efektu na 0.5.

Zanim uruchomisz kod, zastanów się - sądzisz, że liczebność pójdzie w górę, czy w dół?
'''

# import numpy as np
# from statsmodels.stats.power import TTestIndPower

# effect_size = 0.5
# alpha = 0.05
# power = 0.8

# sample_size = np.ceil(
#     TTestIndPower().solve_power(
#         effect_size=effect_size,
#         alpha=alpha,
#         power=power,
#         alternative="two-sided"
#     )
# )

# print(sample_size)


#sample size wyraźnie maleje wraz ze wzrostem siły efektu



#CD Python - 264

'''
Przeprowadź testy statystyczne, aby sprawdzić, czy kwoty (amount)
różnią się istotnie statystycznie między poszczególnymi miesiącami zamówień.

Wykonaj analizę krok po kroku:

Sprawdź normalność grup
Wybierz odpowiedni test
Przeprowadź dodatkowe testy post hoc, jeżeli jest taka potrzeba.
Przypisz do zmiennej months_different liczbę par miesięcy, które różnią się istotnie statystycznie.

Przykład: jeżeli jest taka różnica w styczniu-lutym i styczniu-marcu:

months_different = 2
Przyjmij poziom istotności 0.05.

Wskazówka
Możesz przypisać wartości kwot poszczególnych miesięcy do list w liście,
a następnie przekazać tę listę jako argument do funkcji testu używając znaku *:

groups = [[1,2,3], [3,4,5]]
test(*groups)
'''

# import pandas as pd
# from scipy.stats import normaltest, kruskal

# df = pd.read_csv("orders.csv")

# df.dtypes
# df['month'] = pd.to_datetime(df['order_date']).dt.month
# df.head()

# #testy na normalnosc normaltestem
# for i in range(1, 13):
#     tested_group = df['amount'][df['month'] == i]
#     test_result = normaltest(tested_group)[1]
#     print(f'Month {i} results: {test_result}')
# #March dataset is too small, April,  August and October are below the p-value as non-normal
# #czyli ANOVA odpada, musimy zrobić test Kruskal

# groups = []
# for month in df["month"].unique():
#     groups.append(df["amount"][df["month"]==month].values.tolist())
# print(groups)

# alpha = 0.05
# p_value = kruskal(*groups)
# print(p_value) #p_value powyzej 0.05, hipoteza zerowa zostaje, nei ma roznic miedzy srednimi miesiecy

# months_different = 0


#CD Python - 265

'''
Zadanie
Czy jest relacja między ceną, a ceną za metr?
Ile wynosi współczynnik korelacji Pearsona dla zależności między ceną, a ceną za metr?

Odpowiedź przypisz do zmiennej corr.
'''

# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# df.head()

# corr = df['price'].corr(df['price_per_m'])
# print(corr)

#CD Python - 266

'''
Zadanie
Czy istnieje zależność między datą (df["date"]), a ceną za metr?
Mając kolumnę z datami, by wyciągnąć więcej informacji,
często przetwarzamy ją na kolumnę numeryczną,
np. odejmując datę w danym wierszu od minimalnej daty z kolumny 
- tworząc przez to kolumnę z różnicą w dniach.

Stwórz taką kolumnę i oblicz współczynnik korelacji Pearsona między tą kolumną, a ceną za metr.
Odpowiedź przypisz do zmiennej corr.

'''


# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# df.head()

# df["date"] = pd.to_datetime(df["date"])
# df["date_days"] = df["date"] - df["date"].min()

# corr = df["date_days"].corr(df["price_per_m"])
# print(corr)


#CD Python - 267

'''
Czy istnieje zależność między datą (df["date"]), a ceną za metr?
Mając kolumnę z datami, by wyciągnąć więcej informacji, często przetwarzamy ją na kolumnę numeryczną,
np. odejmując datę w danym wierszu od minimalnej daty z kolumny - tworząc przez to kolumnę z różnicą w dniach.

Stwórz taką kolumnę i oblicz współczynnik korelacji Pearsona między tą kolumną, a ceną za metr. Odpowiedź przypisz do zmiennej corr.
'''

#CD Python - 268

'''
Zadanie
Czy istnieją statystyczne dowody na to, że cena za metr jest zależna od piętra (df["floor_no"])?

Przypisz odpowiedź True / False do zmiennej are_related.
'''

# import pandas as pd


# df = pd.read_csv("mini-df.csv")
# df.head()

# df = df[['floor_no', 'price_per_m']]
# corr = df['floor_no'].corr(df['price_per_m'], method = 'spearman')
# print(corr) #0.076 - powyżej 0.05, nie możemy obalić hipotezy zerowej, zależności nie ma.

# are_related = False



#CD Python - 269


'''
Dopasuj wzór na regresję liniową, który na podstawie metrażu będzie przewidywał cenę za metr.

Przypisz odpowiednie wartości zaokrąglone do 2 cyfr po przecinku do zmiennych a i b,
by poniższy kod pokazywał cały wzór:

wzor = f"cena za metr = {a} * metr + {b}"
print(wzor)


'''

# import pandas as pd
# from scipy.stats import linregress
# df = pd.read_csv("mini-df.csv")
# df.head()

# x = linregress(df['area'], df['price_per_m'])
# print(x)

# a = round(x.slope, 2)
# #slope to A 
# b = round(x.intercept, 2)
# #intercept to B

# wzor = f"cena za metr = {a} * metr + {b}"
# print(wzor)



#CD Python - 270

'''
Zadanie
Ile powinna wynosić cena za metr dla mieszkania, które ma 65 m2 według modelu regresji liniowej,
który stworzyła/eś w poprzednim zadaniu?

Przypisz odpowiedź (cenę za metr) do zmiennej predicted_price.
'''

# import pandas as pd
# from scipy.stats import linregress

# df = pd.read_csv("mini-df.csv")
# df.head()

# x = linregress(df['area'], df['price_per_m'])

# a = x.slope #-19 
# b = x.intercept #11369

# predicted_price = a * 65 + b
# print(predicted_price) #wychodzi 10100



#CD Python - 271

'''
Zadanie
Obliczmy, jak dobrze działa nasz pierwszy model regresji liniowej:

Stwórz model regresji liniowej, który przewiduje cenę za metr na podstawie metrażu mieszkania.
Stwórz nową kolumnę w DataFrame df["predicted_price_per_m"],
która dla każdej oferty mieszkania zawiera przewidywaną cenę na podstawie modelu.
Oblicz średni błąd bezwzględny: średnią bezwzględnych różnic między rzeczywistą ceną (df["price_per_m"]), 
a przewidywaną (df["predicted_price_per_m"]).

Przypisz ją do zmiennej mae (skrót od Mean Absolute Error).
Jak uważasz, średnia różnica między rzeczywistymi cenami a przewidywanymi jest duża, czy mała?

Wskazówka
Aby wykonać to zadanie polecam stosowanie funkcji LinearRegression z biblioteki sklearn.
Po stworzeniu modelu możemy przewidzieć wiele wartości za pomocą metody predict(), jej użycie było pokazane na lekcji.
'''

# from sklearn.linear_model import LinearRegression

# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# df.head()

# df = df[['price_per_m', 'area']]

# x = LinearRegression()
# x.fit(df[['area']], df['price_per_m'])

# print(x.coef_, x.intercept_)

# df['predicted_price_per_m'] = x.predict(df[['area']])
# df['prediction_difference'] = df['predicted_price_per_m'] - df['price_per_m']

# mae = round(df['prediction_difference'].abs().mean())
# print(mae)
# df.head()



#CD Python - 272

'''
Korelacja jest symetryczna, czyli porównując dwie cechy nie jest istotne jaką przyjmą kolejność w funkcji pearsonr.

Regresja liniowa nie jest symetryczna - wyróżniamy tutaj zmienną zależną i niezależną.
Oblicz współczynnik kierunkowy regresji liniowej, 
która przewiduje metraż na podstawie ceny za metr. 
Odpowiedź przypisz do zmiennej coeff.

'''

# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# df.head()

# # korelacja jest symetryczna
# from scipy.stats import pearsonr
# from sklearn.linear_model import LinearRegression #I used the sklearn's Class first, but Kasia's task expected the scipy linregress version
# a = df["area"]
# b = df["price_per_m"]
# print(pearsonr(a, b))
# print(pearsonr(b, a))

# model = LinearRegression() #
# model.fit(df[['price_per_m']], df['area'])
# print(model)
# coeff = model.coef_
# print(coeff[0])


# from scipy.stats import linregress
# result = linregress(b, a)
# coeff = result.slope
# print(coeff)


#CD Python - 273
'''
Regresja liniowa może być oparta na wielu zmiennych. 
Użyj algorytmu regresji liniowej do przewidzenia ceny za metr
na podstawie na podstawie szerokości i długości geograficznej.

Przypisz odpowiednie wartości zaokrąglone do 2 cyfr po przecinku do zmiennych a1, a2 i b,
by poniższy kod pokazywał cały wzór:

wzor = f"cena za metr = {a1} * latitude + {a2} * longitude + {b}"
print(wzor)
'''


# import pandas as pd
# from sklearn.linear_model import LinearRegression
# df = pd.read_csv("mini-df.csv")
# df.head()

# model = LinearRegression()
# model.fit(df[['latitude', 'longitude']], df['price_per_m'])
# print(model.coef_)
# a1 = (model.coef_)[0]
# a2 = (model.coef_)[1]
# b = model.intercept_

# wzor = f"cena za metr = {a1} * latitude + {a2} * longitude + {b}"
# print(wzor)



#CD Python - 274

'''
Czy istnieje statystycznie istotna zależność między typem rynku (market_type), a typem ogrzewania (heating)?

Przyjmij poziom istotności 0.05.

Przypisz odpowiedź True / False do zmiennej are_related.
'''

# import pandas as pd
# from scipy.stats import chi2_contingency
# df = pd.read_csv("mini-df.csv")
# df.head()

# tab = pd.crosstab(df['market_type'], df['heating'])
# print(tab)

# result = chi2_contingency(tab)
# print(result) #0.02 - sa skorelowane, bo p-valuej jest ponizej poziomu istotnosci - nie ma tu przypadku,
# #hipoteza zerowa ('Nie ma korelacji') do odrzucenia

# are_related = True



#CD Python - 275 

'''
Czy zarobki między analitykiem danych, a inżynierem danych różnią się istotnie statystycznie?

Przyjmij poziom istotności 0.05.

Przypisz odpowiedź True / False do zmiennej is_significant.
'''


# import pandas as pd
# from scipy.stats import normaltest, kruskal
# df = pd.DataFrame({"position": ["Data Analyst"] * 18 + ["Data Engineer"] * 25, "salary": [7200, 7500, 7800, 8100, 8400, 7600, 7900, 8200, 8500, 8800, 7300, 7700, 8000, 8300, 8600, 8100, 7900, 8450, 8800, 9200, 9500, 9800, 10100, 9400, 9700, 9900, 10300, 9600, 10000, 10500, 9300, 10200, 10800, 9700, 9900, 10400, 11000, 9800, 10100, 10600, 11200, 10900, 10700]})
# df.head()


# da_salary = df[df['position'] == 'Data Analyst']
# de_salary = df[df['position'] == 'Data Engineer']


# x = normaltest(da_salary['salary'])
# print(x)
# x = normaltest(de_salary['salary'])
# print(x)

# from scipy.stats import ttest_ind
# result = ttest_ind(da_salary['salary'], de_salary['salary'])
# alpha = 0.05
# is_significant = result.pvalue < 0.05


#CD Python - 276

'''
Czy istnieje istotna statystycznie zależność pomiędzy kanałem pozyskania użytkownika a dokonaniem zakupu?

Przyjmij poziom istotności 0.05.

Przypisz odpowiedź True / False do zmiennej is_significant.

'''


# import pandas as pd
# users = pd.DataFrame({"user_id": range(1, 221), "channel": ["Google"] * 120 + ["Facebook"] * 100})
# events = pd.DataFrame({"user_id": list(range(1, 221)), "event": ["purchase"] * 42 + ["page_view"] * 78 + ["purchase"] * 24 + ["page_view"] * 76})
# #mamy tu danych kategorialnych i w zasadzie możemy bazować tylko na liczebnościach (kontyngencja) - czyli chi2

# users.head()

# #najpierw tworzymy crosstaba z kanałem pozyskania i eventami
# x = pd.crosstab(users['channel'], events['event'])
# print(x)
# #teraz pora na test chi kwadrat (chi2_contingency)
# from scipy.stats import chi2_contingency
# test = chi2_contingency(x)
# print(test)


# is_significant = test.pvalue < 0.05 #p_value 0.10, hipoteza zerowa się utrzymuje - NIE MA statystycznie istotnej ZALEŻNOŚCI między kanałami
# print(is_significant)


#CD Python - 277

'''
Zadanie
Czy kwota pierwszej transakcji użytkownika jest istotnie statystycznie związana z czasem,
jaki upłynął od założenia konta do wykonania tej transakcji?

Przyjmij poziom istotności 0.05.

Przypisz odpowiedź True / False do zmiennej is_significant.
'''


# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt

# np.random.seed(42)

# users = pd.DataFrame({
#     "user_id": range(1, 31),
#     "created_at": pd.to_datetime("2025-01-01") + pd.to_timedelta(np.random.randint(0, 90, 30), unit="D")
# })

# transactions = pd.DataFrame({
#     "user_id": np.random.choice(users["user_id"], 120),
#     "transaction_type": np.random.choice(
#         ["deposit", "purchase", "withdrawal", "transfer"],
#         120,
#         p=[0.25, 0.45, 0.15, 0.15]
#     ),
#     "amount": np.random.randint(20, 2000, 120)
# })

# transactions["created_at"] = (
#     transactions["user_id"]
#     .map(users.set_index("user_id")["created_at"])
#     + pd.to_timedelta(np.random.randint(1, 180, len(transactions)), unit="D")
# )

# #najpierw kilka transformacji, zmieniam nazwę dla porządku i jasności
# users['acc_created_at'] = users['created_at']
# del users['created_at']

# df = users.merge(transactions, on = 'user_id', how = 'left') #mergujemy

# df_first_transactions = df.groupby(['user_id', 'acc_created_at']).agg(
#     first_transaction_amt = ('amount', 'first'),
#     first_transaction_date = ('created_at', 'first')
#     ).reset_index()

# #agregacja z wymaganymi do porównania danymi


# #przeksztacenia do datetime i odejmowanie
# df_first_transactions['days_passed'] = (pd.to_datetime(df_first_transactions['first_transaction_date']) - pd.to_datetime(df_first_transactions['acc_created_at'])).dt.days
# df_first_transactions.head()

# #teraz pora na korelację - ale przedtem trzeba jeszcze sprawdzić na scatterplocie jak wygląda zależność
# sns.scatterplot(
#     data = df_first_transactions,
#     x = 'first_transaction_amt',
#     y = 'days_passed'
# )
# plt.show()

# #raczej mocno nieliniowo to wygląda, rozkłąd jest porozrzucany mocno, więc skorzystam z metody Spearmana zamiast standardowego Pearsona
# #najpierw machnąłem się i użyłem standardowej opcji, ale ogarnąłem w porę, że to nie jest właściwa droga.

# corr_test = df_first_transactions['first_transaction_amt'].corr(df_first_transactions['days_passed'], method = 'spearman')
# print(corr_test) #0.1072 - brak istotnie statystycznej różnicy, co ciekawe podobny wynik co Pearson i tak

# is_significant = False


#CD Python - 278

'''
Współczynnik korelacji nie zależy od jednostki ani skali, w jakiej wyrażone są dane.

Oblicz współczynnik korelacji Pearsona dla lat doświadczenia i pozostałych zmiennych w df.

Dla jakiej kolumny (salary_pln czy performance_score) współczynnik jest wyższy? 
Przypisz nazwę kolumny do zmiennej more_correlated.
'''


# import pandas as pd
# df = pd.DataFrame({
#     "experience_years": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
#     "salary_pln": [5200, 5800, 6100, 6800, 7200, 7900, 8600, 9100, 9800, 10500, 11100, 11800, 12600, 13400, 14300],
#     "performance_score": [42, 47, 50, 55, 58, 63, 67, 71, 75, 79, 83, 87, 90, 94, 99]
# })
# df.head()

# salary_correlation = df['experience_years'].corr(df['salary_pln'], method = 'pearson')
# performance_correlation = df['experience_years'].corr(df['performance_score'], method = 'pearson')
# print(salary_correlation, performance_correlation)
# #0.9969359780698949 0.9996371491619361 
# #Minimalnie wieksza korelacja w przypadku performance_score

# #Tak czy inaczej mocna korelacja w obu przypadkach

# more_correlated = 'performance_score'


#CD Python - 279


'''
Stwórz model regresji liniowej przewidujący zarobki na podstawie lat doświadczenia.

Ile powinna zarabiać według wzoru regresji osoba, która ma 0 lat doświadczenia?

Zaokrąglij liczbę do 2 cyfr po przecinku i przypisz do zmiennej salary.

'''



# import pandas as pd
# from sklearn.linear_model import LinearRegression

# df = pd.DataFrame({
#     "experience_years": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
#     "salary_pln": [5200, 5800, 6100, 6800, 7200, 7900, 8600, 9100, 9800, 10500, 11100, 11800, 12600, 13400, 14300],
# })
# df.head()
# x = LinearRegression()
# x.fit(df[['experience_years']], df['salary_pln'])
# print(x.coef_, x.intercept_)

# salary = x.coef_[0] * 0 + x.intercept_
# print(salary)



#CD Python - 280

'''
Czy kampania marketingowa Spring Sale wpłynęła istotnie statystycznie na współczynnik konwersji (liczba sprzedaży do liczby odwiedzin)? 
Porównaj wskaźnik konwersji przed kampanią i od dnia kampanii (uwzględniając ten dzień).

Przypisz wartość p z odpowiedniego testu statystycznego do zmiennej p_value.
'''

# import numpy as np
# import pandas as pd
# rng = np.random.default_rng(42)

# marketing_campaigns = pd.DataFrame({
#     "campaign_id": [1],
#     "campaign_name": ["Spring Sale"],
#     "date": ["2025-03-15"],
# })

# days = pd.date_range("2025-03-01", "2025-03-31")
# events = []
# for day in days:
#     visits = rng.poisson(350 if "2025-03-15" <= str(day.date()) <= "2025-03-21" else 120)
#     purchases = rng.poisson(40 if "2025-03-15" <= str(day.date()) <= "2025-03-21" else 8)

#     events += [{"event_time": day, "event_type": "visit"} for _ in range(visits)]
#     events += [{"event_time": day, "event_type": "purchase"} for _ in range(purchases)]

# events = pd.DataFrame(events)
# events['after_campaign'] = pd.to_datetime(events['event_time']) >= pd.to_datetime('2025-03-15') #data kampanii
# events.head() 

# table = pd.crosstab(events['event_type'], events['after_campaign']) #crosstab na ilosci danych eventow pod katem tego, czy jest przed czy po kampanii

# from scipy.stats import chi2_contingency
# result = chi2_contingency(table)
# p_value = result.pvalue
# print(p_value) #p value wynosi 0.01 - czyli można odrzucić H0, że zmienne są niezależne (czyli są zależne i jest jakiś związek)

#CD Python - 281

'''
Stwórz model regresji liniowej przewidujący cenę za metr na podstawie wszystkich kolumn z danymi numerycznymi 
(oczywiście prócz kolumny price). Aby dopasować model, usuń wiersze z brakującymi wartościami.

Wytrenowany model przypisz do zmiennej model.

Oblicz średni błąd bezwzględny (mean_absolute_error) i przypisz go do zmiennej mae.
'''

# import pandas as pd
# from sklearn.linear_model import LinearRegression
# df = pd.read_csv("mini-df.csv")
# df.head()

# df = df.select_dtypes(include='number')
# cond = df.notna().all(axis=1)
# df[cond].shape
# df = df[cond]

# df.head()
# model = LinearRegression()
# x = df.drop(columns=["price", "price_per_m"])
# y = df["price_per_m"]
# model.fit(x, y)

# from sklearn.metrics import mean_absolute_error
# y_pred = model.predict(x)
# mae = round(mean_absolute_error(y, y_pred), 2)
# print(mae)
#Wychodzi mae 1442


#CD Python - 281

'''
Zadanie
Skopiuj kod z poprzedniego zadania dotyczącego regresji liniowej i poeksplorujmy jakie wartości przewiduje model.

Stwórz wykres punktowy (ang. scatterplot), który pokazuje na osi X rzeczywiste wartości price_per_m, a na osi Y wartości przewidziane przez model. Gdyby model przewidywał wartości idealnie, wszystkie punkty ułożyłyby się na prostej linii. Na podstawie wykresu oceń, czy model popełnia większe błędy dla określonych zakresów cen, np. dla tańszych lub droższych nieruchomości.

Możemy także stworzyć bardziej zaawansowane wizualizacje. Stwórz wykres punktowy, który przedstawia metraż względem ceny za metr kwadratowy, a jako kolor (argument hue w seaborn.scatterplot) wykorzystaj bezwzględną różnicę między ceną przewidzianą przez model a rzeczywistą ceną. Na podstawie wykresu oceń, dla jakich nieruchomości model popełnia największe błędy.

Żeby pokazać wykres w notatniku na końcu kodu użyj funkcji:

plt.show()

'''

# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_absolute_error
# import matplotlib.pyplot as plt
# import seaborn as sns

# df = pd.read_csv("mini-df.csv")
# df.head()

# df = df.select_dtypes(include='number')
# cond = df.notna().all(axis=1)
# df[cond].shape
# df = df[cond]

# df.head()
# model = LinearRegression()
# x = df.drop(columns=["price", "price_per_m"])
# y = df["price_per_m"]
# model.fit(x, y)

# df['price_predicted'] = model.predict(x)
# check_df = df[['price_predicted', 'price_per_m']]
# df['diff'] = (df['price_predicted'] - df['price_per_m']).abs

# plot = sns.scatterplot(
#     check_df,
#     x = 'price_per_m',
#     y = 'price_predicted'
# )
# plt.show()

# scatterplot2 = sns.scatterplot(
#     df,
#     x = 'area',
#     y = 'price_per_m',
#     hue = 'diff'
# )
# plt.show()

#CD Python - 282

'''
Zadanie
Stwórz model regresji logistycznej przewidujący czy mieszkanie ma garaż (df["garage"])
na podstawie wszystkich kolumn z danymi numerycznymi. 
Aby dopasować model, usuń wiersze z brakującymi wartościami.

Wytrenowany model przypisz do zmiennej model.

Oblicz dokładność (accuracy_score) i przypisz go do zmiennej accuracy.
'''


# import pandas as pd
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score
# df = pd.read_csv("mini-df.csv")
# df.head()

# #najpierw wybieramy tylko dane numeryczne i tylko not nulle
# df = df.select_dtypes(include = 'number')
# cond = df.notna().all(axis = 1)
# df = df[cond]

# #df treningowy, wywalamy garage
# training_df = df.drop(columns=["garage"])
# model = LogisticRegression()
# model.fit(training_df, df['garage']) #trenujemy model
# print(model)


# df['predicted_garage'] = model.predict(training_df) #dodajemy predykcje
# accuracy = round(accuracy_score(df['garage'], df['predicted_garage']), 2) #porównujemy predykcje accuracy scorem
# print(accuracy) #0.72 wychodzi, 72% poprwaności predykcji

#CD Python - 283
'''
Zadanie
Stwórz listę i przypisz do zmiennej wrong_predictions indeksy (index) mieszkań, 
dla których model błędnie przewidział klasę.
'''


# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# df = df.select_dtypes(include="number")
# df = df.dropna()

# from sklearn.linear_model import LogisticRegression
# model = LogisticRegression()
# X = df.drop(columns=["garage"])
# y = df["garage"]
# model.fit(X, y)

# df['pred'] = model.predict(X)
# df.head()

# wrong_predictions = []
# for index, row in df.iterrows():
#     garage = row['garage']
#     prediction = row['pred']
#     if garage != prediction:
#         wrong_predictions.append(index)

# print(wrong_predictions)


#CD Python - 284
'''
Zadanie
Modele klasyfikacyjne oprócz przewidywanej klasy potrafią 
również zwrócić prawdopodobieństwo przynależności do każdej z klas.

Metoda predict_proba() zwraca dla każdej obserwacji prawdopodobieństwa wszystkich klas. 
Przykładowo wynik [0.43121095, 0.56878905] oznacza, że model ocenia prawdopodobieństwo klasy 0 na około 43%, 
a klasy 1 na około 57%.

Stwórz listę i przypisz do zmiennej most_likely 10 indeksów reprezentujących mieszkania
o najwyższym prawdopodobieństwie przynależności do klasy 1.
'''


# import pandas as pd
# df = pd.read_csv("mini-df.csv")

# df = df.select_dtypes(include="number")
# df = df.dropna()

# from sklearn.linear_model import LogisticRegression
# model = LogisticRegression()
# X = df.drop(columns=["garage"])
# y = df["garage"]
# model.fit(X, y)
# y_pred_proba = model.predict_proba(X)
# print(y_pred_proba)

# #Kasia's approach (the correct one - this is very imporatnt because my faulty approach was giving wrong indexes)
# #dropping null columns drops indexes but without resetting them here, so we get gaps e.g. 0, 2, 3, 7 etc.
# df["predict_proba"] = y_pred_proba[:, 1]
# most_likely = list(df.sort_values(by="predict_proba", ascending=False).head(10).index)
# print(most_likely)



#CD Python - 285

'''
Zadanie
Stwórz model, który będzie przewidywał czy ktoś kupi kurs df["bought_course"].

Wytrenowany model przypisz do zmiennej model.
'''


# import pandas as pd
# import numpy as np
# from sklearn.linear_model import LogisticRegression
# np.random.seed(42)

# n = 500
# df = pd.DataFrame({
#     "age": np.random.randint(18, 55, n),
#     "days_since_signup": np.random.randint(1, 180, n),
#     "visited_pricing_page": np.random.choice([0, 1], n, p=[0.45, 0.55]),
#     "watched_webinar": np.random.choice([0, 1], n, p=[0.65, 0.35]),
#     "opened_email": np.random.choice([0, 1], n, p=[0.4, 0.6]),
#     "time_on_page": np.random.normal(6, 2, n).round(2),
#     "number_of_visits": np.random.poisson(4, n),
# })
# score = (
#     0.8 * df["visited_pricing_page"] + 1.2 * df["watched_webinar"] + 0.7 * df["opened_email"] + 0.15 * df["number_of_visits"] + 0.08 * df["time_on_page"] - 0.01 * df["days_since_signup"] + np.random.normal(0, 0.8, n)
# )
# probability = 1 / (1 + np.exp(-score))
# df["bought_course"] = (probability > 0.65).astype(int)

# x = df.drop(columns = ['bought_course'])
# y = df['bought_course']

# model = LogisticRegression()
# model.fit(x, y)
# print(model)



#CD Python - 286
'''
Zadanie
Stwórz model regresji liniowej przewidujący powierzchnię mieszkania na podstawie ceny za metr, 
piętra i roku budynku.

O ile zmienia się przewidywana powierzchnia mieszkania przy wzroście piętra o 1,
zakładając, że pozostałe cechy pozostają bez zmian? 
Przypisz odpowiedź zaokrągloną do 2 cyfr po przecinku do zmiennej floor_coef.

'''
# import pandas as pd
# from sklearn.linear_model import LinearRegression

# df = pd.read_csv("mini-df.csv")
# df = df[["price_per_m", "floor_no", "build_year", "area"]].dropna()
# df.head()

# X = df.drop(columns = ['area'])
# y = df['area']
# model = LinearRegression()
# model.fit(X, y)
# df['pred_area'] = model.predict(X)
# df.head()

# floor_coef = round(model.coef_[1], 2)



#CD Python - 287 

'''
Zadanie
Stwórz model regresji liniowej przewidujący powierzchnię mieszkania na podstawie ceny za metr, piętra i roku budynku.

Jaki jest przewidywany metraż dla mieszkania, które kosztuje 9500 zł/m2, jest na 2 piętrze i powstało w 2021 roku?

Przypisz odpowiedź zaokrągloną do 2 cyfr po przecinku do zmiennej predicted_area.
'''


# import pandas as pd
# from sklearn.linear_model import LinearRegression
# df = pd.read_csv("mini-df.csv")
# df = df[["price_per_m", "floor_no", "build_year", "area"]].dropna()
# df.head()

# check_df = df.drop(columns = ['area'])
# predicted_df = df['area']

# model = LinearRegression()
# model.fit(check_df, predicted_df)
# predicted_area = model.predict([[9500, 2.0, 2021.0]])[0].round(2)

# print(predicted_area)




#CD Python - 287 

'''
Stwórz model drzewa decyzyjnego, który przewiduje cenę za metr. 
Jako cechy do wytrenowania modelu możesz wybrać cokolwiek dostępnego w df. 

Ustaw maksymalną głębokość drzewa na 3 (argument max_depth).

Przypisz wytrenowany model do zmiennej model.

Oblicz średni błąd bezwzględny (mean_absolute_error) i przypisz go do zmiennej mae.

'''


# import pandas as pd
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.metrics import mean_absolute_error
# df = pd.read_csv("mini-df.csv")
# df.head()


# training_df= df[['area', 'rooms_no', 'floor_no', 'separate_kitchen', 'air_conditioning', 'balcony', 'garage']]
# predicted_df = df['price_per_m']

# model = DecisionTreeRegressor(max_depth = 3)
# model.fit(training_df, predicted_df)
# print(model)

# df['predicted_ppm'] = model.predict(training_df)
# mae = mean_absolute_error(df['price_per_m'], df['predicted_ppm'])
# print(mae)



#CD Python - 289 
'''
Zadanie
Współczynniki kierunkowe w modelu regresji liniowej mogą pomóc określić, 
które cechy mają największy wpływ na przewidywaną wartość.

Takie porównanie ma jednak sens tylko wtedy, 
gdy wszystkie cechy są zapisane w tej samej skali. 
Trudno porównywać współczynnik dla powierzchni (area),
wyrażonej w metrach kwadratowych z liczbą pięter (floor_no), czy rokiem wybudowania budynku (build_year).

Będziemy się uczyć w kolejnych tygodniach jak przygotować dane do modelu, 
ale już teraz możecie zobaczyć jak działa skalowanie danych, które sprowadza wszystkie cechy do porównywalnej skali.

Kod trenuje model regresji liniowej przewidujący cenę za metr na wyskalowanych danych. 
Porównując współczynniki kierunkowe określ, która cecha ma największy wpływ na przewidywaną wartość
i przypisz nazwę tej kolumny do zmiennej most_important_feature.

'''

# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# df = df.select_dtypes(include="number")
# df = df.drop(columns=["price"])
# df = df.dropna()

# X = df.drop(columns=["price_per_m"])
# y = df["price_per_m"]

# # sprowadź cechy do porównywalnej skali
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# scaler.fit(X)
# X_scaled = scaler.transform(X)

# # wytrenuj model na wyskalowanych cechach
# from sklearn.linear_model import LinearRegression
# model = LinearRegression()
# model.fit(X_scaled, y)

# # znajdź współczynniki kierunkowe dla cech
# import numpy as np
# df_coef = pd.DataFrame({"col": X.columns, "coef": np.abs(model.coef_)})
# df_coef.head()

# '''
# 	col	coef
# 0	area	747.877450
# 1	rooms_no	1799.929739
# 2	floor_no	416.886916
# 3	build_year	939.885562
# 4	build_floor_num	418.043071
# '''

# most_important_feature = 'rooms_no'


#CD Python - 290
'''
Zadanie
Algorytm drzewa decyzyjnego może być wykorzystywany zarówno do regresji, jak i klasyfikacji.

Znajdź odpowiednią funkcję w bibliotece scikit-learn i zmień kod tak, 
aby model przewidywał, czy mieszkanie ma garaż, wykorzystując algorytm drzewa decyzyjnego. 

Wytrenowany model przypisz do zmiennej model.

Po wytrenowaniu modelu znajdź kolejną funkcję z biblioteki scikit-learn, która zwizualizuje drzewo graficznie.
'''

# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_csv("mini-df.csv")
# df = df.select_dtypes(include="number")
# df = df.dropna()

# from sklearn.linear_model import LogisticRegression
# from sklearn.tree import DecisionTreeClassifier, plot_tree
# model = DecisionTreeClassifier()
# X = df.drop(columns=["garage"])
# y = df["garage"]
# model.fit(X, y)

# y_pred = model.predict(X)
# x = plot_tree(model, max_depth = 2, feature_names = X.columns)
# plt.show()



#CD Python - 291

'''
Zadanie
Wytrenowany model możemy zapisać do pliku, 
aby później wykorzystać go np. w aplikacji lub procesie automatyzacji do przewidywania wyników dla nowych danych.

Możemy do tego wykorzystać funkcję dump z biblioteki joblib.

Zapisz wytrenowany model do pliku o nazwie "model.pkl" i usuń z przestrzeni roboczej Pythona zmienną model.

import joblib
joblib.dump(model, nazwa_pliku)

'''
# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# df = df.select_dtypes(include="number")
# df = df.dropna()

# from sklearn.linear_model import LogisticRegression
# model = LogisticRegression()
# X = df.drop(columns=["garage"])
# y = df["garage"]
# model.fit(X, y)

# import joblib
# joblib.dump(model, 'model.pkl')
# del model


#CD Python - 292
'''
Regularyzacja to technika, która ogranicza złożoność modelu, dzięki czemu zmniejsza ryzyko przeuczenia.

Lasso to jeden z rodzajów regularyzacji. Podczas trenowania model "karze" duże wartości współczynników regresji. 
W efekcie współczynniki mniej istotnych cech stają się coraz mniejsze, 
część z nich może zostać ustawiona dokładnie na 0.

Przypisz nazwy kolumn, których współczynniki wynoszą 0 do zmiennej not_important_features.

'''

# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# df = df.select_dtypes(include="number")
# df = df.drop(columns=["price"])
# df = df.dropna()

# X = df.drop(columns=["price_per_m"])
# y = df["price_per_m"]

# # sprowadź cechy do porównywalnej skali
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# scaler.fit(X)
# X_scaled = scaler.transform(X)

# # wytrenuj model na wyskalowanych cechach
# from sklearn.linear_model import Lasso
# model = Lasso(alpha=100)
# model.fit(X_scaled, y)

# print(X.columns)
# df_coef = pd.DataFrame({"col": X.columns, "coef": model.coef_})
# print(df_coef)

# not_important_features = ['build_floor_num', 'balcony', 'garden', 'nan', 'two_storey']



#CD Python - 293

'''
Zadanie
Porównaj dokładność (ang. accuracy) modelu regresji logistycznej z modelem drzewa decyzyjnego.

Oblicz metrykę dla obu modeli, a następnie przypisz wyniki (zaokrąglone do 2 miejsc po przecinku) 
do zmiennych accuracy_log_reg oraz accuracy_tree.
'''

# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_csv("mini-df.csv")
# df = df.select_dtypes(include="number")
# df = df.dropna()

# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score
# model = LogisticRegression()
# X = df.drop(columns=["garage"])
# y = df["garage"]
# model.fit(X, y)
# y_pred = model.predict(X)

# accuracy_log_reg = round(accuracy_score(y_pred, df['garage']), 2)
# print(accuracy_score)

# from sklearn.tree import DecisionTreeClassifier
# model = DecisionTreeClassifier()
# model.fit(X, y)
# y_pred = model.predict(X)

# accuracy_tree = round(accuracy_score(y_pred, df['garage']), 2)
# print(accuracy_tree)


#CD Python - 294

'''
Zadanie
Wytrenuj model przewidujący wynagrodzenie (salary) na podstawie pozostałych cech. 
Użyj obojętnie jakiego algorytmu. Przypisz model do zmiennej model, 
oceń model za pomocą odpowiedniej metryki i przypisz ją do zmiennej metric.
'''


# import numpy as np
# import pandas as pd
# np.random.seed(42)
# n = 300
# experience = np.random.randint(0, 16, n)
# education = np.random.choice([0, 1, 2], n, p=[0.4, 0.4, 0.2])  # lic., mgr, phd
# remote = np.random.choice([0, 1], n)
# company_size = np.random.randint(20, 5000, n)

# salary = (5000 + experience * 900 + education * 2500 + remote * 1200 + company_size * 0.8 + np.random.normal(0, 2500, n))

# df = pd.DataFrame({ "experience": experience, "education": education, "remote": remote, "company_size": company_size, "salary": salary.round()})
# df.head()

# #wybieram regresję liniową i mae - regresja, bo dane numeryczne i pasuje mi
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_absolute_error

# X = df.drop(columns = ['salary'])
# y = df['salary']

# model = LinearRegression()
# model.fit(X, y)
# y_pred = model.predict(X)

# metric = mean_absolute_error(y_pred, y)
# print(metric)


#CD Python - 295

'''
Zadanie
Rozdziel dane w sposób losowy dla zmiennych X i y na:

zbiór treningowy, zawierający 80% rekordów
zbiór testowy, zawierający 20% rekordów
Przypisz zbiory do zmiennych X_train, X_test, y_train, y_test.
'''

# import pandas as pd
# from sklearn.model_selection import train_test_split
# df = pd.read_csv("mini-df.csv")

# X = df[["area", "rooms_no", "floor_no"]]
# y = df["price_per_m"]

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.20, random_state=42)



#CD Python - 296

'''
Nie każdy zbiór danych dzielimy na zbiór treningowy i testowy w sposób losowy. 
W przypadku szeregów czasowych, gdzie każdy wiersz reprezentuje kolejny moment w czasie (np. dzień), 
taki podział mógłby prowadzić do wykorzystania informacji z przyszłości podczas trenowania modelu.

Dlatego chcemy, aby podział jak najlepiej odzwierciedlał rzeczywistą sytuację, 
czyli model powinien uczyć się na wcześniejszych danych i przewidywać wartości dla późniejszych.

Chcemy stworzyć model przewidujący sprzedaż (sales) na podstawie pozostałych kolumn. 
Utwórz zmienne X_train, X_test, y_train, y_test, w których pierwsze 80% obserwacji 
(uporządkowanych według kolumny df["date"]) znajduje się w zbiorze treningowym, a pozostałe 20% w zbiorze testowym.
'''


# import pandas as pd; 
# from sklearn.model_selection import train_test_split
# import numpy as np; np.random.seed(42); 
# df = pd.DataFrame({"date": pd.date_range("2025-01-01", "2025-03-31"), "sales": np.random.randint(80, 180, 90), "orders": np.random.randint(5, 30, 90), "temperature": np.random.randint(-5, 31, 90), "marketing": np.random.choice([0, 1], 90, p=[0.8, 0.2])})

# df.head()
# df.tail()

# X = df.drop(columns = ['sales'])
# y = df['sales']

# X_train, X_test, y_train, y_test = train_test_split(
#     X, 
#     y,
#     shuffle = False,
#     test_size = 0.2
# )



#CD Python - 297

'''
Zadanie
Stwórz model, który będzie przewidywał czy ktoś kupi kurs df["bought_course"]. 
Model wytrenuj na zbiorze treningowym, a oceń model na zbiorze testowym.

Wytrenowany model przypisz do zmiennej model, a odpowiednią metrykę ewaluacji do zmiennej metric.

'''
# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import accuracy_score
# np.random.seed(42)

# n = 500
# df = pd.DataFrame({
#     "age": np.random.randint(18, 55, n),
#     "days_since_signup": np.random.randint(1, 180, n),
#     "visited_pricing_page": np.random.choice([0, 1], n, p=[0.45, 0.55]),
#     "watched_webinar": np.random.choice([0, 1], n, p=[0.65, 0.35]),
#     "opened_email": np.random.choice([0, 1], n, p=[0.4, 0.6]),
#     "time_on_page": np.random.normal(6, 2, n).round(2),
#     "number_of_visits": np.random.poisson(4, n),
# })
# score = (
#     0.8 * df["visited_pricing_page"] + 1.2 * df["watched_webinar"] + 0.7 * df["opened_email"] + 0.15 * df["number_of_visits"] + 0.08 * df["time_on_page"] - 0.01 * df["days_since_signup"] + np.random.normal(0, 0.8, n)
# )
# probability = 1 / (1 + np.exp(-score))
# df["bought_course"] = (probability > 0.65).astype(int)

# df.head()

# X = df.drop(columns = ['bought_course'])
# y = df['bought_course']

# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size = 0.3
# )


# model = DecisionTreeClassifier()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print(model)

# metric = accuracy_score(y_test, y_pred)
# print(metric)


#CD Python - 298

'''
Zadanie
Ile razy dla zbioru testowego model przewidział, że mieszkanie ma garaż, a nie powinien tego przewidzieć?

Odpowiedź przypisz do zmiennej false_positives.
'''


# import pandas as pd
# import matplotlib.pyplot as plt

# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# df = pd.read_csv("mini-df.csv")
# df = df.select_dtypes(include="number")
# df = df.dropna()

# X = df.drop(columns=["garage"])
# y = df["garage"]

# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# model = LogisticRegression()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)

# matrix = confusion_matrix(y_test, y_pred)
# ConfusionMatrixDisplay(matrix).plot()
# plt.show() #widać tu 3 false positives


#CD Python - 299

'''
Zadanie
Oblicz metrykę precyzji (ang. precision) dla zbioru testowego, czyli określ, 
jaki odsetek obserwacji przewidzianych przez model jako pozytywne rzeczywiście należał do klasy pozytywnej.

Odpowiedź przypisz do zmiennej precision.
'''

# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.metrics import precision_score
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression

# df = pd.read_csv("mini-df.csv")
# df = df.select_dtypes(include="number")
# df = df.dropna()

# X = df.drop(columns=["garage"])
# y = df["garage"]
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# model = LogisticRegression()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)

# precision = precision_score(y_test, y_pred)
# print(precision) #0.4 


#CD Python - 300
'''
Zadanie
Porównaj dokładność (ang. accuracy) modelu drzewa decyzyjnego na całym zbiorze danych
z wynikami uzyskanymi przez model stworzony z podziałem na zbiór treningowy i testowy.

Oblicz metrykę dla obu modeli, a następnie przypisz wyniki do zmiennych accuracy_entire_dataset oraz accuracy_split_dataset.

'''


# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import accuracy_score

# df = pd.read_csv("mini-df.csv")
# df = df.select_dtypes(include="number")
# df = df.dropna()

# model = DecisionTreeClassifier(random_state=42)
# X = df.drop(columns=["garage"])
# y = df["garage"]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# model.fit(X, y)

# y_full = model.predict(X)
# accuracy_entire_dataset = accuracy_score(y, y_full)
# print(accuracy_entire_dataset) #1.0 XD



# model.fit(X_train, y_train)
# y_split = model.predict(X_test)
# accuracy_split_dataset = accuracy_score(y_test, y_split)
# print(accuracy_split_dataset) #tu juz wychodzi 0.61



#CD Python - 301

'''
Metryki precyzji (ang. precision) oraz czułości (ang. recall) są szczególnie przydatne, 
gdy dane są niezbalansowane, czyli jedna z klas występuje znacznie rzadziej od drugiej.

Stwórz model wykorzystujący algorytm Lasu Losowego przewidujący czy wiadomość e-mail jest spamem.

Którą metrykę wybierzesz jako ważniejszą, jeżeli zależy Ci na tym, 
aby jak najmniej wiadomości spam trafiło do skrzynki odbiorczej użytkownika? 
Wybierz metrykę i przypisz jaką wartość otrzymuje na zbiorze testowym do zmiennej metric.
'''


# import numpy as np
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import recall_score #w tym kontekście interesuje nas czułość - chcemy wręcz za często być alarmowani

# np.random.seed(42)
# n = 1000
# df = pd.DataFrame({"message_length": np.random.randint(10, 500, n),"uppercase_ratio": np.random.beta(1, 8, n),
# "exclamation_count": np.random.poisson(2, n), "link_count": np.random.poisson(0.5, n), "digit_ratio": np.random.beta(2, 10, n),
# "contains_free": np.random.binomial(1, 0.15, n), "contains_win": np.random.binomial(1, 0.10, n), "contains_urgent": np.random.binomial(1, 0.12, n),"sender_reputation": np.random.uniform(0, 1, n),
# })
# score = (1.8 * df["contains_free"] + 2.2 * df["contains_win"] + 1.6 * df["contains_urgent"] + 1.5 * df["link_count"] + 8 * df["uppercase_ratio"]
#     + 0.03 * df["message_length"] + 5 * df["digit_ratio"] - 4 * df["sender_reputation"] + np.random.normal(0, 2, n)
# )
# threshold = np.percentile(score, 70)
# df["is_spam"] = (score > threshold).astype(int)

# X = df.drop(columns=["is_spam"])
# y = df["is_spam"]


# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# model = RandomForestClassifier(random_state=42)
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)

# metric = recall_score(y_test, y_pred)
# print(metric)


#CD Python - 302

'''
Zadanie
Pojedyncze drzewa decyzyjne mają tendencję do przeuczania się (ang. overfitting). 
Jednym ze sposobów sprawdzenia, czy model jest przeuczony, jest porównanie jego wyników na zbiorze treningowym i testowym. 
Jeżeli model osiąga znacznie lepsze wyniki na zbiorze treningowym niż na testowym, może to świadczyć o przeuczeniu.

Oblicz średni błąd bezwzględny (ang. Mean Absolute Error, MAE) dla zbioru treningowego oraz testowego. 
Przypisz otrzymane wartości do zmiennych mae_train oraz mae_test, a następnie porównaj je, aby ocenić, 
czy model wykazuje oznaki przeuczenia.
'''



# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.metrics import mean_absolute_error

# df = pd.read_csv("mini-df.csv")

# X = df[["area", "rooms_no", "floor_no"]]
# y = df["price_per_m"]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model = DecisionTreeRegressor(random_state=42)
# model.fit(X_train, y_train)

# y_pred_train = model.predict(X_train)
# mae_train = round(mean_absolute_error(y_train, y_pred_train), 2)
# print(mae_train) #roznica 47.89 - ewidentnie bardzo mała, co nie dziwi w tym kotneskcie


# y_pred_test = model.predict(X_test)
# mae_test = round(mean_absolute_error(y_test, y_pred_test), 2)
# print(mae_test) #roznica 3251 - alarmujaca roznica w porownaniu do zbioru testowego


#CD Python - 303 

'''
Zadanie
Pojedyncze drzewa decyzyjne często przeuczają się, ponieważ potrafią się rozbudowywać bez końca, 
próbując się dopasować do każdego przypadku w danych - 
zamiast uczyć się ogólnych zależności zbyt mocno dopasowują się do szumu informacyjnego.

Aby ograniczyć ten problem, stosuje się drzewa losowe (ang. Random Forest). 
Zamiast jednego drzewa model buduje wiele drzew decyzyjnych,
a każde z nich jest trenowane na losowej próbce danych oraz wykorzystuje losowy podzbiór cech podczas podejmowania decyzji. 
Dzięki temu poszczególne drzewa uczą się nieco innych zależności, 
a końcowa predykcja powstaje na podstawie ich wspólnego głosu (w klasyfikacji) lub średniej przewidywanej wartości (w regresji).

Wytrenuj model Random Forest przewidujący price_per_m,
a następnie oblicz pierwiastek ze średniego błądu kwadratowego (ang. root mean squared error, RMSE) 
dla zbioru treningowego i testowego. Przypisz wynik do zmiennych rmse_train oraz rmse_test.
'''


# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import root_mean_squared_error

# df = pd.read_csv("mini-df.csv")

# X = df[["area", "rooms_no", "floor_no"]]
# y = df["price_per_m"]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model = RandomForestRegressor(random_state=42)
# model.fit(X_train, y_train)

# y_train_pred = model.predict(X_train)
# rmse_train = round(root_mean_squared_error(y_train, y_train_pred), 2)

# y_test_pred = model.predict(X_test)
# rmse_test = round(root_mean_squared_error(y_test, y_test_pred), 2)

# print(rmse_train, rmse_test)


#CD Python - 304

'''
Zbudowano dwa modele uczenia maszynowego, które przewidują różne zmienne: sprzedaż (sales) oraz zysk (profit).

Porównaj jakość obu modeli, wybierając metrykę, która pozwala porównywać różne modele regresji. 
Na podstawie wybranej metryki określ, który model osiąga lepsze wyniki.

Określ, który z celów jest łatwiejszy do przewidywania i przypisz jego nazwę ("sales" lub "profit") 
do zmiennej better_to_predict.
'''

# import pandas as pd
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_absolute_percentage_error, r2_score

# df = pd.DataFrame({
#     "employees": [5, 7, 9, 11, 13, 16, 18, 21, 24, 27, 30, 34, 38, 42, 46, 50, 55, 60, 66, 72],
#     "marketing_budget": [2000, 2400, 2800, 3500, 4200, 5000, 5800, 6700, 7600, 8600, 9700, 10900, 12200, 13600, 15100, 16700, 18400, 20200, 22100, 24100],
#     "website_visits": [700, 850, 980, 1150, 1350, 1600, 1850, 2150, 2450, 2800, 3150, 3550, 3950, 4400, 4850, 5350, 5900, 6500, 7150, 7800],
#     "avg_order_value": [82, 84, 86, 88, 90, 92, 94, 96, 98, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 120],
#     "sales": [45000, 51000, 58000, 66000, 74000, 86000, 95000, 109000, 122000, 137000, 151000, 168000, 185000, 204000, 223000, 245000, 268000, 292000, 318000, 345000],
#     "profit": [6200, 7100, 9800, 8700, 12600, 11900, 15800, 14900, 18600, 17300, 22400, 20700, 25500, 23900, 28600, 27100, 33200, 30400, 37100, 34800]
# })

# # model przewidujący sprzedaż
# X_1 = df.drop(columns=["sales"])
# y_1 = df["sales"]
# model_1 = RandomForestRegressor(max_depth=2, random_state=42)
# model_1.fit(X_1, y_1)
# y_pred_1 = model_1.predict(X_1)

# # model przewidujący zysk
# X_2 = df.drop(columns=["profit"])
# y_2 = df["profit"]
# model_2 = RandomForestRegressor(max_depth=2, random_state=42)
# model_2.fit(X_2, y_2)
# y_pred_2 = model_2.predict(X_2)

# # Współczynnik determinacji R2
# sales = round(r2_score(y_1, y_pred_1), 4)
# profit = round(r2_score(y_2, y_pred_2), 4)
# print(f"sprzedaż: {sales}, zysk: {profit}")

# #blad procentowy MAPE
# mape1 = mean_absolute_percentage_error(y_1, y_pred_1)
# mape2 = mean_absolute_percentage_error(y_2, y_pred_2)
# print(mape1, mape2)

# better_to_predict = 'sales'



#CD Python - 305
'''
Standardowo modele klasyfikacyjne przypisują obserwację do klasy pozytywnej, 
jeżeli prawdopodobieństwo tej klasy wynosi co najmniej 0.5.

Sprawdź, jak zmieni się precyzja (precision), 
jeżeli zamiast domyślnego progu 0.5 zastosujemy próg 0.7. 
Oznacza to, że obserwacja zostanie przypisana do klasy pozytywnej tylko wtedy, 
gdy przewidywane prawdopodobieństwo klasy 1 będzie wynosiło co najmniej 0.7.

Prawdopodobieństwo predykcji otrzymasz używając metody predict_proba() na wytrenowanym modelu.

Obliczoną wartość przypisz do zmiennej new_threshold_precision.

'''

# import numpy as np
# import pandas as pd

# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import precision_score


# np.random.seed(42)
# n = 1000
# df = pd.DataFrame({"message_length": np.random.randint(10, 500, n),"uppercase_ratio": np.random.beta(1, 8, n),
# "exclamation_count": np.random.poisson(2, n), "link_count": np.random.poisson(0.5, n), "digit_ratio": np.random.beta(2, 10, n),
# "contains_free": np.random.binomial(1, 0.15, n), "contains_win": np.random.binomial(1, 0.10, n), "contains_urgent": np.random.binomial(1, 0.12, n),"sender_reputation": np.random.uniform(0, 1, n),
# })
# score = (1.8 * df["contains_free"] + 2.2 * df["contains_win"] + 1.6 * df["contains_urgent"] + 1.5 * df["link_count"] + 8 * df["uppercase_ratio"]
#     + 0.03 * df["message_length"] + 5 * df["digit_ratio"] - 4 * df["sender_reputation"] + np.random.normal(0, 2, n)
# )
# threshold = np.percentile(score, 70)
# df["is_spam"] = (score > threshold).astype(int)

# X = df.drop(columns=["is_spam"])
# y = df["is_spam"]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# model = RandomForestClassifier(random_state=42)
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)
# standard_precision = precision_score(y_test, y_pred)
# print(standard_precision) #wychodzi 78%

# new_threshold_pred = model.predict_proba(X_test)[:, 1] >= 0.7
# new_threshold_precision = precision_score(y_test, new_threshold_pred)
# print(new_threshold_precision) #tutaj juz 89%


#CD Python - 306

'''
Zadanie
Uruchom kod i odpowiedz na pytanie: czy zbudowany model lepiej rozróżnia klasy niż model losowy? 
Przypisz True lub False do zmiennej answer.
'''
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.metrics import roc_curve, roc_auc_score
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier

# np.random.seed(42)
# n = 1000
# df = pd.DataFrame({"message_length": np.random.randint(10, 500, n),"uppercase_ratio": np.random.beta(1, 8, n),
# "exclamation_count": np.random.poisson(2, n), "link_count": np.random.poisson(0.5, n), "digit_ratio": np.random.beta(2, 10, n),
# "contains_free": np.random.binomial(1, 0.15, n), "contains_win": np.random.binomial(1, 0.10, n), "contains_urgent": np.random.binomial(1, 0.12, n),"sender_reputation": np.random.uniform(0, 1, n),
# })
# score = (1.8 * df["contains_free"] + 2.2 * df["contains_win"] + 1.6 * df["contains_urgent"] + 1.5 * df["link_count"] + 8 * df["uppercase_ratio"]
#     + 0.03 * df["message_length"] + 5 * df["digit_ratio"] - 4 * df["sender_reputation"] + np.random.normal(0, 2, n)
# )
# threshold = np.percentile(score, 70)
# df["is_spam"] = (score > threshold).astype(int)

# X = df.drop(columns=["is_spam"])
# y = df["is_spam"]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# model = RandomForestClassifier(random_state=42)
# model.fit(X_train, y_train)
# y_pred_proba = model.predict_proba(X_test)[:, 1]

# # ROC AUC
# roc_auc = roc_auc_score(y_test, y_pred_proba)
# print(f"ROC AUC = {roc_auc:.3f}")

# # Krzywa ROC
# fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
# plt.figure(figsize=(6, 6))
# plt.plot(fpr, tpr, label=f"ROC AUC = {roc_auc:.3f}")
# plt.plot([0, 1], [0, 1], "--", color="gray", label="Losowy model")
# plt.xlabel("False Positive Rate")
# plt.ylabel("True Positive Rate")
# plt.title("Krzywa ROC")
# plt.legend()
# plt.grid(True)
# plt.show()

# answer = True



#CD Python - 306
'''
Zadanie
Nie wszystkie kolumny są przydatne do budowy modelu. 
Przykładowo, identyfikatory użytkowników czy numer zamówienia mają zazwyczaj unikalną wartość dla każdej obserwacji. 
Takie kolumny nie zawierają informacji, które model mógłby wykorzystać do znalezienia zależności, 
dlatego przed trenowaniem często są usuwane.

Usuń z DataFrame df wszystkie kolumny, w których co najmniej 99% wartości jest unikalnych.

Wynik przypisz ponownie do zmiennej df.
'''
# import numpy as np
# import pandas as pd

# np.random.seed(42)
# n = 1000

# df = pd.DataFrame({
#     "user_id": np.arange(100000, 101000),
#     "order_id": np.arange(500000, 501000),
#     "email": [f"user{i}@example.com" for i in range(n)],
#     "age": np.random.randint(18, 70, n),
#     "salary": np.random.randint(3000, 18000, n),
#     "city": np.random.choice(
#         ["Warszawa", "Kraków", "Gdańsk", "Poznań"],
#         size=n
#     ),
#     "purchased": np.random.randint(0, 2, n)
# })

# print(df.nunique())

# df = df.drop(columns = ['user_id', 'order_id', 'email'])



#CD Python - 307
'''
Zadanie
Chcemy przewidzieć, czy klient zrezygnuje z subskrypcji (df["churn"]). 
Dane są niezbalansowane, tylko około 15% klientów rezygnuje z usługi.

Jaka metryka będzie najlepsza, jeżeli:

nie chcemy pomijać klientów, którzy odejdą
jednocześnie nie chcemy błędnie oznaczać zbyt wielu lojalnych klientów jako zagrożonych odejściem

Zadanie

Wytrenowany model przypisz do zmiennej model

Wybierz odpowiednią metrykę i przypisz jej nazwę jako string do zmiennej metric:
accuracy
precision
recall
f1-score

Oblicz wartość tej metryki dla zbioru testowego i przypisz ją do zmiennej result
'''


# import numpy as np
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier #random forest sprawdza się idealnie, gdy nie wiemy do końca, co badamy
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import f1_score #f1 score w tym wypadku dla zbalansowania czułości i precyzji - to średnia harmoniczna z obu,
# #średnia harmoniczna balansuje te wartości, ALE TEŻ USTAWIA JE TAK, ŻEBY NIE BYŁY ZA MAŁE

# np.random.seed(42)
# n = 500

# df = pd.DataFrame({
#     "months_as_customer": np.random.randint(1, 73, n),
#     "monthly_fee": np.random.randint(30, 201, n),
#     "logins_last_month": np.random.poisson(10, n),
#     "support_tickets": np.random.poisson(2, n),
#     "late_payments": np.random.poisson(1, n),
#     "contract_months": np.random.choice([1, 6, 12, 24], n, p=[0.35, 0.20, 0.30, 0.15])
# })
# churn_score = (
#     -0.04 * df["months_as_customer"]
#     + 0.015 * df["monthly_fee"]
#     - 0.10 * df["logins_last_month"]
#     + 0.50 * df["support_tickets"]
#     + 0.70 * df["late_payments"]
#     - 0.08 * df["contract_months"]
#     + np.random.normal(0, 1.5, n)
# )
# df["churn"] = (churn_score >= churn_score.quantile(0.85)).astype(int)

# X = df.drop(columns = 'churn')
# y = df['churn']

# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size = 0.3,
#     random_state = 42
# )

# model = RandomForestClassifier()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# metric = 'f1-score'
# result = f1_score(y_test, y_pred)
# print(result)


#CD Python - 308

'''
Przy niezbalansowanych danych warto podczas podziału na zbiór treningowy i testowy upewnić się, 
że proporcja obu klas będzie podobna w obu zbiorach.

Spróbuj użyć argumentu stratify=y w metodzie train_test_split 
i zobacz czy proporcja zostaje zachowana w zbiorze treningowym i testowym.

Przypisz do zmiennej positive_share odsetek pozytywnych klas w zbiorze testowym, zaokrąglony do 2 cyfr po przecinku.
'''

# import numpy as np
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import f1_score

# np.random.seed(42)
# n = 500

# df = pd.DataFrame({
#     "months_as_customer": np.random.randint(1, 73, n),
#     "monthly_fee": np.random.randint(30, 201, n),
#     "logins_last_month": np.random.poisson(10, n),
#     "support_tickets": np.random.poisson(2, n),
#     "late_payments": np.random.poisson(1, n),
#     "contract_months": np.random.choice([1, 6, 12, 24], n, p=[0.35, 0.20, 0.30, 0.15])
# })
# churn_score = (
#     -0.04 * df["months_as_customer"]
#     + 0.015 * df["monthly_fee"]
#     - 0.10 * df["logins_last_month"]
#     + 0.50 * df["support_tickets"]
#     + 0.70 * df["late_payments"]
#     - 0.08 * df["contract_months"]
#     + np.random.normal(0, 1.5, n)
# )
# df["churn"] = (churn_score >= churn_score.quantile(0.85)).astype(int)

# X = df.drop(columns=["churn"])
# y = df["churn"]

# X_train, X_test, y_train, y_test = train_test_split(X, 
# y, 
# test_size=0.3, 
# random_state=42,
# stratify = y
# )

# print(f"train share: {y_train.sum()/len(y_train)}")
# positive_share = y_test.sum()/len(y_test) #train share: 0.15142857142857144
# print(f"test share: {positive_share}") #test share: 0.14666666666666667



#CD Python - 309

'''
Pojedyncze drzewo decyzyjne ma tendencje do przeuczania się.

Zapoznaj się z dokumentacją i zobacz jakie hiperparametry można zmienić dla algorytmu drzewa, 
zrób research które z nich wpływają na przeuczenie i spróbuj zbudować trochę lepszy model.

Spróbuj dodać argumenty do DecisionTreeClassifier(random_state=42),
aby dokładność na zbiorze testowym wyszła trochę wyższa niż 0.62.

'''



# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score

# df = pd.read_csv("mini-df.csv")
# df = df.select_dtypes(include="number")
# df = df.dropna()

# model = DecisionTreeClassifier(
#     splitter = 'random',
#     min_samples_leaf = 3,
#     max_depth = 3,
#     random_state=42)
# X = df.drop(columns=["garage"])
# y = df["garage"]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# model.fit(X_train, y_train)

# y_pred_test = model.predict(X_test)
# accuracy = round(accuracy_score(y_test, y_pred_test), 2)
# print(accuracy)



#CD Python - 310


'''
Użyj wybranej metody kodowania, aby zamienić wartości kategorialne w df na wartości numeryczne lub True/False, 
które są akceptowane przez model. 

Zapisz przekształcony DataFrame ponownie w zmiennej df.
'''

# import pandas as pd
# df = pd.read_csv("mini-df.csv")
# df = df[["heating", "build_owner", "build_type", "market_type"]]
# df.head()

# df = pd.get_dummies(df)
# df.head()


#CD Python - 311

'''
Przeskaluj wartości w df tak, aby znajdowały się w przedziale od 0 do 1. 

Zapisz przekształcony DataFrame ponownie w zmiennej df.
'''

# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler


# df = pd.read_csv("mini-df.csv")
# df = df[["area", "price_per_m", "rooms_no"]]
# df.head()

# scaler = MinMaxScaler()
# df = pd.DataFrame(scaler.fit_transform(df), columns = df.columns)
# print(df)


#CD Python - 312

'''
Stwórz model regresji liniowej przewidujący powierzchnię mieszkania na podstawie ceny za metr, piętra i roku budynku.

Dodaj do pipeline'u na odpowiednim etapie:

podział na zbiór treningowy i testowy
wyskalowanie jednostek zmiennych używanych do przewidywania metrażu
Oblicz metrykę RMSE jaką model osiąga dla zbioru testowego i przypisz ją do zmiennej rmse.

'''

# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import root_mean_squared_error
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler

# df = pd.read_csv("mini-df.csv")
# df = df[["price_per_m", "floor_no", "build_year", "area"]].dropna()
# df.head()

# X = df.drop(columns = ['area'])
# y = df['area']

# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size = 0.2,
#     random_state=42
# )

# scaler = StandardScaler()
# scaled_X_train = scaler.fit_transform(X_train)

# model = LinearRegression()
# model.fit(scaled_X_train, y_train)

# X_test_scaled = scaler.transform(X_test)
# y_pred = model.predict(X_test_scaled)

# rmse = root_mean_squared_error(y_test, y_pred)
# print(round(rmse), 2) #35 2


#CD Python - 313

'''
Tworząc kodowanie typu one-hot encoding musimy uważać na liczbę kategorii, 
aby nie tworzyć mnóstwo kolumn dla pojedynczych przypadków.

Kolumna country zawiera wiele różnych krajów. Zamień wszystkie kraje, 
które stanowią mniej niż 1% wszystkich obserwacji na kategorię Other.

Następnie stwórz transformację typu one-hot encoding i zapisz przetworzone dane pod zmienną df.
'''

# import numpy as np
# import pandas as pd


# np.random.seed(42)
# countries = np.random.permutation(["Poland"]*40 + ["Germany"]*20 + ["France"]*15 + ["Spain"]*10 + ["Italy"]*8 + ["Netherlands"]*5 + ["Czech Republic"]*5 + ["Portugal"]*4 + ["Sweden"]*3 + ["Norway"]*3 + ["Denmark"]*2 + ["Finland"]*2 + ["Belgium"]*2 + ["Austria"]*2 + ["Hungary", "Romania", "Bulgaria", "Croatia", "Serbia", "Greece", "Turkey", "Japan", "South Korea", "Brazil", "Mexico", "Australia", "New Zealand", "South Africa", "India", "Singapore"])
# np.random.shuffle(countries)
# df = pd.DataFrame({"country": countries})


# df.value_counts()
# threshold = len(df)/100

# countries_list = df.value_counts().reset_index()
# countries_list = countries_list['country'][countries_list['count'] <= threshold].values.tolist()
# df['country'] = df['country'].replace(countries_list, 'Other')

# df = pd.get_dummies(df)
# df.head()


#CD Python - 314

'''
Sprawdź, która cecha ma największy wpływ na przewidywanie, 
czy użytkownik kupi kurs (df["bought_course"]). 

Uzupełnij kod o odpowiednie kroki, które pozwolą to określić.

Nazwę cechy o największym wpływie przypisz do zmiennej most_important_feature.
'''

# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.preprocessing import RobustScaler

# np.random.seed(42)

# n = 500
# df = pd.DataFrame({
#     "age": np.random.randint(18, 55, n),
#     "days_since_signup": np.random.randint(1, 180, n),
#     "visited_pricing_page": np.random.choice([0, 1], n, p=[0.45, 0.55]),
#     "watched_webinar": np.random.choice([0, 1], n, p=[0.65, 0.35]),
#     "opened_email": np.random.choice([0, 1], n, p=[0.4, 0.6]),
#     "time_on_page": np.random.normal(6, 2, n).round(2),
#     "number_of_visits": np.random.poisson(4, n),
# })
# score = (
#     0.8 * df["visited_pricing_page"] + 1.2 * df["watched_webinar"] + 0.7 * df["opened_email"] + 0.15 * df["number_of_visits"] + 0.08 * df["time_on_page"] - 0.01 * df["days_since_signup"] + np.random.normal(0, 0.8, n)
# )
# probability = 1 / (1 + np.exp(-score))
# df["bought_course"] = (probability > 0.65).astype(int)

# df.head()


# X = df.drop(columns="bought_course")
# y = df["bought_course"]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# model = LogisticRegression()

# scaler = RobustScaler()
# scaled_X_train = scaler.fit_transform(X_train)

# model.fit(scaled_X_train, y_train)
# print(model.coef_)

# most_important_feature = 'watched_webinar'


#CD Python - 315

'''
Przetwórz dane czasowe i dodaj do df nowe kolumny:

time_to_purchase_minutes – liczba minut, 
    które upłynęły między wejściem na stronę (visit_time) a zakupem kursu (purchase_time),
month – miesiąc, w którym dokonano zakupu
dow – dzień tygodnia, w którym dokonano zakupu
is_weekend – informacja True / False czy zakupu dokonano w weekend
hour – godzina, w której dokonano zakupu
'''

# import pandas as pd

# df = pd.DataFrame({
#     "visit_time": [
#         "2026-07-01 09:15:24",
#         "2026-07-01 10:42:10",
#         "2026-07-02 14:08:35",
#         "2026-07-03 18:20:12",
#         "2026-07-04 08:55:41",
#         "2026-07-05 16:11:53",
#         "2026-07-06 12:37:29",
#         "2026-07-07 19:45:08",
#     ],
#     "purchase_time": [
#         "2026-07-01 09:28:15",
#         "2026-07-01 11:05:42",
#         "2026-07-02 14:51:18",
#         "2026-07-03 19:43:56",
#         "2026-07-04 09:12:30",
#         "2026-07-05 17:48:04",
#         "2026-07-06 13:05:10",
#         "2026-07-07 20:01:39",
#     ]
# })
# df.head()

# df['visit_time'] = pd.to_datetime(df['visit_time'])
# df['purchase_time'] = pd.to_datetime(df['purchase_time'])

# df['time_to_purchase_minutes'] = round((df['purchase_time'] - df['visit_time']).dt.total_seconds() / 60, 0)
# df.head()

# df['month'] = df['purchase_time'].dt.month
# df['dow'] = df['purchase_time'].dt.dayofweek
# df["hour"] = df["purchase_time"].dt.hour
# df['is_weekend'] = df['dow'].isin([5, 6])
# df.head()



#CD Python - 316

'''
Podczas pracy nad modelem często nie dzielimy danych tylko na zbiór treningowy i testowy.

Nie chcemy, aby wynik zależał od jednego, konkretnego podziału danych, 
ponieważ może się zdarzyć, że model osiągnie wyjątkowo dobry lub słaby wynik tylko dlatego, 
że do zbioru testowego trafiły łatwiejsze lub trudniejsze obserwacje.

Nie chcemy także wielokrotnie sprawdzać metryk na zbiorze testowym, 
ponieważ doprowadzamy wtedy do wycieku danych. 
Za każdym razem, gdy analizujemy wyniki na zbiorze testowym i na ich podstawie zmieniamy model lub hiperparametry,
pośrednio "uczymy się" tego zbioru. 

W efekcie zbiór testowy przestaje być niezależny, a uzyskane metryki stają się zbyt optymistyczne.

Aby uzyskać bardziej wiarygodną ocenę jakości modelu, 
stosujemy walidację krzyżową (ang. cross validation): dane są dzielone na kilka części (ang. folds), 
a model jest trenowany i oceniany wielokrotnie na różnych podziałach.

Zadanie
Aby przeprowadzić walidację krzyżową i dopasować model do kilku różnych części, 
użyjemy funkcji KFold oraz cross_validate z biblioteki Sklearn.

Zmień podany kod tak, aby dzielił zbiór treningowy na 4 części (foldy). 

Następnie oblicz średnią wartość metryki uzyskaną podczas walidacji krzyżowej i przypisz ją do zmiennej mean_score.
'''


# import pandas as pd
# from sklearn.model_selection import train_test_split, KFold, cross_validate
# from sklearn.linear_model import LinearRegression


# df = pd.read_csv("mini-df.csv")
# df = df[["price_per_m", "floor_no", "build_year", "area"]].dropna()

# X = df[["area", "floor_no", "build_year"]]
# y = df["price_per_m"]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model = LinearRegression()

# cv = KFold(
#     n_splits=4,
#     shuffle=True,
#     random_state=42
# )

# cv_results = cross_validate(model, X_train, y_train, cv=cv, return_train_score=True, scoring="neg_mean_absolute_error")
# print(cv_results["test_score"])

# mean_score = sum([float(i) for i in cv_results["test_score"]]) / len([float(i) for i in cv_results["test_score"]])
# print(mean_score)


#CD Python - 317

'''
Mamy zbiór danych w którym każdy wiersz reprezentuje liczbę ticketów rozwiązanych przez konkretnego agenta danego dnia.

Chcemy zbudować model przewidujący liczbę rozwiązanych zgłoszeń. 

Aby sprawdzić jak model poradzi sobie z nowymi agentami, nie będziemy dzielić danych losowo po wierszach. 
Zamiast tego cały zestaw danych każdego agenta powinien trafić wyłącznie do zbioru treningowego
lub wyłącznie do zbioru testowego.

Wylosuj 5 unikalnych wartości z kolumny agent_id. 

Wszystkie obserwacje dotyczące tych agentów przypisz do zbioru treningowego (df_train), 
a obserwacje pozostałych 3 agentów do zbioru testowego (df_test).
'''


# import numpy as np
# import pandas as pd
# import random
# from sklearn.model_selection import train_test_split



# agents = pd.DataFrame({
#     "agent_id": [101, 102, 103, 104, 105, 106, 107, 108],
#     "team_id": ["A", "A", "A", "B", "B", "B", "C", "C"],
#     "seniority": ["Junior", "Mid", "Senior", "Junior", "Mid", "Senior", "Mid", "Senior"]
# })

# df = (
#     pd.DataFrame({"date": pd.date_range("2025-01-01", periods=30)})
#     .merge(agents, how="cross")
# )

# rng = np.random.default_rng(42)

# base = df["seniority"].map({"Junior": 12, "Mid": 18, "Senior": 24})
# team_bonus = df["team_id"].map({"A": 0, "B": 2, "C": -1})

# df["tickets_resolved"] = (
#     base + team_bonus + rng.normal(0, 2.5, len(df))
# ).round().clip(lower=0).astype(int)

# df.head()

# agent_ids = df["agent_id"].unique().tolist()
# train_agent_ids = random.sample(agent_ids, k=5)
# df_train = df[df["agent_id"].isin(train_agent_ids)]
# df_test = df[~df["agent_id"].isin(train_agent_ids)]


#CD Python - 318 

'''
Zadanie
Aby obliczyć odległość od danego punktu, najlepiej użyć dedykowanej biblioteki, np. geopy.

Dodaj do df dodatkową kolumnę distance_to_center,
która dla każdej oferty mieszkania (kolumn latitude i longitude) liczy odległość od rynku w Krakowie.
'''

# import pandas as pd
# from geopy.distance import geodesic

# df = pd.read_csv("mini-df.csv")

# krakow_rynek = (50.0617, 19.9373)
# punkt = (50.0670, 19.9450)
# distance = geodesic(krakow_rynek, punkt).km
# print(distance)

# df['distance_to_center'] = df[['latitude', 'longitude']].apply(
#     lambda row: geodesic(krakow_rynek, (row['latitude'], row['longitude'])).km,
#     axis = 1
# )
# df.head()


#CD Python - 319

'''
Zadanie
Wyciągnij kwotę wynagrodzenia z tekstu i przypisz ją jako wartość numeryczną (nie tekstową) do nowej kolumny salary.

'''


# import pandas as pd

# df = pd.DataFrame({
#     "offer": [
#         "Junior Data Analyst | Wynagrodzenie: 8500 PLN miesięcznie",
#         "Python Developer (B2B) - stawka 18 000 PLN + premie",
#         "Poszukujemy SQL Developera. Oferujemy 11500 PLN brutto.",
#         "Data Scientist | Zarobki od 22 000 PLN miesięcznie",
#         "Business Analyst - wynagrodzenie 9900 PLN",
#         "Senior Data Engineer | Pensja: 27 500 PLN + bonus roczny",
#         "ML Engineer - oferujemy nawet 24000 PLN!",
#         "Analityk Danych | Widełki zaczynają się od 10 800 PLN",
#         "BI Developer | Wynagrodzenie: 16200 PLN brutto",
#         "Staż Data Analyst - stypendium 4 800 PLN miesięcznie",
#         "Data Engineer | Oferujemy 14500 PLN oraz prywatną opiekę medyczną",
#         "AI Engineer | Wynagrodzenie: 31 000 PLN + akcje spółki"
#     ]
# })
# df.head()


# df['salary'] = df[['offer']].apply(
#     lambda row: float(''.join([str(num) for num in row['offer'].split() if num.isnumeric()])),
#     axis = 1
# )
# df.head()




#CD Python - 320

'''
Zadanie
Użyj biblioteki shap, aby zrozumieć która cecha była najważniejsza
do przewidywania ceny za metr dla mieszkania o indexie == 2.

Przypisz nazwę cechy do zmiennej feature.
'''


# import pandas as pd
# from sklearn.tree import DecisionTreeRegressor
# import shap

# df = pd.read_csv("mini-df.csv")
# df = df[["price_per_m", "floor_no", "build_year", "area"]].dropna()

# X = df[["area", "floor_no", "build_year"]]
# y = df["price_per_m"]

# model = DecisionTreeRegressor()
# model.fit(X, y)

# explainer = shap.TreeExplainer(model)
# shap_values = explainer(X)
# shap.plots.bar(shap_values[2])
# shap.plots.waterfall(shap_values[2])

# feature = 'area'



#CD Python - 321

'''
Zadanie
Stwórz nową kolumnę seniority i przypisz jej wartości numeryczne:

1 - jeżeli nazwa stanowiska zawiera słowo junior
3 - jeżeli nazwa stanowiska zawiera słowo senior
2 - w innych przypadkach
'''

#Ja zrobiłem to tak jak poniżej najpierw


# import pandas as pd
# from sklearn.preprocessing import OrdinalEncoder

# df = pd.DataFrame({
#     "job_offer": [
#         "Junior Data Analyst",
#         "Data Analyst",
#         "Senior Data Scientist",
#         "Python Developer",
#         "Mid Data Engineer",
#         "Senior BI Developer",
#         "Machine Learning Engineer",
#         "Junior SQL Developer",
#         "Analytics Engineer",
#         "Lead Data Engineer",
#         "Senior Python Developer",
#         "Data Engineer (Junior)",
#         "Business Intelligence Analyst",
#         "Junior Machine Learning Engineer",
#         "Principal Data Scientist",
#         "Data Analyst - Senior",
#         "ETL Developer",
#         "Junior BI Specialist",
#         "Senior Analytics Engineer",
#         "Data Scientist"
#     ]
# })
# df.head()

# seniorities = ['junior', 'senior']

# def find_seniority(text):
#     split_text = text.lower().split()
#     for seniority in seniorities:
#         if seniority in split_text:
#             return seniority
#     return 'other'

# df['seniority'] = df[['job_offer']].apply(
#     lambda row: find_seniority(row['job_offer']),
#     axis = 1
# )


# encoder = OrdinalEncoder(categories = [['junior', 'other', 'senior']])
# print(encoder)

# df['seniority'] = encoder.fit_transform(
#     df[['seniority']],
# )

# df.head()


#rozwiazanie było w sumie o wiele prostsze i nawet nie korzystało z encodingu,
# ale ozstawiam też powyższe, bo przyda się w trudniejszych sytuacjach


# def ordinal_encoding(row):
#     seniority = 2
#     if "junior" in row.lower():
#         seniority = 1
#     elif "senior" in row.lower():
#         seniority = 3
#     return seniority

# df["seniority"] = df["job_offer"].apply(ordinal_encoding)
# df.head()


#CD Python - 322

'''
W kolumnie salary znajdują się wartości odstające.

Przeskaluj wartości w kolumnie salary, 
wybierając metodę skalowania odpowiednią dla danych zawierających wartości odstające. 

Zapisz wynik w nowej kolumnie salary_scaled.
'''


# import pandas as pd
# from sklearn.preprocessing import RobustScaler #w tym wypadku RobustScaler, dobrze radzi sobie z outlierami, bazuje na medianie i IQR


# df = pd.DataFrame({
#     "job_title": [
#         "Junior Data Analyst",
#         "Data Analyst",
#         "Senior Data Analyst",
#         "Junior Data Scientist",
#         "Data Scientist",
#         "Senior Data Scientist",
#         "Junior Data Engineer",
#         "Data Engineer",
#         "Senior Data Engineer",
#         "Analytics Engineer",
#         "BI Analyst",
#         "Machine Learning Engineer"
#     ],
#     "salary": [
#         7000,
#         10500,
#         16000,
#         8000,
#         14000,
#         21000,
#         7500,
#         13500,
#         20000,
#         14500,
#         9500,
#         120000
#     ]
# })
# df.head()
# scaler = RobustScaler()
# df['salary_scaled'] = scaler.fit_transform(df[['salary']])
# df.head()



#CD Python - 323

'''
Popraw błędy w kodzie.


import pandas as pd
from sklearn.linear_model import LinearRegression
df = pd.read_csv("mini-df.csv")
df = df[["price_per_m", "floor_no", "build_year", "area"]].dropna()

X = df[["price_per_m", "floor_no", "build_year"]]
y = df["area"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

model = LinearRegression()
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test)

from sklearn.metrics import root_mean_squared_error
rmse = root_mean_squared_error(y_train, y_pred)
print(round(rmse, 2))
'''


# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import StandardScaler
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import root_mean_squared_error

# df = pd.read_csv("mini-df.csv")
# df = df[["pe_per_m", "floor_no", "build_year", "area"]].dropna()

# X = df[["price_per_m", "floor_no", "build_year"]]
# y = df["area"]

# X_train, X_test, y_train, y_test = train_test_split(
#     X, 
#     y,
#     test_size=0.2,
#     random_state=42)

# scaler = StandardScaler()
# X_train_scaled = scaler.fit_transform(X_train) #po pierwsze skalowanie danych treningowych

# model = LinearRegression()
# model.fit(X_train_scaled, y_train) #trenowanie

# X_test_scaled = scaler.transform(X_test) #teraz ważne skalowanie danych testowych, ALE BEZ FIT, wykorzystujemy już wyuczone dane z danych treningowych
# y_pred = model.predict(X_test_scaled) #i dopiero predykcja na wyskalowanych danych testowych

# rmse = root_mean_squared_error(y_test, y_pred) #tu też był błąd - oczywiście chcemy dane y_test
# print(round(rmse, 2))




#CD Python - 324

'''
Która cecha ma największy wpływ na przewidywanie ceny za metr kwadratowy przy użyciu algorytmu lasu losowego?

Przypisz nazwę cechy/ kolumny do zmiennej top_feature.
'''



# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor
# import shap

# df = pd.read_csv("mini-df.csv")
# df = df[["price_per_m", "floor_no", "build_year", "area", "garage"]].dropna()


# X = df[["area", "floor_no", "build_year", "garage"]]
# y = df["price_per_m"]


# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model = RandomForestRegressor(random_state=42)
# model.fit(X_train, y_train)
# print(model.feature_importances_) #mozna też po prostu tak i też od razu widać, ta opcja była w zadaniu

# explainer = shap.TreeExplainer(model) #ja skorzystałem z shapa akurat
# shap_values = explainer(X_test)
# shap.plots.bar(shap_values)

# top_feature = 'build_year'