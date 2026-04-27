class deneme:
    
    def __init__():
        print("deneme sınıfı oluşturuldu")
    
    def yaz():
        print("yaz fonksiyonu çalıştı")


    def list_operations():
        """
        Bu fonksiyon sorted(), map(), filter() fonksiyonlarını professional şekilde kullanır.
        """
        
        # Örnek liste
        numbers = [5, 2, 8, 1, 9, 3, 7, 4, 6]
        
        # filter() ile 5'den büyük ve 8'den küçük sayıları filtrele
        filtered = filter(lambda x: x > 5 and x < 8, numbers)
        
        # map() ile filtrelenmiş sayıları 2 ile çarp
        mapped = map(lambda x: x * 2, filtered)
        
        # sorted() ile sonuçları sırala
        result = sorted(list(mapped))
        
        print(f"Orijinal liste: {numbers}")
        print(f"Sonuç (5'den büyük sayılar * 2, sıralı): {result}")
        return result

        
class deneme2:
    
    def __init__():
        print("deneme2 sınıfı oluşturuldu")
    
    def yaz():
        print("yaz fonksiyonu çalıştı")        
