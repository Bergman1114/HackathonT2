import carDetails as cd
from products import Products
import buyers_func as dbfun
import decimal as decimal
from colorama import Fore,Style


def calculatePrice(carPrice,carColor,isBuyerVeteran, tax_percent):
    carPriceDetails = cd.CarDetail()
    salePrice = carPrice
    disc_amt = 0

    veteran_disc_amt = 0
    dnpayment_discount = 0
    veteran_discount = 0
    dnpmt_amt = carPrice * decimal.Decimal(0.1)
    colorDiscount = 0
    color_dnpayment_discount = 0
    veteran_dnpayment_discount = 0
    notes = ''
    print()
    print(Fore.RED,f'******************************************')
    print('             CHECKOUT                      ')
    print('******************************************')
    print()

    if (carColor == 'black'):
        notes = notes + '25 percent discount for Black car' 
        print(f'Congratulations!You have got 25% discount for picking Black color car.')
        colorDiscount = carPrice*decimal.Decimal(0.25)
    elif (carColor == 'white'):
        notes = notes + '$400 discount toward your downpayment'
        print(f'Congratulations! You have got $400 discount toward your downpayment.')
        color_dnpayment_discount = 400
    
    if (isBuyerVeteran == 'y'):
        notes = notes + '25 percent discount and $500 toward downpayment'
        print(f'Congratulations!You have got 25% discount and $500 toward downpayment as you are an veteran')
        veteran_dnpayment_discount = 500
        veteran_disc_amt = carPrice*decimal.Decimal(0.25)

    

    total_discount = colorDiscount + veteran_disc_amt
    dnpayment_discount = color_dnpayment_discount + veteran_dnpayment_discount
    dnpmt_amt= dnpmt_amt - dnpayment_discount
    total_price = carPrice - total_discount - dnpayment_discount
    total_tax = total_price*tax_percent

    carPriceDetails.setCarPrice(total_price+total_tax)
    carPriceDetails.setDisc_amount(total_discount+dnpayment_discount)
    carPriceDetails.setDnpaymentAmount(dnpmt_amt)
    carPriceDetails.setFinal_price(total_price*1)
    carPriceDetails.setNotes(notes)
    carPriceDetails.setTax_amount(total_tax)
    carPriceDetails.setBonus(dnpayment_discount)
    
    return carPriceDetails
