import React, { useState, useEffect/*, Component */} from 'react';
import './App.css';


function Perihal(){
    return(
<div>
    <div>
        <h2>
        Konsep Singkat
        </h2>
    </div>
    <p>
        Aplikasi ini adalah sebuah search engine yang menampilkan hasil terurut berdasarkan cosine similarity.
        dokumen yang ditampilkan sebagai hasil pencarian berasal dari webscraping 2 buah website yaitu kompas.com
        dan tribunnews.com dan juga dokumen yang diupload oleh pengguna secara manual.
    </p>
    <p>
        Saat pertama kali dibuka program akan melakukan webscraping ke dua web tersebut, hasil webscraping ini kemudian dibersihkan
        dan dilakukan stemming. ketika query dimasukkan, program akan mengecek apakah pengguna telah melakukan upload dokumen. jika iya
        program akan menbaca dokumen yang diupload pengguna, melakukan cleaning, dan juga stemming. kemudian program melakukan perthitungan
        cosine similarity pada dokumen-dokumen yang sudah dibersihkan tersebut. Judul, similarity, dan kalimat pertama dari 5 dokumen dengan
        similarity paling besar akan ditampilkan di layar. Tabel berisi jumlah setiap kata dalam query di dokumen juga akan ditampilkan.
    </p>
    <div>
        <h2>
        How to Use
        </h2>
    </div>
    <p>
        Untuk melakukan pencarian, ketikkan query yang diinginkan. Kemudian tekan tombol search. Tunggu beberapa saat sampai hasil muncul.
        Ulangi hal yang sama jika ingin mencari query yang lain.

        
    </p>
    <p>
        Untuk melakukan upload file, tekan tombol choose file. Kemudian pilih file yang ingin diupload, lalu tekan tombol upload.
        Ulangi hal yang sama jika ingin mengupload file yang lain
    </p>

    <div>
        <h2>
        About Us
        </h2>
    </div>
    <p>
        Ronggur Mahendra (13519008)
    </p>
    <p>
        Muhammad Furqon (13519184)
    </p>
    <p>
        Ahmad Saladin (13519187)
    </p>

</div>
    )
}
export default Perihal;