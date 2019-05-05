# CatsAndDogs

## Question 1:

For debugging purposes, you can lower the number of training and validation samples
by a factor of say 20, and run for 1 epoch (Note: if you make the number of training samples
too small, it triggers some internal error in Keras). What accuracy do you obtain, and why?

Epoch 1/1

1/5 [=====>........................] - ETA: 9s - loss: 0.6579 - acc: 0.6875

2/5 [===========>..................] - ETA: 6s - loss: 0.8373 - acc: 0.5938

3/5 [=================>............] - ETA: 4s - loss: 0.9934 - acc: 0.5000

4/5 [=======================>......] - ETA: 2s - loss: 0.9992 - acc: 0.5156
5/5 [==============================] - 15s 3s/step - loss: 0.9960 - acc: 0.5125 - val_loss: 0.7363 - val_acc: 0.6562

## Question 2: 

If you fine-tune for 1 or 2 epochs using the original number of training and validation
samples, what accuracy do you obtain, and why? Does your saved model le now work better
with your testing util

