import json

p_str = "-32.98561,0.194442 -65.97385,-0.03659 -98.95946,0.0875 -8.96302,0.07202 -10.83654,0.32168 -12.24068,0.549143 -8.46772,1.371679 -11.9671,3.010958 -17.22279,8.094662 -6.06875,5.870047 -10.215559,12.183537 -13.890629,21.133599 -1.18454,2.88476 -3.18214,8.68125 -4.10104,11.88985 l -0.39687,1.38906 4.59713,-0.008 1.67847,-2.72018 c 3.98303,-6.47462 8.746329,-11.9417 12.559499,-14.419792 4.75827,-3.09246 11.11171,-4.54079 19.99245,-4.54767 h 3.00144 c -0.68763,7.885652 -1.21502,15.785322 -1.78594,23.680222 -1.77345,24.67054 -1.79996,24.98328 -2.79453,31.35312 -2.89825,18.56025 -5.44909,25.5942 -13.17943,36.34845 -6.96621,9.68984 -8.16187,11.95494 -8.73945,16.56133 -0.80217,6.39763 2.56206,11.74089 8.73945,13.89063 2.88079,0.94705 6.23147,0.96557 9.00404,-0.32245 v 0.008 c 3.18929,-1.57012 6.90589,-5.91158 9.21914,-10.76537 4.22937,-8.87439 8.94212,-33.42745 12.17083,-63.39151 0.27361,-2.53928 3.44779,-46.132752 3.44779,-47.304862 l 37.10782,-0.0546 c -2.43652,16.982822 -3.91637,34.104802 -5.37422,51.196892 -0.45365,5.94386 -0.61995,25.59155 -0.26458,30.99857 0.99266,15.10109 3.43667,24.50862 7.91263,30.42708 3.88407,5.13583 8.52327,8.28755 13.97316,9.50013 2.44454,0.54385 7.5311,0.40283 10.01289,-0.28112 4.18201,-1.1525 8.67622,-3.93118 12.45182,-7.69778 4.90458,-4.89268 8.06583,-11.04795 10.44284,-20.34805 0.91652,-3.5859 2.373,-11.32919 2.373,-12.59258 l -4.60534,0.0909 c -0.78949,3.8346 -1.09993,5.02893 -1.71154,6.53203 -1.74733,4.29366 -5.13397,7.48797 -9.55807,9.03711 -5.48508,1.63766 -11.31676,0.80986 -16.18932,-2.06703 -4.73552,-3.09324 -7.63456,-8.28728 -8.83868,-15.84193 -1.26174,-26.36254 1.79115,-52.80553 5.44883,-78.888172"
ps = p_str.replace('c', '').replace('l', '').replace('h', '').replace('v', '').split()
ps = [ p.split(',') for p in ps ]
print(ps)
for p in ps:
    if len(p) != 2:
        print(p)
ps = [ (float(x[0]), float(x[1])) for x in ps ]

with open('svg.json', 'w') as f:
    json.dump(ps, f)