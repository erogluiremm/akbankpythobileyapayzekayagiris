Sürücüsüz Metro Simülasyonu (Rota Optimizasyonu)

Bu proje, bir metro ağında en hızlı ve en az aktarmalı rotaları bulmak için BFS (Breadth-First Search) ve A* benzeri algoritmalar** kullanarak bir simülasyon sunar.

🚀 Proje Amacı

Bu projede aşağıdaki hedeflere ulaşılması amaçlanmıştır:

Metro ağını bir graf yapısı ile modellemek

BFS algoritması ile en az aktarmalı rotayı bulmak

A* algoritmasına benzer bir yöntemle en hızlı rotayı bulmak**

Gerçek dünya problemlerini algoritmalarla çözmek

🛠 Kullanılan Teknolojiler ve Kütüphaneler

Python: Genel programlama dili

collections.deque: BFS algoritması için kuyruk yapısı

heapq: Öncelik kuyruğu ile en hızlı rotayı bulma

defaultdict: Hatları organize etmek için kullanılan veri yapısı

📌 Algoritmaların Çalışma Mantığı

1️⃣ BFS (En Az Aktarmalı Rota)

Kuyruk (queue) kullanılarak istasyonlar sırayla ziyaret edilir.

Ziyaret edilen istasyonlar işaretlenir.

Hedef istasyona ulaşana kadar en kısa yol aranır.

2️⃣ A* Algoritması Benzeri Yaklaşım (En Hızlı Rota)**

Heapq (öncelik kuyruğu) kullanılarak en düşük maliyetli yol öncelikli seçilir.

Ziyaret edilen istasyonlar ve süreler takip edilir.

Her adımda en hızlı ulaşım süresi güncellenir.

📊 Örnek Kullanım

# Metro ağı oluşturuluyor
metro = MetroAgi()
metro.istasyon_ekle("A", "Kızılay", "Kırmızı")
metro.istasyon_ekle("B", "Ulus", "Kırmızı")
metro.istasyon_ekle("C", "Sıhhiye", "Mavi")
metro.baglanti_ekle("A", "B", 5)
metro.baglanti_ekle("A", "C", 3)

# En az aktarmalı rota
rota = metro.en_az_aktarma_bul("A", "C")
print(" -> ".join(i.ad for i in rota))

# En hızlı rota
rota, sure = metro.en_hizli_rota_bul("A", "C")
print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))


🔍 Geliştirme Fikirleri

Görselleştirme eklenmesi (Grafikleriyle metro haritası çizilebilir)

Gerçek dünya verileriyle genişletme (Örnek olarak İstanbul veya Ankara metrosu)

Trafik yoğunluğu ve bekleme süreleri ekleme
