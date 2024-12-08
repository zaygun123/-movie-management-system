# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 17:30:54 2024

@author: Zeynep_Aygün
"""

import tkinter as tk
from tkinter import messagebox

class Film:
    def __init__(self, ad, yonetmen, yil, tur):
        self.ad = ad
        self.yonetmen = yonetmen
        self.yil = yil
        self.tur = tur

    def __str__(self):
        return f"Film: {self.ad}, Yönetmen: {self.yonetmen}, Yıl: {self.yil}, Tür: {self.tur}"

class FilmYoneticisi:
    def __init__(self):
        self.filmler = []

    def film_ekle(self, film):
        self.filmler.append(film)

    def film_sil(self, film_ad):
        for film in self.filmler:
            if film.ad == film_ad:
                self.filmler.remove(film)
                return f"{film_ad} filmi silindi."
        return f"{film_ad} bulunamadı."

    def film_listele(self, filtre_tur=None, filtre_yil=None):
        liste = self.filmler
        if filtre_tur:
            liste = [film for film in liste if film.tur == filtre_tur]
        if filtre_yil:
            liste = [film for film in liste if film.yil == filtre_yil]
        return [str(film) for film in liste]

class FilmYonetimGUI:
    def __init__(self, root):
        self.film_yonetici = FilmYoneticisi()
        self.root = root
        self.root.title("Film Yönetim Sistemi")

        
        self.film_ad_label = tk.Label(root, text="Film Adı:")
        self.film_ad_label.pack()
        self.film_ad_entry = tk.Entry(root)
        self.film_ad_entry.pack()

        self.yonetmen_ad_label = tk.Label(root, text="Yönetmen Adı:")
        self.yonetmen_ad_label.pack()
        self.yonetmen_ad_entry = tk.Entry(root)
        self.yonetmen_ad_entry.pack()

        self.yil_label = tk.Label(root, text="Yıl:")
        self.yil_label.pack()
        self.yil_entry = tk.Entry(root)
        self.yil_entry.pack()

        self.tur_label = tk.Label(root, text="Tür:")
        self.tur_label.pack()
        self.tur_entry = tk.Entry(root)
        self.tur_entry.pack()

        self.film_ekle_button = tk.Button(root, text="Film Ekle", command=self.film_ekle)
        self.film_ekle_button.pack()

        
        self.film_listele_button = tk.Button(root, text="Filmleri Listele", command=self.film_listele)
        self.film_listele_button.pack()

        self.film_listesi = tk.Listbox(root, height=10, width=50)
        self.film_listesi.pack()

        
        self.sil_film_ad_label = tk.Label(root, text="Silinecek Film Adı:")
        self.sil_film_ad_label.pack()
        self.sil_film_ad_entry = tk.Entry(root)
        self.sil_film_ad_entry.pack()

        self.film_sil_button = tk.Button(root, text="Film Sil", command=self.film_sil)
        self.film_sil_button.pack()

        
        self.filtre_yil_label = tk.Label(root, text="Filtrele Yıl:")
        self.filtre_yil_label.pack()
        self.filtre_yil_entry = tk.Entry(root)
        self.filtre_yil_entry.pack()

        self.filtre_tur_label = tk.Label(root, text="Filtrele Tür:")
        self.filtre_tur_label.pack()
        self.filtre_tur_entry = tk.Entry(root)
        self.filtre_tur_entry.pack()

        self.filtrele_button = tk.Button(root, text="Filtrele", command=self.filtrele)
        self.filtrele_button.pack()

    def film_ekle(self):
        film_ad = self.film_ad_entry.get()
        yonetmen_ad = self.yonetmen_ad_entry.get()
        yil = self.yil_entry.get()
        tur = self.tur_entry.get()
        if film_ad and yonetmen_ad and yil and tur:
            film = Film(film_ad, yonetmen_ad, int(yil), tur)
            self.film_yonetici.film_ekle(film)
            self.film_ad_entry.delete(0, tk.END)
            self.yonetmen_ad_entry.delete(0, tk.END)
            self.yil_entry.delete(0, tk.END)
            self.tur_entry.delete(0, tk.END)
            messagebox.showinfo("Başarılı", f"{film_ad} filmi başarıyla eklendi.")
        else:
            messagebox.showerror("Hata", "Tüm alanlar doldurulmalıdır.")

    def film_listele(self):
        self.film_listesi.delete(0, tk.END)
        filmler = self.film_yonetici.film_listele()
        for film in filmler:
            self.film_listesi.insert(tk.END, film)

    def film_sil(self):
        film_ad = self.sil_film_ad_entry.get()
        if film_ad:
            mesaj = self.film_yonetici.film_sil(film_ad)
            messagebox.showinfo("Sonuç", mesaj)
            self.sil_film_ad_entry.delete(0, tk.END)
            self.film_listele()
        else:
            messagebox.showerror("Hata", "Film adı boş olamaz.")

    def filtrele(self):
        yil = self.filtre_yil_entry.get()
        tur = self.filtre_tur_entry.get()
        if yil or tur:
            if yil:
                yil = int(yil)
            else:
                yil = None
            filmler = self.film_yonetici.film_listele(filtre_yil=yil, filtre_tur=tur)
            self.film_listesi.delete(0, tk.END)
            for film in filmler:
                self.film_listesi.insert(tk.END, film)
        else:
            messagebox.showerror("Hata", "Filtreleme için yıl veya tür girilmelidir.")

if __name__ == "__main__":
    root = tk.Tk()
    gui = FilmYonetimGUI(root)
    root.mainloop()
