from Product import product
from ProductType import ProductType


class InitialData:
    __products = []
    __product_types = []

    def __init__(self):
        #inisial jenis produk
        rokok = ProductType("R","Rokok")
        makanan = ProductType("MA","Makanan ")
        minuman = ProductType("MI", "Minuman")
        sabun = ProductType("SB", "Sabun")
        sampo = ProductType("SM", "Sampo")
        pasta_gigi = ProductType("PG", "Pasta Gigi")
        self.__product_types = [rokok,makanan,minuman,sabun,sampo,pasta_gigi]

        #inisial data produk
        magnum_blu = product("MB", "Magnum Blu", 20000, rokok)
        gudang_garam = product("GG", "Gudang Garam", 20000, rokok)
        marlboro = product("ML", "Marlboro", 30000, rokok)
        sampoerna_mild = product("SM", "Sampoerna Mild", 23000, rokok)
        djarum_super = product("D", "Djarum super", 19000, rokok)
        sampoerna_kretek = product("SS", "Sampoerna Sretek", 18000, rokok)
        sedap_goreng = product("SG", "Sedap Goreng", 2500, makanan)
        sedap_rebus = product("SR", "Sedap Rebus", 3000, makanan)
        indomie_rebus = product("IR", "Indomie Rebus", 3000, makanan)
        indomie_goreng = product("IG", "Indomie Goreng", 3500, makanan)
        bear_brand = product("SB", "Bear Brand", 9000, minuman)
        larutan_kaleng = product("LK", "Larutan Kaleng", 6000, minuman)
        pocari_sweat = product("PS", "Pocari_Sweat", 6000, minuman)
        coca_cola = product("CC", "Coca Cola", 5000, minuman)
        panta = product("P", "Panta", 5000, minuman)
        sprite = product("S", "Spirte", 5000, minuman)
        air_mineral = product("AM", "Air Mineral", 2500, minuman)
        teh_botol = product("TB", "Teh Botol", 3500, minuman)
        teh_pucuk = product("TP", "Teh Pucuk", 4000, minuman)
        lifebuoy = product("LF", "lifebuoy", 3000, sabun)
        give = product("GV", "Give", 2000, sabun)
        nuvo = product("NV", "Nuvo", 2500, sabun)
        shinzui = product("SH", "Shinzui", 4500, sabun)
        emeron = product("SLF", "Emeron", 14000, sampo)
        zinc = product("Z", "Zinc", 26000, sampo)
        clear = product("C", "Clear", 23000, sampo)
        pantene = product("P", "Pantene", 21000, sampo)
        sunsilk = product("SU", "Sunsilk", 25000, sampo)
        tresemmen = product("T", "tresemmen", 26000, sampo)
        pepsodent = product("PS1", "Pepsodent", 12000, pasta_gigi)
        ciptadent = product("PS2", "Ciptadent", 9000, pasta_gigi)
        sensodyne = product("PS3", "Sensodyne", 10000, pasta_gigi)
        colgate = product("PS4", "colgate", 6000, pasta_gigi)
        formula = product("PS5", "formula", 10000, pasta_gigi)
        self.__products = [sabun,sampo,magnum_blu,gudang_garam,marlboro,sampoerna_mild,djarum_super,sampoerna_kretek,sedap_goreng,sedap_rebus,
                           indomie_rebus,indomie_goreng,sunsilk,bear_brand,larutan_kaleng,pocari_sweat,coca_cola,colgate,panta,sprite,
                           air_mineral,teh_botol,teh_pucuk,lifebuoy,give,zinc,nuvo,shinzui,emeron,clear,pantene,tresemmen,pepsodent,
                           ciptadent,sensodyne,formula]
    # mengaambil list product
    def get_products(self):
        return self.__products
    def get_product_types(self):
        return self.__product_types
