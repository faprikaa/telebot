from cgi import test
from telethon import *

bot_token="5055839545:xxxxxxx"

bot = TelegramClient("run","555555","xxxxxxxxxxxxxxxxx").start(bot_token="5055839545:xxxxxxxxxxxxxxxxx")


@bot.on(events.CallbackQuery)

@bot.on(events.ChatAction)
async def mention(event):
	if event.is_mention:
		select_tkp()
	else:
		pass

@bot.on(events.NewMessage)
async def select_tkp(event):
	supmax2 = ["Berikut adalah list TKP yang support Ekstra Unlimited dan Unlimax :", "Bandar Lampung", "Bandung Barat", "Bangka", "Bangka Barat", "Bangkalan", "Bangka Selatan", "Bangka Tengah", "Banjar", "Bantaeng", "Batang", "Belitung", "Belitung Timur", "Brebes", "Cianjur", "Cirebon", "Hulu Sungai Selatan", "Hulu Sungai Tengah", "Hulu Sungai Utara", "Indramayu", "Jeneponto", "Jombang", "Karawang", "Kota Banjar Baru", "Kota Banjarmasin", "Kota Cilegon", "Kota Cimahi", "Kota Cirebon", "Kota Mataram", "Kota Mojokerto", "Kota Pekalongan", "Kota Pontianak", "Kota Serang", "Kota Singkawang", "Kota Sukabumi", "Kota Tegal", "Kubu Raya", "Kuningan", "Lampung Selatan", "Lampung Timur", "Lebak", "Lombok Barat", "Lombok Tengah", "Lombok Timur", "Lombok Utara", "Majalengka", "Mempawah", "Metro", "Mojokerto", "Pamekasan", "Pandeglang", "Pekalongan", "Pemalang", "Pesawaran", "Pringsewu", "Purwakarta", "Sambas", "Sampang", "Serang", "Subang", "Sukabumi", "Sumedang", "Sumenep", "Takalar", "Tegal"]
	sup2 = ["Berikut adalah list TKP yang support Ekstra Unlimited saja :", "Aceh Tamiang", "Aceh Timur", "Agam", "Badung", "Bandung", "Bangli", "Bantul", "Banyu Asin", "Barru", "Bengkulu Tengah", "Bintan", "Bolaang Mongondow", "Bondowoso", "Buleleng", "Bulukumba", "Ciamis", "Deli Serdang", "Demak", "Garut", "Gianyar", "Gowa", "Gresik", "Jembrana", "Karanganyar", "Karang Asem", "Karimun", "Kediri", "Kendal", "Kepahiang", "Kepulauan Selayar", "Klaten", "Klungkung", "Kota Bandung", "Kota Banjar Kota Tasikmalaya", "Kota Batam", "Kota Batu", "Kota Bengkulu", "Kota Binjai", "Kota Bontang", "Kota Bukit Tinggi", "Kota Denpasar", "Kota Gorontalo", "Kota Jambi", "Kota Kediri", "Kota Langsa", "Kota Makassar", "Kota Malang", "Kota Manado", "Kota Medan", "Kota Metro", "Kota Padang", "Kota Palembang", "Kota Pangkal Pinang", "Kota Parepare", "Kota Pariaman", "Kota Payakumbuh", "Kota Pematang Siantar", "Kota Prabumulih", "Kota Salatiga", "Kota Semarang", "Kota Solok", "Kota Surabaya", "Kota Surakarta", "Kota Tangerang", "Kota Tangerang Selatan", "Kota Tanjung Pinang", "Kota Tebing Tinggi", "Kota Tomohon", "Kota Waringin Barat", "Kota Waringin Timur", "Kota Yogyakarta", "Langkat", "Lima Puluh Kota", "Magetan", "Malang", "Maros", "Minahasa", "Minahasa Utara", "Muara Enim", "Muaro Jambi", "Nganjuk", "Ogan Ilir", "Ogan Komering Ilir", "Ogan Komering Ulu", "Ogan Komering Ulu Timur", "Padang Pariaman", "Pangandaran", "Samosir", "Seluma", "Semarang", "Serdang Bedagai", "Sidoarjo", "Simalungun", "Sleman", "Solok", "Soppeng", "Sukoharjo", "Tabanan", "Tangerang", "Tasikmalaya", "Tebo", "Toba Samosir", "Way Kanan"]
	tsup2 = ["Berikut adalah list TKP yang **TIDAK** support Ekstra Unlimited dan Unlimax (bag.1) :", "Aceh Barat", "Aceh Barat Daya", "Aceh Besar", "Aceh Jaya", "Aceh Selatan", "Aceh Singkil", "Aceh Tengah", "Aceh Tenggara", "Aceh Utara", "Alor", "Asahan", "Asmat", "Balangan", "Banggai", "Banggai Kepulauan", "Banggai Laut", "Banjarnegara", "Banyumas", "Banyuwangi", "Barito Kuala", "Barito Selatan", "Barito Timur", "Barito Utara", "Batam", "Batang Hari", "Batu Bara", "Bekasi", "Belu", "Bener Meriah", "Bengkalis", "Bengkayang", "Bengkulu Selatan", "Bengkulu Utara", "Berau", "Besukur", "Besukurhigh", "Biak Numfor", "Bima", "Bireuen", "Blitar", "Blora", "Boalemo", "Bogor", "Bojonegoro", "Bolaang Mongondow Selatan", "Bolaang Mongondow Timur", "Bolaang Mongondow Utara", "Bombana", "Bone", "Bone Bolango", "Boven Digoel", "Boyolali", "Bukit Raya", "Bukit Siguntang", "Bulungan", "Bungo", "Buol", "Buru", "Buru Selatan", "Buton", "Buton Selatan", "Buton Tengah", "Buton Utara", "Ceremai", "Cianjur", "Cilacap", "Dairi", "Deiyai", "Dharmasraya", "Dobonsolo", "Dogiyai", "Dompu", "Donggala", "Dorolonda", "Empat Lawang", "Ende", "Enrekang", "Fakfak", "Flores Timur", "Gayo Lues", "Gorontalo", "Gorontalo Utara", "Grobogan", "Gunung Dempo", "Gunung Kidul", "Gunung Mas", "Gunungsitoli", "Halmahera Barat", "Halmahera Selatan", "Halmahera Tengah", "Halmahera Timur", "Halmahera Utara", "Hulu Sungai Selatan", "Hulu Sungai Tengah", "Humbang Hasundutan", "Indragiri Hilir", "Indragiri Hulu", "Intan Jaya", "Jakarta Barat", "Jakarta Pusat", "Jakarta Selatan", "Jakarta Timur", "Jakarta Utara", "Jayapura", "Jayawijaya", "Jember", "Jepara", "Kaimana", "Kampar", "Kapal", "Kapuas", "Kapuas Hulu", "Karangasem", "Karo", "Katingan", "Kaur", "Kayong Utara", "Kebumen", "Keerom", "Kelimutu", "Kelud", "Kepulauan Anambas", "Kepulauan Aru", "Kepulauan Mentawai", "Kepulauan Meranti", "Kepulauan Sangihe", "Kepulauan Seribu", "Kepulauan Sula", "Kepulauan Talaud", "Kepulauan Yapen", "Kerinci", "Ketapang", "Kolaka", "Kolaka Timur", "Kolaka Utara", "Konawe", "Konawe Kepulauan", "Konawe Selatan", "Konawe Utara", "Kota Ambon", "Kota Balikpapan", "Kota Banda Aceh", "Kota Bandar Lampung", "Kota Banjar", "Kota Banjar Baru", "Kota Banjarmasin", "Kota Baru", "Kota Bau-Bau", "Kota Baubau", "Kota Bekasi", "Kota Bima", "Kota Bitung", "Kota Blitar", "Kota Bogor", "Kota Depok", "Kota Dumai", "Kota Jayapura", "Kota Kendari", "Kota Kotamobagu", "Kota Kupang", "Kota Lhokseumawe", "Kota Lubuklinggau", "Kota Lubuk Linggau", "Kota Madiun", "Kota Magelang", "Kota Padang Panjang", "Kota Padangsidimpuan", "Kota Pagar Alam", "Kota Palangkaraya", "Kota Palopo", "Kota Palu", "Kota Pangkalpinang", "Kota Pare-Pare", "Kota Pasuruan", "Kota Pekanbaru", "Kota Probolinggo", "Kota Sabang", "Kota Samarinda", "Kota Sawah Lunto", "Kota Sengkang", "Kota Sibolga", "Kota Sorong", "Kota Subulussalam", "Kota Sungai Penuh", "Kota Tanjung Balai", "Kota Tarakan", "Kota Tasikmalaya", "Kota Ternate", "Kota Tidore Kepulauan", "Kota Tual", "Kuantan Singingi", "Kudus", "Kulon Progo", "Kupang", "Kutai Barat", "Kutai Kartanegara", "Kutai Kertanegara", "Kutai Timur"]
	tsup3 = ["Berikut adalah list TKP yang **TIDAK** support Ekstra Unlimited dan Unlimax (bag.2) :", "Labobar", "Labuhan Batu", "Labuhan Batu Selatan", "Labuhan Batu Utara", "Lahat", "Lamandau", "Lambelu", "Lamongan", "Lampung Barat", "Lampung Tengah", "Lampung Utara", "Landak", "Lanny Jaya", "Lawit", "Lebong", "Lembata", "Lingga", "Lombok Utara", "Lumajang", "Luwu", "Luwu Timur", "Luwu Utara", "Madiun", "Madura", "Magelang", "Mahakam Ulu", "Majene", "Malaka", "Malinau", "Maluku Barat Daya", "Maluku Tengah", "Maluku Tenggara", "Maluku Tenggara Barat", "Mamasa", "Mamberamo Raya", "Mamberamo Tengah", "Mamuju", "Mamuju Tengah", "Mamuju Utara", "Mandailing Natal", "Manggarai", "Manggarai Barat", "Manggarai Timur", "Manokwari", "Manokwari Selatan", "Mappi", "Mataram Lombok", "Maybrat", "Melawi", "Merangin", "Merauke", "Mesuji", "Mimika", "Minahasa Selatan", "Minahasa Tenggara", "Morowali", "Morowali Utara", "Mukomuko", "Muna", "Muna Barat", "Murung Raya", "Musi Banyuasin", "Musi Rawas", "Musi Rawas Utara", "Nabire", "Nagan Raya", "Nagekeo", "Natuna", "Nduga", "Ngada", "Ngawi", "Nggapulu", "Nias", "Nias Barat", "Nias Selatan", "Nias Utara", "Ntb", "Nunukan", "Ogan Komering Ulu Selatan", "Pacitan", "Padang Lawas", "Padang Lawas Utara", "Pakpak Bharat", "Pangkajene Dan Kepulauan", "Paniai", "Pantura", "Parigi Moutong", "Pasaman", "Pasaman Barat", "Paser", "Pasuruan", "Pati", "Payakumbuh", "Pegunungan Arfak", "Pegunungan Bintang", "Pelalawan", "Pemalang", "Pematangsiantar", "Pematangsiantarout", "Penajam Paser Utara", "Penukal Abab Lematang Ilir", "Pesisir Barat", "Pesisir Selatan", "Pidie", "Pidie Jaya", "Pinrang", "Pohuwato", "Polewali Mandar", "Ponorogo", "Pontianak", "Poso", "Probolinggo", "Pulang Pisau", "Pulau Morotai", "Pulau Taliabu", "Puncak", "Puncak Jaya", "Purbalingga", "Purworejo", "Raja Ampat", "Rejang Lebong", "Rembang", "Rokan Hilir", "Rokan Hulu", "Rote Ndao", "Sabu Raijua", "Sanggau", "Sarmi", "Sarolangun", "Sekadau", "Selayar", "Seram Bagian Barat", "Seram Bagian Timur", "Seruyan", "Siak", "Siau Tagulandang Biaro", "Sibolga", "Sibolgaout", "Sidenreng Rappang", "Sigi", "Sijunjung", "Sikka", "Simeulue", "Sinabung", "Sinjai", "Sintang", "Sirimau", "Situbondo", "Solok Selatan", "Sorong", "Sorong Selatan", "Sragen", "Sukamara", "Sumba Barat", "Sumba Barat Daya", "Sumba Tengah", "Sumba Timur", "Sumbawa", "Sumbawa Barat", "Sungai Penuh", "Supiori", "Tabalong", "Tambrauw", "Tanah Bumbu", "Tanah Datar", "Tanah Laut", "Tana Tidung", "Tana Toraja", "Tanggamung", "Tanggamus", "Tanjung Jabung Barat", "Tanjung Jabung Timur", "Tapanuli", "Tapanuli Selatan", "Tapanuli Tengah", "Tapanuli Utara", "Tapin", "Teluk Bintuni", "Teluk Wondama", "Temanggung", "Tidar", "Tilongkabila", "Timor Tengah Selatan", "Timor Tengah Utara", "Tojo Una-Una", "Toli-Toli", "Tolikara", "Toraja Utara", "Trenggalek", "Tuban", "Tulangbawang", "Tulang Bawang Barat", "Tulungagung", "Wajo", "Wakatobi", "Waropen", "Wonogiri", "Wonosobo", "Yahukimo", "Yalimo"]
	supmax = ("kota pekalongan","pekalongan","lombok utara","bandar lampung","pemalang","tegal","banjar","hulu sungai selatan","metro","hulu sungai tengah","hulu sungai utara","kota banjar baru","bandung barat","kota banjarmasin","lampung selatan","cianjur","lampung timur","cirebon","kota cirebon","kota pontianak","indramayu","kota singkawang","kota cimahi","bangkalan","kuningan","jombang","kubu raya","majalengka","mempawah","subang","kota mojokerto","sambas","pesawaran","sumedang","mojokerto","bantaeng","bangka barat","bangka","bangka selatan","bangka tengah","belitung","belitung timur", "pringsewu","kota cilegon", "kota serang", "lebak", "pandeglang","serang", "karawang", "kota sukabumi", "purwakarta", "sukabumi","brebes","batang","lombok timur","takalar","jeneponto","lombok barat","lombok tengah","pamekasan","kota tegal","sumenep","sampang","kota mataram")
	sup = ("aceh tamiang", "aceh timur", "bantul", "deli serdang", "demak", "kota binjai", "karanganyar", "kota langsa", "kendal", "kota medan", "klaten", "kota pematang siantar", "kota salatiga", "kota tebing tinggi", "kota surakarta", "langkat", "kota yogyakarta", "samosir", "semarang", "serdang bedagai", "sleman", "simalungun", "sukoharjo", "toba samosir", "agam", "bintan", "karimun", "kota semarang", "kota batam", "kota bukit tinggi", "kota padang", "kota pariaman", "kota payakumbuh", "bondowoso", "kota solok", "gresik", "kota tanjung pinang", "kota batu", "lima puluh kota", "kota kediri", "padang pariaman", "kota malang", "solok", "kota surabaya", "magetan", "malang", "sidoarjo", "banyu asin", "kediri", "bengkulu tengah", "kepahiang", "nganjuk", "kota bengkulu", "kota jambi", "kota metro", "badung", "kota palembang", "bangli", "kota pangkal pinang", "buleleng", "kota prabumulih", "gianyar", "jembrana", "karang asem", "muara enim", "klungkung", "muaro jambi", "kota denpasar", "ogan ilir", "ogan komering ilir", "ogan komering ulu", "ogan komering ulu timur", "tabanan", "seluma", "tebo", "way kanan", "kota bontang", "kota tangerang", "kota tangerang selatan", "kota waringin barat", "tangerang", "kota waringin timur", "bandung", "barru", "ciamis", "bolaang mongondow", "garut", "bulukumba", "kota bandung", "gowa", "kota banjar kota tasikmalaya", "kepulauan selayar", "pangandaran", "kota gorontalo", "tasikmalaya", "kota makassar", "kota manado", "kota parepare", "kota tomohon", "maros", "minahasa", "minahasa utara", "soppeng",)
	tsup = ("aceh jaya", "batam", "besukur", "besukurhigh", "kapal", "karangasem", "ceremai", "sinabung", "kota bau-bau", "kota lubuk linggau", "kota pangkalpinang", "kota sengkang", "bukit raya", "bukit siguntang", "dobonsolo", "dorolonda", "gunung dempo", "kelimutu", "kelud", "labobar", "lambelu", "lawit", "nggapulu", "sirimau", "tidar", "tilongkabila", "madura", "mataram lombok", "ntb", "pantura", "payakumbuh", "pematangsiantar", "pematangsiantarout", "pontianak", "selayar", "sibolga", "sibolgaout", "sungai penuh", "tanah bumbu", "tanah datar", "tanah laut", "tanggamus", "tanjung jabung barat", "tanjung jabung timur", "tapanuli tengah", "aceh selatan", "tapin", "aceh utara", "tulungagung", "temanggung", "asahan", "timor tengah selatan", "banggai kepulauan", "timor tengah utara", "banggai laut", "tojo una-una", "banjarnegara", "trenggalek", "tulang bawang barat", "aceh barat", "barito kuala", "aceh barat daya", "aceh besar", "batu bara", "aceh singkil", "belu", "bener meriah", "aceh tengah", "bengkayang", "aceh tenggara", "bengkulu selatan", "alor", "asmat", "bengkulu utara", "balangan", "bireuen", "blitar", "banggai", "bolaang mongondow selatan", "bolaang mongondow timur", "bolaang mongondow utara", "bungo", "buru selatan", "buton", "buton selatan", "buton tengah", "buton utara", "banyumas", "cilacap", "banyuwangi", "dharmasraya", "barito selatan", "dompu", "barito timur", "donggala", "barito utara", "empat lawang", "ende", "batang hari", "flores timur", "bekasi", "gayo lues", "gorontalo utara", "bengkalis", "grobogan", "berau", "gunung kidul", "biak numfor", "halmahera barat", "bima", "halmahera selatan", "blora", "halmahera tengah", "boalemo", "halmahera timur", "bogor", "halmahera utara", "bojonegoro", "hulu sungai selatan", "bombana", "hulu sungai tengah", "bone", "bone bolango", "humbang hasundutan", "boven digoel", "indragiri hulu", "boyolali", "jember", "jepara", "bulungan", "buol", "kampar", "buru", "cianjur", "karo", "katingan", "dairi", "kaur", "deiyai", "kepulauan anambas", "dogiyai", "kepulauan aru", "enrekang", "kepulauan mentawai", "fakfak", "kepulauan meranti", "kepulauan sangihe", "kepulauan sula", "gorontalo", "kepulauan talaud", "kerinci", "gunung mas", "gunungsitoli", "kolaka timur", "indragiri hilir", "kolaka utara", "konawe kepulauan", "intan jaya", "konawe utara", "kota balikpapan", "jakarta barat", "kota bandar lampung", "jakarta pusat", "jakarta selatan", "kota banjar", "jakarta timur", "kota banjar baru", "jakarta utara", "kota baru", "jayapura", "jayawijaya", "kaimana", "kota bekasi", "kapuas", "kapuas hulu", "kota bima", "kota bitung", "kayong utara", "kota blitar", "kebumen", "kota bogor", "keerom", "kepulauan seribu", "kota depok", "kepulauan yapen", "kota dumai", "ketapang", "kolaka", "konawe", "kota kotamobagu", "konawe selatan", "kota ambon", "kota lhokseumawe", "kota banda aceh", "kota lubuklinggau", "kota banjarmasin", "kota madiun", "kota baubau", "kota padang panjang", "kota jayapura", "kota padangsidimpuan", "kota kendari", "kota pagar alam", "kota kupang", "kota palangkaraya", "kota magelang", "kota palopo", "kota palu", "kota pasuruan", "kota pare-pare", "kota pekanbaru", "kota probolinggo", "kota sabang", "kota samarinda", "kota sawah lunto", "kota sibolga", "kota subulussalam", "kota sorong", "kota sungai penuh", "kutai barat", "kutai kertanegara", "lamongan", "lanny jaya", "kota tanjung balai", "kota tarakan", "lombok utara", "kota tasikmalaya", "lumajang", "luwu timur", "mamasa", "kota ternate", "mamberamo raya", "kota tidore kepulauan", "mamberamo tengah", "mamuju tengah", "kota tual", "mamuju utara", "mandailing natal", "manggarai barat", "manokwari", "kuantan singingi", "manokwari selatan", "mappi", "kudus", "maybrat", "kulon progo", "merauke", "mimika", "kupang", "kutai kartanegara", "nabire", "all", "kutai timur", "nduga", "labuhan batu", "nias", "labuhan batu selatan", "nias selatan", "labuhan batu utara", "paniai", "lahat", "pegunungan arfak", "lamandau", "pegunungan bintang", "lampung barat", "pesisir selatan", "pidie jaya", "lampung tengah", "pinrang", "probolinggo", "lampung utara", "puncak", "landak", "purbalingga", "lebong", "purworejo", "lembata", "rembang", "lingga", "rokan hilir", "rokan hulu", "luwu", "luwu utara", "sanggau", "madiun", "sarmi", "magelang", "seram bagian barat", "mahakam ulu", "seruyan", "majene", "sijunjung", "malaka", "sikka", "malinau", "maluku barat daya", "maluku tengah", "sorong", "maluku tenggara", "sorong selatan", "maluku tenggara barat", "mamuju", "manggarai", "manggarai timur", "sumba timur", "sumbawa", "melawi", "sumbawa barat", "merangin", "supiori", "mesuji", "tambrauw", "minahasa selatan", "tanggamung", "minahasa tenggara", "tapanuli", "tapanuli selatan", "tapanuli utara", "morowali", "morowali utara", "teluk bintuni", "teluk wondama", "mukomuko", "muna", "toli-toli", "muna barat", "tolikara", "murung raya", "toraja utara", "musi banyuasin", "tuban", "musi rawas", "tulangbawang", "musi rawas utara", "wajo", "nagan raya", "wakatobi", "nagekeo", "waropen", "natuna", "ngada", "wonogiri", "wonosobo", "ngawi", "yalimo", "nias barat", "yahukimo", "nias utara", "nunukan", "ogan komering ulu selatan", "pacitan", "padang lawas", "padang lawas utara", "pakpak bharat", "pangkajene dan kepulauan", "parigi moutong", "pasaman", "pasaman barat", "paser", "pasuruan", "pati", "pelalawan", "pemalang", "penajam paser utara", "penukal abab lematang ilir", "pesisir barat", "pidie", "pohuwato", "polewali mandar", "ponorogo", "poso", "pulang pisau", "pulau morotai", "pulau taliabu", "puncak jaya", "raja ampat", "rejang lebong", "rote ndao", "siak", "sabu raijua", "sarolangun", "sekadau", "seram bagian timur", "siau tagulandang biaro", "sidenreng rappang", "sigi", "simeulue", "sinjai", "sintang", "situbondo", "solok selatan", "sragen", "sukamara", "sumba barat", "sumba barat daya", "sumba tengah", "tabalong", "tana tidung", "tana toraja",)
	harsh = ("kontol","memek","ngentot","kntl","mmk")

	if event.message.message.lower() == "1supeks":
		await event.reply("\n - ".join(sup2))

	elif event.message.message.lower() == "1supmax":
		await event.reply("\n - ".join(supmax2))

	elif event.message.message.lower() == "1tsup":
		await event.reply("\n - ".join(tsup2))
	
	elif event.message.message.lower() == "1tsup2":
		await event.reply("\n - ".join(tsup3))

	elif event.message.message.lower() in sup:
		inline = [[Button.inline("Order","order2")]]		
		msg = f"Hasilnya, TKP Anda ```{event.message.message}```, :  \n \nSupport Ekstra Unlimited ✅ \nSupport Unlimited Max ❌\n   \nMasukkan /order atau tekan **tombol** dibawah untuk pembelian."
		await event.reply(msg,buttons=inline)		

	elif event.message.message.lower() in supmax:
		inline = [[Button.inline("Order","order2")]]
		msg = f"Hasilnya,  TKP Anda ```{event.message.message}```, : \n  \nSupport Ekstra Unlimited ✅ \nSupport Unlimited Max ✅  \n \nMasukkan /order atau tekan **tombol** dibawah untuk pembelian untuk pembelian"
		await event.reply(msg,buttons=inline)

	elif event.message.message.lower() in tsup:
		inline = [[Button.inline("Order  !!","order3")]]
		msg = f"Hasilnya, TKP Anda ```{event.message.message}```, :  \n \nSupport Ekstra Unlimited ❌ \nSupport Unlimited Max ❌ \n  \nTenang anda masih tetap bisa melakukan pembelian dengan /order2 atau dengan tekan **tombol** dibawah."
		await event.reply(msg,buttons=inline)
		
	elif event.message.message.lower() in harsh:
		await event.reply("bacot ngentot !")
	
	elif (
        event.message.message.lower() not in [supmax,sup,tsup,harsh]
        and not event.message.message.lower() in ["/notes","/order","/help","/start","/order2","/info","/list"]):
	
#	else:
		await event.reply(f"Maaf, __{event.message.message}__ tidak mengerti,   \nMasukkan /help untuk melihat command dan /notes untuk melihat catatan")


@bot.on(events.CallbackQuery(data=b"order3"))
@bot.on(events.InlineQuery)
async def order3(event):
	inline = [[Button.url("Order 1 Bulan","https://www.tokopedia.com/warungmaniez/perdana-telkomsel-3000gb")],[Button.url("Order 4 Bulan","https://www.tokopedia.com/warungmaniez/perdana-telkomsel-3000gb-120hari")]]
	msg = "**Silahkan tekan tombol dibawah untuk melakukan Pembelian**"
	await event.edit(msg,buttons=inline)

@bot.on(events.CallbackQuery(data=b"order2"))
@bot.on(events.InlineQuery)
async def order2(event):
	inline = [[Button.url("Testi dan Pricelist","https://t.me/testimaniez/5")],[Button.url("Kontak Admin","t.me/warungmaniez")]]
	msg = "**Silahkan chat Admin untuk melakukan Pembelian**"
	await event.edit(msg,buttons=inline)

@bot.on(events.NewMessage(pattern="/order2$"))
async def order4(event):
	inline = [[Button.url("Order 1 Bulan","https://www.tokopedia.com/warungmaniez/perdana-telkomsel-3000gb?utm_source=salinlink&utm_medium=share&utm_campaign=PDP-124552512-2742162704-010222")],[Button.url("Order 4 Bulan","https://www.tokopedia.com/warungmaniez/perdana-telkomsel-3000gb-120hari")],[Button.url("Kontak Admin","t.me/warungmaniez")]]
	msg = "**Silahkan chat Admin dengan tekan tombol dibawah untuk melanjutkan Pembelian**"
	await event.reply(msg,buttons=inline)


@bot.on(events.NewMessage(pattern="/notes$"))
async def notes(event):
	msg = "**notes** : \n \n1. Jika sudah memasukkan nama kabupaten dengan benar namun masih \'..tidak dimengerti..\' coba tambahkan \'kota\' didepannya \n2. Penambahan kata \'kota\' dapat menghasilkan hasil yang berbeda \n3. Jika masih belum berhasil coba tambahkan bagian kabupaten, seperti Jakarta Timur, Jakarta Pusat, Bandung Barat, dll. \n4. Informasi TKP dari bot ini adalah Valid"
	await event.reply(msg)

@bot.on(events.NewMessage(pattern="/order$"))
async def order(event):
	inline = [[Button.url("Testi dan Pricelist","https://t.me/testimaniez/5")],[Button.url("Kontak Admin","t.me/warungmaniez")]]
	msg = "**Silahkan chat Admin untuk melakukan Pembelian**"
	await event.reply(msg,buttons=inline)

@bot.on(events.NewMessage(pattern="/help$"))
async def help(event):
	inline = [[Button.url("Admin","t.me/warungmaniez")]]
	msg = "**help** : \n \n/start untuk memulai \n/order untuk pembelian \n/order2 untuk melakukan pembelian kartu perdana \n/notes untuk melihat notes \n/list untuk melihat list TKP \n/help untuk melihat commnad \n/info untuk melihat informasi tentang bot"
	await event.reply(msg,buttons=inline)

@bot.on(events.NewMessage(pattern="/start$"))
async def start(event):
	await event.reply("Selamat datang di CEK TKP BOT \n**Harap membaca /notes terlebih dahulu !!** \n \n======================== \nUntuk memulai, \nSilahkan masukkan kabupaten \n========================")

@bot.on(events.NewMessage(pattern="/info$"))
async def start(event):
	await event.reply("\n **CEK TKP BOT** \n \nVersion : 3.5 \nFramework : Telethon \nDeveloper : dibuat oleh @warungmaniez dengan dukungan mental oleh @xolvadev ")

@bot.on(events.NewMessage(pattern="/list$"))
async def start(event):
    await event.respond('Berikut adalah list TKP secara lengkap, \n▪️ TKP dengan warna **PUTIH** artinya hanya bisa beli kuota **Eksta Unlimited** saja, \n▪️ TKP warna **KUNING** artinya bisa beli **Ekstra Unlimited** dan **Unlimited Max**, \n▪️ TKP tidak ada digambar artinya **tidak bisa** membeli kedua paket tersebut.',file="list.jpg")


bot.run_until_disconnected()
