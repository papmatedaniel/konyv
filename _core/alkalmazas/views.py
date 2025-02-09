from django.shortcuts import render, redirect, get_object_or_404
from .models import Konyvek, Szerzok, Mufajok
# from django.shortcuts import get_object_or_404
# from .forms import KonyvekForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')

def hozzad(request):
    szerzok = Szerzok.objects.all()
    mufajok = Mufajok.objects.all()

    if request.method == "POST":
        cime = request.POST['cim']
        szerzoje = request.POST['szerzo']
        mufaja = request.POST['mufaj']
        kiadas_eve = request.POST.get('kiadas_ev')
        kiado = request.POST.get('kiado')
        nyelv = request.POST.get('nyelv')
        oldalszam = request.POST.get('oldalszam')
        kotes_tipus = request.POST.get('kotes')
        leiras = request.POST.get('leiras')
        # borito_kep = request.FILES.get('borito_kep')

        # oldalszam = int(oldalszam) if oldalszam else None
        # kiadas_eve = int(kiadas_eve) if kiadas_eve else None

        szerzo, _ = Szerzok.objects.get_or_create(szerzo=szerzoje)
        mufaj, _ = Mufajok.objects.get_or_create(mufaj=mufaja)

        konyv = Konyvek.objects.create(
            cim=cime,
            kiadas_eve=kiadas_eve,
            kiado=kiado,
            nyelv=nyelv,
            oldalszam=oldalszam,
            kotes_tipus=kotes_tipus,
            leiras=leiras,
            # borito_kep=borito_kep
        )
        konyv.szerzok.add(szerzo)
        konyv.mufajok.add(mufaj)
        
        return redirect('adatok')
    
    return render(request, 'hozzad.html', {'szerzok': szerzok, 'mufajok': mufajok, 'konyv': None})

def konyvek(request):
    konyvek = Konyvek.objects.all()
    return render(request, 'konyvek.html', {'konyvek': konyvek})

def szerzok(request):
    szerzok = Szerzok.objects.all()
    return render(request, 'szerzok.html', {'szerzok': szerzok})

def mufajok(request):
    mufajok = Mufajok.objects.all()
    return render(request, 'mufajok.html', {'mufajok': mufajok})

def adatok(request):
    konyvek = Konyvek.objects.all()
    return render(request, 'adatok.html', {'konyvek': konyvek})


def szerkeszt_konyv(request, konyv_id):
    konyv = get_object_or_404(Konyvek, id=konyv_id)
    szerzok = Szerzok.objects.all()
    mufajok = Mufajok.objects.all()
    kezdo_szerzok = ", ".join([szerzo.szerzo for szerzo in konyv.szerzok.all()])
    kezdo_mufajok = ", ".join([mufaj.mufaj for mufaj in konyv.mufajok.all()])

    if request.method == "POST":
        # Cím és opcionális mezők frissítése
        konyv.cim = request.POST.get('cim', konyv.cim)
        konyv.kiadas_eve = request.POST.get('kiadas_ev', konyv.kiadas_eve)
        konyv.kiado = request.POST.get('kiado', konyv.kiado)
        konyv.nyelv = request.POST.get('nyelv', konyv.nyelv)
        konyv.oldalszam = request.POST.get('oldalszam', konyv.oldalszam)
        konyv.kotes_tipus = request.POST.get('kotes', konyv.kotes_tipus)
        konyv.leiras = request.POST.get('leiras', konyv.leiras)
        konyv.save()

        # Szerzők frissítése (vesszővel elválasztott szöveg feldolgozása)
        szerzo_nevek = [nev.strip() for nev in request.POST.get('szerzo', '').split(',')]
        konyv.szerzok.clear()
        for nev in szerzo_nevek:
            if nev:  # Csak nem üres értékek feldolgozása
                szerzo, _ = Szerzok.objects.get_or_create(szerzo=nev)
                konyv.szerzok.add(szerzo)

        # Műfajok frissítése (vesszővel elválasztott szöveg feldolgozása)
        mufaj_nevek = [nev.strip() for nev in request.POST.get('mufaj', '').split(',')]
        konyv.mufajok.clear()
        for nev in mufaj_nevek:
            if nev:  # Csak nem üres értékek feldolgozása
                mufaj, _ = Mufajok.objects.get_or_create(mufaj=nev)
                konyv.mufajok.add(mufaj)

        return redirect('adatok')

    return render(request, 'szerkeszt.html', {
        'konyv': konyv,
        'szerzok': szerzok,
        'mufajok': mufajok,
        'kezdo_szerzok': kezdo_szerzok,
        'kezdo_mufajok': kezdo_mufajok
    })



@login_required
def torol_konyv(request, konyv_id):
    print("Törlés nézet meghívva")  # Hibakeresés
    konyv = get_object_or_404(Konyvek, id=konyv_id)
    if request.method == "POST":
        print("POST kérés érkezett")  # Hibakeresés
        konyv.delete()
        print("Könyv törölve")  # Hibakeresés
        return redirect('adatok')
    return redirect('szerkeszt_konyv', konyv_id=konyv_id)