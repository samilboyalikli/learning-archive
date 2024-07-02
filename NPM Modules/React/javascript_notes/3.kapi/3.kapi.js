/*
Bu oyun üç aşamadan oluşur:
1. Aşama: iki kapı vardır (burada kullanıcı dümdüz input girer)
2. Aşama: beş kapı vardır (burada kullanıcı kapı şeklindeki butonlardan birini seçer)
3. Aşama: on kapı vardır (burada da aynı şekilde kullanıcı kapı şeklindeki butonlardan birini seçer)
*/



/*1. Aşama: iki kapı vardır (burada kullanıcı dümdüz input girer)*/
function sifirBir() {
    var girilenDeger = document.getElementById('bir_sifir').value;
    if (girilenDeger === '1') {
        window.location.href = 'ikinci_asama.html';
    } else if (girilenDeger === '0') {
        window.location.href = 'kaybettin.html';
    } else {
        alert('LÜTFEN 1 VEYA 0 TUŞLARINDAN BİRİNİ GİRİNİZ');
    }
}

/*2. Aşama: beş kapı vardır (kullanıcı burada kapılardan birini click eder)*/
function trueDoor() {
    window.location.href = 'ucuncu_asama.html';
}
function falseDoor() {
    window.location.href = 'kaybettin.html';
}

/*3. Aşama: on kapı vardır (kullanıcı burada kapılardan birini click eder)*/
function dtrueDoor() {
    window.location.href = 'kazandin.html';
}