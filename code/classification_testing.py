# This is code to load trained model and test it
from keras.models import load_model
from os import environ
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator

def predict_and_plot(model, test_generator, columns=5):
    text_labels = []
    plt.figure(figsize=(30, 20))
    for i, batch in enumerate(test_generator):
        pred = model.predict(batch[0])
        if pred > 0.5:
            text_labels.append('dog')
        else:
            text_labels.append('cat')
        plt.subplot(5 / columns + 1, columns, i + 1)
        plt.title('This is a ' + text_labels[i])
        imgplot = plt.imshow(batch[0][0])
        i += 1
        if i % 10 == 0:
            break
    plt.show()
    return text_labels

def load_my_model(modelpath, weightpath):
    model = load_model(modelpath)
    model.load_weights(weightpath)
    return model

def get_generator(data_directory, target_size):
    return ImageDataGenerator(rescale=1. / 255).flow_from_directory(
        data_directory,
        target_size=target_size,
        batch_size=1,
        class_mode='binary')


if __name__ == '__main__':

    # Needed to run model
    environ['KMP_DUPLICATE_LIB_OK'] = 'True'

    # dimensions of our images.
    img_width, img_height = 150, 150

    # Path to data
    local_path = '/Users/alejandro.robles/PycharmProjects/CatsAndDogs/{}'
    test_data_dir = local_path.format('classification testing utility')  # Validation and test set are the same here

    # Path to model and weights
    model_path, model_path_better = 'models/model_keras.h5', 'models/model_keras_full.h5'
    model_weights_path, model_weights_path_better = 'models/model_weights.h5', 'models/model_weights_full.h5'

    # Loading models
    model = load_my_model(model_path, model_weights_path)
    model_better = load_my_model(model_path_better, model_weights_path_better)

    # Test Generator
    test_generator = get_generator(test_data_dir, (img_width, img_height))

    # Predictions
    predicted_labels = predict_and_plot(model, test_generator)
    predicted_labels_better_model = predict_and_plot(model, test_generator)






