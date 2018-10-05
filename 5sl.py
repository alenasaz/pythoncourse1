def expres001(x,y,z,f):
    expres=((x*(y-x))/z + x +(f+z)/(f)**y-(z-f)/z)/((z+f)/((z)**y)-f)
    print("Значение выражения равно:",expres)
expres001(5,2.3,2,7.5)