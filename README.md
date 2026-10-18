# ATM Simülasyonu

Basit bir Python terminal uygulaması. Temel bankacılık işlemlerini simüle eder.

## Proje Hakkında

Bu proje, Python öğrenme sürecimde yazdığım küçük bir terminal uygulamasıdır. Gerçek bir banka sistemi değildir; amacım döngüler, koşullar, hata yönetimi ve modül kullanımı gibi temel Python kavramlarını pekiştirmekti.

## Özellikler

- Parola ile giriş (çalışma zamanında belirlenir, dosyada saklanmaz)
- Bakiye görüntüleme
- Para yatırma
- Para çekme
- Hatalı girişleri yakalama (try-except)
- Çıkış

## Kullanılan Teknolojiler

- Python 3
- getpass modülü (parolaları gizli almak için)

## Nasıl Çalıştırılır?

Python 3 kurulu olması yeterlidir.

`
python main.py
`

Program başlarken önce bir parola belirlemenizi, ardından başlangıç bakiyenizi girmenizi ister.

## Bu Projede Öğrendiklerim

- while döngüsü ve break / continue kullanımı
- try-except ile hata yönetimi
- Fonksiyon tanımlama ve parametre kullanımı
- import ile modül kullanımı
- getpass modülüyle gizli giriş alma
