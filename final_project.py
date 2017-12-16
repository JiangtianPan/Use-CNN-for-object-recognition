# -*- coding: utf-8 -*-

from CNN_model import *

if __name__ == '__main__':
    # 1. Load processed data (which means objects are selected separately)
    # 2. Resize the Images
    # 3. Label every image
    # 4. Separate the Images and Labels into two parts
    train_1,train_2,test_1,test_2 = load_dataset.load_dataset()

    # 5. Second process to data.
    # (Note: We should use array in numpy so as to evaluate our data conveniently)
    X_train = np.array(train_1)
    Y_train = np.array(train_2)
    X_test = np.array(test_1)
    Y_test = np.array(test_2)
    X_train, Y_train, X_test, Y_test = data_preprocessing(X_train, Y_train, X_test, Y_test)

    print(len(Y_test))
    print(Y_test)

    # 6. Build up a CNN model using keras
    model = model_built()

    # 7. Training the data and exhibit the loss/accuracy rate
    model.fit(X_train, Y_train,epochs=10,
              batch_size=32, verbose=0, validation_split=0.1)

    # 8. Evaluate model on test data
    score = model.evaluate(X_test, Y_test, verbose=0)
    print('Loss value = %f, average classification = %f'%(score[0],score[1]))

    # you can also calculate everything step by step
    #First predict the output, this will give you the scores of the softmax function
    prediction = model.predict(X_test)

    fix = []
    for j in range(0,len(prediction)):
        for i in range(0,len(prediction[0])):
            fix_row=[]
            if i==0:
                fix_row.append(0.5)
            else:
                fix_row.append(0)
        fix.append(fix_row)


    prediction -= fix
    #find the node that has the maximum activation

    # calculate the average classification
    predict_class = prediction.argmax(axis = 1)
    i=0
    classification = 0

    # print(predict_class[:100])
    # print(test_2[:100])
    for pc in predict_class:
        if i<10:
            print(pc,test_2[i])
        if pc in test_2[i]:
            classification+=1
        i+=1
    ave_classification = float(classification)/ len(predict_class)


    # ave_classification = np.mean(predict_class in np.array(test_2))
    print('Average classification = %f'%(ave_classification))

    # A. Appendix : Test code
    # cv2.imshow('image',X_test[0])
    # cv2.waitKey(0)