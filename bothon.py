from telethon import *

bot_token="5055839545:AAGM1cCGOoGMyATJfpYJYLZ__wH8PVLcCRs"

bot = TelegramClient("run","9552817","d174b0958f3d5a591b8713199fb6950b").start(bot_token="5055839545:AAGM1cCGOoGMyATJfpYJYLZ__wH8PVLcCRs")


@bot.on(events.CallbackQuery)


@bot.on(events.NewMessage)
async def select_tkp(event):
	supmax = ("kota pekalongan","pekalongan","Lombok Utara","bandar lampung","Pemalang","tegal","banjar","Hulu Sungai Selatan","Metro","Hulu Sungai Tengah","hulu sungai utara","kota Banjar Baru","Bandung Barat","kota Banjarmasin","lampung selatan","Cianjur","lampung timur","cirebon","kota cirebon","kota pontianak","indramayu","kota singkawang","kota cimahi","bangkalan","kuningan","jombang","kubu raya","majalengka","mempawah","subang","kota mojokerto","sambas","pesawaran","sumedang","mojokerto","bantaeng","bangka barat","bangka","bangka selatan","bangka tengah","belitung","belitung timur", "pringsewu","kota cilegon", "kota serang", "lebak", "pandeglang","serang", "karawang", "kota sukabumi", "purwakarta", "sukabumi","brebes","batang","lombok timur","takalar","jeneponto","lombok barat","lombok tengah","pamekasan","kota tegal","sumenep","sampang","kota mataram")
	sup = ("aceh tamiang", "aceh timur", "bantul", "deli serdang", "demak", "kota binjai", "karanganyar", "kota langsa", "kendal", "kota medan", "klaten", "kota pematang siantar", "kota salatiga", "kota tebing tinggi", "kota surakarta", "langkat", "kota yogyakarta", "samosir", "semarang", "serdang bedagai", "sleman", "simalungun", "sukoharjo", "toba samosir", "agam", "bintan", "karimun", "kota semarang", "kota batam", "kota bukit tinggi", "kota padang", "kota pariaman", "kota payakumbuh", "bondowoso", "kota solok", "gresik", "kota tanjung pinang", "kota batu", "lima puluh kota", "kota kediri", "padang pariaman", "kota malang", "solok", "kota surabaya", "magetan", "malang", "sidoarjo", "banyu asin", "kediri", "bengkulu tengah", "kepahiang", "nganjuk", "kota bengkulu", "kota jambi", "kota metro", "badung", "kota palembang", "bangli", "kota pangkal pinang", "buleleng", "kota prabumulih", "gianyar", "jembrana", "karang asem", "muara enim", "klungkung", "muaro jambi", "kota denpasar", "ogan ilir", "ogan komering ilir", "ogan komering ulu", "ogan komering ulu timur", "tabanan", "seluma", "tebo", "way kanan", "kota bontang", "kota tangerang", "kota tangerang selatan", "kota waringin barat", "tangerang", "kota waringin timur", "bandung", "barru", "ciamis", "bolaang mongondow", "garut", "bulukumba", "kota bandung", "gowa", "kota banjar kota tasikmalaya", "kepulauan selayar", "pangandaran", "kota gorontalo", "tasikmalaya", "kota makassar", "kota manado", "kota parepare", "kota tomohon", "maros", "minahasa", "minahasa utara", "soppeng",)
	tsup = ("aceh jaya", "batam", "besukur", "besukurhigh", "kapal", "karangasem", "ceremai", "sinabung", "kota bau-bau", "kota lubuk linggau", "kota pangkalpinang", "kota sengkang", "bukit raya", "bukit siguntang", "dobonsolo", "dorolonda", "gunung dempo", "kelimutu", "kelud", "labobar", "lambelu", "lawit", "nggapulu", "sirimau", "tidar", "tilongkabila", "madura", "mataram lombok", "ntb", "pantura", "payakumbuh", "pematangsiantar", "pematangsiantarout", "pontianak", "selayar", "sibolga", "sibolgaout", "sungai penuh", "tanah bumbu", "tanah datar", "tanah laut", "tanggamus", "tanjung jabung barat", "tanjung jabung timur", "tapanuli tengah", "aceh selatan", "tapin", "aceh utara", "tulungagung", "temanggung", "asahan", "timor tengah selatan", "banggai kepulauan", "timor tengah utara", "banggai laut", "tojo una-una", "banjarnegara", "trenggalek", "tulang bawang barat", "aceh barat", "barito kuala", "aceh barat daya", "aceh besar", "batu bara", "aceh singkil", "belu", "bener meriah", "aceh tengah", "bengkayang", "aceh tenggara", "bengkulu selatan", "alor", "asmat", "bengkulu utara", "balangan", "bireuen", "blitar", "bandung barat", "banggai", "bolaang mongondow selatan", "bolaang mongondow timur", "bolaang mongondow utara", "bungo", "buru selatan", "buton", "buton selatan", "buton tengah", "buton utara", "banyumas", "cilacap", "banyuwangi", "dharmasraya", "barito selatan", "dompu", "barito timur", "donggala", "barito utara", "empat lawang", "ende", "batang hari", "flores timur", "bekasi", "gayo lues", "gorontalo utara", "bengkalis", "grobogan", "berau", "gunung kidul", "biak numfor", "halmahera barat", "bima", "halmahera selatan", "blora", "halmahera tengah", "boalemo", "halmahera timur", "bogor", "halmahera utara", "bojonegoro", "hulu sungai selatan", "bombana", "hulu sungai tengah", "bone", "bone bolango", "humbang hasundutan", "boven digoel", "indragiri hulu", "boyolali", "jember", "jepara", "bulungan", "buol", "kampar", "buru", "cianjur", "karo", "katingan", "dairi", "kaur", "deiyai", "kepulauan anambas", "dogiyai", "kepulauan aru", "enrekang", "kepulauan mentawai", "fakfak", "kepulauan meranti", "kepulauan sangihe", "kepulauan sula", "gorontalo", "kepulauan talaud", "kerinci", "gunung mas", "gunungsitoli", "kolaka timur", "indragiri hilir", "kolaka utara", "konawe kepulauan", "intan jaya", "konawe utara", "kota balikpapan", "jakarta barat", "kota bandar lampung", "jakarta pusat", "jakarta selatan", "kota banjar", "jakarta timur", "kota banjar baru", "jakarta utara", "kota baru", "jayapura", "jayawijaya", "kaimana", "kota bekasi", "kapuas", "kapuas hulu", "kota bima", "kota bitung", "kayong utara", "kota blitar", "kebumen", "kota bogor", "keerom", "kepulauan seribu", "kota depok", "kepulauan yapen", "kota dumai", "ketapang", "kolaka", "konawe", "kota kotamobagu", "konawe selatan", "kota ambon", "kota lhokseumawe", "kota banda aceh", "kota lubuklinggau", "kota banjarmasin", "kota madiun", "kota baubau", "kota padang panjang", "kota jayapura", "kota padangsidimpuan", "kota kendari", "kota pagar alam", "kota kupang", "kota palangkaraya", "kota magelang", "kota palopo", "kota palu", "kota pasuruan", "kota pare-pare", "kota pekanbaru", "kota probolinggo", "kota sabang", "kota samarinda", "kota sawah lunto", "kota sibolga", "kota subulussalam", "kota sorong", "kota sungai penuh", "kutai barat", "kutai kertanegara", "lamongan", "lanny jaya", "kota tanjung balai", "kota tarakan", "lombok utara", "kota tasikmalaya", "lumajang", "luwu timur", "mamasa", "kota ternate", "mamberamo raya", "kota tidore kepulauan", "mamberamo tengah", "mamuju tengah", "kota tual", "mamuju utara", "mandailing natal", "manggarai barat", "manokwari", "kuantan singingi", "manokwari selatan", "mappi", "kudus", "maybrat", "kulon progo", "merauke", "mimika", "kupang", "kutai kartanegara", "nabire", "all", "kutai timur", "nduga", "labuhan batu", "nias", "labuhan batu selatan", "nias selatan", "labuhan batu utara", "paniai", "lahat", "pegunungan arfak", "lamandau", "pegunungan bintang", "lampung barat", "pesisir selatan", "pidie jaya", "lampung tengah", "pinrang", "probolinggo", "lampung utara", "puncak", "landak", "purbalingga", "lebong", "purworejo", "lembata", "rembang", "lingga", "rokan hilir", "rokan hulu", "luwu", "luwu utara", "sanggau", "madiun", "sarmi", "magelang", "seram bagian barat", "mahakam ulu", "seruyan", "majene", "sijunjung", "malaka", "sikka", "malinau", "maluku barat daya", "maluku tengah", "sorong", "maluku tenggara", "sorong selatan", "maluku tenggara barat", "mamuju", "manggarai", "manggarai timur", "sumba timur", "sumbawa", "melawi", "sumbawa barat", "merangin", "supiori", "mesuji", "tambrauw", "minahasa selatan", "tanggamung", "minahasa tenggara", "tapanuli", "tapanuli selatan", "tapanuli utara", "morowali", "morowali utara", "teluk bintuni", "teluk wondama", "mukomuko", "muna", "toli-toli", "muna barat", "tolikara", "murung raya", "toraja utara", "musi banyuasin", "tuban", "musi rawas", "tulangbawang", "musi rawas utara", "wajo", "nagan raya", "wakatobi", "nagekeo", "waropen", "natuna", "ngada", "wonogiri", "wonosobo", "ngawi", "yalimo", "nias barat", "yahukimo", "nias utara", "nunukan", "ogan komering ulu selatan", "pacitan", "padang lawas", "padang lawas utara", "pakpak bharat", "pangkajene dan kepulauan", "parigi moutong", "pasaman", "pasaman barat", "paser", "pasuruan", "pati", "pelalawan", "pemalang", "penajam paser utara", "penukal abab lematang ilir", "pesisir barat", "pidie", "pohuwato", "polewali mandar", "ponorogo", "poso", "pulang pisau", "pulau morotai", "pulau taliabu", "puncak jaya", "raja ampat", "rejang lebong", "rote ndao", "siak", "sabu raijua", "sarolangun", "sekadau", "seram bagian timur", "siau tagulandang biaro", "sidenreng rappang", "sigi", "simeulue", "sinjai", "sintang", "situbondo", "solok selatan", "sragen", "sukamara", "sumba barat", "sumba barat daya", "sumba tengah", "tabalong", "tana tidung", "tana toraja",)
	harsh = ("kontol","memek","ngentot","kntl","mmk")

	if event.message.message.lower() in sup:
		inline = [[Button.inline("Order","order2")]]		
		msg = "Hasilnya, TKP Anda :  \n \nSupport Ekstra Unlimited ✅ \nSupport Unlimited Max ❌\n   \nMasukkan /order atau tekan **tombol** dibawah untuk pembelian."
		await event.reply(msg,buttons=inline)		

	elif event.message.message.lower() in tsup:
		inline = [[Button.inline("Order  !!","order3")]]
		msg = "Hasilnya, TKP Anda :  \n \nSupport Ekstra Unlimited ❌ \nSupport Unlimited Max ❌ \n  \nTenang anda masih tetap bisa melakukan pembelian dengan /order2 atau dengan tekan **tombol** dibawah."
		await event.reply(msg,buttons=inline)

	elif event.message.message.lower() in supmax:
		inline = [[Button.inline("Order","order2")]]
		msg = "Hasilnya,  TKP Anda : \n  \nSupport Ekstra Unlimited ✅ \nSupport Unlimited Max ✅  \n \nMasukkan /order atau tekan **tombol** dibawah untuk pembelian untuk pembelian"
		await event.reply(msg,buttons=inline)
	
	elif (
        event.message.message.lower() not in [supmax,sup,tsup]
        and not event.message.message.lower() in ["/notes","/order","/help","/start","/order2","/info"]):
#	else:
		await event.reply(f"Maaf, {event.message.message} tidak mengerti,   \nMasukkan /help untuk melihat command dan /notes untuk melihat catatan")


@bot.on(events.CallbackQuery(data=b"order3"))
@bot.on(events.InlineQuery)
async def order3(event):
	inline = [[Button.url("Order !!","https://www.tokopedia.com/warungmaniez/perdana-telkomsel-3000gb?utm_source=salinlink&utm_medium=share&utm_campaign=PDP-124552512-2742162704-010222")]]
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
	inline = [[Button.url("Order Disini","https://www.tokopedia.com/warungmaniez/perdana-telkomsel-3000gb?utm_source=salinlink&utm_medium=share&utm_campaign=PDP-124552512-2742162704-010222")],[Button.url("Kontak Admin","t.me/warungmaniez")]]
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
	msg = "**help** : \n \n/start untuk memulai \n/order untuk pembelian \n/order2 untuk melakukan pembelian kartu perdana \n/note untuk melihat notes \n/help untuk melihat commnad \n/info untuk melihat informasi tentang bot"
	await event.reply(msg,buttons=inline)

@bot.on(events.NewMessage(pattern="/start$"))
async def start(event):
	await event.reply("Selamat datang di CEK TKP BOT \nUntuk memulai, \nSilahkan masukkan kabupaten")

@bot.on(events.NewMessage(pattern="/info$"))
async def start(event):
	await event.reply("\n **CEK TKP BOT** \n \nVersion : 2.0 \nFramework : Telethon \nDeveloper : dibuat oleh @warungmaniez dengan dukungan mental oleh @xolvadev ")


bot.run_until_disconnected()
