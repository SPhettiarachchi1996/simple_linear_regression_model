{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "from random import randint "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "TRAIN_SET_LIMIT = 1000\n",
    "TRAIN_SET_COUNT = 100\n",
    "\n",
    "TRAIN_INPUT = list()\n",
    "TRAIN_OUTPUT = list()\n",
    "for i in range(TRAIN_SET_COUNT):\n",
    "    a = randint(0, TRAIN_SET_LIMIT)\n",
    "    b = randint(0, TRAIN_SET_LIMIT)\n",
    "    c = randint(0, TRAIN_SET_LIMIT)\n",
    "    op = a + (2*b) + (3*c)\n",
    "    TRAIN_INPUT.append([a, b, c])\n",
    "    TRAIN_OUTPUT.append(op)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LinearRegression(n_jobs=-1)"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "\n",
    "predictor = LinearRegression(n_jobs=-1)\n",
    "predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Outcome : [140.]\n",
      "Coefficients : [1. 2. 3.]\n"
     ]
    }
   ],
   "source": [
    "X_TEST = [[10, 20, 30]]\n",
    "outcome = predictor.predict(X=X_TEST)\n",
    "coefficients = predictor.coef_\n",
    "\n",
    "print('Outcome : {}\\nCoefficients : {}'.format(outcome, coefficients))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
