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


best_prices_by_tier = df.groupby(['brand', 'tier'])['price_pct_of_launch'].mean().groupby('brand').idxmax()
worst_prices_by_tier = df.groupby(['brand', 'tier'])['price_pct_of_launch'].mean().groupby('brand').idxmin()
print(best_prices_by_tier)
print(worst_prices_by_tier)
check_prices_by_tier = df.groupby(['brand', 'tier'])['price_pct_of_launch'].mean()
print(check_prices_by_tier)

#W7 D4 - T3
'''`transform('rank')` ranks individual rows within a group, not per-tier averages. 
Your output had one rank per row, not one per tier. The correct approach: aggregate first, then rank.
'''

tier_avg = df.groupby(['brand', 'tier'])['price_pct_of_launch'].mean().reset_index()
tier_avg['retention_rank'] = tier_avg.groupby('brand')['price_pct_of_launch'].rank(ascending=False)

df = df.merge(tier_avg, on = ['brand', 'tier'])
