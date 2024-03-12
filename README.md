# Derinlik Tahmini

Bu proje, görüntülerde derinlik tahmini yapmak için kullanılan bir derin öğrenme modelini içerir.

## Kurulum

Projeyi yerel makinenize klonlayın:

```bash
git clone https://github.com/kullanici/derinlik-tahmini.git
```

Python bağımlılıklarını yükleyin:

```bash
pip install -r requirements.txt
```

## Kullanım

Uygulama, komut satırı arayüzü üzerinden kullanılır. `cli.py` dosyasını kullanarak derinlik tahmini yapabilirsiniz.

```bash
python cli.py giriş_görüntüsü.png çıkış_görüntüsü.png
```

- `giriş_görüntüsü.png`: Derinlik tahmini yapmak istediğiniz görüntünün dosya yolu.
- `çıkış_görüntüsü.png`: Derinlik haritasının kaydedileceği dosyanın yolu.

Örnek:

```bash
python cli.py input/image.png output/depth_map.png
