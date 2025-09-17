# Öğrenci Yönetim Sistemi
PASS_THRESHOLD = 50  # Geçme notu (isteğe göre değiştirilebilir)

# Başlangıç değişkenleri (görev 1)
class_name = "10A Sınıfı"
ogrenciler = [
    {"isim": "ALİ", "yas": 20, "not": 85},
    {"isim": "AYŞE", "yas": 21, "not": 90},
    {"isim": "MEHMET", "yas": 19, "not": 45},
    {"isim": "FATMA", "yas": 23, "not": 70}
]

# Programın başlangıçtaki özet değişkenleri
num_students = len(ogrenciler)
class_avg = sum([s['not'] for s in ogrenciler]) / num_students if num_students > 0 else 0.0
class_active = True  # sınıf aktif mi?


def print_menu():
    print('\n=== Öğrenci Yönetim Sistemi ===')
    print('1. Öğrenci Ekle')
    print('2. Öğrencileri Listele')
    print('3. Öğrenci Ara')
    print('4. İstatistikler')
    print('5. Çıkış')


def add_student():
    """Kullanıcıdan öğrenci alır, string işlemleri yapar ve listeye ekler."""
    global num_students, class_avg
    isim = input('İsim girin: ').strip().upper()  # isim büyük harfe çevrildi (görev 3)
    yas_girdi = input('Yaş girin: ').strip()
    not_girdi = input('Not girin: ').strip()

    try:
        yas = int(yas_girdi)  # yaş int'e çevrildi
        notu = int(not_girdi)  # not int'e çevrildi
    except ValueError:
        print('Hatalı değer girdiniz. Yaş ve not tam sayı olmalı.')
        # Hatalı girişte fonksiyondan döneriz; çağıran menü tekrar gösterir.
        pass
        return

    # Basit kontrol; örneğin negatif yaşsa işlem yapmayalım
    if yas <= 0:
        print('Geçersiz yaş girdiniz.')
        return

    ogrenci = {"isim": isim, "yas": yas, "not": notu}
    ogrenciler.append(ogrenci)

    # İstatistikleri güncelle
    num_students = len(ogrenciler)
    class_avg = sum([s['not'] for s in ogrenciler]) / num_students

    durum = 'Geçti' if notu >= PASS_THRESHOLD else 'Kaldı'
    
    # İsim ekranda daha okunaklı olsun diye title case ile gösteriyoruz
    print(f"{isim.title()} adlı öğrenci başarıyla eklendi. (Durum: {durum})")


def list_students():
    """Tüm öğrencileri listeler (görev 4)."""
    if not ogrenciler:
        print('Kayıtlı öğrenci yok.')
        return

    print('\nÖğrenciler:')
    # for döngüsü ile listeleme (görev 4)
    for s in ogrenciler:
        # Eğer not negatifse atla (örnek continue kullanımı)
        if s['not'] < 0:
            continue
        print(f"- {s['isim'].title()} ({s['yas']} yaşında) → Not: {s['not']}")


def search_student():
    """İsimle arama yapar. Bulursa döngüyü kırar (break kullanımı)."""
    if not ogrenciler:
        print('Arama yapılamaz — öğrenci kaydı yok.')
        return

    ara = input('Aranacak isim girin: ').strip().upper()

    for s in ogrenciler:
        if s['isim'] == ara:
            print(f"Bulundu: {s['isim'].title()} — Yaş: {s['yas']}, Not: {s['not']}")
            break
    else:
        # for-else: döngü kırılmazsa (yani bulunamazsa) burası çalışır
        print(f"{ara.title()} adlı öğrenci bulunamadı.")


def statistics():
    """Not istatistiklerini hesaplar (ortalama, max, min), list comprehension örnekleri."""
    if not ogrenciler:
        print('İstatistik yok — öğrenci kaydı yok.')
        return

    notlar = [s['not'] for s in ogrenciler]
    ort = sum(notlar) / len(notlar)
    en_yuksek = max(notlar)
    en_dusuk = min(notlar)

    # List comprehension ile geçen öğrencilerin isimleri (görev 5)
    gecenler = [s['isim'].title() for s in ogrenciler if s['not'] >= PASS_THRESHOLD]

    # Tüm notların kareleri (görev 5)
    not_kareleri = [n * n for n in notlar]

    # Set kullanımı: isimleri bir sete atıyoruz (görev 6)
    isim_seti = set([s['isim'].title() for s in ogrenciler])

    print('\n=== İstatistikler ===')
    print(f'Toplam öğrenci: {len(ogrenciler)}')
    print(f'Ortalama not: {ort:.2f}')
    print(f'En yüksek not: {en_yuksek}')
    print(f'En düşük not: {en_dusuk}')
    print(f'Geçen öğrenciler: {", ".join(gecenler) if gecenler else "Yok"}')
    print(f'Not kareleri: {not_kareleri}')
    print(f'Tekrarsız isimler (set): {sorted(list(isim_seti))}')


def main():
    """Ana menü döngüsü (görev 4: while + for kullanılcak)."""
    global class_name, class_active
    print(f"Program: {class_name} — Aktif: {class_active}")

    while True:
        print_menu()
        secim = input('Seçiminiz: ').strip()

        # Menü akışı kontrolü: pass/continue/break örnekleri
        if secim == '1':
            add_student()
        elif secim == '2':
            list_students()
        elif secim == '3':
            search_student()
        elif secim == '4':
            statistics()
        elif secim == '5':
            print('Programdan çıkılıyor...')
            break  # menüden çıkmak için break
        else:
            print('Geçersiz seçim, lütfen 1-5 arasında bir değer girin.')
            continue  # yanlış seçimde döngü başa sarar

    print('Görüşürüz!')


if __name__ == '__main__':
    main()