import pandas as pd
import numpy as np

df= pd.read_csv("home_prices.csv")


def gradient_descent(x, y, lr=0.01, epochs=3000): #here lr= Learning Rate and epochs is =
    m, b = 0.0, 0.0


    x_min, x_max = x.min(), x.max()
    y_min, y_max = y.min(), y.max()

    x_scaled = (x-x_min)/(x_max - x_min)
    y_scaled = (y-y_min)/(y_max - y_min)

    for epoch in range(epochs):
        y_pred = m * x_scaled + b
        error = y_scaled - y_pred
        cost = np.mean(error**2)
        dm = -2 * np.mean(error * x_scaled)
        db = -2 * np.mean(error)

        b -= db * lr
        m -= dm * lr

        if epoch%100 ==0:
            print(f"Epoch {epoch}: cost = {cost}, b = {b}, m = {m}")

    m_original = m * (y_max - y_min) / (x_max - x_min)
    b_original = y_min + (y_max - y_min) * (
            b - m * x_min / (x_max - x_min)
    )

    return  m_original,b_original

if __name__=="__main__":
    # x = np.array([1,2,3,4,5])
    # y = np.array([5,6,7,8,9])
    x = df["area_sqr_ft"].to_numpy()
    y = df["price_lakhs"].to_numpy()
    # print(df.head())

    m, b = gradient_descent(x,y)
    print(f"Final Results: m = {m}, b = {b}")


