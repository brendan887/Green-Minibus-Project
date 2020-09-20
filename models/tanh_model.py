import numpy as np
import matplotlib.pyplot as plt
from keras import layers
from keras import models
from keras import optimizers
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Config
train_data_dir = '/media/sq/Win Data/Brendan EE/training'
validation_data_dir = '/media/sq/Win Data/Brendan EE/validation'
epochs = 10
batch_size = 8
lr = 0.01
trials = 5

if __name__ == "__main__":
    for i in range(trials):
        print(f"TRIAL {i}")
        print("="*25)
        sgd = optimizers.SGD(learning_rate=lr, momentum=0.0, nesterov=False, name="SGD")

        # tanh model
        tanh_model = models.Sequential()
        tanh_model.add(layers.Conv2D(16, (14, 14), strides=2, activation='tanh', input_shape=(480, 640, 3)))
        tanh_model.add(layers.MaxPooling2D((2, 2)))
        tanh_model.add(layers.Conv2D(16, (11, 11), strides=2, activation='tanh'))
        tanh_model.add(layers.MaxPooling2D((2, 2)))
        tanh_model.add(layers.Conv2D(16, (8, 8), activation='tanh'))
        tanh_model.add(layers.MaxPooling2D((2, 2)))
        tanh_model.add(layers.Flatten())
        tanh_model.add(layers.Dense(256, activation='tanh'))
        tanh_model.add(layers.Dense(1, activation='sigmoid'))
        tanh_model.compile(optimizer=sgd, loss='binary_crossentropy', metrics=['acc'])
        # Set pixel values to 0-1
        train_datagen = ImageDataGenerator(rescale=1. / 255)
        validation_datagen = ImageDataGenerator(rescale=1. / 255)

        train_generator = train_datagen.flow_from_directory(
            train_data_dir,
            target_size=(480, 640),
            batch_size=batch_size,
            class_mode='binary',
            shuffle=True)
        validation_generator = validation_datagen.flow_from_directory(
            validation_data_dir,
            target_size=(480, 640),
            batch_size=batch_size,
            class_mode='binary',
            shuffle=True)

        # Train network
        history = tanh_model.fit_generator(
            train_generator,
            # number of iteration per epoch = number of data / batch size
            steps_per_epoch=np.floor(train_generator.n / batch_size),
            epochs=epochs,
            # number of iteration per epoch = number of data / batch size
            validation_data=validation_generator,
        )

        # Plot graphs
        acc = history.history['acc']
        val_acc = history.history['val_acc']
        loss = history.history['loss']
        val_loss = history.history['val_loss']

        x_axis = range(1, len(acc) + 1)

        plt.figure()
        plt.plot(x_axis, acc, 'bo', label='Training acc')
        plt.plot(x_axis, val_acc, 'b', label='Validation acc')
        plt.title(f"Training and validation accuracy (Tanh Trial {i})")
        plt.xlabel("Epoch")
        plt.ylabel("Validation accuracy")
        plt.legend()
        plt.savefig(f"trial_{i}_tanh_accuracy.png")

        plt.figure()
        plt.plot(x_axis, loss, 'bo', label='Training loss')
        plt.plot(x_axis, val_loss, 'b', label='Validation loss')
        plt.title(f"Training and validation loss (Tanh Trial {i})")
        plt.xlabel("Epoch")
        plt.ylabel("Validation loss")
        plt.legend()
        plt.savefig(f"trial_{i}_tanh_loss.png")
