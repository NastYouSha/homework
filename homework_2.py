# 1

amount_ag = int(input())
total_cost= int(input())

quantity_au = amount_ag/16
sold_ag = amount_ag*48
sold_au = total_cost-sold_ag
cost_au = sold_au/quantity_au
print(int(cost_au))

# 2
Country = (input('Name'))
NewCountry = Country.split()
for item in NewCountry:
    print(item)

#3
FoxyBox, Milka = map(int,input().split())
print(FoxyBox + Milka, '- The total cost of chocolates')

#4
wife = int(input('how many wives? - '))
bag = int(input('How many bags? - '))
cat = int(input('How many cats? - '))
kitty = int(input ('How many kittens? - '))
print(wife*cat*kitty + 2)

#5
Amount_sls = int(input('Enter the planned sales amount - '))
PorcentProfit = int(input('Enter the percentage of profit from sales - '))
NewPorcent = PorcentProfit/100
Profit = Amount_sls*NewPorcent
print("Profit = {:.2f}".format(Profit))

#6
wght = float(input('Enter your body weight in pounds - '))
hght = float(input('Enter your body height in inch - '))
wght = wght*0.45
hght = hght*0.025
IMT = wght/(hght**2)
print(IMT)

#7
prcpttn_lvl = int(input('Enter precipitation level in centimeters - '))
prcpttn_lvl = prcpttn_lvl/100
print(int(10000*prcpttn_lvl))

#8
N, M = map(int,(input()).split())
people = N+1
print (people//M)

#9
N,K = map(int, input().split())
Bulls_fml = N//K
release = N - Bulls_fml*K
print(release)

#10
metr = int(input('Enter meters - '))
mile = metr*0.00062
print(mile)