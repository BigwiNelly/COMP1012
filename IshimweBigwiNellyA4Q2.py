# Purpose: Calculating the area under the parabola using the Monte Carlo Technique

import numpy.random as npr
from time import ctime


def display_termination_message():
    print("""
Programmed by ISHIMWE BIGWI Nelly
Date: %s
End of processing.""" % ctime())


def get_positive(prompt): # Function to get a positive number only
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


def parabola(h, k, x_coordinates): # Function to get the points on the parabola according to xCoordinates 
    a = -k / (h * h)
    y_yoordinates = a * pow((x_coordinates - h), 2) + k
    return yCoordinates


def monte_carlo(fx, h, k, points):
    y_points = npr.uniform(0, k, points)  # y points in general
    y_coordinates = fx  # y point on parabola based on x coordinates
    in_parabola = y_points <= y_coordinates
    probability = sum(in_parabola) / points
    estim_area = probability * h * k * 2
    return estim_area


def main(): # The main function to call other functions into and perform or operations
    points = get_positive('Enter the number of intervals / points: ')
    h = get_positive('Enter the value of h in cm: ')
    k = get_positive('Enter the value of k in cm: ')
    x_coordinates = npr.uniform(0, 2 * h, points)
    area = 4 / 3 * h * k
    estim_area = monte_carlo(parabola(h, k, x_coordinates), h, k, points)
    error = abs(estim_area - area)
    print("""
    
    Area computed using the Monte Carlo technique.
    
    Area is from x = %.2f to x = %.2f 
    Approximate area of the parabola is %.14e cm^2
         Actual area of the parabola is %.14e cm^2
      The error in the approximation is %.6e cm^2""" % (0, 2 * h, estim_area, area, error))
    display_termination_message()


main()
