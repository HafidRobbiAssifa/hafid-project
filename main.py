from Initial_Data import InitialData


class main :
    print("======Warung Rakyat======")
    print("List Jenis Produk")
    # list product type
    initial_data = InitialData()
    for i in initial_data.get_product_types():
        print(i.code+" : "+i.name)
    print("===========================")
    productTypeCode = input("Masukan Kode Jenis Produk : ")
    #ngambil objek yang bertipe data product type yang kodenya sesuai input jika tidak di temukan maka memunculkan eror
    product_Type = ""
    for i in initial_data.get_product_types():
        if i.code == productTypeCode:
            product_Type = i
    if product_Type == "":
        print("Jenis Produk Tidak Ditemukan")
    else:
        print("list Produk")
        products = []
        for i in initial_data.get_products():
            if i.product_types == products:
                products.append(i)
                print(i.code+" : "+i.name)
        productCode = input("Masukan Kode Produk :")
        product = ""
        for i in products:
            if i.code == productCode:
                product = i
        if product == "":
            print("Produk Tidak Ditemukan")
        else:
            item_input = input("Masukan Jumlah Item Produk :")
            print("harga : "+str(product.price))
            total_price = product.price * int(item_input);
            print("Total Harga : "+str(total_price))
            diskon = total_price * 10/100
            print("Diskon 10% =",diskon)
            print(" Terima Kasih Telah Mengunjungi Toko Kami ")




    # input product type


    #area panggil