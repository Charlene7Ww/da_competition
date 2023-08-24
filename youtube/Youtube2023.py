#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_csv('Global YouTube Statistics.csv', encoding = 'latin-1')
df


# In[4]:


df.info()


# In[4]:


df.describe()


# In[5]:


df = df.dropna(subset = ['created_date'])
df


# In[6]:


df['date'] = df['created_year'].astype(int).astype(str) + ',' + df['created_month'] + ',' + df['created_date'].astype(int).astype(str)


# In[7]:


df


# In[8]:


# df.to_csv('Global YouTube Statistics.csv', index=False)


# In[9]:


# Creating word cloud

for i in df['Title']:
    print(i)


# In[10]:


text ='''T-Series
youtubemovies
MrBeast
Cocomelon - Nursery Rhymes
SET India
Music
ýýý Kids Diana Show
PewDiePie
Like Nastya Vlog
Vlad and Niki
Zee Music Company
WWE
Gaming
BLACKPINK
goldmines
Sony SAB
5-Minute Crafts 2.0
BANGTANTV
sports
Justin Bieber
HYBE LABELS
Zee TV
Pinkfong Baby Shark - Kids' Songs & Stories
Canal KondZilla
ChuChu TV Nursery Rhymes & Kids Songs
Shemaroo Filmi Gaane
Colors TV
T- SERIES BHAKTI SAGAR
Dude Perfect
Movieclips
Tips Official
El Reino Infantil
Wave Music
Aaj Tak
Sony Music India
EminemMusic
Marshmello
YRF
LooLoo Kids - Nursery Rhymes and Children's ï¿½
Ed Sheeran
Infobells - Hindi
Taylor Swift
Ariana Grande
BillionSurpriseToys  - Nursery Rhymes & Cartï¿½
JuegaGerman
Billie Eilish
Get Movies
Shemaroo
badabun
SonyMusicIndiaVEVO
aefour
badbunny
Fernanfloo
Voot Kids
Felipe Neto
Vocï¿½ï¿½ï¿½
HAR PAL GEO
brightside
Katy Perry
whinderssonnunes
ABS-CBN Entertainment
alanwalker
holasoygerman. 2
Shakira
ýýýýýýýý ýý ýýýýýýýýýýýýýý
ARY Digital HD
Speed Records
Masha and The Bear
Like Nastya Show
Rihanna
Ishtar Music
Kimberly Loaiza
Little Baby Bum - Nursery Rhymes & Kids Songs
Luis Arturo Villar Sudek
elrubiusOMG
Toys and colors
shfa2 - ï¿½ï¿½
LUCCAS NETO- LUCCAS TOON
CarryMinati
XXXTENTACION
Super Simple Songs - Kids Songs
Mikecrack
WorkpointOfficial
GR6 EXPLODE
TEDx Talks
ýýýýýýýýýý ýýýýýý
Goldmines Gaane Sune Ansune
21 Savage
TheEllenShow
Sony PAL
Daddy Yankee
Vlad vï¿½ï¿½ï
Like Nastya ESP
ýýýýýýýýýýýý one31
Jkk Entertainment
ABP NEWS
Maria Clara & JP
Bruno Mars
Maroon 5
Ultra Bollywood
PowerKids TV
YouTube
News
Ozuna
MrBeastGaming
La Granja de Zenï¿½
Saregama Music
IndiaTV
T-Series Bollywood Classics
totalgaming
Markiplier
Ryan's World
Genevieve's Playhouse - Learning Videos for ï¿½
T- Series Apna Punjab
TechnoGamerz
Geet MP3
J Balvin
Jess No Limit
Jingle Toons
VEGETTA777
Galinha Pintadinha
SSSniperWolf
Desi music factory
Selena Gomez
Rajshri
Ch3Thailand
KHANDESHI MOVIES
NoCopyrightSounds
CVS 3D Rhymes & Kids Songs
Ricis Official
BabyBus - Kids Songs and Cartoons
Mzaalo
BETER Bï¿½ï¿½
DisneyMusicVEVO
The Weeknd
wowkidz
KAROL G
Mr Bean
rezendeevil
StarPlus
SMTOWN
GMA  Network
GENIAL
MR. INDIAN HACKER
Worldwide Records Bhojpuri
DONA ï¿½ï¿½
Dream
Lucas and Marcus
JustinBieberVEVO
luisfonsi
Peppa Pig - Official Channel
YOLO AVENTURAS
The Tonight Show Starring Jimmy Fallon
TheDonato
ImagineDragons
Diana and Roma ESP
Round2hell
Zee News
AboFlah
AH
Trap Nation
ýýýýýýýýýýýýýýý ýýýýýý ýýýýýýýýýýýýýýýýýý
Boram Tube Vlog [ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿
Adele
TalkingTom
ýýýýýýýý ýýýýýýýý ýýýýýýýýýý | toyoraljanahtv
frostdiamond
Spinnin' Records
Little Angel: Nursery Rhymes & Kids Songs
jacksepticeye
Shawn Mendes
ashish chanchlani vines
Ultra Records
Popular on Youtube
MaLuMa
Zhong
Enaldinho
AuronPlay
shorts break
infobells - Tamil
Aditya Music
The Late Late Show with James Corden
Aditya Movies
Masha y El oso
infobells - Telugu
HUM TV
Shemaroo Movies
Michael Jackson
drake
Goldmines Dishoom
Sandeepmaheshwari
Bounce Patrol - Kids Songs
toycantando
Leaux Pass
Wiz Khalifa
JYP Entertainment
ýýý Kids Roma Show
DanTDM
Nick Jr.
Crazy XYZ
ToyPudding TV[ï¿½ï¿½ï¿½ï¿½ï
Dushyant kukreja
Gulshan Kalra
Brent Rivera
Renato Garcia YT
Beast Reacts
enchufetv
Netflix
Raffy Tulfo in Action
WORLDSTARHIPHOP
Goldmines Bollywood
Alan Chikin Chow
PANDA BOI
BB Ki Vines
D Billions
Junya.ï¿½ï¿½ï¿½ï¿½
Smosh
1MILLION Dance Studio
NichLmao
Beyoncï¿
mariliamendonca
Indosiar
VanossGaming
David Guetta
LosPolinesios
Nicki Minaj
Fede Vigevani
TaylorSwiftVEVO
zhc
Post Malone
Rans Entertainment
LankyBox
Coldplay
LAS RATITAS
WB Kids
ABPLIVE
The Lallantop
RihannaVEVO
WatchMojo.com
TRANS7 OFFICIAL
Anuel AA
Dan Rhodes
Yuya
America's Got Talent
mujjuu___14
EminemVEVO
Chloe Ting
KatyPerryVEVO
Mark Rober
1theK (ï¿½ï¿½ï¿½ï¿½ï
Like Nastya AE
Amit Bhadana
Pen Movies
MrBeast en Espaï¿½ï
shfa show India
Super JoJo - Nursery Rhymes & Kids Songs
Alejo Igoa
Daniel LaBelle
netd mï¿½ï¿
DJ Snake
Diana and Roma ARA
KSI
Spider Slack
Ti Ti
Preston
James Charles
Collins Key
Diana and Roma EN
Venus Entertainment
Troom Troom
Enrique Iglesias
Ninja
FaZeRug
Mister Max
That Little Puff
NickyJamTV
Juan De Dios Pantoja
Logan Paul
Maya and Mary
Peppa Pig Espaï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½
Jelly
Miss Katy
Tilak
Valentina Pontes ofc
Sesame Street
Happy Lives
Lady Gaga
Akshay Nagwadiya
Wave Music Bhojpuri
GMM GRAMMY OFFICIAL
TED
unknown boy varun
Kids TV - Nursery Rhymes And Baby Songs
Tsuriki Show
Technical Guruji
DrossRotzank
White Hill Music
Ultra Movie Parlour
Alan Becker
toyorbabytv
BabyBus - Canciones Infantiles & Videos paraï¿½
KL BRO Biju Rithvik
Vania Mania Kids
Like Nastya PRT
Sun TV
Heroindori
The Chainsmokers
mmoshaya
Sia
LeoNata Family
Goldmines Cineplex
Vlad and Niki Arabic
SSundee
Paulo Londra
SMILE Family
FGTeeV
Kinder Spielzeug Kanal (Kidibli)
Charlie Puth
Vlad and Niki ESP
Sagawa /ï¿½ï¿½ï¿½
Ben Azelart
Zach Choi ASMR
Topper Guild
disneylatinoamerica
Stokes Twins
National Geographic
Dua Lipa
OneDirectionVEVO
rotana5018
NETFLIX INDIA
Sourav Joshi Vlogs
ZAMZAM ELECTRONICS TRADING
DUDU e CAROL
Village Cooking Channel
Eva Bravo Play
Tekashi 6ix9ine
tlnovelas
Claudio
INVICTOR
YOLO
Sidhu Moose Wala
The Royalty Family
Becky G
Ishaan Ali 11
Infinite
Azhan5star
Dangal TV Channel
KHAN GS RESEARCH CENTRE
GMA Public  Affairs
Tasty
Baim Paula
nigahiga
Rafa & Luiz
Lyrical Lemonade
Vlad and Niki IDN
Dr. Vivek Bindra: Motivational Speaker
Fatos Desconhecidos
Brave Wilderness
LIV Crime
Minecraft - Topic
RomeoSantos
Canal Canalha
Kurzgesagt ï¿½ï¿½ï¿½ï¿½ï¿½ï¿
Yoeslan
5-Minute Crafts DIY
Zach King
tuzelity SHUFFLE
NBA
deddycorbuzier
Bizarrap
Avicii
Mnet K-POP
LazarBeam
Ninja Kidz TV
Totoy kids - Portuguï¿½
Jake Paul
linkinpark
Vijay Television
SlivkiShow
Emiway Bantai
Got Talent Global
ýýýýýýýýýýýýýýý - Genevieve's Playhouse
BabyBus - Cerita & Lagu Anak-anak
Ami Rodriguez
Noor Stars
FamilyGamesTV
Kiddiestv Hindi - Nursery Rhymes & Kids Songs
dednahype
Marta and Rustam
MiawAug
CookieSwirlC
Skrillex
AuthenticGames
Homem Aranha player
Pencilmation
7clouds
5-Minute Crafts PLAY
MarvelEntertainment
BuzzFeedVideo
REACT
Vevo
Gordon Ramsay
pentatonix
Green Gold TV - Official Channel
Gusttavo Lima Oficial
HaerteTest
Crafty Panda
TIME NEWS
JennaMarbles
Troom Troom Es
OfficialPinkPanther
Britain's Got Talent
SCTV
ASGaming
Sony AATH
tabii Urdu
DaFuq!?Boom!
Clash of Clans
RKD Studios
DLS News
JukiLop
etvteluguindia
FIFA
Manoj  parihar
Vsauce
Unbox Therapy
shane
Sonotek
Jimmy Kimmel Live
TheOdd1sOut
Goldmines Great Indian Comedy
Lil Nas X
ýýýýýýýýýýýýýý ýýýý
SUPER SLICK SLIME SAM
Wow Kidz Action
Turma da Mï¿½ï¿½
Calvin Harris
KBS WORLD TV
HiMan
Masha e o Urso
Little Angel Espaï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½
TED-Ed
Sidemen
Cardi B
TG MAYANK YT
Farruko
ýýýýýýýýýýýýýýýýýýýýýý
Triggered Insaan
cKn
ali-a
Shemaroo Comedy
Smile Family Spanish
GRAMMY GOLD OFFICIAL
ýýýýýýýý ýýýýýýýýýý ýýýýýýýýýý | Arab Games ýýý
Dan-Sa / Daniel Saboya
Marmok
The ACE Family
Like Nastya Vlog
Willie Salim
PDK Films
TheWillyrex
RsiamMusic : ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½
Alejandro Basalo
shakiraVEVO
Naisa Alifia Yuriza (N.A.Y)
Miley Cyrus
IShowSpeed
Bobby chourasiya
INCRï¿½ï¿
Jake Fellman
GEN HALILINTAR
SQUEEZIE
Blippi - Educational Videos for Kids
officialpsy
Ajay Sharma
Manual do Mundo
How Ridiculous
ANDtv
Sebastiï¿½ï¿½ï¿½
SonyMusicSouthVEVO
TheGrefg
BeatboxJCOP
David Dobrik
KatieAngel
RobleisIUTU
Lele Pons
Demi Lovato
Like Nastya VNM
Jason Derulo
MGC Playhouse
zuni and family
Priyal Kukreja
MSA Previously My Story Animated
ýýýýýýýýý KIMPRO
Jane ASMR ï¿½ï¿½
ArianaGrandeVevo
jaanvi patel
tanboy kun
Lil Pump
Porta dos Fundos
24 ï¿½ï¿½ï¿½ï
Les' Copaque Production
El Payaso Plim Plim
zbing z.
MissaSinfonia
ýýýýýýýýý Liziqi
DeGoBooM
JFlaMusic
FactTechz
News18 India
Fun For Kids TV - Hindi Rhymes
IGN
Aphmau
AMARINTV : ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½
ýýýýýýýýýýýýýýýý - Al-Remas
Koray Zeynep
Apple
Stubborn Facts
Taarak Mehta Ka Ooltah Chashmah
HowToBasic
PopularMMOs
Marques Brownlee
Anitta
Jason Oo
El Reino a Jugar
Willyrex
TheBrianMaps
TRANS TV Official
Liza Koshy
Queen Official
Prajapati News
gabyandalex
LuisFonsiVEVO
Pop Chartbusters
Guava Juice
EeOneGuy
VICE
Aayu and Pihu Show
Danny Fitt
Bispo Bruno Leonardo
de toxomoroxo
Doggy Doggy Cartoons
deepesh zo
Like Nastya IDN
Gato Galactico | GALï¿½ï¿
salman Noman
CoryxKenshin
With Kids[ï¿½ï¿½ï¿½ï¿½ï
Travis Scott
Tu COSMOPOLIS
Ivana Alawi
werever2morro
Ideas En 5 Minutos
NMF News
SriBalajiMovies
Lahari Music - TSeries
Younes Zarou
Jordan Matter
ýýýýýýýý ýýýýýýýýýýýýýýýýýýýýýý
FailArmy
BBC News Hindi
FunFun Toy Doll TV
Sandra Cires Art
Kaykai Salaider
UFC - Ultimate Fighting Championship
Ch7HD
RCTI - LAYAR DRAMA INDONESIA
Alfredo Larin
GMMTV OFFICIALï¿½ï¿½
MattStonie
Boyce Avenue
Camila Cabello
Little Mix
SAM SMITH
Pitbull
Bollywood Classics
Technoblade
W2S
Jennifer Lopez
Kids Play
T3ddy
JJ Olatunji
POPS Kids
Thairath Online
LEGO
XO TEAM Family
Aday Cï¿½ï¿½ï¿½ï¿½ï
Extra polinesios
Dyland PROS
Live
Vlad and Niki ARA
Canal IN
TWICE
Daily Dose Of Internet
Fitdance Academy
Panda Shorts
Disney Junior
larosadeguadalupe
sagar kalra (Shorts)
wifistudy by Unacademy
Antrax
enesbatur
Totoy kids - Espaï¿½ï
Kung Fu Padla
DopeLyrics
jeffreestar
Lyna
MK MUSIC
Unspeakable
Camilo
Dear Sir
Narendra Modi
Arif muhammad
Rotten Tomatoes Trailers
Volga Video
DM - Desi Melodies
My Family
Team Films Bhojpuri
Zee Music Classic
Prime Video India
Caeli YT
Kuplinov ï¿½ï¿½ï¿
Linus Tech Tips
Juliana Baltar
5-Minute Crafts FAMILY
Blippi Espaï¿½ï
Super Senya
Katakit Baby TV
Infobells Bangla
ýýýýýýýý ýý ýýýýýýýý
Henrique e Juliano
MrDegree
Kashvi Adlakha
Talking Tom & Friends
ýýýýýýýý ýýýýýýýýýýýýýý ýýýý 5 ýýýýýýýýýý
Harsh Beniwal
FFUNTV
Mobile Legends: Bang Bang
Roman Atwood Vlogs
Mrwhosetheboss
Genierock
zayn
Kerajinan 5-Menit
FC Barcelona
Dave and Ava - Nursery Rhymes and Baby Songs
LOKESH GAMER
ILYA BORZOV
Mazhavil Manorama
Pokï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½
The MriDul
Niana Guerrero
SRK MUSIC
Sony LIV
T-Series Hamaar Bhojpuri
Oyuncak Avï¿
CNN
NDTV India
It's Mamix
Kim Loaiza
Daftar Populer
Jordi Sala
Ranz Kyle
PowerfulJRE
Mariale
Makiman131
Hongyu ASMR ï¿½ï¿½ï
Mohamed Ramadan I ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï
EdisonPts
BIGBANG
Rubï¿½ï¿½ï¿½ï¿½ï¿½ï¿½
ABS-CBN News
Chapitosiki
AdeleVEVO
MoreAliA
Chetan Monga Vlogs
Little Angel - Mï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½
League of Legends
Therichest
XpressTV
PlayStation
Kwebbelkop
Gyani Beast
THE BROWN SIBLINGS
Sony Music South
Big School
Ray William Johnson
KOMPASTV
ISSEI / ï¿½ï¿½ï¿½ï¿½
Zï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï
A2 Motivation by Arvind Arora
50 Cent
MNCTV OFFICIAL
ERB
melanie martinez
iTownGamePlay *Terror&Diversiï¿½ï
ýýýýýýýýýýýý8 : Thai Ch8
ZutiGang
ýýýýýý
TazerCraft
ýýýýýýýýýýýýýýýýýýBAYASHITV
Fueled By Ramen
CrashCourse
MattyBRaps
Lachlan
ýýýýýýýý ýýýýýýýý
Meghan Trainor
Jorge & Mateus Oficial
MajorLazerOfficial
Beast Philanthropy
Filaretiki
5-Minute Crafts Recycle
ýýýýýýýýýý ýýýýýýýýýýýý
Maha Fun Tv
Canal Nostalgia TV
The Slow Mo Guys
StudyIQ IAS
Chad Wild Clay
CollegeHumor
Netflix Jr.
Colors Rishtey
ABC News
Camila Loures
Doc Tops
Auron
Jesser
Planeta das Gï¿½ï¿½
Preston
Martin Garrix
O Reino Infantil
Fifth Harmony
Mis Pastelitos
Noman Official
Like Nastya Stories
les boys tv2
Lotus Music
IDEIAS INCRï¿½ï¿½
Reaction Time
BBC News
Eli Kids - Cartoons & Songs
Boram Tube ToysReview [ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï
Aadishakti Films
Telemundo
GMM25Thailand
TV9 Bharatvarsh
Maroon5VEVO
Saad Lamjarred | ï¿½ï¿½ï¿½ï¿½ï¿½ï¿
Hear This Music
Lilly Singh
ýýýýýýýýýýýýýýýýýýýýý
Gyan Gamingï¿½
Drawblogs
nobru
ýýýýýýýýýýýý ýýýýýýýýýýýý I ýýýýýý ýý ýýýýýýýýý
Cyprien
Rclbeauty101
Rohail Hyatt
Indore Physical Academy
Rosanna Pansino
Vlad and Niki PRT
RS 1313 SHORTS
Zig & Sharko
SelenaGomezVEVO
ZEE5
Super Polina
RebeccaZamolo
Wish 107.5
Invento na Hora
SiS
NikkieTutorials
TommyInnit
E-MasterSensei
infobells - Kannada
CrazyFrog
Dorukhan Gï¿½ï¿½ï
SEVENGERS
Zee Bangla
DangMattSmith
Neha Kakkar
#Refugio Mental
ýýýýýýýýýýýýýýýýýýýý ýýýýýýýýýýýýýýýýýýýý
TrapCity
Supercar Blondie
Yudist Ardhana
Lana Del Rey
MalumaVEVO
F2Freestylers - Ultimate Soccer Skills Channï¿½
Bie The Ska
AM3NlC
Narins Beauty
TV Ana Emilia
ýýýýýýýýýýýý
Luli Pampï¿½
Gallina Pintadita
ViralHog
ETV Jabardasth
zeetelugu
Crescendo com Luluca
Jazzghost
karameeshchannel
Darkar Company Studios
Dental Digest
T-Series Regional
ADEL et SAMI
jamuna tv24
Atlantic Records
ýýýýýýýý ýý ýýýýýýýýýýýý
Veritasium
Alexa Rivera
Airrack
Hacksmith Industries
JD Pantoja
ýýýýýýýý/Atro
123 GO! Spanish
Geo News
Kids TV India Hindi Nursery Rhymes
Think Music India
O Que Nï¿½ï¿½ï¿½ï¿½ï¿½ï¿
Goldmines Premiere
MAIKI021
The Vishal bhatt
NishaMadhulika
MyMissAnand
FAPTV
Wesley Safadï¿½
infobells
Desi gamers
Acenix
Zeinab Harake
DALLMYD
Lindsey Stirling
JOJO TV - Hindi Stories
BBC
Saturday Night Live
BUDI01 GAMING
Typical Gamer
Anaysa
Julia Gisella
Awakening Music
Lady Diana
Sanjoy Das Official
Woody & Kleiny
Vijay Kumar Viner Vlogs
Conor Maynard
Wengie
Vlad y Niki Show
Codiscos
The World Adventures ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½
Vibhu 96
Blockbuster Movies
ATHLEAN-Xï¿½
My Mate Nate
H2ODelirious
GMA Integrated News
Peet Montzingo
Tom Duggan
Trakin Tech
theRadBrad
Matt Steffanina
straykids
Kurt Hugo Schneider
Vogue
ýýýýýýýýýýýýýýýýýý
Kids Lineï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½
VexTrex
penguinz0
Just For Laughs Gags
Kabita's Kitchen
BanderitaX
AzzyLand
HUBAï¿½ï¿½
BIBO ï¿½ï¿½ï¿½ï¿½ï¿½ï¿
Brawl Stars
Einerd
Sonotek Bhakti
Vilmei
MC Divertida
The Infographics Show
jbalvinVEVO
ýýýýýýTwinsFromRussia
Technology Gyan
CookingShooking Hindi
Ryan Trahan
Alex Gonzaga Official
WiederDude
Ian Boggs
Lokdhun Punjabi
Knowledge Tv ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½
Painzeiro
Peppa Pig em Portuguï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½
ýýýýýýýýýýýýýýý Ms Yeah
Hungria Hip Hop
RaptorGamer
RedeTV
twenty one pilots
DjKhaled
Davie504
Everson Zoio
Calon Sarjana
Lofi Girl
SRK Edie soon
GH'S
JesseAndMike
Wolfoo Channel
Susy Mouriz
7 Minutoz
The LaBrant Fam
Pastor Antï¿½ï¿½ï¿½ï¿½ï
Matheus Yurley
gymvirtual
BIBOï¿½ï¿½ï¿½ï¿½ï
Top Viral Talent
Akon
AlArabiya ï¿½ï¿½ï¿½ï¿½ï¿
Rauw Alejandro
EnriqueIglesiasVEVO
ýýýýýýýý ýýýý ýýýýýýýýýýýýýý
The Shiny Peanut
Talking Angela
Melon City Show - ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿
Duo Tiempo De Sol
Troom Troom India
MrSuicideSheep
Adam W
Right to Shiksha
Beyoncï¿½ï¿½
FACT FIRE KING
Ian Lucas
Franco Escamilla
Adexe & Nau
Diana and Roma IND
JassRecords
Future AMV's
YoungBoy Never Broke Again
Blossom
#Refugio Mental
Piuzinho
Heidi y Zidane
Go Ami Go!
Morgz
CaseyNeistat
ýýýýýýýýýSULGI
NickiMinajAtVEVO
Ellie Goulding
colinfurze
People Vs Food
Wolfoo Family
jamill
Health Time
Yair17
Little Baby Bum en Espaï¿½ï
First We Feast
Mï¿½ï¿½ï¿½ï¿½
Bebefinn - Nursery Rhymes & Kids Songs
Troom Troom PT
Parafernalha
NDTV
elcarteldesantatv
Family Fitness
Zee Tamil
Flowers Comedy
Mundo Bita
Wave Music Bhakti
TROOM TROOM INDONESIA
CKM
Mr_Mughall Gaming
_vector_
DEV Ke Facts
Hero Movies 2023
WatchLOUD
Gibby :)
GustavoParodias
SAAIHALILINTAR
Timba Vk
Heidi and Zidane HZHtube
DaniRep | +6 Vï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï¿½ï
Zee Kids
Pari's Lifestyle
DisneyChannelUK
MoniLinaFamily
bharatzkitchen HINDI
TKoR
annakova
Avril Lavigne
Caylus
Migos ATL
Natan por Aï¿
Free Fire India Official
HybridPanda
RobTopGames
Make Joke Of'''


# In[11]:


with open('wordcloud.txt', 'w') as file:
    file.write(text)


# In[12]:


df['channel_type'].unique()


# In[13]:


df['category'].unique()


# In[14]:


df_duplicated = df.append(df, ignore_index=True)

# 添加新的一列'path'
df_duplicated['path'] = [1] * len(df) + [102] * len(df)


# In[15]:


df_duplicated[df_duplicated['Youtuber']=='T-Series']


# In[ ]:





# In[19]:


#df_duplicated['channel_type_count'] = df_duplicated.groupby('channel_type').transform('count')
df_duplicated


# In[ ]:


'''
channel_type_count_mapping = df_duplicated['channel_type'].value_counts().to_dict()
df_duplicated['channel_type_count'] = df_duplicated['channel_type'].map(channel_type_count_mapping)
df_duplicated['channel_type_count'] = df_duplicated['channel_type_count']/2
'''


# In[ ]:


# df_duplicated[df_duplicated['channel_type']=='Games']


# In[ ]:


# df_duplicated['countYTB']= 1/2
# df_duplicated


# In[ ]:





# In[ ]:


df_duplicated.columns


# In[24]:


df_duplicated['avg_monthly_earnings'] = (df_duplicated['lowest_monthly_earnings']+df_duplicated['highest_monthly_earnings'])/2


# In[25]:


df_duplicated['avg_yearly_earnings'] = (df_duplicated['lowest_yearly_earnings']+df_duplicated['highest_yearly_earnings'])/2


# In[ ]:


df_corr = df_duplicated[['subscribers', 'video views',
       'uploads', 'video_views_for_the_last_30_days', 'avg_monthly_earnings',
       'avg_yearly_earnings', 'subscribers_for_last_30_days']]
correlation_matrix = df_corr.corr()

# correlation
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap')
plt.show()


# In[60]:


df_duplicated = df_duplicated.drop_duplicates()


# In[62]:





# In[54]:


radar = df_duplicated[['rank','subscribers', 'video views',
       'uploads','avg_monthly_earnings','channel_type_count','channel_type','Country']]


# In[72]:


# standarization
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 10))
df_duplicated[['subscribers_s', 'video views_s',
       'uploads_s','avg_monthly_earnings_s','channel_type_count_s']] = scaler.fit_transform(radar[['subscribers', 'video views',
       'uploads','avg_monthly_earnings','channel_type_count']])
df_duplicated


# In[63]:


radar.to_csv('radar.csv', index=False)


# In[57]:


radar.drop_duplicates()


# In[70]:


df_duplicated = df_duplicated.drop(columns= ['path'])


# In[71]:


df_duplicated.drop_duplicates()


# In[77]:


df_duplicated['subscribers_s_avg'] = df_duplicated.groupby('subscribers_s').transform('mean')


# In[73]:


df_duplicated.to_csv('Global YouTube Statistics.csv', index=False)


# In[6]:


df = df.drop_duplicates()


# In[7]:


df.to_csv('Global YouTube Statistics.csv', index=False)


# In[ ]:




