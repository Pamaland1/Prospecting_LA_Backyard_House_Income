import pandas as pd
import numpy as np


# create a function to take in user-entered address and apply the model
def backyard_house(user_input):
    # read in the database
    df = pd.read_csv("backyard_house_income_segmentation.csv")

    # show user final message
    #get user address input
    #mask dataframe row to user_input address
    mask = df["address"] == user_input

    #create new dataframe from mask
    info = df[mask]

    if info.shape[0] == 0:
        final_message = "%s cannot accomodate a backyard house of minimum 400 square feet." % user_input

    else:
        #create list from masked dataframe
        prop_info = list(info.iloc[0])

        #extract user output from list
        #bedrooms
        br = prop_info[2]

        #baths
        ba = prop_info[5]

        #square feet
        sf = prop_info[6]

        #nightly price/income
        price = prop_info[7]

        #LA segment
        segment = prop_info[8]

        #create tuple to use in string
        test_tuple = (price, user_input, segment, sf, br, ba)

        #print output
        final_message = """Your nightly income prediction is $%d for a backyard house located at %s.  This is in the %s income segment for Los Angeles.\n
        Your property can accomodate a %d square foot backyard house. \n
        This is typically a %d bedroom, %d bath unit. \n""" % test_tuple

    return final_message

if __name__ == "__main__":

    backyard_house("1070 CASIANO RD LOS ANGELES CA 90049")
    backyard_house("asdf1070 CASIANO RD LOS ANGELES CA 90049")
