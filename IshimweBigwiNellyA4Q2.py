# Purpose: Calculating the area under the parabola using the Monte Carlo Technique

import numpy.random as npr
from time import ctime


def displayTerminationMessage():
    print("""
Programmed by ISHIMWE BIGWI Nelly
Date: %s
End of processing.""" % ctime())


def getPositive(prompt): # Function to get a positive number only
    state = True
    while state:
        number = input(prompt).strip()
        if number != '':
            try:
                number = eval(number)
            except:
                print('Invalid input')
            else:
                if isinstance(number, (int, float)):
                    if number > 0:
                        return number
                    else:
                        print(number, 'is not greater than zero!')
                else:
                    print(number, 'is not a number!')
        else:
            print('Missing input!')


def parabola(h, k, xCoordinates): # Function to get the points on the parabola according to xCoordinates 
    a = -k / (h * h)
    yCoordinates = a * pow((xCoordinates - h), 2) + k
    return yCoordinates


def monteCarlo(fx, h, k, points):
    yPoints = npr.uniform(0, k, points)  # y points in general
    yCoordinates = fx  # y point on parabola based on x coordinates
    inParabola = yPoints <= yCoordinates
    probability = sum(inParabola) / points
    estimArea = probability * h * k * 2
    return estimArea


def main(): # The main function to call other functions into and perform or operations
    points = getPositive('Enter the number of intervals / points: ')
    h = getPositive('Enter the value of h in cm: ')
    k = getPositive('Enter the value of k in cm: ')
    xCoordinates = npr.uniform(0, 2 * h, points)
    area = 4 / 3 * h * k
    estimArea = monteCarlo(parabola(h, k, xCoordinates), h, k, points)
    error = abs(estimArea - area)
    print("""
    
    Area computed using the Monte Carlo technique.
    
    Area is from x = %.2f to x = %.2f 
    Approximate area of the parabola is %.14e cm^2
         Actual area of the parabola is %.14e cm^2
      The error in the approximation is %.6e cm^2""" % (0, 2 * h, estimArea, area, error))
    displayTerminationMessage()


main()
