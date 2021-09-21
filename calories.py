# This program determines the amount of calories required to gain weight.

def poundsToKG(pounds):
    return(pounds / 2.205)


def bmr(w, h, a):
    return((10 * w) + (6.25 * h) - (5 * a) + 5)


def basalMetabolicRate():
    weight = poundsToKG(float(input('Enter your weight in pounds: ')))
    height = float(input('Enter your height in CM: '))
    age = int(input('Enter your age: '))
    metabolicRate = bmr(weight, height, age)
    print('Your BMR is approximately %.0f' % metabolicRate)
    print('You need to consume roughly %.0f calories' % (metabolicRate * 2.05))
    return(metabolicRate * 1.95)


def calorieConsumption():
    gainRate = basalMetabolicRate()
    meals = []
    kcal = []
    newCal = 0
    while newCal < gainRate:
        meals.append(input('What did you eat? '))
        try:
            cal = float(input('How many calories did it have? '))
        except ValueError:
            print('Try again')
            cal = float(input('How many calories did it have? '))
        newCal += cal
        print('You need to eat roughly %.2f more calories.'
              % (gainRate - newCal))
    else:
        print('You have met the required amount of calories today! Yay!')


calorieConsumption()
