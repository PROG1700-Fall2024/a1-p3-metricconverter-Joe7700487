#Program 3 – Imperial to Metric Conversion
#Write a console program that converts a weight given in tons (imperial), stones, pounds, and ounces 
# to the metric equivalent in metric tons, kilograms, and grams.

def main():
    #get input
    tons = float(input("Input number of tons: "))
    stone = float(input("Input number of stone: "))
    pounds = float(input("Input number of pounds: "))
    ounces = float(input("Input number of ounces: "))

    #convert all units to ounces
    ounces = 35840 * tons + 224 * stone + 16 * pounds + ounces
    #convert ounces to kilos
    kilos = ounces / 35.274

    #get metric tons and drop the remainder
    metricTons = int(kilos/1000)
    #make kilos equal to the remainder of the tons calculation and then drop the remainder of that
    kilos = kilos - metricTons * 1000
    #get the remainder of the kilo calculation and convert to grams
    remainder = kilos - int(kilos)
    grams = remainder * 1000

    #print the final values
    print("The metric weight is {0:.0f} metric tons, {1:.0f} kilos, and {2:.1f} grams.".format(metricTons, kilos, grams))
main()