# Ielādējam vajadzīgās bibliotēkas
import tkinter as tk  # Lai izveidotu logu un pogas
from tkinter import messagebox, Scrollbar, Toplevel, Listbox  # Papildu logiem un sarakstiem
import requests  # Lai nosūtītu pieprasījumu uz NASA mājaslapu
import webbrowser  # Lai atvērtu saites pārlūkā
import os  # Lai saglabātu failus datorā
import sqlite3 # Lai izveidotu databāzi un saglabātu favorītos
from PIL import Image  # Lai saglabātu bildes
from io import BytesIO  # Lai varētu strādāt ar bilžu datiem
import json  # Lai saglabātu un nolasītu favorītus kā sarakstu

# Nodrošina, ka mape "data" eksistē, kur tiks glabāta datubāze
os.makedirs("data", exist_ok=True)

# Pieslēdzas vai izveido datubāzes failu noteiktā mapē
conn = sqlite3.connect("C:/Users/Public/Pictures/nasa_app.db")
c = conn.cursor()

# Izveido tabulu, ja tā vēl neeksistē
c.execute('''CREATE TABLE IF NOT EXISTS favorites
             (title TEXT, date TEXT, explanation TEXT, url TEXT)''')
conn.commit()

# Šī klase palīdz mums sazināties ar NASA attēlu datubāzi
class NASASearch:
    def __init__(self, api_key="NKSphrGFoyGFmJONVTxPhNTRMM6I0bUWxr8iZzL4"):
        self.api_key = api_key  # Saglabā NASA API atslēgu

    # Šī funkcija meklē bildes pēc ievadīta vārda 
    def search_images(self, query, max_results=100): # Šis regulē, cik daudz rezultātu izmetīsies meklētājā
        url = f"https://images-api.nasa.gov/search?q={query}&media_type=image"
        response = requests.get(url)  # Nosūta pieprasījumu NASA serverim
        if response.status_code == 200:
            # Ja viss ir kārtībā, saņemam atbildi ar attēlu datiem
            items = response.json().get("collection", {}).get("items", [])
            return items[:max_results]  # Atgriežam tikai pirmos 100 rezultātus
        else:
            # Ja kaut kas noiet greizi
            print("Kļūda:", response.status_code)
            return []

# Funkcija, kas lejupielādē izvēlēto attēlu
def download_image():
    selected = listbox.curselection()  # Noskaidro, kuru rindu sarakstā izvēlējāmies
    if selected:
        index = selected[0]  # Paņemam izvēlēto kārtas numuru
        links = found_results[index].get("links", [{}])
        image_url = links[0].get("href") if links else None  # Atrodam attēla interneta adresi
        if image_url:
            response = requests.get(image_url)
            if response.status_code == 200:
                image_data = Image.open(BytesIO(response.content))  # Ielādējam bildi
                
                # V ŠĪ RINDA MAINA, KUR TIEK FAILS SAGLABĀTS
                file_name = f"C:/Users/Public/Pictures/nasa_image_{index + 1}.jpg"  # Izdomājam, kā nosaukt failu un kur to lokāli lejupielādēt
                
                image_data.save(file_name)  # Saglabājam failu datorā
                messagebox.showinfo("Veiksmīgi", f"Attēls saglabāts kā {file_name}")
            else:
                messagebox.showerror("Kļūda", "Neizdevās lejupielādēt attēlu.")
        else:
            messagebox.showerror("Kļūda", "Nav pieejams attēla URL.")
    else:
        messagebox.showwarning("Uzmanību", "Lūdzu, izvēlies attēlu no saraksta.")

# Funkcija, kas saglabā izvēlēto attēlu kā favorītu
def save_to_favorites():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        data = found_results[index].get("data", [{}])[0]
        links = found_results[index].get("links", [{}])
        image_url = links[0].get("href") if links else ""
        title = data.get("title", "Nav virsraksta")
        date = data.get("date_created", "Nav datuma")[:10]

        # Sagatavojam vienu favorīta ierakstu kā vārdnīcu
        favorite = {"title": title, "date": date, "url": image_url}

        # Nolasa jau esošos favorītus
        favorites = []
        if os.path.exists("favorites.json"):
            with open("favorites.json", "r", encoding="utf-8") as f:
                favorites = json.load(f)

        favorites.append(favorite)  # Pievieno jaunu favorītu sarakstam
        with open("favorites.json", "w", encoding="utf-8") as f:
            json.dump(favorites, f, ensure_ascii=False, indent=2)  # Saglabā failā

        messagebox.showinfo("Saglabāts", f"Attēls '{title}' pievienots favorītiem.")
    else:
        messagebox.showwarning("Uzmanību", "Izvēlies attēlu, ko pievienot.")

# Funkcija, kas atver logu, kur redzami visi favorīti
def open_favorites_window():
    if not os.path.exists("favorites.json"):
        messagebox.showinfo("Nav datu", "Favorītu saraksts ir tukšs.")
        return

    with open("favorites.json", "r", encoding="utf-8") as f:
        favorites = json.load(f)

    # Jauns logs priekš favorītiem
    top = Toplevel(root)
    top.title("Favorīti")
    top.geometry("600x400")
    top.configure(bg="#1e1e2f")

    listbox_fav = Listbox(top, font=("Arial", 12), bg="#2a2a3d", fg="white", width=80, height=20)
    listbox_fav.pack(pady=20)

    # Ievietojam katru favorītu sarakstā
    for item in favorites:
        listbox_fav.insert(tk.END, f"{item['date']} | {item['title']}")

# Funkcija, kas veic meklēšanu pēc ievadītā vārda
def perform_search():
    query = entry_search.get()  # Iegūstam, ko lietotājs ir ierakstījis
    if not query:
        messagebox.showwarning("Brīdinājums", "Ievadi, ko meklēt.")
        return

    listbox.delete(0, tk.END)  # Iztīra vecos rezultātus
    global found_results
    found_results = nasa.search_images(query)  # Veic meklēšanu

    if found_results:
        for i, item in enumerate(found_results, start=1):
            data = item.get("data", [{}])[0]
            title = data.get("title", "Nav nosaukuma")
            date = data.get("date_created", "Nav datuma")[:10]
            listbox.insert(tk.END, f"{i}. {date} | {title}")  # Ievieto sarakstā
    else:
        messagebox.showinfo("Nav rezultātu", "Attēli netika atrasti.")

# Funkcija, kas atver attēlu pārlūkā
def open_image():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        links = found_results[index].get("links", [{}])
        image_url = links[0].get("href") if links else None
        if image_url:
            webbrowser.open(image_url)
        else:
            messagebox.showerror("Kļūda", "Nav pieejams attēla URL.")
    else:
        messagebox.showwarning("Brīdinājums", "Izvēlies attēlu, ko atvērt.")

# ====== Sākam veidot pašu logu (interface) ======

# Izveidojam galveno logu
root = tk.Tk()
root.title("NASA Attēlu Meklētājs")
root.geometry("850x600")
root.configure(bg="#1e1e2f")  # Tumšs fons

# Virsraksts augšpusē
label_title = tk.Label(root, text="NASA Attēlu Meklētājs", font=("Helvetica", 20, "bold"), bg="#1e1e2f", fg="white")
label_title.pack(pady=10)

# Rinda ar meklēšanas lauku un pogu
frame_search = tk.Frame(root, bg="#1e1e2f")
frame_search.pack()

entry_search = tk.Entry(frame_search, font=("Arial", 14), width=40)
entry_search.pack(side=tk.LEFT, padx=10)

btn_search = tk.Button(frame_search, text="Meklēt", font=("Arial", 12), bg="#4e88e3", fg="white", command=perform_search)
btn_search.pack(side=tk.LEFT)

# Saraksts, kur parādās meklēšanas rezultāti
frame_listbox = tk.Frame(root)
frame_listbox.pack(pady=10)

scrollbar = Scrollbar(frame_listbox)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame_listbox, font=("Arial", 12), width=100, height=15, bg="#2a2a3d", fg="white", yscrollcommand=scrollbar.set)
listbox.pack()

scrollbar.config(command=listbox.yview)

# Dažādas pogas zem saraksta
btn_open = tk.Button(root, text="Atvērt attēlu pārlūkā", font=("Arial", 12), bg="#34a853", fg="white", command=open_image)
btn_open.pack(pady=5)

btn_download = tk.Button(root, text="Lejupielādēt attēlu", font=("Arial", 12), bg="#ff9800", fg="white", command=download_image)
btn_download.pack(pady=5)

btn_fav = tk.Button(root, text="Pievienot favorītiem", font=("Arial", 12), bg="#8e44ad", fg="white", command=save_to_favorites)
btn_fav.pack(pady=5)

btn_view_fav = tk.Button(root, text="Skatīt favorītus", font=("Arial", 12), bg="#607d8b", fg="white", command=open_favorites_window)
btn_view_fav.pack(pady=5)

# Izveido NASA API objektu
nasa = NASASearch()
found_results = []  # Tukšs saraksts, kur glabāsim atrastos rezultātus

# Palaidam programmu
root.mainloop()