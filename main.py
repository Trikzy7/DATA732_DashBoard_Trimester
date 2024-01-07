import json
import plotly.express as px
import pandas as pd
from api_search import get_event


# Opening JSON file
with open('topaz-data732--france--fr.sputniknews.africa--20190101--20211231.json') as json_file:
    data = json.load(json_file)

data_all = data['data-all']

dict_country_with_cities = {
    'Afghanistan': ['Kaboul', 'Herat', 'Mazar-e-Sharif', 'Kandahar'],
    'Albanie': ['Tirana', 'Durrës', 'Vlorë', 'Shkodër'],
    'Algérie': ['Alger', 'Oran', 'Constantine', 'Annaba'],
    'Andorre': ['Andorre-la-Vieille', 'Encamp', 'Escaldes-Engordany', 'La Massana'],
    'Angola': ['Luanda', 'Lobito', 'Huambo', 'Benguela'],
    'Antigua-et-Barbuda': ['Saint John', 'All Saints', 'Liberta', 'Bolans'],
    'Argentine': ['Buenos Aires', 'Córdoba', 'Rosario', 'Mendoza'],
    'Arménie': ['Erevan', 'Gyumri', 'Vanadzor', 'Ejmiatsin'],
    'Australie': ['Sydney', 'Melbourne', 'Brisbane', 'Perth'],
    'Autriche': ['Vienne', 'Graz', 'Linz', 'Salzbourg'],
    'Azerbaïdjan': ['Bakou', 'Gandja', 'Sumqayit', 'Mingachevir'],
    'Bahamas': ['Nassau', 'Freeport', 'Lucaya', 'Andros Town'],
    'Bahreïn': ['Manama', 'Muharraq', 'Riffa', 'Hamad Town'],
    'Bangladesh': ['Dacca', 'Chittagong', 'Khulna', 'Rajshahi'],
    'Barbade': ['Bridgetown', 'Speightstown', 'Oistins', 'Bathsheba'],
    'Biélorussie': ['Minsk', 'Gomel', 'Moguilev', 'Vitebsk'],
    'Belgique': ['Bruxelles', 'Anvers', 'Gand', 'Bruges'],
    'Belize': ['Belmopan', 'Belize City', 'San Ignacio', 'Orange Walk'],
    'Bénin': ['Porto-Novo', 'Cotonou', 'Parakou', 'Djougou'],
    'Bhoutan': ['Thimphu', 'Phuntsholing', 'Gelephu', 'Paro'],
    'Bolivie': ['La Paz', 'Sucre', 'Cochabamba', 'Santa Cruz de la Sierra'],
    'Bosnie-Herzégovine': ['Sarajevo', 'Banja Luka', 'Tuzla', 'Zenica'],
    'Botswana': ['Gaborone', 'Francistown', 'Molepolole', 'Serowe'],
    'Brésil': ['Brasília', 'São Paulo', 'Rio de Janeiro', 'Salvador'],
    'Brunei': ['Bandar Seri Begawan', 'Kuala Belait', 'Seria', 'Tutong'],
    'Bulgarie': ['Sofia', 'Plovdiv', 'Varna', 'Bourgas'],
    'Burkina Faso': ['Ouagadougou', 'Bobo-Dioulasso', 'Koudougou', 'Ouahigouya'],
    'Burundi': ['Bujumbura', 'Gitega', 'Ngozi', 'Rumonge'],
    'Cap-Vert': ['Praia', 'Mindelo', 'Assomada', 'Porto Novo'],
    'Cambodge': ['Phnom Penh', 'Siem Reap', 'Sihanoukville', 'Battambang'],
    'Cameroun': ['Yaoundé', 'Douala', 'Bamenda', 'Bafoussam'],
    'Canada': ['Ottawa', 'Toronto', 'Vancouver', 'Montréal'],
    'République centrafricaine': ['Bangui', 'Bimbo', 'Berbérati', 'Carnot'],
    'Tchad': ['N’Djamena', 'Moundou', 'Sarh', 'Abéché'],
    'Chili': ['Santiago', 'Valparaíso', 'Concepción', 'La Serena'],
    'Chine': ['Pékin', 'Shanghai', 'Guangzhou', 'Shenzhen'],
    'Colombie': ['Bogotá', 'Medellín', 'Cali', 'Barranquilla'],
    'Comores': ['Moroni', 'Mutsamudu', 'Fomboni', 'Domoni'],
    'Congo': ['Brazzaville', 'Pointe-Noire', 'Dolisie', 'Owando'],
    'Costa Rica': ['San José', 'Limon', 'San Francisco', 'Alajuela'],
    'Croatie': ['Zagreb', 'Split', 'Rijeka', 'Osijek'],
    'Cuba': ['La Havane', 'Santiago de Cuba', 'Camagüey', 'Holguín'],
    'Chypre': ['Nicosie', 'Limassol', 'Larnaca', 'Famagouste'],
    'Tchéquie': ['Prague', 'Brno', 'Ostrava', 'Pilsen'],
    'Danemark': ['Copenhague', 'Aarhus', 'Odense', 'Aalborg'],
    'Djibouti': ['Djibouti', 'Ali Sabieh', 'Tadjoura', 'Obock'],
    'Dominique': ['Roseau', 'Portsmouth', 'Marigot', 'Berekua'],
    'République dominicaine': ['Saint-Domingue', 'Santiago de los Caballeros', 'Saint-Domingue Ouest', 'La Romana'],
    'Timor oriental (Timor-Leste)': ['Dili', 'Maliana', 'Suai', 'Baucau'],
    'Équateur': ['Quito', 'Guayaquil', 'Cuenca', 'Santo Domingo de los Colorados'],
    'Égypte': ['Le Caire', 'Alexandrie', 'Gizeh', 'Shubra El Kheima'],
    'Salvador': ['San Salvador', 'Santa Ana', 'San Miguel', 'Mejicanos'],
    'Guinée équatoriale': ['Malabo', 'Bata', 'Ebebiyin', 'Aconibe'],
    'Érythrée': ['Asmara', 'Keren', 'Massawa', 'Assab'],
    'Estonie': ['Tallinn', 'Tartu', 'Narva', 'Pärnu'],
    'Eswatini': ['Mbabane', 'Manzini', 'Lobamba', 'Siteki'],
    'Éthiopie': ['Addis-Abeba', 'Dire Dawa', 'Mekelle', 'Gondar'],
    'Fidji': ['Suva', 'Nadi', 'Lautoka', 'Labasa'],
    'Finlande': ['Helsinki', 'Espoo', 'Tampere', 'Vantaa'],
    'France': ['Paris', 'Marseille', 'Lyon', 'Toulouse'],
    'Gabon': ['Libreville', 'Port-Gentil', 'Franceville', 'Oyem'],
    'Gambie': ['Banjul', 'Serekunda', 'Brikama', 'Bakau'],
    'Géorgie': ['Tbilissi', 'Koutaïssi', 'Batoumi', 'Roustavi'],
    'Allemagne': ['Berlin', 'Hambourg', 'Munich', 'Cologne'],
    'Ghana': ['Accra', 'Kumasi', 'Tamale', 'Sekondi-Takoradi'],
    'Grèce': ['Athènes', 'Thessalonique', 'Patras', 'Le Pirée'],
    'Grenade': ['Saint-Georges', 'Gouyave', 'Grenville', 'Victoria'],
    'Guatemala': ['Guatemala', 'Mixco', 'Villa Nueva', 'Quetzaltenango'],
    'Guinée': ['Conakry', 'Nzérékoré', 'Kankan', 'Kindia'],
    'Guinée-Bissau': ['Bissau', 'Bafatá', 'Gabú', 'Bissorã'],
    'Guyana': ['Georgetown', 'Linden', 'New Amsterdam', 'Bartica'],
    'Haïti': ['Port-au-Prince', 'Cap-Haïtien', 'Carrefour', 'Delmas'],
    'Honduras': ['Tegucigalpa', 'San Pedro Sula', 'Choloma', 'La Ceiba'],
    'Hongrie': ['Budapest', 'Debrecen', 'Szeged', 'Miskolc'],
    'Islande': ['Reykjavik', 'Kópavogur', 'Hafnarfjörður', 'Akureyri'],
    'Inde': ['New Delhi', 'Bombay', 'Calcutta', 'Chennai'],
    'Indonésie': ['Jakarta', 'Surabaya', 'Bandung', 'Medan'],
    'Iran': ['Téhéran', 'Mashhad', 'Ispahan', 'Karaj'],
    'Irak': ['Bagdad', 'Bassora', 'Mossoul', 'Erbil'],
    'Irlande': ['Dublin', 'Cork', 'Limerick', 'Galway'],
    'Israël': ['Jérusalem', 'Tel Aviv', 'Haïfa', 'Rishon LeZion'],
    'Italie': ['Rome', 'Milan', 'Naples', 'Turin'],
    'Côte d\'Ivoire': ['Abidjan', 'Bouaké', 'Daloa', 'Yamoussoukro'],
    'Jamaïque': ['Kingston', 'New Kingston', 'Spanish Town', 'Montego Bay'],
    'Japon': ['Tokyo', 'Yokohama', 'Osaka', 'Nagoya'],
    'Jordanie': ['Amman', 'Zarqa', 'Irbid', 'Russeifa'],
    'Kazakhstan': ['Noursoultan', 'Almaty', 'Karaganda', 'Chymkent'],
    'Kenya': ['Nairobi', 'Mombasa', 'Kisumu', 'Nakuru'],
    'Kiribati': ['Tarawa Sud', 'Betio', 'Bikenibeu', 'Teinainano Urban'],
    'Corée du Nord': ['Pyongyang', 'Hamhung', 'Chongjin', 'Nampo'],
    'Corée du Sud': ['Séoul', 'Busan', 'Incheon', 'Daegu'],
    'Kosovo': ['Pristina', 'Pec', 'Gjakova', 'Mitrovica'],
    'Koweït': ['Koweït', 'Al Ahmadi', 'Hawalli', 'As-Salimiyah'],
    'Kirghizistan': ['Bichkek', 'Och', 'Jalal-Abad', 'Karakol'],
    'Laos': ['Vientiane', 'Pakse', 'Savannakhet', 'Luang Prabang'],
    'Lettonie': ['Riga', 'Daugavpils', 'Liepaja', 'Jelgava'],
    'Liban': ['Beyrouth', 'Tripoli', 'Sidon', 'Tyre'],
    'Lesotho': ['Maseru', 'Teyateyaneng', 'Mafeteng', 'Hlotse'],
    'Libéria': ['Monrovia', 'Gbarnga', 'Kakata', 'Harper'],
    'Libye': ['Tripoli', 'Benghazi', 'Misrata', 'Tobrouk'],
    'Liechtenstein': ['Vaduz', 'Schaan', 'Triesen', 'Balzers'],
    'Lituanie': ['Vilnius', 'Kaunas', 'Klaipėda', 'Šiauliai'],
    'Luxembourg': ['Luxembourg', 'Esch-sur-Alzette', 'Differdange', 'Dudelange'],
    'Madagascar': ['Antananarivo', 'Toamasina', 'Antsirabe', 'Fianarantsoa'],
    'Malawi': ['Lilongwe', 'Blantyre', 'Mzuzu', 'Zomba'],
    'Malaisie': ['Kuala Lumpur', 'George Town', 'Ipoh', 'Shah Alam'],
    'Maldives': ['Malé', 'Addu City', 'Fuvahmulah', 'Kulhudhuffushi'],
    'Mali': ['Bamako', 'Sikasso', 'Mopti', 'Ségou'],
    'Malte': ['La Valette', 'Birkirkara', 'Mosta', 'Qormi'],
    'Îles Marshall': ['Majuro', 'Kwajalein', 'Arno', 'Wotje'],
    'Mauritanie': ['Nouakchott', 'Nouadhibou', 'Zouerate', 'Kaedi'],
    'Maurice': ['Port-Louis', 'Beau Bassin-Rose Hill', 'Vacoas-Phoenix', 'Curepipe'],
    'Mexique': ['Mexico', 'Guadalajara', 'Monterrey', 'Puebla'],
    'Micronésie': ['Palikir', 'Weno', 'Kolonia', 'Toyn Town'],
    'Moldavie': ['Chisinau', 'Tiraspol', 'Bălți', 'Bender'],
    'Monaco': ['Monaco', 'Monte-Carlo', 'La Condamine', 'Fontvieille'],
    'Mongolie': ['Oulan-Bator', 'Erdenet', 'Darkhan', 'Choibalsan'],
    'Monténégro': ['Podgorica', 'Niksic', 'Pljevlja', 'Herceg Novi'],
    'Maroc': ['Rabat', 'Casablanca', 'Fès', 'Marrakech'],
    'Mozambique': ['Maputo', 'Matola', 'Beira', 'Nampula'],
    'Myanmar': ['Naypyidaw', 'Rangoun', 'Mandalay', 'Taunggyi'],
    'Namibie': ['Windhoek', 'Swakopmund', 'Walvis Bay', 'Oshakati'],
    'Nauru': ['Yaren', 'Denigomodu', 'Anabar', 'Uaboe'],
    'Népal': ['Katmandou', 'Pokhara', 'Lalitpur', 'Bharatpur'],
    'Pays-Bas': ['Amsterdam', 'Rotterdam', 'La Haye', 'Utrecht'],
    'Nouvelle-Zélande': ['Wellington', 'Auckland', 'Christchurch', 'Hamilton'],
    'Nicaragua': ['Managua', 'León', 'Masaya', 'Matagalpa'],
    'Niger': ['Niamey', 'Zinder', 'Maradi'],
     'Nigeria': ['Abuja', 'Lagos', 'Kano', 'Ibadan'],
    'Macédoine du Nord': ['Skopje', 'Bitola', 'Kumanovo', 'Prilep'],
    'Norvège': ['Oslo', 'Bergen', 'Stavanger', 'Trondheim'],
    'Oman': ['Mascate', 'Seeb', 'Salalah', 'Bawshar'],
    'Pakistan': ['Islamabad', 'Karachi', 'Lahore', 'Faisalabad'],
    'Palaos': ['Ngerulmud', 'Koror', 'Melekeok', 'Ngaraard'],
    'Panama': ['Panama', 'San Miguelito', 'Tocumen', 'David'],
    'Papouasie-Nouvelle-Guinée': ['Port Moresby', 'Lae', 'Arawa', 'Mount Hagen'],
    'Paraguay': ['Asuncion', 'San Lorenzo', 'Luque', 'Capiata'],
    'Pérou': ['Lima', 'Arequipa', 'Callao', 'Trujillo'],
    'Philippines': ['Manille', 'Quezon City', 'Davao City', 'Cebu City'],
    'Pologne': ['Varsovie', 'Cracovie', 'Łódź', 'Wrocław'],
    'Portugal': ['Lisbonne', 'Porto', 'Amadora', 'Braga'],
    'Qatar': ['Doha', 'Al Rayyan', 'Umm Salal', 'Al Wakrah'],
    'Roumanie': ['Bucarest', 'Cluj-Napoca', 'Timisoara', 'Iasi'],
    'Russie': ['Moscou', 'Saint-Pétersbourg', 'Novossibirsk', 'Iekaterinbourg'],
    'Rwanda': ['Kigali', 'Butare', 'Gitarama', 'Ruhengeri'],
    'Saint-Christophe-et-Niévès': ['Basseterre', 'Charlestown', 'Dieppe Bay Town', 'Half Way Tree'],
    'Sainte-Lucie': ['Castries', 'Vieux Fort', 'Micoud', 'Soufrière'],
    'Saint-Vincent-et-les-Grenadines': ['Kingstown', 'Kingstown Park', 'Georgetown', 'Byera Village'],
    'Samoa': ['Apia', 'Vaitele', 'Faleula', 'Siusega'],
    'Saint-Marin': ['Saint-Marin', 'Serravalle', 'Borgo Maggiore', 'Domagnano'],
    'Sao Tomé-et-Principe': ['Sao Tomé', 'Neves', 'Santo Amaro', 'Guadalupe'],
    'Arabie saoudite': ['Riyad', 'Djeddah', 'La Mecque', 'Médine'],
    'Sénégal': ['Dakar', 'Thiès', 'Kaolack', 'Ziguinchor'],
    'Serbie': ['Belgrade', 'Novi Sad', 'Niš', 'Kragujevac'],
    'Seychelles': ['Victoria', 'Anse Etoile', 'Takamaka', 'Cascade'],
    'Sierra Leone': ['Freetown', 'Kenema', 'Bo', 'Koidu'],
    'Singapour': ['Singapour', 'Woodlands', 'Tampines', 'Jurong West'],
    'Slovaquie': ['Bratislava', 'Kosice', 'Presov', 'Nitra'],
    'Slovénie': ['Ljubljana', 'Maribor', 'Celje', 'Kranj'],
    'Îles Salomon': ['Honiara', 'Auki', 'Gizo', 'Kirakira'],
    'Somalie': ['Mogadiscio', 'Hargeisa', 'Berbera', 'Kismayo'],
    'Afrique du Sud': ['Pretoria', 'Le Cap', 'Durban', 'Johannesburg'],
    'Soudan du Sud': ['Juba', 'Wau', 'Malakal', 'Bor'],
    'Espagne': ['Madrid', 'Barcelone', 'Valence', 'Séville'],
    'Sri Lanka': ['Colombo', 'Dehiwala-Mount Lavinia', 'Moratuwa', 'Negombo'],
    'Soudan': ['Khartoum', 'Omdurman', 'Kassala', 'Port-Soudan'],
    'Surinam': ['Paramaribo', 'Lelydorp', 'Brokopondo', 'Nieuw Nickerie'],
    'Suède': ['Stockholm', 'Göteborg', 'Malmö', 'Uppsala'],
    'Suisse': ['Zurich', 'Genève', 'Bâle', 'Lausanne'],
    'Syrie': ['Damas', 'Alep', 'Homs', 'Hama'],
    'Taïwan': ['Taipei', 'New Taipei', 'Kaohsiung', 'Taichung'],
    'Tadjikistan': ['Douchanbé', 'Khodjent', 'Koulob', 'Kourgan-Tioube'],
    'Tanzanie': ['Dodoma', 'Dar es Salaam', 'Mwanza', 'Arusha'],
    'Thaïlande': ['Bangkok', 'Nonthaburi', 'Nakhon Ratchasima', 'Chiang Mai'],
    'Togo': ['Lomé', 'Sokodé', 'Kara', 'Atakpamé'],
    'Tonga': ['Nuku\'alofa', 'Neiafu', 'Pangai', 'Ohonua'],
    'Trinité-et-Tobago': ['Port-dEspagne', 'Chaguanas', 'San Fernando', 'Arima'],
    'Tunisie': ['Tunis', 'Sfax', 'Sousse', 'Kairouan'],
    'Turquie': ['Ankara', 'Istanbul', 'Izmir', 'Bursa'],
    'Turkménistan': ['Achgabat', 'Turkmenabad', 'Dasoguz', 'Mary'],
    'Tuvalu': ['Funafuti', 'Fongafale', 'Vaiaku', 'Tanrake'],
    'Ouganda': ['Kampala', 'Gulu', 'Lira', 'Mbarara'],
    'Ukraine': ['Kiev', 'Kharkiv', 'Odessa', 'Dnipro'],
    'Émirats arabes unis': ['Abou Dabi', 'Dubai', 'Charjah', 'Al Ain'],
    'Royaume-Uni': ['Londres', 'Birmingham', 'Manchester', 'Glasgow'],
    'États-Unis': ['Washington', 'New York', 'Los Angeles', 'Chicago'],
    'Uruguay': ['Montevideo', 'Salto', 'Ciudad de la Costa', 'Paysandu'],
    'Ouzbékistan': ['Tachkent', 'Namangan', 'Andijan', 'Samarkand'],
    'Vanuatu': ['Port-Vila', 'Luganville', 'Norsup', 'Port-Olry'],
    'Cité du Vatican': ['Cité du Vatican', 'Cité du Vatican', 'Cité du Vatican', 'Cité du Vatican'],
    'Venezuela': ['Caracas', 'Maracaibo', 'Valence', 'Barquisimeto'],
    'Vietnam': ['Hanoï', 'Hô Chi Minh-Ville', 'Haiphong', 'Da Nang'],
    'Yémen': ['Sanaa', 'Aden', 'Taëz', 'Hodeïda'],
    'Zambie': ['Lusaka', 'Ndola', 'Kitwe', 'Kabwe'],
    'Zimbabwe': ['Harare', 'Bulawayo', 'Chitungwiza', 'Mutare']
}

# print(list(dict_country_with_cities.keys())[0])


def get_five_kws_articles(data_all):
    """
    GOAL : Get the 5 first key words and locs of each articles
    :param data_all: dictionnary with all the data
    :return: dict with:  all year -> months group by trimester -> date_start, date_end, dict articles with his kws.
    :example :
        {
            // -- trimestre 1
	        0 : {
				date_start: 01-2019,
				date_end: 03-2019,
				nb_days: 90,
				articles: {
					nbMonth_nbDay_idArticle : {
						keywords : [kw1, kw2, kw3, kw4, kw5],
						locs : [loc1, loc2, loc3, loc4, loc5]
					},
					1_27_0 : {
						keywords : [kw1, kw2, kw3, kw4, kw5],
						locs : [loc1, loc2, loc3, loc4, loc5]
					},
					1_28_0 : {
						keywords : [kw1, kw2, kw3, kw4, kw5],
						locs : [loc1, loc2, loc3, loc4, loc5]
					},
					...
				}
			},
		}
    """

    dict_with_year_with_trimester_5_kw_articles = {}


    # -- Pour chaque année
    for year in data_all:
        # -- Pour chaque trimestre
            # -- Get ids of months in a list
        list_months = list(data_all[year].keys())
            # -- Convert ids in the list
        list_months = [ int(id_month) for id_month in list_months ]
            # -- Sorted ids in the list
        list_months.sort()

        dict_5_kw_articles_by_trimester_for_one_year = {}

        # -- Get 3 first months, then the 3 following, then the 3 following:
        for num_trimester in range(0, 4):

            # -- Prendre 3 mois par 3 mois -> list_months[0:3], puis list_months[3:6], puis ...
            start_trimester = num_trimester * 3
            end_trimester = num_trimester * 3 + 3

            # -- Get the months and the content's months of the current semester
            months_current_trimester_with_content = {month: data_all[year][month]
                                                        for month, content in data_all[year].items()
                                                            if start_trimester < int(month) <= end_trimester
                                                    }

            # print(months_current_trimester_with_content)

            # -- Get all the article of months of the current trimester pour les mettre au même niveau dans le json file
                # -- Reset le dict a chaque trimestre
            articles_current_trimester = {}

            for month, days in months_current_trimester_with_content.items():
                for day, articles in data_all[year][month].items():
                    for id_article, article in enumerate(data_all[year][month][day]):
                        articles_current_trimester.update({
                            str(month) + "_" + str(day) + "_" + str(id_article): {
                                'kws': sorted(article['kws'], key=lambda x: article['kws'][x], reverse=True)[:5],
                                'locs': sorted(article['loc'], key=lambda x: article['loc'][x], reverse=True)[:5]
                            }
                        })


            # -- Get nb days in current trimester
            nb_days_current_trimester = 0

            for idMonth, content in months_current_trimester_with_content.items():
                nb_days_current_trimester += len(data_all[year][idMonth])

            dict_5_kw_articles_by_trimester_for_one_year.update({num_trimester: {
                    'date_start': start_trimester + 1,
                    'date_end': end_trimester,
                    'nb_days': nb_days_current_trimester,
                    'articles': articles_current_trimester
                }})

        dict_with_year_with_trimester_5_kw_articles[year] = dict_5_kw_articles_by_trimester_for_one_year

    return dict_with_year_with_trimester_5_kw_articles


def get_five_kws_trimester(dict_with_year_with_trimester_5_kw_articles):
    """
    GOAL : Avoir les 5 key words qui reviennent le plus au cours d'un trimestre pour chaque trimestre de chaque année
    :param dict_with_year_with_trimester_5_kw_articles:
    :return: dict same as the method 'get_five_kws_articles' but there is no anymore attribute 'months' but kew_words of the trimester
    """

    # -- For each year
    for year in dict_with_year_with_trimester_5_kw_articles:
        # -- For each trimester
        for trimester in dict_with_year_with_trimester_5_kw_articles[year]:

            # -- Dict pour avoir tous les key words d'un trimestre et avoir le nombre de fois qu'ils sont apparus {kw1: 4, kw2: 7, kw3: 1, ...}
            kw_value_trimestre = {}

            # -- For each article
            for article, content in dict_with_year_with_trimester_5_kw_articles[year][trimester]['articles'].items():
                for kw in content['kws']:
                    if kw not in kw_value_trimestre:
                        kw_value_trimestre[kw] = 0
                    else:
                        kw_value_trimestre[kw] += 1


            # -- Récupérer les 7 mots clés qui sont revenu le plus ce trimestre dans une list
            kws_7_in_trimester = sorted(kw_value_trimestre, key=lambda x: kw_value_trimestre[x], reverse=True)[:7]

            # -- Pour les 7 kws qui sont le plus revenu -> les mettre dans notre dict final avec leur fréquence
            # d'apparition par jour calculée (frequence = value/nb_of_days)
            kw_value_freq_trimestre = {}
            for kw in kws_7_in_trimester:
                kw_value_freq_trimestre[kw] = kw_value_trimestre[kw] / dict_with_year_with_trimester_5_kw_articles[year][trimester]['nb_days']

            dict_with_year_with_trimester_5_kw_articles[year][trimester]['kws'] = kw_value_freq_trimestre

    return dict_with_year_with_trimester_5_kw_articles


def get_five_locs_trimester(dict_five_kws_trimester, dict_country_with_cities):
    """
    GOAL : Avoir les 5 locations qui reviennent le plus au cours d'un trimestre pour chaque trimestre de chaque année
    :param dict_with_year_with_trimester_5_kw_articles:
    :return: dict same as the method 'get_five_kws_articles' but there is no anymore attribute 'months' but kew_words of the trimester
    """

    # -- For each year
    for year in dict_five_kws_trimester:
        # -- For each trimester
        for trimester in dict_five_kws_trimester[year]:

            # -- Dict pour avoir tous les locs d'un trimestre et avoir le nombre de fois qu'ils sont apparus {loc1: 4, loc2: 7, loc3: 1, ...}
            locs_value_trimestre = {}

            # -- For each article
            for article, content in dict_five_kws_trimester[year][trimester]['articles'].items():
                for loc in content['locs']:
                    # Si la loc n'est pas dans la liste de tous les pays du monde ou dans la liste de leurs
                    # villes principales
                    if loc in list(dict_country_with_cities.keys()):
                        # - Si il n'est pas déjà présent dans les pays qu'on recup pour un trimestre
                        if (loc not in locs_value_trimestre):
                            locs_value_trimestre[loc] = 0
                        else:
                            locs_value_trimestre[loc] += 1


            # -- Récupérer les 7 mots clés qui sont revenu le plus ce trimestre dans une list
            locs_7_in_trimester = sorted(locs_value_trimestre, key=lambda x: locs_value_trimestre[x], reverse=True)[:4]

            # -- Pour les 7 kws qui sont le plus revenu -> les mettre dans notre dict final avec leur fréquence
            # d'apparition par jour calculée (frequence = value/nb_of_days)
            locs_value_freq_trimestre = {}
            for loc in locs_7_in_trimester:
                locs_value_freq_trimestre[loc] = locs_value_trimestre[loc] / dict_five_kws_trimester[year][trimester]['nb_days']

            dict_five_kws_trimester[year][trimester]['locs'] = locs_value_freq_trimestre

    return dict_five_kws_trimester


def get_event_trimester(dict_with_year_with_trimester_5_kw_articles):
    """
    GOAL : Get l'event marquant pour tous les trimestres recherché avec les keys words et la date
    :param dict_with_year_with_trimester_5_kw_articles:
    :return: dict same as the method get_event_trimester with the event added
    """

    # -- For each year
    for year in dict_with_year_with_trimester_5_kw_articles:
        # -- For each trimester
        for trimester in dict_with_year_with_trimester_5_kw_articles[year]:

            # -- S'il y a des keywords pour ce trimestre
            if len(dict_with_year_with_trimester_5_kw_articles[year][trimester]['kws']) != 0:
                # -- Ajouter la date au kws pour faire la recherche
                listKeyWords = list(dict_with_year_with_trimester_5_kw_articles[year][trimester]['kws'].keys())
                search_words = listKeyWords + ['trimestre ' + str(trimester+1), year]


                # -- Ajouter l'event'
                dict_with_year_with_trimester_5_kw_articles[year][trimester]['event'] = get_event(search_words)

    return dict_with_year_with_trimester_5_kw_articles


def do_dict_trimester(data_all, dict_country_with_cities):
    """
    GOAL : Faire les différents traitements pour avoir le dict final des trimestre
    :param data_all: dict with all data
    :return: dict avec tous les traitements effectués
    """

    # -- GET 5 Key Words
    dict_with_year_with_trimester_5_kw_articles = get_five_kws_articles(data_all)
    dict_five_kws_trimester = get_five_kws_trimester(dict_with_year_with_trimester_5_kw_articles)

    # -- GET Locations
    dict_five_locs_trimester = get_five_locs_trimester(dict_five_kws_trimester, dict_country_with_cities)

    # -- GET Event
    dict_event_trimester = get_event_trimester(dict_five_locs_trimester)

    return dict_event_trimester


def write_dict_in_json(name_file, dict_data):
    with open(name_file, 'w') as file_json:
        json.dump(dict_data, file_json)


def do_bar_chart(dict:dict, columns:list, title:str):
    """
    GOAL : Create a bar chart
    :param dict: data you want make a bar chart
    :param columns: list containing names of columns
    :param title: chart's title
    :return: void
    """
    dataFrame_of_dict = pd.DataFrame(dict.items(), columns=columns)

    fig = px.bar(dataFrame_of_dict, x=columns[0], y=columns[1], title=title)
    fig.show()


# -- FUNCTION CALLS
# dict_trimester = do_dict_trimester(data_all)
# dict_5_kw_first_step = get_five_kws_articles(data_all)
# dict_5_kw_second_step = get_five_kws_trimester(dict_5_kw_first_step)
# dict_locs = get_five_locs_trimester(dict_5_kw_second_step)

dict_trimester = do_dict_trimester(data_all, dict_country_with_cities)
write_dict_in_json('trimester/trimester_5_kws_topaz-data732--france--fr.sputniknews.africa--20190101--20211231.json', dict_trimester)
# do_bar_chart( dict_five_kws_trimester['2020'][0]['kws'], ['word', 'freq'], "Mots qui apparaissent le plus ce trimestre" )













