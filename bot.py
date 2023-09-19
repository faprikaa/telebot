from telegram.ext import *
from telegram import *
import time

print ("bot  dimulai")

def start_dong(update, context):
	update.message.reply_text("Selamat datang di CEK TKP BOT \nUntuk memulai, \nSilahkan masukkan kabupaten")

def sample_responses(input_text):
	user_message = str(input_text).lower()

	sup = ("aceh tamiang", "aceh timur", "bantul", "deli serdang", "demak", "kota binjai", "karanganyar", "kota langsa", "kendal", "kota medan", "klaten", "kota pematang siantar", "kota salatiga", "kota tebing tinggi", "kota surakarta", "langkat", "kota yogyakarta", "samosir", "semarang", "serdang bedagai", "sleman", "simalungun", "sukoharjo", "toba samosir", "agam", "bintan", "karimun", "kota semarang", "kota batam", "kota bukit tinggi", "kota padang", "kota pariaman", "kota payakumbuh", "bondowoso", "kota solok", "gresik", "kota tanjung pinang", "kota batu", "lima puluh kota", "kota kediri", "padang pariaman", "kota malang", "solok", "kota surabaya", "magetan", "malang", "sidoarjo", "banyu asin", "kediri", "bengkulu tengah", "kepahiang", "nganjuk", "kota bengkulu", "kota jambi", "kota metro", "badung", "kota palembang", "bangli", "kota pangkal pinang", "buleleng", "kota prabumulih", "gianyar", "jembrana", "karang asem", "muara enim", "klungkung", "muaro jambi", "kota denpasar", "ogan ilir", "ogan komering ilir", "ogan komering ulu", "ogan komering ulu timur", "tabanan", "seluma", "tebo", "way kanan", "kota bontang", "kota tangerang", "kota tangerang selatan", "kota waringin barat", "tangerang", "kota waringin timur", "bandung", "barru", "ciamis", "bolaang mongondow", "garut", "bulukumba", "kota bandung", "gowa", "kota banjar kota tasikmalaya", "kepulauan selayar", "pangandaran", "kota gorontalo", "tasikmalaya", "kota makassar", "kota manado", "kota parepare", "kota tomohon", "maros", "minahasa", "minahasa utara", "soppeng",)

	if user_message in sup:
		return "Hasilnya, TKP Anda : \nSupport Ekstra Unlimited ✅ \nSupport Unlimited Max ❌ \nMasukkan /order untuk pembelian"

	tsup = ("aceh jaya", "batam", "besukur", "besukurhigh", "kapal", "karangasem", "ceremai", "sinabung", "kota bau-bau", "kota lubuk linggau", "kota pangkalpinang", "kota sengkang", "bukit raya", "bukit siguntang", "dobonsolo", "dorolonda", "gunung dempo", "kelimutu", "kelud", "labobar", "lambelu", "lawit", "nggapulu", "sirimau", "tidar", "tilongkabila", "madura", "mataram lombok", "ntb", "pantura", "payakumbuh", "pematangsiantar", "pematangsiantarout", "pontianak", "selayar", "sibolga", "sibolgaout", "sungai penuh", "tanah bumbu", "tanah datar", "tanah laut", "tanggamus", "tanjung jabung barat", "tanjung jabung timur", "tapanuli tengah", "aceh selatan", "tapin", "aceh utara", "tulungagung", "temanggung", "asahan", "timor tengah selatan", "banggai kepulauan", "timor tengah utara", "banggai laut", "tojo una-una", "banjarnegara", "trenggalek", "tulang bawang barat", "aceh barat", "barito kuala", "aceh barat daya", "aceh besar", "batu bara", "aceh singkil", "belu", "bener meriah", "aceh tengah", "bengkayang", "aceh tenggara", "bengkulu selatan", "alor", "asmat", "bengkulu utara", "balangan", "bireuen", "blitar", "bandung barat", "banggai", "bolaang mongondow selatan", "bolaang mongondow timur", "bolaang mongondow utara", "bungo", "buru selatan", "buton", "buton selatan", "buton tengah", "buton utara", "banyumas", "cilacap", "banyuwangi", "dharmasraya", "barito selatan", "dompu", "barito timur", "donggala", "barito utara", "empat lawang", "ende", "batang hari", "flores timur", "bekasi", "gayo lues", "gorontalo utara", "bengkalis", "grobogan", "berau", "gunung kidul", "biak numfor", "halmahera barat", "bima", "halmahera selatan", "blora", "halmahera tengah", "boalemo", "halmahera timur", "bogor", "halmahera utara", "bojonegoro", "hulu sungai selatan", "bombana", "hulu sungai tengah", "bone", "bone bolango", "humbang hasundutan", "boven digoel", "indragiri hulu", "boyolali", "jember", "jepara", "bulungan", "buol", "kampar", "buru", "cianjur", "karo", "katingan", "dairi", "kaur", "deiyai", "kepulauan anambas", "dogiyai", "kepulauan aru", "enrekang", "kepulauan mentawai", "fakfak", "kepulauan meranti", "kepulauan sangihe", "kepulauan sula", "gorontalo", "kepulauan talaud", "kerinci", "gunung mas", "gunungsitoli", "kolaka timur", "indragiri hilir", "kolaka utara", "konawe kepulauan", "intan jaya", "konawe utara", "kota balikpapan", "jakarta barat", "kota bandar lampung", "jakarta pusat", "jakarta selatan", "kota banjar", "jakarta timur", "kota banjar baru", "jakarta utara", "kota baru", "jayapura", "jayawijaya", "kaimana", "kota bekasi", "kapuas", "kapuas hulu", "kota bima", "kota bitung", "kayong utara", "kota blitar", "kebumen", "kota bogor", "keerom", "kepulauan seribu", "kota depok", "kepulauan yapen", "kota dumai", "ketapang", "kolaka", "konawe", "kota kotamobagu", "konawe selatan", "kota ambon", "kota lhokseumawe", "kota banda aceh", "kota lubuklinggau", "kota banjarmasin", "kota madiun", "kota baubau", "kota padang panjang", "kota jayapura", "kota padangsidimpuan", "kota kendari", "kota pagar alam", "kota kupang", "kota palangkaraya", "kota magelang", "kota palopo", "kota palu", "kota pasuruan", "kota pare-pare", "kota pekanbaru", "kota probolinggo", "kota sabang", "kota samarinda", "kota sawah lunto", "kota sibolga", "kota subulussalam", "kota sorong", "kota sungai penuh", "kutai barat", "kutai kertanegara", "lamongan", "lanny jaya", "kota tanjung balai", "kota tarakan", "lombok utara", "kota tasikmalaya", "lumajang", "luwu timur", "mamasa", "kota ternate", "mamberamo raya", "kota tidore kepulauan", "mamberamo tengah", "mamuju tengah", "kota tual", "mamuju utara", "mandailing natal", "manggarai barat", "manokwari", "kuantan singingi", "manokwari selatan", "mappi", "kudus", "maybrat", "kulon progo", "merauke", "mimika", "kupang", "kutai kartanegara", "nabire", "all", "kutai timur", "nduga", "labuhan batu", "nias", "labuhan batu selatan", "nias selatan", "labuhan batu utara", "paniai", "lahat", "pegunungan arfak", "lamandau", "pegunungan bintang", "lampung barat", "pesisir selatan", "pidie jaya", "lampung tengah", "pinrang", "probolinggo", "lampung utara", "puncak", "landak", "purbalingga", "lebong", "purworejo", "lembata", "rembang", "lingga", "rokan hilir", "rokan hulu", "luwu", "luwu utara", "sanggau", "madiun", "sarmi", "magelang", "seram bagian barat", "mahakam ulu", "seruyan", "majene", "sijunjung", "malaka", "sikka", "malinau", "maluku barat daya", "maluku tengah", "sorong", "maluku tenggara", "sorong selatan", "maluku tenggara barat", "mamuju", "manggarai", "manggarai timur", "sumba timur", "sumbawa", "melawi", "sumbawa barat", "merangin", "supiori", "mesuji", "tambrauw", "minahasa selatan", "tanggamung", "minahasa tenggara", "tapanuli", "tapanuli selatan", "tapanuli utara", "morowali", "morowali utara", "teluk bintuni", "teluk wondama", "mukomuko", "muna", "toli-toli", "muna barat", "tolikara", "murung raya", "toraja utara", "musi banyuasin", "tuban", "musi rawas", "tulangbawang", "musi rawas utara", "wajo", "nagan raya", "wakatobi", "nagekeo", "waropen", "natuna", "ngada", "wonogiri", "wonosobo", "ngawi", "yalimo", "nias barat", "yahukimo", "nias utara", "nunukan", "ogan komering ulu selatan", "pacitan", "padang lawas", "padang lawas utara", "pakpak bharat", "pangkajene dan kepulauan", "parigi moutong", "pasaman", "pasaman barat", "paser", "pasuruan", "pati", "pelalawan", "pemalang", "penajam paser utara", "penukal abab lematang ilir", "pesisir barat", "pidie", "pohuwato", "polewali mandar", "ponorogo", "poso", "pulang pisau", "pulau morotai", "pulau taliabu", "puncak jaya", "raja ampat", "rejang lebong", "rote ndao", "siak", "sabu raijua", "sarolangun", "sekadau", "seram bagian timur", "siau tagulandang biaro", "sidenreng rappang", "sigi", "simeulue", "sinjai", "sintang", "situbondo", "solok selatan", "sragen", "sukamara", "sumba barat", "sumba barat daya", "sumba tengah", "tabalong", "tana tidung", "tana toraja",)

	if user_message in tsup:
		return "Hasilnya, TKP Anda : \nSupport Ekstra Unlimited ❌ \nSupport Unlimited Max ❌ \nMohon maaf, Anda belum bisa melakukan pemebelian"
    
	supmax = ("kota pekalongan","pekalongan","Lombok Utara","bandar lampung","Pemalang","tegal","banjar","Hulu Sungai Selatan","Metro","Hulu Sungai Tengah","hulu sungai utara","kota Banjar Baru","Bandung Barat","kota Banjarmasin","lampung selatan","Cianjur","lampung timur","cirebon","kota cirebon","kota pontianak","indramayu","kota singkawang","kota cimahi","bangkalan","kuningan","jombang","kubu raya","majalengka","mempawah","subang","kota mojokerto","sambas","pesawaran","sumedang","mojokerto","bantaeng","bangka barat","bangka","bangka selatan","bangka tengah","belitung","belitung timur", "pringsewu","kota cilegon", "kota serang", "lebak", "pandeglang","serang", "karawang", "kota sukabumi", "purwakarta", "sukabumi","brebes","batang","lombok timur","takalar","jeneponto","lombok barat","lombok tengah","pamekasan","kota tegal","sumenep","sampang","kota mataram",)

	if user_message in supmax:
		return "Hasilnya, TKP Anda : \nSupport Ekstra Unlimited ✅ \nSupport Unlimited Max ✅ \nMasukkan /order untuk pembelian"
    
	harsh = ("kontol","memek","ngentot","kntl","mmk")

	if user_message in harsh:
		return("bacot ngentot")
    
	return str("Maaf, kata kata tidak dimengerti \nMasukkan /help untuk bantuan.")
    
def help_dong(update, context):
    update.message.reply_text("help : \n \n/start untuk memulai \n/order untuk pembelian \n/note untuk melihat notes \n/admin untuk menghubungi admin \n/help untuk bantuan")
    
def order(update, context):
    update.message.reply_text("order : \n  \nSilahkan hubungi admin dengan /admin untuk melakukan pembelian \nUntuk melihat pricelist tekan disini https://t.me/testimaniez/5")
    
def admin(update, context):
    update.message.reply_text("admin : \n  \nUntuk menghubungin admin kirim pesan ke \n@warungmaniez")

def notes(update, context):
    update.message.reply_text("notes : \n \n1. Jika sudah memasukkan nama kabupaten dengan benar namun masih \'..tidak diketahui..\' coba tambahkan \'kota\' didepannya \n2. Penambahan kata \'kota\' dapat menghasilkan hasil yang berbeda")

def handle_message(update, context):
	text =  str(update.message.text).lower()
	response = sample_responses(text)

	update.message.reply_text(response)

def main():
	updater = Updater('5055839545:xxxxxxxxxxxxxxxxxxxx', use_context=True)
	dp = updater.dispatcher

	dp.add_handler(CommandHandler("start", start_dong))
	dp.add_handler(CommandHandler("order", order))
	dp.add_handler(CommandHandler("help", help_dong))
	dp.add_handler(CommandHandler("note", notes))

	dp.add_handler(MessageHandler(Filters.text, handle_message))

	updater.start_polling()

main()
