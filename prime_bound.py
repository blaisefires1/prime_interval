file = open("primeresults.txt", "a+")
upper_limit = int(input("Input upper limit: "))
lower_limit = int(input("Input lower limit: "))
iul = upper_limit + 1
file.write("All the prime numbers between " + str(upper_limit) + " and " + str(lower_limit) + " are: " + "\n")
for i in range(lower_limit, iul):
             for x in range(2,i):
                if (i % x ==0):
                    break
             else:
                file.write(str(i) + ", ")
file.close()