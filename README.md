# IT Field Service Routing Optimization

## 1. Real-World Problem Context
Büyük bir şirketin bilgi işlem (IT) saha destek ekipleri, ağ (network) veya donanım arızalarına müdahale etmek için sürekli hareket halindedir. Arıza durumunda (downtime), sistemlerin kapalı kaldığı her dakika şirket için maddi kayıp ve iş gücü israfı anlamına gelir. Bu nedenle saha teknisyenlerinin hedeflerine ulaştıkları seyahat süresini minimuma indirmek kritik bir Yönetim Bilişim Sistemleri (MIS) ve lojistik problemidir.

## 2. Problem Definition
Şirketin "Fabrika" lokasyonunda kritik bir sunucu arızası meydana gelmiştir. "Merkez IT" ofisinde bulunan donanımlı destek ekibinin, şehir içi trafik ve mesafe faktörleri göz önüne alındığında "Fabrika" lokasyonuna ulaşabileceği en kısa ve en hızlı rotayı bulması gerekmektedir. 

## 3. Network Model
Bu problemde kurulan ağ modeli bir ulaşım ağıdır.
* **Nodes (Düğümler):** Şirketin ofisleri, şubeleri, veri merkezi ve Merkez IT binasını temsil etmektedir (Toplam 7 düğüm).
* **Edges (Kenarlar):** Bu lokasyonlar arasındaki mevcut karayolu bağlantılarını temsil eder.
* **Weights (Ağırlıklar):** Düğümler arasındaki kenarların ağırlıkları, mesafeye ve trafik durumuna bağlı "tahmini seyahat süresi (dakika)" olarak belirlenmiştir.

## 4. Nodes and Edges
**Nodes (7 Adet):** Merkez IT, Sube A, Sube B, Sube C, Sube D, Veri Merkezi, Fabrika.
**Edges (9 Adet) ve Ağırlıklar (Dakika):**
- Merkez IT <-> Sube A: 15
- Merkez IT <-> Sube B: 20
- Sube A <-> Sube C: 10
- Sube B <-> Sube C: 12
- Sube B <-> Sube D: 25
- Sube C <-> Veri Merkezi: 30
- Sube C <-> Sube D: 18
- Sube D <-> Fabrika: 15
- Veri Merkezi <-> Fabrika: 20

## 5. Selected Algorithm
Bu problem için **Shortest Path (En Kısa Yol)** optimizasyon modeli ve ardalanında çalışan **Dijkstra Algoritması** seçilmiştir. Hedefimiz başlangıç noktası (Merkez IT) ile bitiş noktası (Fabrika) arasındaki toplam ağırlığı (zamanı) minimize etmektir.

## 6. Python Implementation
Proje, Python ve ağ optimizasyonu için `NetworkX` kütüphanesi kullanılarak geliştirilmiştir. 
1. `nx.Graph()` ile yönlendirilmemiş bir graf oluşturuldu.
2. Düğümler ve bağlantılar tahmini varış süreleriyle grafiğe eklendi.
3. `nx.shortest_path()` fonksiyonu kullanılarak algoritma çalıştırıldı.
4. `matplotlib` kullanılarak ağın tamamı ve bulunan en kısa yol görselleştirildi.

## 7. Results
Algoritma çalıştırıldığında şu sonuçlar elde edilmiştir:
* **Seçilen Optimum Rota:** Merkez IT -> Sube A -> Sube C -> Sube D -> Fabrika
* **Toplam Seyahat Süresi:** 58 Dakika

Algoritma, görünürde daha az durak içeren (Merkez IT -> Sube B -> Sube D -> Fabrika = 60 dakika) rotayı değil, süre açısından daha kârlı olan alternatif rotayı (58 dakika) seçerek en hızlı yolu bulmuştur.

## 8. Managerial Interpretation
Bir MIS yöneticisi (IT Manager) veya İnsan Kaynakları İş Geliştirme (HR Business Development) uzmanı perspektifinden bu sonuçların anlamı şudur:
* **Hizmet Seviyesi Anlaşması (SLA) Uyumluluğu:** Arızaya müdahale süresi 60 dakikanın (1 saat) altına çekilerek şirketin kalite standartları korunmuştur.
* **Zaman ve İş Gücü Tasarrufu:** Manuel olarak rota planlaması yapıldığında çalışanlar tahmini rotalara yönelebilir. Veriye dayalı karar alma süreci (Data-Driven Decision Making) sayesinde seyahat süreleri %3-5 arasında optimize edilmiş, saha ekiplerinin verimliliği artırılmıştır.
* **Maliyet Düşüşü:** Seyahat süresinin kısalması, doğrudan yakıt tüketimini ve operasyonel maliyetleri düşürmektedir.

## 9. How to Run the Code
Kodu bilgisayarınızda çalıştırmak için:
1. Python'un sisteminizde kurulu olduğundan emin olun.
2. Terminali açın ve gerekli kütüphaneleri indirin: `pip install networkx matplotlib`
3. Proje dizinine gidin ve dosyayı çalıştırın: `python src/solution.py`
4. Çıktılar terminale yazdırılacak ve ağ görseli `results` klasörü içerisine oluşturulacaktır.

## 10. References
* NetworkX Documentation: https://networkx.org/documentation/stable/
* Management Information Systems Concepts, Routing Operations.
