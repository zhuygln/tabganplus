# System Design

In this system, we integrated tabular GAN with other machine learning models or automated machine learning pipeline during training GAN. During training, GAN model could write generated data and the loss function score on the fly. However, the loss function is not always converage. Empirical number of epoch for training is given at the beginning of the job. 