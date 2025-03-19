
#TEST VE DOĞRULAMA AŞAMASI
from collections import defaultdict, deque
import heapq
from typing import Dict, List, Tuple, Optional


class Istasyon:
    """
    Metro istasyonlarını temsil eden sınıf.
    """

    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx  # İstasyonun benzersiz kimliği
        self.ad = ad  # İstasyon adı
        self.hat = hat  # İstasyonun bulunduğu metro hattı
        self.komsular: List[Tuple['Istasyon', int]] = []  # Komşu istasyonlar ve süreleri

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        """
        İstasyona bir komşu ekler.
        :param istasyon: Komşu istasyon nesnesi
        :param sure: İki istasyon arasındaki seyahat süresi (dakika)
        """
        self.komsular.append((istasyon, sure))

    def __lt__(self, other: 'Istasyon'):
        """
        Heapq karşılaştırmaları için eklenen metod.
        """
        return self.idx < other.idx  # Karşılaştırma için istasyon kimliği kullanılır


class MetroAgi:
    """
    Metro ağını temsil eden sınıf.
    """

    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}  # İstasyon kimliği -> Istasyon nesnesi
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)  # Hat adı -> İstasyon listesi

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        """
        Yeni bir istasyon ekler.
        """
        if idx not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        """
        İki istasyon arasında bağlantı ekler.
        """
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)

    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        """
        BFS algoritması kullanarak en az aktarma yapılan rotayı bulur.
        """
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        kuyruk = deque([(baslangic, [baslangic])])
        ziyaret_edildi = set()

        while kuyruk:
            mevcut, yol = kuyruk.popleft()
            if mevcut == hedef:
                return yol

            ziyaret_edildi.add(mevcut.idx)
            for komsu, _ in mevcut.komsular:
                if komsu.idx not in ziyaret_edildi:
                    kuyruk.append((komsu, yol + [komsu]))

        return None

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        """
        A* algoritmasına benzer şekilde en hızlı rotayı bulur.
        """
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        pq = [(0, baslangic.idx, baslangic, [baslangic])]
        ziyaret_edildi = {}

        while pq:
            toplam_sure, _, mevcut, yol = heapq.heappop(pq)
            if mevcut == hedef:
                return yol, toplam_sure

            if mevcut.idx in ziyaret_edildi and ziyaret_edildi[mevcut.idx] <= toplam_sure:
                continue

            ziyaret_edildi[mevcut.idx] = toplam_sure
            for komsu, sure in mevcut.komsular:
                heapq.heappush(pq, (toplam_sure + sure, komsu.idx, komsu, yol + [komsu]))

        return None


# Test Kodları
if __name__ == "__main__":
    metro = MetroAgi()
    metro.istasyon_ekle("A", "Kızılay", "Kırmızı")
    metro.istasyon_ekle("B", "Ulus", "Kırmızı")
    metro.istasyon_ekle("C", "Sıhhiye", "Mavi")
    metro.istasyon_ekle("D", "Gar", "Turuncu")
    metro.baglanti_ekle("A", "B", 5)
    metro.baglanti_ekle("A", "C", 3)
    metro.baglanti_ekle("B", "C", 4)
    metro.baglanti_ekle("C", "D", 2)

    test_senaryolari = [
        ("A", "D"),
        ("B", "C"),
        ("C", "A"),
        ("D", "B")
    ]

    for baslangic, hedef in test_senaryolari:
        print(f"\n{baslangic} -> {hedef} Testi")
        rota = metro.en_az_aktarma_bul(baslangic, hedef)
        if rota:
            print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
        else:
            print("Rota bulunamadı!")

        sonuc = metro.en_hizli_rota_bul(baslangic, hedef)
        if sonuc:
            rota, sure = sonuc
            print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
        else:
            print("Rota bulunamadı!")
