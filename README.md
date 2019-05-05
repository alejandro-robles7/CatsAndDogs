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


We get an accuracy of 0.6562 for validation set. This is pretty good for a small dataset. 
The reason we get a good result is because we are using transfer learning which means we are taking 
advantage of a pre-trained model that has been trained on a very large dataset. The intuition is that
this model has already learnt basic shape and structures of animals so we only need to train higher level 
features. 


## Question 2: 

If you fine-tune for 1 or 2 epochs using the original number of training and validation
samples, what accuracy do you obtain, and why? Does your saved model le now work better
with your testing util


Found 7178 images belonging to 2 classes.

Found 1796 images belonging to 2 classes.

WARNING:tensorflow:From /Users/alejandro.robles/anaconda3/envs/WebsiteClassification/lib/python3.7/site-packages/tensorflow/python/ops/math_ops.py:3066: to_int32 (from tensorflow.python.ops.math_ops) is deprecated and will be removed in a future version.

Instructions for updating:

Use tf.cast instead.

Epoch 1/1

1/1875 [..............................] - ETA: 1:26:06 - loss: 0.7838 - acc: 0.4375

2/1875 [..............................] - ETA: 1:15:23 - loss: 0.7769 - acc: 0.4375

3/1875 [..............................] - ETA: 1:12:30 - loss: 0.7626 - acc: 0.4583

4/1875 [..............................] - ETA: 1:10:44 - loss: 0.7604 - acc: 0.4531

5/1875 [..............................] - ETA: 1:09:38 - loss: 0.7312 - acc: 0.5250

.

.

.

1872/1875 [============================>.] - ETA: 6s - loss: 0.2419 - acc: 0.8956

1873/1875 [============================>.] - ETA: 4s - loss: 0.2418 - acc: 0.8956

1874/1875 [============================>.] - ETA: 2s - loss: 0.2418 - acc: 0.8957

1875/1875 [==============================] - 4101s 2s/step - loss: 0.2417 - acc: 0.8957 - val_loss: 0.1872 - val_acc: 0.9185