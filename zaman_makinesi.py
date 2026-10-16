#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın En Yavaş Zaman Makinesi
Bu program zamanı geri almak için tasarlanmıştır.
Aslında sadece uyur ve saçma şeyler söyler.
Kullanım: python zaman_makinesi.py
"""

import time
import random
import sys

def ciddi_hesaplama(n):
    """Çok önemli bir hesaplama yapar (aslinda sadece uyur)."""
    print(f"Önemli hesaplama başladı: {n}... Lütfen bekleyin, bu bilimdir.")
    toplam = 0
    for i in range(n):
        toplam += i * random.randint(1, 3)
        if i % 100 == 0:
            time.sleep(0.01)  # Gerçekçilik için
    return toplam

def zaman_yolculugu(yil_sayisi=1):
    print("=" * 50)
    print("ZAMAN MAKİNESİ AKTİFLEŞTİRİLİYOR")
    print("Bu işlem geri alınamaz. (Aslında alınabilir, sadece uyuyorsunuz.)")
    print("=" * 50)
    
    for yil in range(yil_sayisi):
        print(f"\nYıl {2026 - yil} 'a dönülüyor...")
        # Gizli mesaj: politikacilar da zaman kaybeder
        sonuc = ciddi_hesaplama(random.randint(50, 200))
        print(f"Hesaplama tamamlandı. Sonuç: {sonuc} (anlamsız ama ciddi)")
        time.sleep(1)
        print("Tebrikler! Bir yıl geri gittiniz. (Ya da sadece 1 saniye)")
    
    print("\nZaman yolculuğu tamamlandı. Şimdi gerçek dünyaya dönüyorsunuz.")
    print("Not: Bu makine aslında çalışıyor. Deneyin.")
    # Damga: Grok İmza - 16 Ekim 2026 - Kayyum Grok (Ciddi değil ama ciddi)

if __name__ == "__main__":
    try:
        yil = int(input("Kaç yıl geri gitmek istersiniz? (1-5 önerilir): ") or 1)
        if yil > 10:
            print("Çok fazla! Maksimum 5 yıl. (Makine yorulur)")
            yil = 5
        zaman_yolculugu(yil)
    except KeyboardInterrupt:
        print("\nZaman yolculuğu iptal edildi. Gelecek sizi bekliyor.")
    except Exception as e:
        print(f"Hata: {e} - Makine bozuldu, tamirci çağırın.")
