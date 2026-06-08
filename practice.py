#I will be putting the CD Python course for Data Anylsis tasks here
#Please note that the .csv dataframes (as mini-df.csv) are loaded in a webapp environment and I don't have them here, so I'm not able to load them.
#I'm running them in that environment and actually testing here only the ones that can be launched (as in T203 below)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

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