def quiz():
    sorular = [
        {"soru": "Python hangi yıl çıkmıştır?", "cevap": "1991", "puan": 10, "kategori": "Programlama"},
        {"soru": "Dünya'nın uydusu nedir?", "cevap": "Ay", "puan": 5, "kategori": "Genel Kültür"},
        {"soru": "HTML bir programlama dili midir?", "cevap": "Hayır", "puan": 5, "kategori": "Web Teknolojileri"},
        {"soru": "Türkiye'nin başkenti neresidir?", "cevap": "Ankara", "puan": 5, "kategori": "Coğrafya"},
        {"soru": "Su kaç derecede donar?", "cevap": "0", "puan": 5, "kategori": "Fen Bilgisi"},
        {"soru": "Python'da listeleri sıralamak için hangi fonksiyon kullanılır?", "cevap": "sort", "puan": 10, "kategori": "Programlama"},
        {"soru": "Güneş sistemindeki en büyük gezegen hangisidir?", "cevap": "Jüpiter", "puan": 10, "kategori": "Astronomi"},
        {"soru": "Bir HTML sayfasında başlık etiketleri hangi harflerle başlar?", "cevap": "h", "puan": 5, "kategori": "Web Teknolojileri"}
    ]

    print("Merhaba! Gelişmiş Quiz'e hoş geldiniz.\n")
    toplam_puan = 0

    for soru_obj in sorular:
        soru = soru_obj["soru"]
        cevap = soru_obj["cevap"]
        puan = soru_obj["puan"]
        kategori = soru_obj["kategori"]

        print(f"Kategori: {kategori}")
        kullanici_cevap = input(soru + " ")
        if kullanici_cevap.strip().lower() == cevap.lower():
            print(f"Doğru! +{puan} puan\n")
            toplam_puan += puan
        else:
            print(f"Yanlış! Doğru cevap: {cevap}\n")

    print(f"Quiz tamamlandı! Toplam puanınız: {toplam_puan}/{sum(q['puan'] for q in sorular)}\n")

    max_puan = sum(q['puan'] for q in sorular)
    if toplam_puan == max_puan:
        print("Muhteşemsin dostum! Tüm soruları doğru cevapladınız.")
    elif toplam_puan >= max_puan * 0.7:
        print("Harika! Çok iyi bir performans.")
    elif toplam_puan >= max_puan * 0.4:
        print("Eh İşte.. Daha fazla çalışmalısınız.")
    else:
        print("Aooo malesef düşük puan. Daha fazla çalışma yapın!")

if __name__ == "__main__":
    quiz()