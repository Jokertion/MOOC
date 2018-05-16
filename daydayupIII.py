N =eval(input())

dayfactor =1.0

dayup = pow(dayfactor+N/1000,365)
daydown =pow(dayfactor-N/1000,365)
difference = int(dayup//daydown)

print ("{:.2f},{:.2f},{}".format(dayup,daydown,difference))