#fungsi garis
def garis1():
    print("=================================================")

def garis2():
    print("----------------------------------------------")

buku = []

#fungsi show buku ( perlihatkan buku )
def show_buku():
    if len(buku) <= 0:
        garis1()
        print ("Buku Kosong mas!")
        garis1()
    else:
        for indeks in range(len(buku)):
            print ("[{}] {}".format (indeks,buku [indeks]))

#fungsi untuk edit buku
def edit_buku():
    show_buku()
    indeks = 1
    int(input("Inputan ID Buku : "))
    if indeks > len(buku):
        garis1()
        print("ID SALAH")
        garis1()
    else:
        judul_baru = input("Judul Baru : ")
        garis2()
        buku[indeks] = judul_baru
        garis1()


#fungsi delete buku
def delete_buku():
    show_buku()
    indeks = int(input("Inputan ID Buku : "))
    if indeks > len(buku):
        print("ID Salah")
    else:
        buku.remove(buku[indeks])
        print("Buku berhasil dihapus")


#fungsi insert buku
def insert_buku():
    buku_baru = input("Judul Buku : ")
    buku.append(buku_baru)
    garis2()
    print("Buku berhasil ditambah")
    show_buku()
    garis2()

# Menu untuk tampilan perpus
def show_menu():
    print("\n")
    print("Selamat datang di Perpus-")
    print("1. Show buku")
    print("2. Insert buku")
    print("3. Edit buku")
    print("4. Delete buku")
    print("5. Keluar")

    menu = int(input("Pilih Menu : > "))
    print("\n")

    if menu == 1:
        show_buku()
    elif menu == 2:
        insert_buku()
    elif menu == 3:
        edit_buku()
    elif menu == 4:
        delete_buku()
    elif menu == 5:
        exit()
    else:
        print ("Upss Salah")

# tampilkan Menu
if __name__ == "__main__":
    while True:
        show_menu()
