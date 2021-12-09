from random import randint;

pc_num = randint(0,100);
player_num = int(input("Bir sayı girin : "));
try_count = 0;

while player_num != pc_num:
	try_count += 1;
	if(player_num > pc_num):
		player_num = int(input("Daha küçük bir sayı girin : "));
	elif(player_num < pc_num):
		player_num = int(input("Daha büyük bir sayı girin : "));
print(f"Tebrikler Buldunuz !\nDeneme sayınız : {try_count}".upper());
