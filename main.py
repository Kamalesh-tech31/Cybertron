from model.predictor import predict_message

message = input("Enter a message: ")

result = predict_message(message)

print("\nPrediction Result:")
print(result)