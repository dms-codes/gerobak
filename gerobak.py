print(70*'-')
print('GEROBAK FRIED CHICKEN'.center(70))
print(70*'-')
print('No\tKode\tJenis Potong\tHarga Satuan\tBanyak\tSubtotal')
print(70*'-')
i = 1
subtotal = []

while True:
    print(f'{i}\t',end='')
    kode = input()
    if kode in ['d','D']:
        print(f'\033[F\t\tDada\t',end='')
        print('\tRp 2500\t\t',end='')
        banyak = int(input())
        subtotal.append(banyak * 2500)
        print(f'\033[F\t\t\t\t\t\t\tRp {subtotal[-1]}')
        i += 1
        continue
    elif kode in ['p','P']:
        print(f'\033[F\t\tPaha\t',end='')
        print('\tRp 2000\t\t',end='')
        banyak = int(input())
        subtotal.append(banyak * 2000)
        print(f'\033[F\t\t\t\t\t\t\tRp {subtotal[-1]}')
        i += 1
        continue
    elif kode in ['s','S']:
        print(f'\033[F\t\tSayap\t',end='')
        print('\tRp 1500\t\t',end='')
        banyak = int(input())
        subtotal.append(banyak * 1500)
        print(f'\033[F\t\t\t\t\t\t\tRp {subtotal[-1]}')
        i += 1
        continue
    elif kode in ['t','T']:
        print(f'\033[F'+70*'-')
        jumlah_bayar = int(sum(subtotal))
        pajak = int(0.1*sum(subtotal))
        total = jumlah_bayar + pajak
        print(f'\t\t\t\t\tJumlah Bayar\tRp {jumlah_bayar}')
        print(f'\t\t\t\t\tPajak(10%)\tRp {pajak}')
        print(f'\t\t\t\t\tTotal\t\tRp {total}')
        i += 1
        break
    else: 
        i += 1
        print(f'\033[F\033[F')
        continue
