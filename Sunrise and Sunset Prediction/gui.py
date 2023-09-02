import requests
from datetime import datetime, timedelta
from pathlib import Path
from tkinter import *
import tkinter.messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/achmadmaulanakusnadi/Desktop/Sunrise and Sunset Prediction/assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def show_message_box(message):
    root = Tk()
    root.withdraw()
    tkinter.messagebox.showerror("Error", message)

def mengisiData():
    canvas.itemconfig(harinya1,text= sunrise_sunset_data[0]['day'])
    canvas.itemconfig(harinya2,text= sunrise_sunset_data[1]['day'])
    canvas.itemconfig(harinya3,text=sunrise_sunset_data[2]['day'])
    canvas.itemconfig(harinya4,text= sunrise_sunset_data[3]['day'])
    canvas.itemconfig(harinya5,text=sunrise_sunset_data[4]['day'])
    canvas.itemconfig(harinya6,text=sunrise_sunset_data[5]['day'])

    canvas.itemconfig(tanggalnya1,text= sunrise_sunset_data[0]['date'])
    canvas.itemconfig(tanggalnya2,text= sunrise_sunset_data[1]['date'])
    canvas.itemconfig(tanggalnya3,text=sunrise_sunset_data[2]['date'])
    canvas.itemconfig(tanggalnya4,text= sunrise_sunset_data[3]['date'])
    canvas.itemconfig(tanggalnya5,text=sunrise_sunset_data[4]['date'])
    canvas.itemconfig(tanggalnya6,text=sunrise_sunset_data[5]['date'])

    canvas.itemconfig(waktuterbit1,text= sunrise_sunset_data[0]['sunrise'])
    canvas.itemconfig(waktuterbit2,text= sunrise_sunset_data[1]['sunrise'])
    canvas.itemconfig(waktuterbit3,text=sunrise_sunset_data[2]['sunrise'])
    canvas.itemconfig(waktuterbit4,text= sunrise_sunset_data[3]['sunrise'])
    canvas.itemconfig(waktuterbit5,text=sunrise_sunset_data[4]['sunrise'])
    canvas.itemconfig(waktuterbit6,text=sunrise_sunset_data[5]['sunrise'])

    canvas.itemconfig(waktuterbenam1,text= sunrise_sunset_data[0]['sunset'])
    canvas.itemconfig(waktuterbenam2,text= sunrise_sunset_data[1]['sunset'])
    canvas.itemconfig(waktuterbenam3,text=sunrise_sunset_data[2]['sunset'])
    canvas.itemconfig(waktuterbenam4,text= sunrise_sunset_data[3]['sunset'])
    canvas.itemconfig(waktuterbenam5,text=sunrise_sunset_data[4]['sunset'])
    canvas.itemconfig(waktuterbenam6,text=sunrise_sunset_data[5]['sunset'])

def menghapusData():
    canvas.itemconfig(harinya1,text= " ")
    canvas.itemconfig(harinya2,text= " ")
    canvas.itemconfig(harinya3,text= " ")
    canvas.itemconfig(harinya4,text= " ")
    canvas.itemconfig(harinya5,text= " ")
    canvas.itemconfig(harinya6,text= " ")

    canvas.itemconfig(tanggalnya1,text= " ")
    canvas.itemconfig(tanggalnya2,text= " ")
    canvas.itemconfig(tanggalnya3,text= " ")
    canvas.itemconfig(tanggalnya4,text= " ")
    canvas.itemconfig(tanggalnya5,text= " ")
    canvas.itemconfig(tanggalnya6,text= " ")

    canvas.itemconfig(waktuterbit1,text= " ")
    canvas.itemconfig(waktuterbit2,text= " ")
    canvas.itemconfig(waktuterbit3,text= " ")
    canvas.itemconfig(waktuterbit4,text= " ")
    canvas.itemconfig(waktuterbit5,text= " ")
    canvas.itemconfig(waktuterbit6,text= " ")

    canvas.itemconfig(waktuterbenam1,text= " ")
    canvas.itemconfig(waktuterbenam2,text= " ")
    canvas.itemconfig(waktuterbenam3,text= " ")
    canvas.itemconfig(waktuterbenam4,text= " ")
    canvas.itemconfig(waktuterbenam5,text= " ")
    canvas.itemconfig(waktuterbenam6,text= " ")    

API_KEY = "d485793245775bad0112e296db963d3a"

# fungsi tombol search
def tombolSearch():
    global sunrise_sunset_data
    global tempat_terbit_1,tempat_terbit_2,tempat_terbit_3,tempat_terbit_4, tempat_terbit_5,tempat_terbit_6
    global tempat_terbenam_1,tempat_terbenam_2,tempat_terbenam_3,tempat_terbenam_4,tempat_terbenam_5,tempat_terbenam_6
    global terbit_1,terbit_2,terbit_3,terbit_4,terbit_5,terbit_6
    global terbenam_1,terbenam_2,terbenam_3,terbenam_4,terbenam_5,terbenam_6
    global harinya1,harinya2,harinya3,harinya4,harinya5,harinya6
    global tanggalnya1,tanggalnya2,tanggalnya3,tanggalnya4,tanggalnya5,tanggalnya6
    global waktuterbit1,waktuterbit2,waktuterbit3,waktuterbit4,waktuterbit5,waktuterbit6
    global waktuterbenam1,waktuterbenam2,waktuterbenam3,waktuterbenam4,waktuterbenam5,waktuterbenam6
    
    # Hapus data
    try:
        menghapusData()
    except:
        NameError

    def get_sunrise_sunset_info(lat, lng, date):
    # Membuat permintaan GET ke API terbit-terbenam matahari dengan lintang, bujur, dan tanggal sebagai parameter
        response = requests.get(f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&date={date}")

        # Mengecek apakah respon dari API valid
        if response.status_code == 200:
            # Mengekstrak data JSON dari respon
            data = response.json()

            # Mengubah waktu terbit dan terbenam dari UTC menjadi WITA
            sunrise_utc = datetime.strptime(data['results']['sunrise'], '%I:%M:%S %p')
            sunrise_wita = sunrise_utc + timedelta(hours=8)
            sunset_utc = datetime.strptime(data['results']['sunset'], '%I:%M:%S %p')
            sunset_wita = sunset_utc + timedelta(hours=8)

            # Mengembalikan waktu terbit dan terbenam dalam format yang diinginkan
            return sunrise_wita.strftime('%I:%M:%S %p'), sunset_wita.strftime('%I:%M:%S %p')
        else:
            # Menampilkan pesan error jika respon dari API tidak valid
            tkinter.messagebox.showerror("Error", f"API error: {response.status_code} {response.text} \n Terjadi Error")

    # Menyimpan data terbit-terbenam matahari dalam sebuah list
    sunrise_sunset_data = []

    # Membuat permintaan GET ke API geocoding dengan nama kota sebagai parameter
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={inputKota()}&appid={API_KEY}")

    # Mengecek apakah respon dari API valid
    if response.status_code == 200:
        # Mengekstrak data JSON dari respon
        data = response.json()

        if data :
            # Dapatkan tanggal saat ini
                now = datetime.now()

                # Iterasikan melalui 7 hari berikutnya
                for i in range(7):
                    # Hitung tanggal untuk iterasi saat ini
                    date = now + timedelta(days=i)
                    # Format tanggal sebagai YYYY-MM-DD
                    date_str = date.strftime('%Y-%m-%d')
                    # Dapatkan waktu terbit dan terbenam matahari untuk tanggal saat ini
                    sunrise, sunset = get_sunrise_sunset_info(data[0]['lat'], data[0]['lon'], date_str)
                    # Tambahkan tanggal, terbit, dan terbenam ke list
                    sunrise_sunset_data.append({
                        'day': date.strftime('%A'),
                        'date': date.strftime('%d %B %Y'),
                        'sunrise': sunrise,
                        'sunset': sunset
                    })
        else:
            tkinter.messagebox.showerror(f"{inputKota} Not Found", "Silakan periksa apakah Anda telah mengetik dengan benar")

    else:
            # Menampilkan pesan error jika respon dari API tidak valid
            tkinter.messagebox.showerror("Error", f"API error: {response.status_code} {response.text} \n Terjadi Error")

    # Kolom 1
    harinya1 = canvas.create_text(
        26,
        86,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Inter", 30 * -1)
    )

    tanggalnya1 = canvas.create_text(
        26,
        123,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Inter", 12 * -1)
    )

    waktuterbit1 = canvas.create_text(
        247,
        89,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Inter", 12 * -1)
    )

    waktuterbenam1 = canvas.create_text(
        247,
        126,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Inter", 12 * -1)
    )

    tempat_terbit_1 = PhotoImage(
        file=relative_to_assets("Terbit.png"))
    terbit_1 = canvas.create_image(
        226,
        94,
        image=tempat_terbit_1
    )

    tempat_terbenam_1 = PhotoImage(
        file=relative_to_assets("Terbenam.png"))
    terbenam_1 = canvas.create_image(
        222,
        131,
        image=tempat_terbenam_1
    )

    # Kolom 2

    harinya2 = canvas.create_text(
        26.,
        166,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Inter", 30 * -1)
    )

    tanggalnya2 = canvas.create_text(
        26,
        204,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Inter", 12 * -1)
    )


    waktuterbit2 = canvas.create_text(
        247,
        170,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Inter", 12 * -1)
    )

    waktuterbenam2 = canvas.create_text(
        247,
        207,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Inter", 12 * -1)
    )

    tempat_terbit_2 = PhotoImage(
        file=relative_to_assets("Terbit.png"))
    terbit_2 = canvas.create_image(
        226,
        175,
        image=tempat_terbit_2
    )

    tempat_terbenam_2 = PhotoImage(
        file=relative_to_assets("Terbenam.png"))
    terbenam_2 = canvas.create_image(
        222,
        212,
        image=tempat_terbenam_2
    )

    # Kolom 3

    harinya3 = canvas.create_text(
        26,
        247,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Inter", 30 * -1)
    )

    tanggalnya3 = canvas.create_text(
        26,
        285,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Inter", 12 * -1)
    )



    waktuterbit3 = canvas.create_text(
        247,
        251,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Inter", 12 * -1)
    )

    waktuterbenam3 = canvas.create_text(
        247,
        288,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Inter", 12 * -1)
    )


    tempat_terbit_3 = PhotoImage(
        file=relative_to_assets("Terbit.png"))
    terbit_3 = canvas.create_image(
        226,
        255,
        image=tempat_terbit_3
    )

    tempat_terbenam_3 = PhotoImage(
        file=relative_to_assets("Terbenam.png"))
    terbenam_3 = canvas.create_image(
        222,
        293,
        image=tempat_terbenam_3
    )

    # Kolom 4

    harinya4 = canvas.create_text(
        26,
        328,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Inter", 30 * -1)
    )

    tanggalnya4 = canvas.create_text(
        26,
        366,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Inter", 12 * -1)
    )

    waktuterbit4 = canvas.create_text(
        247,
        332,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Inter", 12 * -1)
    )

    waktuterbenam4 = canvas.create_text(
        247,
        368,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Inter", 12 * -1)
    )

    tempat_terbit_4 = PhotoImage(
        file=relative_to_assets("Terbit.png"))
    terbit_4 = canvas.create_image(
        226,
        336,
        image=tempat_terbit_4
    )

    tempat_terbenam_4 = PhotoImage(
        file=relative_to_assets("Terbenam.png"))
    terbenam_4 = canvas.create_image(
        222,
        373,
        image=tempat_terbenam_4
    )

    # Kolom 5

    harinya5 = canvas.create_text(
        26,
        409,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Inter", 30 * -1)
    )

    tanggalnya5 = canvas.create_text(
        26,
        446,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Inter", 12 * -1)
    )

    waktuterbit5 = canvas.create_text(
        247,
        413,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Inter", 12 * -1)
    )

    waktuterbenam5 = canvas.create_text(
        247,
        449,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Inter", 12 * -1)
    )

    tempat_terbit_5 = PhotoImage(
        file=relative_to_assets("Terbit.png"))
    terbit_5 = canvas.create_image(
        226,
        417,
        image=tempat_terbit_5
    )

    tempat_terbenam_5 = PhotoImage(
        file=relative_to_assets("Terbenam.png"))
    terbenam_5 = canvas.create_image(
        222,
        454,
        image=tempat_terbenam_5
    )

    # Kolom 6

    harinya6 = canvas.create_text(
        26,
        490,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Inter", 30 * -1)
    )

    tanggalnya6 = canvas.create_text(
        26,
        527,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Inter", 12 * -1)
    )

    waktuterbit6 = canvas.create_text(
        247,
        494.07025146484375,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Inter", 12 * -1)
    )

    waktuterbenam6 = canvas.create_text(
        247,
        530.6324462890625,
        anchor="nw",
        text=" ",
        fill="#FFFFFF",
        font=("Inter", 12 * -1)
    )

    tempat_terbit_6 = PhotoImage(
        file=relative_to_assets("Terbit.png"))
    terbit_6 = canvas.create_image(
        222,
        499,
        image=tempat_terbit_6
    )

    tempat_terbenam_6 = PhotoImage(
        file=relative_to_assets("Terbenam.png"))
    terbenam_6 = canvas.create_image(
        222,
        535,
        image=tempat_terbenam_6
    )
    # Fungsi mengisi data canvas text
    mengisiData()

window = Tk()

window.geometry("354x640")
window.configure(bg = "#FFFFFF")
window.title("Sunrise and Sunset Prediction")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 640,
    width = 356,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    167.0,
    311.0,
    image=image_image_1
)

tempat_terbit_1 = PhotoImage(
    file=relative_to_assets("Terbit.png"))
terbit_1 = None

tempat_terbit_2 = PhotoImage(
    file=relative_to_assets("Terbit.png"))
terbit_2 = None

tempat_terbit_3 = PhotoImage(
    file=relative_to_assets("Terbit.png"))
terbit_3 = None

tempat_terbit_4 = PhotoImage(
    file=relative_to_assets("Terbit.png"))
terbit_4 = None

tempat_terbit_5 = PhotoImage(
    file=relative_to_assets("Terbit.png"))
terbit_5 = None

tempat_terbit_6 = PhotoImage(
    file=relative_to_assets("Terbit.png"))
terbit_6 = None

tempat_terbenam_1 = PhotoImage(
    file=relative_to_assets("Terbenam.png"))
terbenam_1 = None

tempat_terbenam_2 = PhotoImage(
    file=relative_to_assets("Terbenam.png"))
terbenam_2 = None

tempat_terbenam_3 = PhotoImage(
    file=relative_to_assets("Terbenam.png"))
terbenam_3 = None

tempat_terbenam_4 = PhotoImage(
    file=relative_to_assets("Terbenam.png"))
terbenam_4 = None

tempat_terbenam_5 = PhotoImage(
    file=relative_to_assets("Terbenam.png"))
terbenam_5 = None

tempat_terbenam_6 = PhotoImage(
    file=relative_to_assets("Terbenam.png"))
terbenam_6 = None



def inputKota():
    input_kota = var.get()
    return input_kota

def temp_text(e):
   entry_1.delete(0,"end")

var = StringVar()

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    201,
    40,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#999999",
    justify="left",
    highlightthickness=0,
    font=("Inter", 31 * -1),
    textvariable = var
)

entry_1.insert(0, "SEARCH HERE")
entry_1.bind("<FocusIn>", temp_text)

def autoupper(*arg):
    var.set(var.get().upper())

var.trace("w", autoupper)

entry_1.place(
    x=94,
    y=25,
    width=235,
    height=26
)


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: tombolSearch(),
    relief="flat"
)
button_1.place(
    x=18,
    y=13,
    width=44,
    height=44
)



window.resizable(False, False)
window.mainloop()
